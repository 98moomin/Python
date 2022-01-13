import sys
# import pymysql
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main.ui")[0]

# conn = pymysql.connect(
#     host="",
#     user="",
#     password="",
#     port=0000,
#     db="",
#     charset="utf8",
# )
# curs = conn.cursor(pymysql.cursors.DictCursor)


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.xyFlag = True
        self.check = True
        self.valueA = 0
        self.valueB = 0
        self.cctvName = ""
        self.cctvPort = None

        self.setupUi(self)
        self.imgLoadBtn.clicked.connect(self.imgLoad)
        self.calcBtn.clicked.connect(self.calc)
        self.sendBtn.clicked.connect(self.sendDB)

    def onclick(self, event):
        if self.xyFlag == True:
            self.outputX1.setText(str(event.xdata))
            self.outputY1.setText(str(event.ydata))
            self.xyFlag = False
        else:
            self.outputX2.setText(str(event.xdata))
            self.outputY2.setText(str(event.ydata))
            self.xyFlag = True

    def imgLoad(self):
        plt.close()
        filename = QFileDialog.getOpenFileName(self, "Open File", "./")
        image = img.imread(filename[0])
        fig, ax = plt.subplots()
        plt.imshow(image)
        cid = fig.canvas.mpl_connect("button_press_event", self.onclick)
        plt.show()

    def calc(self):
        plt.close()
        x1 = float(self.outputX1.toPlainText())
        x2 = float(self.outputX2.toPlainText())
        y1 = float(self.outputY1.toPlainText())
        y2 = float(self.outputY2.toPlainText())

        self.valueA = (x1 - x2) / (y1 - y2)
        self.valueB = x1 - (self.valueA * y1)

        self.outputA.setText(str(self.valueA))
        self.outputB.setText(str(self.valueB))

    def sendDB(self):
        self.cctvName = self.inputCctvName.toPlainText()
        self.cctvPort = self.inputCctvPort.toPlainText()
        if self.cctvPort == "":
            self.cctvPort = None

        if self.valueA == 0:
            self.check = False
        if self.valueB == 0:
            self.check = False
        if self.cctvName == "":
            self.check = False

        if self.check:
            # sql 전송하는 부분
            QMessageBox.about(self, "Good", "Success")
        else:
            QMessageBox.about(self, "Bad", "Failed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = WindowClass()
    Window.show()
    app.exec_()