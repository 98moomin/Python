import os
import urllib.request as img

carName = "carName"
savePath = r"C:\Users\user\Desktop\\"

# 현대
imgLink = "https://www.hyundai.com"
imgLink += "/contents/vr360/NE01/exterior/R3G/{}.png"
# imgLink = "https://www-trucknbus.hyundai.com/kr/images/product/360vr/new-power-truck/exterior/white/white-{}-m.png"   # 트럭
# imgLink = "https://www-trucknbus.hyundai.com/kr/images/product/360vr/superaero-city/exterior/red/red-{}-m.png"        # 버스

def makedirs(p):
    try:
        if not os.path.exists(p):
            os.makedirs(p)
    except OSError:
        print("Error : Failed to create the directory")


makedirs(savePath + carName)

img.urlretrieve(
    imgLink.format("001"), savePath + carName + "\\{}_1.jpg".format(carName)
)

cnt = 2

for idx in range(50, 61):
    img.urlretrieve(
        imgLink.format("0" + str(idx)),
        savePath + carName + "\\" + "{}_{}".format(carName, cnt) + ".jpg",
    )
    cnt += 1


print("Img Download Finish")
