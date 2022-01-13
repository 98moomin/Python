import requests

carName = "benz"
savePath = r"D:\livinglab\label\cars\car"

# 벤츠 (1 ~ 72)
imgLink = "https://imgd.aeplcdn.com/1280x720/cw/360/mercedesbenz/1023/closed-door/{}.jpg?wm=1&q=80&v=20180219015959"

# 벤츠
# 1~3 / 71 ~ 72

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

cnt = 239

for idx in range(1, 4):
    download_file = requests.get(imgLink.format(idx), headers=headers)
    photo = open(savePath + "\\car_{}.jpg".format(cnt), "wb")
    photo.write(download_file.content)
    photo.close()
    cnt += 1

for idx in range(71, 73):
    download_file = requests.get(imgLink.format(idx), headers=headers)
    photo = open(savePath + "\\car_{}.jpg".format(cnt), "wb")
    photo.write(download_file.content)
    photo.close()
    cnt += 1

print(cnt)
print("Img Download Finish")
