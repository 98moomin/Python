import sys
import copy
from PyQt5.QtWidgets import *
from PyQt5 import uic
from numpy import array, zeros

form_class = uic.loadUiType("main.ui")[0]
inputFile = "LU_Input.txt"
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
            QMessageBox.about(self, "Waring", "LU_Input.txt 파일이 없습니다.")
            self.inputBox.setText("LU_Input.txt 파일이 없습니다.\n파일을 확인후 프로그램을 재시작해주세요")
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

        arr = array(data)
        tmp = copy.deepcopy(arr)
        matA = copy.deepcopy(tmp[0 : len(tmp), 0 : len(tmp)])
        matB = copy.deepcopy(tmp[0 : len(tmp), len(tmp) :])

        a = "A행렬\n"
        for item in matA:
            for item2 in item:
                a += str(item2) + " "
            a += "\n"

        b = "\nB행렬\n"
        for item in matB:
            for item2 in item:
                b += str(item2) + " "
            b += "\n"

        ab = a + b
        self.inputBox.setText(ab)

        if len(data) == len(data[0]) - 1:
            pass
        else:
            QMessageBox.about(
                self, "Waring", "올바르지 않은 행렬식입니다.\nLU_Input.txt의 행렬을 형식에 맞추시고 재시작해주세요.."
            )

    def getSolution(self, arrdata):
        tmpA = copy.deepcopy(arrdata[0 : len(arrdata), 0 : len(arrdata)])
        tmpB = copy.deepcopy(arrdata[0 : len(arrdata), len(arrdata) :])
        tmpL = [[0 for col in range(len(tmpA))] for row in range(len(tmpA))]
        tmpU = [[0 for col in range(len(tmpA))] for row in range(len(tmpA))]

        for i in range(len(tmpA)):
            for j in range(i, len(tmpA)):  # U
                tmp = 0
                for k in range(i):
                    tmp += tmpL[i][k] * tmpU[k][j]
                tmpU[i][j] = tmpA[i][j] - tmp

            for j in range(i, len(tmpA)):  # L
                if i == j:
                    tmpL[i][i] = 1
                else:
                    tmp = 0
                    for k in range(i):
                        tmp += tmpL[j][k] * tmpU[k][i]
                    tmpL[j][i] = (tmpA[j][i] - tmp) / tmpU[i][i]

        L = array(tmpL)
        U = array(tmpU)

        f = open("LU_Output.txt", "w", encoding="UTF-8")

        f.write("분해된 L 행렬\n")
        print("분해된 L 행렬")
        print(L)
        tmp = ""
        for item in L:
            for item2 in item:
                f.write(str(item2) + " ")
                tmp += str(item2) + " "
            f.write("\n")
            tmp += "\n"
        self.matrixLBox.setText(tmp)

        f.write("\n분해된 U 행렬\n")
        print("\n분해된 U 행렬")
        print(U)
        tmp = ""
        for item in U:
            for item2 in item:
                f.write(str(item2) + " ")
                tmp += str(item2) + " "
            f.write("\n")
            tmp += "\n"
        self.matrixUBox.setText(tmp)

        tmpY = [0.0 for col in range(len(tmpL))]
        Y = array(tmpY)
        B = array(tmpB)
        for i in range(len(tmpL)):
            Y[i] = B[i]
            for j in range(i):
                Y[i] -= L[i][j] * Y[j]

        f.write("\nY 행렬\n")
        print("\nY 행렬")
        print(Y)
        tmp = ""
        for item in Y:
            tmp += str(item) + "\n"
            f.write(str(item) + "\n")
        self.matrixYBox.setText(tmp)

        tmpX = [0.0 for col in range(len(tmpU))]
        X = array(tmpX)
        for i in range(len(U) - 1, -1, -1):
            tmp = Y[i]
            for j in range(len(U) - 1, i - 1, -1):
                if i == j:
                    tmp /= U[i][j]
                    X[i] = tmp
                else:
                    tmp -= U[i][j] * X[j]
        f.write("\nX 행렬(구하고자하는 해)\n")
        print("\nX 행렬(구하고자하는 해)")
        print(X)
        tmp = ""
        for item in X:
            tmp += str(item) + "\n"
            f.write(str(item) + "\n")
        self.matrixXBox.setText(tmp)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = main()
    Window.show()
    app.exec_()
