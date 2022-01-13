import os
import xml.etree.ElementTree as ET

targetDir = "C:/Users/user/Desktop/data/"
num = 1

##targetDir에서 .xml파일 이름들 리스트로 가져오기
file_list = os.listdir(targetDir)
xml_list = []
for file in file_list:
    if ".xml" in file:
        xml_list.append(file)

##모든 .xml파일에 대해 수정
for xml_file in xml_list:
    target_path = targetDir + xml_file
    targetXML = open(target_path, "rt", encoding="UTF8")

    tree = ET.parse(targetXML)

    root = tree.getroot()

    # <name> 수정
    filename_tag = root.find("name")
    original = filename_tag.text
    modified = original.replace(r".png", r".jpg")
    filename_tag.text = modified

    print("[" + str(num) + "]" + xml_file + "[success]")

    tree.write(target_path)
    num += 1

print("finished")
