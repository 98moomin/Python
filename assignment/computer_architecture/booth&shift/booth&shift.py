import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main.ui")[0]


class main(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calcBtn.clicked.connect(self.boothAlgorithm)  # boothalgorithm
        self.calcBtn.clicked.connect(self.shiftAlgorithm)

    def shiftAlgorithm(self):
        resultData = ""
        if(self.input1.text() == "" or self.input2.text() == "" or self.input1.text() in " " or self.input2.text() in " "):
            QMessageBox.about(self, "error", "Need Input Value")
        elif(" " in self.input1.text() or " " in self.input2.text()):
            QMessageBox.about(self, "error", "입력된 값에 공백이 존재합니다.")
        else:
            try:
                isOneNeg = False
                isTwoNeg = False
                sign = True
                input1 = int(self.input1.text())
                input2 = int(self.input2.text())
                selectBit = self.bitSelector.currentText()
                if(int(selectBit) >= self.typeOfBit(input1) and int(selectBit) >= self.typeOfBit(input2)):
                    if(input1 < 0):
                        input1 = -(input1)
                        isOneNeg = True
                    if(input2 < 0):
                        input2 = -(input2)
                        isTwoNeg = True
                    if((isOneNeg == True and isTwoNeg == True) or (isOneNeg == False and isTwoNeg == False)):
                        sign = True
                    else:
                        sign = False
                    multiplier = self.makeBinaryNumber(input1)  # 피승수
                    multiplicand = self.makeBinaryNumber(input2)  # 승수
                    input1 = int(self.input1.text())
                    input2 = int(self.input2.text())
                    if(self.typeOfBit(input1) > self.typeOfBit(input2)):
                        result = [0 for i in range(self.typeOfBit(input1)*2)]
                        maxlen = self.typeOfBit(input1)
                    else:
                        result = [0 for i in range(self.typeOfBit(input2)*2)]
                        maxlen = self.typeOfBit(input2)
                    tmp = list(multiplicand)
                    tmp.reverse()
                    resultData += "=======================================================shift=======================================================\n"
                    resultData += "0 단계\n"
                    show = ""
                    if(sign == True):
                        show += "( + )"
                    else:
                        show += "( - )"
                    resultData += "최종부호 : " + show + "\n"
                    show = ""
                    for item in multiplicand:
                        show += str(item)
                    resultData += "승수 : " + show + "\n"
                    show = ""
                    for item in multiplier:
                        show += str(item)
                    resultData += "피승수 : " + show + "\n"
                    show = ""
                    for item in result:
                        show += str(item)
                    resultData += "--------------------------------------------------------------------------------------------------------------\n"
                    # resultData += show + "\n"
                    for item in range(maxlen):
                        # resultData += str(item+1) + "단계\n"
                        if(tmp[item] == 0):
                            for item2 in result:
                                resultData += str(item2)
                            resultData += "\n"
                            for item2 in range(len(result)):
                                resultData += "0"
                            resultData += "\n"
                            for item2 in result:
                                resultData += str(item2)
                            resultData += "\n"
                            result.pop()
                            result.reverse()
                            result.append(0)
                            result.reverse()
                            show = ""
                            for item2 in result:
                                show += str(item2)
                            resultData += show + "\n"
                        else:
                            show = ""
                            for item2 in result:
                                show += str(item2)
                            resultData += show + "\n"
                            shift = []
                            for item2 in multiplier:
                                shift.append(item2)
                            while(len(shift) < len(result)):
                                shift.append(0)
                            tmpArr = list(shift)
                            result = self.plusWithResult(result, tmpArr)
                            for item2 in shift:
                                resultData += str(item2)
                            resultData += "\n"
                            show = ""
                            for item2 in result:
                                show += str(item2)
                            resultData += show + "\n"
                            result.pop()
                            result.reverse()
                            result.append(0)
                            result.reverse()
                            show = ""
                            for item2 in result:
                                show += str(item2)
                            resultData += show + "\n"
                        resultData += "------------------------------------------------------------------------------------------------------" + \
                            str(item+1) + "사이클\n"
                    reusltArr = []
                    if(sign == False):
                        tmp = list(result)
                        reusltArr = self.makeTwoSClompLe(tmp, 1)
                        reusltArr.reverse()
                    else:
                        reusltArr = result
                    show = ""
                    for item in reusltArr:
                        show += str(item)
                    resultData += "\n결과 : " + show + \
                        " " + str(input1*input2) + "\n\n"
                    resultData += "=======================================================shift=======================================================\n"
                    self.resultArea_2.setText(resultData)
                else:
                    QMessageBox.about(self, "error", "bit를 늘려주세요.")
            except:
                QMessageBox.about(self, "error", "정수로만 입력해주세요")

    def boothAlgorithm(self):
        resultData = ""
        if(self.input1.text() == "" or self.input2.text() == "" or self.input1.text() in " " or self.input2.text() in " "):
            QMessageBox.about(self, "error", "Need Input Value")
        elif(" " in self.input1.text() or " " in self.input2.text()):
            QMessageBox.about(self, "error", "입력된 값에 공백이 존재합니다.")
        else:
            try:
                input1 = int(self.input1.text())
                input2 = int(self.input2.text())
                selectBit = self.bitSelector.currentText()
                if(int(selectBit) >= self.typeOfBit(input1) and int(selectBit) >= self.typeOfBit(input2)):
                    multiplier = self.makeBinaryNumber(input1)  # 피승수
                    multiplicand = self.makeBinaryNumber(input2)  # 승수
                    # result = 부분 누적곱
                    if(self.typeOfBit(input1) > self.typeOfBit(input2)):
                        result = [0 for i in range(self.typeOfBit(input1)*2)]
                        maxlen = self.typeOfBit(input1)
                    else:
                        result = [0 for i in range(self.typeOfBit(input2)*2)]
                        maxlen = self.typeOfBit(input2)

                    tmp = list(multiplicand)  # 추가비트해서 쉬프트 판별하는 배열
                    tmp.append(0)
                    show = ""
                    for item in tmp:
                        show += str(item)
                    tmp.reverse()
                    cnt = 0
                    resultData += "=======================================================booth=======================================================\n"
                    resultData += "0 단계\n"
                    resultData += "승수 : " + show + " <- 마지막 0 = 추가 비트\n"
                    show = ""
                    for item in multiplier:
                        show += str(item)
                    resultData += "피승수 : " + show + "\n"
                    show = ""
                    for item in result:
                        show += str(item)
                    resultData += "누적 부분곱 : " + show + "\n"
                    resultData += "--------------------------------------------------------------------------------------------------------------\n"
                    for item in range(maxlen):
                        resultData += str(item+1) + "단계\n"
                        if(tmp[item+1] == 0 and tmp[item] == 0):
                            resultData += "승수 : " + \
                                str(tmp[item+1]) + str(tmp[item]) + \
                                "-> 피승수를 왼쪽 시프트\n"
                            shift = []
                            show = []
                            for item2 in range(maxlen-cnt):
                                shift.append(0)
                                show.append('-')
                            for item2 in multiplier:
                                shift.append(0)
                                show.append(str(item2))
                            while(len(shift) < len(result)):
                                shift.append(0)
                                show.append('-')
                            resultData += "피승수 : " + ''.join(show) + "\n"
                            result = self.plusWithResult(result, shift)
                            show = ""
                            for item2 in result:
                                show += str(item2)
                            resultData += "누적 부분곱 : " + show + "\n"
                            cnt += 1
                        elif(tmp[item+1] == 0 and tmp[item] == 1):
                            resultData += "승수 : " + \
                                str(tmp[item+1]) + str(tmp[item]) + \
                                "-> 누적 부분곱에 피승수를 더한 후 피승수를 왼쪽 시프트\n"
                            shift = []
                            show = []
                            if(multiplier[0] == 0):
                                for item2 in range(maxlen-cnt):
                                    shift.append(0)
                                    show.append('-')
                            else:
                                for item2 in range(maxlen-cnt):
                                    shift.append(1)
                                    show.append('-')
                            for item2 in multiplier:
                                shift.append(item2)
                                show.append(str(item2))
                            while(len(shift) < len(result)):
                                shift.append(0)
                                show.append('-')
                            resultData += "피승수 : " + ''.join(show) + "\n"
                            result = self.plusWithResult(result, shift)
                            show = ""
                            for item2 in result:
                                show += str(item2)
                            resultData += "누적 부분곱 : " + show + "\n"
                            cnt += 1
                        elif(tmp[item+1] == 1 and tmp[item] == 0):
                            resultData += "승수 : " + \
                                str(tmp[item+1]) + str(tmp[item]) + \
                                "-> 누적 부분곱에 피승수를 뺀 후 피승수를 왼쪽 시프트\n"
                            shift = []
                            show = []
                            tmpArr = list(multiplier)
                            tmpArr = self.makeTwoSClompLe(tmpArr, 1)
                            tmpArr.reverse()
                            if(tmpArr[0] == 0):
                                for item2 in range(maxlen-cnt):
                                    shift.append(0)
                                    show.append('-')
                            else:
                                for item2 in range(maxlen-cnt):
                                    shift.append(1)
                                    show.append('-')
                            for item2 in tmpArr:
                                shift.append(item2)
                            for item2 in multiplier:
                                show.append(str(item2))
                            while(len(shift) < len(result)):
                                shift.append(0)
                                show.append('-')
                            resultData += "피승수 : " + ''.join(show) + "\n"
                            result = self.plusWithResult(result, shift)
                            show = ""
                            for item2 in result:
                                show += str(item2)
                            resultData += "누적 부분곱 : " + show + "\n"
                            cnt += 1
                        elif(tmp[item+1] == 1 and tmp[item] == 1):
                            resultData += "승수 : " + \
                                str(tmp[item+1]) + str(tmp[item]) + \
                                "-> 피승수를 왼쪽 시프트\n"
                            shift = []
                            show = []
                            for item2 in range(maxlen-cnt):
                                shift.append(0)
                                show.append('-')
                            for item2 in multiplier:
                                shift.append(0)
                                show.append(str(item2))
                            while(len(shift) < len(result)):
                                shift.append(0)
                                show.append('-')
                            resultData += "피승수 : " + ''.join(show) + "\n"
                            result = self.plusWithResult(result, shift)
                            show = ""
                            for item2 in result:
                                show += str(item2)
                            resultData += "누적 부분곱 : " + show + "\n"
                            cnt += 1
                        resultData += "--------------------------------------------------------------------------------------------------------------\n"
                    show = ""
                    for item2 in result:
                        show += str(item2)
                    resultData += "\n결과 : " + show + \
                        " " + str(input1*input2) + "\n\n"
                    resultData += "=======================================================booth=======================================================\n"

                    self.resultArea.setText(resultData)
                else:
                    QMessageBox.about(self, "error", "bit를 늘려주세요.")
            except:
                QMessageBox.about(self, "error", "정수로만 입력해주세요")

    def makeTwoSClompLe(self, arr, jud):
        if(jud == 0):
            for item in range(1, len(arr)):
                if arr[item] == 1:
                    arr[item] = 0
                else:
                    arr[item] = 1

            arr.reverse()
            if arr[0] == 1:
                for item in range(0, (len(arr) - 1)):
                    if arr[item] == 0:
                        arr[item] = 1
                        break
                    else:
                        arr[item] = 0
            else:
                arr[0] = 1
        else:
            for item in range(0, len(arr)):
                if arr[item] == 1:
                    arr[item] = 0
                else:
                    arr[item] = 1

            arr.reverse()
            if arr[0] == 1:
                for item in range(0, (len(arr) - 1)):
                    if arr[item] == 0:
                        arr[item] = 1
                        break
                    else:
                        arr[item] = 0
            else:
                arr[0] = 1

        return arr

    def plusWithResult(self, adding, calMul):
        tmp = []
        upper = 0
        adding.reverse()
        calMul.reverse()
        i = 0
        while(i < len(adding)):
            if(adding[i] + calMul[i] == 0):
                tmp.append(0)
            elif(adding[i] + calMul[i] == 1):
                tmp.append(1)
            elif(adding[i] + calMul[i] == 2):
                tmp.append(0)
                i += 1
                while(i < len(adding)):
                    if(adding[i] == 0 and calMul[i] == 0):
                        tmp.append(1)
                        break
                    elif(adding[i] == 1 and calMul[i] == 1):
                        tmp.append(1)
                        i += 1
                    else:
                        tmp.append(0)
                        i += 1
            i += 1

        tmp.reverse()
        return tmp

    def makeBinaryNumber(self, inputNum):
        binaryNumber = []
        # 입력들어온 숫자가 음수인지 판별
        if(inputNum < 0):
            isNegative = True
            number = -(inputNum)
        else:
            isNegative = False
            number = inputNum

        bit = self.typeOfBit(number)
        if(bit != 0):
            # 이진수로 변환
            while number > 0:
                div = number // 2
                mod = number % 2
                number = div
                binaryNumber.append(mod)
            if(bit != 0):
                while(len(binaryNumber) % bit != 0):
                    binaryNumber.append(0)
            else:
                print("4, 8, 16, 32, 64 bit 범위내 숫자가 아님.")

            if(isNegative == True):
                binaryNumber.pop()
                binaryNumber.append(1)
                binaryNumber.reverse()
                binaryNumber = self.makeTwoSClompLe(binaryNumber, 0)

            binaryNumber.reverse()
        else:
            print("비트 범위를 벗어난 수입니다.")

        return binaryNumber

    def typeOfBit(self, num):
        if(num < 0):
            num = -(num)
        if(0 <= num and num < 8):
            return 4
        elif(8 <= num and num < 128):
            return 8
        elif(128 <= num and num < 32768):
            return 16
        elif(32768 <= num and num < 2147483648):
            return 32
        elif(2147483648 <= num and num < 9223372036854775808):
            return 64
        else:
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = main()
    Window.show()
    app.exec_()
