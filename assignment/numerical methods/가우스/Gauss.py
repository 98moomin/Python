import sys
import copy
from PyQt5.QtWidgets import *
from PyQt5 import uic
from numpy import array, zeros

form_class = uic.loadUiType("main.ui")[0]
inputFile = "Gauss_Input.txt"
rawdata = ""
data = []


class main(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            self.makeData()
            tmp = array(data)
            arrdata = copy.deepcopy(tmp)
        except:
            QMessageBox.about(self, "Waring", "Gauss_Input.txt 파일이 없습니다.")
            self.inputBox.setText("Gauss_Input.txt 파일이 없습니다.\n파일을 확인후 프로그램을 재시작해주세요")
            print("파일 없습니다.")
        self.startBtn.clicked.connect(lambda: self.getSolution(arrdata))

    def makeData(self):
        with open(inputFile) as file_object:
            rawdata = file_object.read()
        arr = rawdata.split("\n")
        for item in arr:
            arr2 = []
            tmp = item.strip().split(" ")
            for item2 in tmp:
                arr2.append(float(item2))
            data.append(arr2)

        tmp = ""
        for item in data:
            for item2 in item:
                tmp += str(int(item2)) + " "
            tmp += "\n"
        self.inputBox.setText(tmp)

        if len(data) == len(data[0]) - 1:
            pass
        else:
            QMessageBox.about(
                self,
                "Waring",
                "올바르지 않은 행렬식입니다.\nGauss_Input.txt의 행렬을 형식에 맞추시고 재시작해주세요..",
            )

    def gauss(self, arrdata):
        for i in range(len(arrdata) - 1):
            for j in range(i, len(arrdata) - 1):  # 부분 피봇팅
                for k in range(j + 1, len(arrdata)):
                    if abs(arrdata[j][i]) < abs(arrdata[k][i]):
                        tmp = copy.deepcopy(arrdata[j])
                        arrdata[j] = arrdata[k]
                        arrdata[k] = tmp
                    elif abs(arrdata[j][i]) == abs(arrdata[k][i]):
                        if abs(arrdata[j][i + 1]) < abs(arrdata[k][i + 1]):
                            tmp = copy.deepcopy(arrdata[j])
                            arrdata[j] = arrdata[k]
                            arrdata[k] = tmp
            for j in range(i + 1, len(arrdata)):  # 가우스 소거
                if arrdata[i][i] == 0:
                    break
                mul = arrdata[j][i] / arrdata[i][i]
                for k in range(len(arrdata) + 1):
                    tmp1 = arrdata[i][k] * mul
                    arrdata[j][k] -= tmp1

    def getSolution(self, arrdata):
        self.gauss(arrdata)
        print("Gauss 소거법이 수행된 이후 행렬")
        print(arrdata)
        arrA = copy.deepcopy(arrdata[0 : len(arrdata), 0 : len(arrdata)])
        arrB = copy.deepcopy(arrdata[0 : len(arrdata), len(arrdata) :])
        result = zeros(len(arrdata))
        for i in range(len(arrdata) - 1, -1, -1):
            tmp = arrB[i]
            for j in range(len(arrdata) - 1, i - 1, -1):
                if i == j:
                    tmp /= arrA[i][j]
                    result[i] = tmp
                else:
                    tmp -= arrA[i][j] * result[j]
        print("구하고자 하는 해")
        print(result)

        f = open("Gauss_Output.txt", "w", encoding="UTF-8")
        string = ""
        f.write("가우스 소거법이 수행된 이후의 행렬\n")
        string += "가우스 소거법이 수행된 이후의 행렬\n"
        tmp = []
        for item in arrdata:
            tmp.append(item.tolist())
        for item in tmp:
            for item2 in item:
                f.write(str(item2) + " ")
                string += str(item2) + " "
            f.write("\n")
            string += "\n"

        f.write("\n구하고자 하는 해\n")
        string += "\n구하고자 하는 해\n"
        tmp = []
        for item in result:
            tmp.append(item.tolist())
        for item in tmp:
            f.write(" " + str(item) + "\n")
            string += str(item) + "\n"

        self.outputBox.setText(string)
        f.close


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = main()
    Window.show()
    app.exec_()
