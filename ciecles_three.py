# __author__: "yudongyue"
# date: 2021/3/25
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 读入图像
bk_png = cv2.imread("plot_folder_user/img_4.png")
img_pil = Image.fromarray(bk_png)
draw = ImageDraw.Draw(img_pil)
# 设置需要显示的字体
# font = ImageFont.truetype("font/simsun.ttc", 25, ImageFont.LAYOUT_RAQM)
font = ImageFont.truetype("font/msyhbd.ttc", 25, ImageFont.LAYOUT_RAQM)
font2 = ImageFont.truetype("font/simsun.ttc", 45, ImageFont.LAYOUT_BASIC)
# 绘制文字信息
total_ele = 861123333
ele_per_day = 277728893
total_RMB = 723685204
total_ele_location_dict = {
    "5": (165, 212),
    "6": (156, 212),
    "7": (143, 212),
    "8": (131, 212),
    "9": (122, 212)
}
ele_per_day_location_dict = {
    "5": (454, 212),
    "6": (443, 212),
    "7": (431, 212),
    "8": (418, 212),
    "9": (406, 212)
}
total_RMB__location_dict = {
    "5": (736, 212),
    "6": (722, 212),
    "7": (713, 212),
    "8": (699, 212),
    "9": (685, 212)
}
Ele_data = [['总用电量(KWh)', '日平均用电量（KWh）', '总电费（RMB）'], [total_ele, ele_per_day, total_RMB]]
draw.text((135, 35), '总用电量(kW·h)', font=font, fill=(166, 108, 90), fontweight='bold')
draw.text((392, 35), '日平均用电量(kW·h)', font=font, fill=(199, 188, 233))
draw.text((713, 35), '总电费(RMB)', font=font, fill=(51, 132, 217))
draw.text(total_ele_location_dict[str(len(str(Ele_data[1][0])))], str(Ele_data[1][0]), font=font2, fill=(0, 0, 255))
draw.text(ele_per_day_location_dict[str(len(str(Ele_data[1][1])))], str(Ele_data[1][1]), font=font2, fill=(0, 0, 255))
draw.text(total_RMB__location_dict[str(len(str(Ele_data[1][2])))], str(Ele_data[1][2]), font=font2, fill=(0, 0, 255))
bk_png = np.array(img_pil)
#  显示图片
cv2.imshow("add_text", bk_png)
cv2.waitKey()
#  保存图片
cv2.imencode('.jpg', bk_png)[1].tofile("plot_folder_user/图片_xxx.png")
# cv2.imwrite("plot_folder_user/图片.png", bk_png)
