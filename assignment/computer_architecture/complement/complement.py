# Copyright 2020 moomin(Donga_Univ/1724560/박무진). All rights reserved

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main.ui")[0]


class main(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.executeBtn.clicked.connect(self.executeFunction)  # ui버튼과 함수 연결

    def executeFunction(self):
        maxNum = 9223372036854775807
        userInputNum = self.userInput.text()
        if userInputNum == "" or userInputNum in " ":
            QMessageBox.about(self, "오류", "입력된 값이 없습니다.")
        elif " " in userInputNum:
            QMessageBox.about(self, "오류", "입력된 값에 공백이 존재합니다.")
        ##################################### 이스터에그 ######################################
        elif userInputNum == "무진" or userInputNum == "무민" or userInputNum == "박무진":
            self.result_0.setText("❤")
            self.result_1.setText("❤")
            self.result_2.setText("❤")
        ##################################### 이스터에그 ######################################
        else:
            try:
                if "," in userInputNum:
                    userInputNum = userInputNum.replace(",", "")
                if int(userInputNum) < 0:
                    userInputNum = -(int(userInputNum))
                    if userInputNum > maxNum:
                        QMessageBox.about(
                            self, "Warning", "64bit 범위 내에서 입력 가능한 숫자보다 큽니다."
                        )
                    else:
                        binaryNumber = []
                        # 이진수로 변환
                        while userInputNum > 0:
                            div = userInputNum // 2
                            mod = userInputNum % 2
                            userInputNum = div
                            binaryNumber.append(mod)
                        self.signedMagnitude(binaryNumber)
                elif userInputNum == "-0":
                    self.result_0.setText(
                        "1000000000000000000000000000000000000000000000000000000000000000"
                    )
                    self.result_1.setText(
                        "1111111111111111111111111111111111111111111111111111111111111111"
                    )
                    self.result_2.setText("-")
                elif userInputNum == "+0":
                    self.result_0.setText(
                        "0000000000000000000000000000000000000000000000000000000000000000"
                    )
                    self.result_1.setText(
                        "0000000000000000000000000000000000000000000000000000000000000000"
                    )
                    self.result_2.setText(
                        "0000000000000000000000000000000000000000000000000000000000000000"
                    )
                else:
                    QMessageBox.about(self, "오류", "음의 정수만 입력해주세요")
                    self.resetInfo()
            except:
                QMessageBox.about(self, "오류", "음의 정수만 입력해주세요")
                self.resetInfo()

    def signedMagnitude(self, binaryNumber):  # 부호와 크기 함수
        if binaryNumber[len(binaryNumber) - 1] == 1:
            binaryNumber.append(0)

        while len(binaryNumber) % 64 != 0:
            binaryNumber.append(0)

        binaryNumber.pop()
        binaryNumber.append(1)
        binaryNumber.reverse()

        resultStr = ""
        for item in binaryNumber:
            resultStr += str(item)

        self.result_0.setText(resultStr)  # 결과 display
        self.result_0.repaint()

        self.oneSComplement(binaryNumber)

    def oneSComplement(self, binaryNumber):  # 1의 보수 함수
        for item in range(1, len(binaryNumber)):
            if binaryNumber[item] == 1:
                binaryNumber[item] = 0
            else:
                binaryNumber[item] = 1
        resultStr = ""
        for item in binaryNumber:
            resultStr += str(item)

        self.result_1.setText(resultStr)  # 결과 display
        self.result_1.repaint()
        self.twoSComplement(binaryNumber)

    def twoSComplement(self, binaryNumber):  # 2의 보수 함수
        binaryNumber.reverse()
        if binaryNumber[0] == 1:
            for item in range(0, (len(binaryNumber) - 1)):
                if binaryNumber[item] == 0:
                    binaryNumber[item] = 1
                    break
                else:
                    binaryNumber[item] = 0
        else:
            binaryNumber[0] = 1
        binaryNumber.reverse()
        resultStr = ""
        for item in binaryNumber:
            resultStr += str(item)

        self.result_2.setText(resultStr)  # 결과 display
        self.result_2.repaint()

    def resetInfo(self):  # 초기화 함수
        self.result_0.clear()
        self.result_0.repaint()
        self.result_1.clear()
        self.result_1.repaint()
        self.result_2.clear()
        self.result_2.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = main()
    Window.show()
    app.exec_()
