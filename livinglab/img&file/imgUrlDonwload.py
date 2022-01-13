import os
import ssl
import urllib.request as img
import requests

context = ssl._create_unverified_context()

carName = "benz"
savePath = r"D:\livinglab\source\\"
# 현대
# imgLink = "https://www.hyundai.com"
# imgLink += "/contents/vr360/NE01/exterior/R3G/{}.png"
# imgLink = "https://www-trucknbus.hyundai.com/kr/images/product/360vr/new-power-truck/exterior/white/white-{}-m.png" #트럭
# imgLink = "https://www-trucknbus.hyundai.com/kr/images/product/360vr/superaero-city/exterior/red/red-{}-m.png" #버스

# 기아
# imgLink = "https://www.kia.com"
# imgLink += "/content/dam/kwcms/kr/ko/images/360vr/exterior/XCK-CKA/H4R/H4R_{}.png"

# 벤츠
imgLink = "https://imgd.aeplcdn.com/1280x720/cw/360/mercedesbenz/980/closed-door/{}.jpg?wm=1&q=80&v=20180212062725"


def makedirs(p):
    try:
        if not os.path.exists(p):
            os.makedirs(p)
    except OSError:
        print("Error : Failed to create the directory")


# makedirs(savePath + carName)

# 벤츠 (1 ~ 72)
download_file = requests.get(imgLink.format("1"))
photo = open(savePath + carName + "\\{}_0.jpg".format(carName), "wb")
photo.write(download_file.content)
photo.close()

# 현대 (2 ~ 49)
# img.urlretrieve(
#     imgLink.format("000"), savePath + carName + "\\{}_0.jpg".format(carName)
# )  # 트럭

# img.urlretrieve(
#     imgLink.format("001"), savePath + carName + "\\{}_1.jpg".format(carName)
# )

# cnt = 2

# for idx in range(50, 61):
#     img.urlretrieve(
#         imgLink.format("0" + str(idx)),
#         savePath + carName + "\\" + "{}_{}".format(carName, cnt) + ".jpg",
#     )
#     cnt += 1

# # 기아 (3 ~ 29 삭제)
# img.urlretrieve(imgLink.format("1"), savePath + carName + "\\{}_0.jpg".format(carName))

# cnt = 1

# for idx in range(30, 36):
#     img.urlretrieve(
#         imgLink.format(str(idx)),
#         savePath + carName + "\\" + "{}_{}".format(carName, cnt) + ".jpg",
#     )
#     cnt += 1

print("Img Download Finish")
