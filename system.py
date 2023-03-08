# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import predict


from PyQt5.QtWidgets import QApplication, QMainWindow

import system  # module test.py
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QTextEdit
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 718)
        MainWindow.setStyleSheet("QWidget#centralwidget{border-image: url(:/background/vision_transformer/hfuu.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_choose = QtWidgets.QPushButton(self.centralwidget)
        self.btn_choose.setGeometry(QtCore.QRect(60, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.btn_choose.setFont(font)
        self.btn_choose.setObjectName("btn_choose")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 180, 521, 431))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_img = QtWidgets.QLabel(self.groupBox)
        self.label_img.setGeometry(QtCore.QRect(20, 40, 471, 401))
        self.label_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(310, 30, 431, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(600, 180, 391, 431))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 351, 381))
        self.textEdit.setObjectName("textEdit")
        self.btn_see = QtWidgets.QPushButton(self.centralwidget)
        self.btn_see.setGeometry(QtCore.QRect(660, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.btn_see.setFont(font)
        self.btn_see.setObjectName("btn_see")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(810, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 110, 361, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_choose.clicked.connect(self.select_file)
        self.btn_see.clicked.connect(self.loading)
        self.btn_start.clicked.connect(self.genMastClicked)

    class Stream(QObject):
        """Redirects console output to text widget."""
        newText = pyqtSignal(str)

        def write(self, text):
            self.newText.emit(str(text))

    class GenMast(QMainWindow):
        """Main application window."""

        def __init__(self):
            super().__init__()

            # Custom output stream.
            sys.stdout = Stream(newText=self.onUpdateText)

        def onUpdateText(self, text):
            """Write console output to text widget."""
            cursor = self.textEdit.textCursor()
            cursor.movePosition(QTextCursor.End)
            cursor.insertText(text)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.ensureCursorVisible()

        def closeEvent(self, event):
            """Shuts down application on close."""
            # Return stdout to defaults.
            sys.stdout = sys.__stdout__
            super().closeEvent(event)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像识别系统"))
        self.btn_choose.setText(_translate("MainWindow", "选择图片"))
        self.groupBox.setTitle(_translate("MainWindow", "当前图片"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">基于Transformer的标志识别系统</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "识别信息"))
        self.btn_see.setText(_translate("MainWindow", "图片预览"))
        self.btn_start.setText(_translate("MainWindow", "开始识别"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "图片路径"))

    def select_file(self):
        """选择文件
        """
        filename, _ = QFileDialog.getOpenFileName(None, "getOpenFileName",
                                                         './',  # 文件的起始路径
                                                         "All Files (*);;JSON Files (*.json)")  # 设置文件类型
        self.lineEdit.setText(filename)

    def loading(self):
        png = QtGui.QPixmap(self.lineEdit.text()).scaled(self.label_img.width(), self.label_img.height())
        self.label_img.setPixmap(png)

    def genMastClicked(self):
        """Runs the main function."""
        print(self.lineEdit.text())
        f = open('D:/path.txt','w')
        a = self.lineEdit.text()
        f.write(a)
        f.close()
        self.printhello()
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        print('Done.')



    def printhello(self):
        predict.main()

    def __init__(self):
        super().__init__()


        # Custom output stream.
        sys.stdout = Stream(newText=self.onUpdateText)

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

class Stream(QObject):
    """Redirects console output to text widget."""
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))



import background_rc
if __name__ == '__main__':
 app = QApplication(sys.argv)
 app.aboutToQuit.connect(app.deleteLater)
 myMainWindow = QMainWindow()
 myUi = system.Ui_MainWindow()
 myUi.setupUi(myMainWindow)
 myMainWindow.show()
 sys.exit(app.exec_())
