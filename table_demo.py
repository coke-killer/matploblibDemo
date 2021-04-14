###########################################################
# !/usr/bin/python3
# -*- coding: utf-8 -*-
## author:qianqiu
from prettytable import PrettyTable
from PIL import Image, ImageDraw, ImageFont
from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType
import imgkit
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


def create_table_img(data, img_name, **kwargs):
    '''
        img_name 图片名称 'D:/project/pythonwork/12306/t.png' 或 t.png
        data 表格内容，首行为表头部
        table_title 表格标题
        line_height 底部描述行高
        font 默认字体路径
        default_font_size 默认字体大小
        default_background_color 图片背景底色
        table_top_heght 设置表格顶部留白高度
        table_botton_heght 设置表格顶部留白高度
        describe 底部描述文字
    '''
    space = 20  ## 表格边距
    # 生成图片-------------------------------
    ### 底部描述行高
    if 'line_height' not in kwargs:
        line_height = 4
    else:
        line_height = kwargs['line_height']

    ### 默认字体
    if 'font' not in kwargs:
        kwargs['font'] = None

    ### 默认字体大小
    if 'default_font_size' not in kwargs:
        kwargs['default_font_size'] = 35

    ### 默认表标题字体大小
    if 'table_title_font_size' not in kwargs:
        kwargs['table_title_font_size'] = 22

    ### 图片背景底色
    if 'default_background_color' not in kwargs:
        kwargs['default_background_color'] = (255, 255, 255, 255)

    ### 设置表格顶部留白高度
    if 'table_top_heght' not in kwargs:
        kwargs['table_top_heght'] = kwargs['table_title_font_size'] + space + int(kwargs['table_title_font_size'] / 2)

    ## 底部描述文字
    if 'describe' in kwargs:
        describe_len = len(kwargs['describe'])
    else:
        describe_len = 0
    ## 历史报警
    if 'historyalarm' in kwargs:
        historyalarm_len = len(kwargs['historyalarm'])
    else:
        describe_len = 0

    ### 设置表格底部留白高度
    if 'table_botton_heght' not in kwargs:
        try:
            kwargs['table_botton_heght'] = describe_len * kwargs['default_font_size'] + space + historyalarm_len * \
                                           kwargs['default_font_size']
        except:
            kwargs['table_botton_heght'] = describe_len * kwargs['default_font_size']

    ### 图片后缀
    if 'img_type' not in kwargs:
        kwargs['img_type'] = 'PNG'

    ### 默认字体及字体大小
    font = ImageFont.truetype(kwargs['font'], kwargs['default_font_size'], encoding='utf-8')
    font2 = ImageFont.truetype(kwargs['font'], kwargs['table_title_font_size'], encoding='utf-8')
    ## Image模块创建一个图片对象
    im = Image.new('RGB', (10, 10), kwargs['default_background_color'])
    ## ImageDraw向图片中进行操作，写入文字或者插入线条都可以
    draw = ImageDraw.Draw(im)

    # 创建表格---------------------------------
    tab = PrettyTable(border=True, header=True, header_style='title', hrules=1, vertical_char=' ', junction_char='-')
    ## 第一行设置为表头
    tab.field_names = data.pop(0)
    for row in data:
        tab.add_row(row)
    tab_info = str(tab)
    ## 根据插入图片中的文字内容和字体信息，来确定图片的最终大小
    img_size = draw.multiline_textsize(tab_info, font=font)
    img_width = img_size[0] + space * 2
    table_height = img_size[1] + space * 2
    img_height = table_height + kwargs['table_botton_heght'] + kwargs['table_top_heght'] + 5
    im_new = im.resize((img_width, img_height))
    del draw
    del im
    draw = ImageDraw.Draw(im_new, 'RGB')

    draw.multiline_text((space, kwargs['table_top_heght']), tab_info + '\n\n', fill=(0, 0, 0), font=font)
    ### 表标题--------------------------
    if 'table_title' in kwargs:
        title_left_padding = (img_width - len(kwargs['table_title']) * kwargs['table_title_font_size']) / 2
        draw.multiline_text((title_left_padding, space), kwargs['table_title'], fill=(17, 0, 0), font=font2,
                            align="center")
    y = table_height + space / 2
    ### 描述内容-----------------------------------
    if 'describe' in kwargs:
        y = y + kwargs['default_font_size']
        frist_row = kwargs['describe'].pop(0)
        draw.text((space, y), frist_row, fill=(255, 0, 0), font=font)
        for describe_row in kwargs['describe']:
            y = y + kwargs['default_font_size'] + line_height
            draw.text((space, y), describe_row, fill=(0, 0, 0), font=font)
    if 'historyalarm' in kwargs:
        y = y + kwargs['default_font_size']
        frist_row = kwargs['historyalarm'].pop(0)
        draw.text((space, y), frist_row, fill=(255, 0, 0), font=font)
        for describe_row in kwargs['historyalarm']:
            y = y + kwargs['default_font_size'] + line_height
            draw.text((space, y), describe_row, fill=(0, 0, 0), font=font)
    del draw
    ### 保存为图片
    im_new.save(img_name, kwargs['img_type'])
    return True


#####################################################################绘制水滴图---得分和击败比例
# https://blog.csdn.net/weixin_40840880/article/details/102944117
# #导出模块
def Score_plot(score, bit, savepath, path_wkimg):
    # 定义函数
    cLiquid = (
        Liquid()
            .add("水滴图", [score / 100], is_outline_show=False, is_animation=False,
                 label_opts=opts.LabelOpts(is_show=False, font_size=50, position="inside"))
            .set_global_opts()
    )

    cLiquid.render('temp.html')  # 定格，括号内为文件名，注意单引号说明文件名省html后缀，双引号文件名，生成后缀，也可以加入路径，默认为代码.py所在的路径或文件夹。

    #########################将html文件转化成图片
    # https://blog.csdn.net/bobyuan888/article/details/108769274
    cfg = imgkit.config(wkhtmltoimage=path_wkimg)
    # 1、将html文件转为图片
    imgkit.from_file('temp.html', savepath, config=cfg)
    ###################截取部分图片
    # 打开一张图
    img = Image.open(savepath)
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度
    x = 0.25 * w
    y = 0.25 * h
    w = 0.4 * w
    h = 0.6 * h
    # 开始截取
    region = img.crop((x, y, x + w, y + h))
    # 保存图片
    region.save(savepath)
    os.remove('temp.html')
    #######################在图片上添加文字
    bk_img = cv2.imread(savepath)
    # 设置需要显示的字体
    fontpath = "font/simsun.ttc"
    font = ImageFont.truetype(fontpath, 50)
    font2 = ImageFont.truetype(fontpath, 20)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # 绘制文字信息
    draw.text((110, 90), str(score) + '分', font=font, fill=(255, 255, 255))
    draw.text((50, 270), '* 设备稳定性击败了' + str(bit) + '%同类设备', font=font2, fill=(0, 0, 255))
    bk_img = np.array(img_pil)
    ####显示图片
    # cv2.imshow("add_text",bk_img)
    # cv2.waitKey()
    ###保存图片
    cv2.imwrite(savepath, bk_img)


#  #######################绘制
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# score=70
# if score<60:
#     color='r'
# elif score<80:
#     color='b'
# else:
#     color='g'
# # ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor= 'yellow', alpha=0.3)
# cir1 = Circle(xy = (0.0, 0.0), radius=2,fc=color,alpha=0.7,)
# # ax.add_patch(ell1)
# ax.add_patch(cir1)
#
# ax.text(-0.8,-0.1,str(score)+'分',fontsize=50,color='w')
# plt.axis('scaled')
# plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length
# plt.show()

###########################################################去除数字字母符号等
# import re
# s = '1123*#$ 中abc国'
# str = re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", s)
# # 去除不可见字符
# str = re.sub('[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+', '',str)
# print(str)

if __name__ == "__main__":
    ####################################
    data = [
        ["单一", "周同比", "20190118", "20190111", "日同比", " 20190118 "],
        ['日注册人数', ' ', ' ', ' ', ' ', ' '],
        ['日注册人数', ' ', ' ', ' ', ' ', ' '],
        ['日活跃人数', ' ', ' ', ' ', ' ', ' '],
        ['日充值人数', ' ', ' ', ' ', ' ', ' '],
        ['日挂号人数', ' ', ' ', ' ', ' ', ' '],
        ['日充值金额', ' ', ' ', ' ', ' ', ' ']
    ]
    describe = ['专家意见：', '日成交笔数H5与ODPS误差为：-3.4600%，高于2%', '日成交笔数H5与ODPS误差为：-3.4600%，高于2%',
                '日成交笔数H5与ODPS误差为：-3.4600%，高于2%']
    historyalarm = ['历史报警：', '日成交笔数H5与ODPS误差为：-3.4600%，高于2%', '日成交笔数H5与ODPS误差为：-3.4600%，高于2%',
                    '日成交笔数H5与ODPS误差为：-3.4600%，高于2%', '1', '2', '3', '4', '5', '6', '7', '8', '1', '2', '3', '4', '5',
                    '6', '7', '8']
    table_title = '日成交笔数'
    result = create_table_img(data, './/plot_folder_user//t1.png', font='C:\Windows\Fonts\simkai.ttf',
                              describe=describe, historyalarm=historyalarm,
                              table_title=table_title)
    if result:
        print('图表生成成功')
