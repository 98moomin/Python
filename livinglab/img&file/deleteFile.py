import os

folder_path = r"D:\livinglab\label\cars\car"
folders = os.listdir(folder_path)

idx = 1
for folder in folders:
    path = folder_path + r"\{}".format(folder)
    imgs = os.listdir(path)
    print("{} 폴더 시작".format(idx))
    for name in imgs:
        tmp = name.split("_")
        tmp = tmp[1].split(".")
        if int(tmp[0]) > 100:
            target = os.path.join(path, name)
            os.remove(target)
    print("{} 폴더 완료".format(idx))
    idx += 1
