from numpy import array
from numpy.linalg import det
import copy

lines = []
filename = "data.txt"
try:
    with open(filename) as file_object:
        lines.append(file_object.read())
        print(lines)
except:
    print("test_data.txt 파일이 없습니다")
    exit()

test = lines[0].split("\n")

if len(test) == 1:
    print("txt에 값이 없습니다.")
    exit()
else:
    b = []
    a = []
    try:
        if len(test) == 4:  # 2 X 2
            b.append(int(test[2]))
            b.append(int(test[3]))
            for i, item in enumerate(test):
                atmp = []
                if i < 2:
                    tmp = item.split(" ")
                    for item2 in tmp:
                        atmp.append(int(item2))
                    a.append(atmp)
            a = array(a)
            b = array(b)
            a1 = copy.deepcopy(a)
            a2 = copy.deepcopy(a)
            for i in range(2):
                a1[i][0] = b[i]
                a2[i][1] = b[i]
            detA = det(a)
            detA1 = det(a1)
            detA2 = det(a2)
            print("|A| = ", detA, "|A1| = ", detA1, "|A2| = ", detA2)
            x1 = detA1 / detA
            x2 = detA2 / detA
            print("x1 = ", x1, "x2 = ", x2)
        else:  # 3 X 3
            b.append(int(test[3]))
            b.append(int(test[4]))
            b.append(int(test[5]))
            for i, item in enumerate(test):
                atmp = []
                if i < 3:
                    tmp = item.split(" ")
                    for item2 in tmp:
                        atmp.append(int(item2))
                    a.append(atmp)
            a = array(a)
            b = array(b)
            a1 = copy.deepcopy(a)
            a2 = copy.deepcopy(a)
            a3 = copy.deepcopy(a)
            for i in range(3):
                a1[i][0] = b[i]
                a2[i][1] = b[i]
                a3[i][2] = b[i]
            detA = det(a)
            detA1 = det(a1)
            detA2 = det(a2)
            detA3 = det(a3)
            print("|A| = ", detA, "|A1| = ", detA1, "|A2| = ", detA2, "|A3| = ", detA3)
            x1 = detA1 / detA
            x2 = detA2 / detA
            x3 = detA3 / detA
            print("x1 = ", x1, "x2 = ", x2, "x3 = ", x3)
    except:
        print("행렬값이 제대로 되어 있는지 확인해주세요")
        exit()
