import os
import glob
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "C:\\Users\\user\\Desktop\\testImg"  # 바꿀 이미지 경로
fileName = "test_"  # 변환하여 저장할 이미지 이름 차 -> car

tmp = glob.glob(path + "/*")


def makedirs(p):
    try:
        if not os.path.exists(p):
            os.makedirs(p)
    except OSError:
        print("Error : Failed to create the directory")


makedirs(path + "\\newImg")  # 폴더가 없다면 생성

for index1, item in enumerate(tmp):
    all_image_files = glob.glob(item + "/*.png")
    print(index1 + 1, " 폴더 시작")
    for index2, file_path in enumerate(all_image_files):
        img = Image.open(file_path).convert("RGB")
        directories = file_path.split("/")
        tmp = directories[-1].split("\\")
        tmp = tmp[0:-2]
        tmp.append("newImg/" + fileName + str(index1))  # 새로운 이미지가 저장될 폴더명 마지막에 / 꼭 붙여야함
        newPath = "/".join(tmp)
        makedirs(newPath)
        newPath += "/" + fileName + str(index1) + "_" + str(index2) + ".jpg"
        img = img.resize((608, 608))
        img.save(newPath)  # jpg파일로 저장한다.
    print(index1 + 1, " 폴더 완료")
