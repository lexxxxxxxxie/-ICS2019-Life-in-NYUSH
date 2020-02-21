# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_game.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 600)
        MainWindow.setMinimumSize(QtCore.QSize(960, 600))
        MainWindow.setMaximumSize(QtCore.QSize(960, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 960, 600))
        self.graphicsView.setStyleSheet("border-image: url(:/figure/life_in_NYUSH_v2.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.step = QtWidgets.QPushButton(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(683, 140, 65, 56))
        self.step.setStyleSheet("border-image: url(:/figure/stepbott.png);")
        self.step.setText("")
        self.step.setObjectName("step")
        self.yelmoney = QtWidgets.QLabel(self.centralwidget)
        self.yelmoney.setGeometry(QtCore.QRect(240, 184, 71, 16))
        self.yelmoney.setStyleSheet("border-image: url(:/game/white.png);\n"
"font: 20pt \"appo paint\";")
        self.yelmoney.setText("")
        self.yelmoney.setObjectName("yelmoney")
        self.yelcash = QtWidgets.QLabel(self.centralwidget)
        self.yelcash.setGeometry(QtCore.QRect(240, 205, 71, 16))
        self.yelcash.setStyleSheet("border-image: url(:/game/white.png);\n"
"font: 20pt \"appo paint\";")
        self.yelcash.setText("")
        self.yelcash.setObjectName("yelcash")
        self.yelhouse = QtWidgets.QLabel(self.centralwidget)
        self.yelhouse.setGeometry(QtCore.QRect(240, 232, 71, 16))
        self.yelhouse.setStyleSheet("border-image: url(:/game/white.png);\n"
"font: 20pt \"appo paint\";")
        self.yelhouse.setText("")
        self.yelhouse.setObjectName("yelhouse")
        self.yelname = QtWidgets.QLabel(self.centralwidget)
        self.yelname.setGeometry(QtCore.QRect(233, 156, 81, 21))
        self.yelname.setStyleSheet("border-image: url(:/game/white.png);\n"
"font: 28pt \"appo paint\";")
        self.yelname.setText("")
        self.yelname.setObjectName("yelname")
        self.yelloan = QtWidgets.QLabel(self.centralwidget)
        self.yelloan.setGeometry(QtCore.QRect(240, 255, 71, 16))
        self.yelloan.setStyleSheet("border-image: url(:/game/white.png);\n"
                                   "font: 20pt \"appo paint\";")
        self.yelloan.setText("")
        self.yelloan.setObjectName("yelloan")

        self.bluehouse = QtWidgets.QLabel(self.centralwidget)
        self.bluehouse.setGeometry(QtCore.QRect(240, 401, 71, 15))
        self.bluehouse.setStyleSheet("border-image: url(:/game/white.png);\n"
"font: 20pt \"appo paint\";")
        self.bluehouse.setText("")
        self.bluehouse.setObjectName("bluehouse")
        self.bluename = QtWidgets.QLabel(self.centralwidget)
        self.bluename.setGeometry(QtCore.QRect(231, 329, 81, 21))
        self.bluename.setStyleSheet("border-image: url(:/game/white.png);\n"
"font: 28pt \"appo paint\";")
        self.bluename.setText("")
        self.bluename.setObjectName("bluename")
        self.bluecash = QtWidgets.QLabel(self.centralwidget)
        self.bluecash.setGeometry(QtCore.QRect(240, 377, 71, 16))
        self.bluecash.setStyleSheet("border-image: url(:/game/white.png);\n"
"font: 20pt \"appo paint\";")
        self.bluecash.setText("")
        self.bluecash.setObjectName("bluecash")
        self.bluemoney = QtWidgets.QLabel(self.centralwidget)
        self.bluemoney.setGeometry(QtCore.QRect(240, 356, 71, 16))
        self.bluemoney.setStyleSheet("border-image: url(:/game/white.png);\n"
"font: 20pt \"appo paint\";")
        self.bluemoney.setText("")
        self.bluemoney.setObjectName("bluemoney")

        self.blueloan = QtWidgets.QLabel(self.centralwidget)
        self.blueloan.setGeometry(QtCore.QRect(240, 429, 71, 15))
        self.blueloan.setStyleSheet("border-image: url(:/game/white.png);\n"
                                    "font: 20pt \"appo paint\";")
        self.blueloan.setText("")
        self.blueloan.setObjectName("blueloan")
        self.fate = QtWidgets.QLabel(self.centralwidget)
        self.fate.setGeometry(QtCore.QRect(370, 310, 451, 41))
        self.fate.setStyleSheet("border-image: url(:/game/infoframe.png);\n"
"font: 40pt \"appo paint\"")
        self.fate.setText("")
        self.fate.setObjectName("fate")
        self.stepnum = QtWidgets.QLabel(self.centralwidget)
        self.stepnum.setGeometry(QtCore.QRect(764, 142, 51, 51))
        self.stepnum.setStyleSheet("font: 40pt \"appo paint\";\n"
"border-image: url(:/game/white.png);")
        self.stepnum.setText("")
        self.stepnum.setObjectName("stepnum")
        self.turn = QtWidgets.QLabel(self.centralwidget)
        self.turn.setGeometry(QtCore.QRect(764, 221, 51, 51))
        self.turn.setStyleSheet("font: 40pt \"appo paint\";\n"
"border-image: url(:/game/white.png);")
        self.turn.setText("")
        self.turn.setObjectName("turn")
        self.player1 = QtWidgets.QLabel(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(10, 40, 41, 51))
        self.player1.setStyleSheet("border-image: url(:/figure/yellowman.png);")
        self.player1.setText("")
        self.player1.setObjectName("player1")
        self.player2 = QtWidgets.QLabel(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(60, 40, 41, 51))
        self.player2.setStyleSheet("border-image: url(:/figure/blueman.png);")
        self.player2.setText("")
        self.player2.setObjectName("player2")
        self.green_center = QtWidgets.QLabel(self.centralwidget)
        self.green_center.setGeometry(QtCore.QRect(121, 105, 88, 15))
        self.green_center.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.green_center.setText("")
        self.green_center.setObjectName("green_center")
        self.public_safety = QtWidgets.QLabel(self.centralwidget)
        self.public_safety.setGeometry(QtCore.QRect(209, 105, 103, 15))
        self.public_safety.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.public_safety.setText("")
        self.public_safety.setObjectName("public_safety")
        self.student_life = QtWidgets.QLabel(self.centralwidget)
        self.student_life.setGeometry(QtCore.QRect(312, 105, 138, 15))
        self.student_life.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.student_life.setText("")
        self.student_life.setObjectName("student_life")
        self.Room110_Gallery = QtWidgets.QLabel(self.centralwidget)
        self.Room110_Gallery.setGeometry(QtCore.QRect(450, 105, 103, 15))
        self.Room110_Gallery.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Room110_Gallery.setText("")
        self.Room110_Gallery.setObjectName("Room110_Gallery")
        self.mail_room = QtWidgets.QLabel(self.centralwidget)
        self.mail_room.setGeometry(QtCore.QRect(553, 105, 100, 15))
        self.mail_room.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mail_room.setText("")
        self.mail_room.setObjectName("mail_room")
        self.luckin = QtWidgets.QLabel(self.centralwidget)
        self.luckin.setGeometry(QtCore.QRect(653, 105, 103, 15))
        self.luckin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.luckin.setText("")
        self.luckin.setObjectName("luckin")
        self.cafeteria = QtWidgets.QLabel(self.centralwidget)
        self.cafeteria.setGeometry(QtCore.QRect(755, 105, 85, 15))
        self.cafeteria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cafeteria.setText("")
        self.cafeteria.setObjectName("cafeteria")
        self.auditorium = QtWidgets.QLabel(self.centralwidget)
        self.auditorium.setGeometry(QtCore.QRect(842, 200, 13, 92))
        self.auditorium.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.auditorium.setText("")
        self.auditorium.setObjectName("auditorium")
        self.the_box = QtWidgets.QLabel(self.centralwidget)
        self.the_box.setGeometry(QtCore.QRect(842, 120, 13, 80))
        self.the_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.the_box.setText("")
        self.the_box.setObjectName("the_box")
        self.cafe = QtWidgets.QLabel(self.centralwidget)
        self.cafe.setGeometry(QtCore.QRect(842, 292, 13, 92))
        self.cafe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cafe.setText("")
        self.cafe.setObjectName("cafe")
        self.bursar = QtWidgets.QLabel(self.centralwidget)
        self.bursar.setGeometry(QtCore.QRect(842, 384, 13, 92))
        self.bursar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bursar.setText("")
        self.bursar.setObjectName("bursar")
        self.IT_center = QtWidgets.QLabel(self.centralwidget)
        self.IT_center.setGeometry(QtCore.QRect(754, 480, 85, 15))
        self.IT_center.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IT_center.setText("")
        self.IT_center.setObjectName("IT_center")
        self.library = QtWidgets.QLabel(self.centralwidget)
        self.library.setGeometry(QtCore.QRect(651, 480, 103, 15))
        self.library.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.library.setText("")
        self.library.setObjectName("library")
        self.arc = QtWidgets.QLabel(self.centralwidget)
        self.arc.setGeometry(QtCore.QRect(553, 480, 99, 15))
        self.arc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.arc.setText("")
        self.arc.setObjectName("arc")
        self.advisor_office = QtWidgets.QLabel(self.centralwidget)
        self.advisor_office.setGeometry(QtCore.QRect(452, 480, 101, 15))
        self.advisor_office.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.advisor_office.setText("")
        self.advisor_office.setObjectName("advisor_office")
        self.H_W_center = QtWidgets.QLabel(self.centralwidget)
        self.H_W_center.setGeometry(QtCore.QRect(348, 480, 104, 15))
        self.H_W_center.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.H_W_center.setText("")
        self.H_W_center.setObjectName("H_W_center")
        self.CDC = QtWidgets.QLabel(self.centralwidget)
        self.CDC.setGeometry(QtCore.QRect(208, 480, 140, 15))
        self.CDC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CDC.setText("")
        self.CDC.setObjectName("CDC")
        self.mac_lab = QtWidgets.QLabel(self.centralwidget)
        self.mac_lab.setGeometry(QtCore.QRect(106, 480, 102, 15))
        self.mac_lab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mac_lab.setText("")
        self.mac_lab.setObjectName("mac_lab")
        self.ally_lounge = QtWidgets.QLabel(self.centralwidget)
        self.ally_lounge.setGeometry(QtCore.QRect(0, 480, 106, 15))
        self.ally_lounge.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ally_lounge.setText("")
        self.ally_lounge.setObjectName("ally_lounge")
        self.fos_lab = QtWidgets.QLabel(self.centralwidget)
        self.fos_lab.setGeometry(QtCore.QRect(105, 387, 15, 94))
        self.fos_lab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fos_lab.setText("")
        self.fos_lab.setObjectName("fos_lab")
        self.piano_room = QtWidgets.QLabel(self.centralwidget)
        self.piano_room.setGeometry(QtCore.QRect(105, 293, 15, 94))
        self.piano_room.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.piano_room.setText("")
        self.piano_room.setObjectName("piano_room")
        self.ima_lab = QtWidgets.QLabel(self.centralwidget)
        self.ima_lab.setGeometry(QtCore.QRect(105, 199, 15, 94))
        self.ima_lab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ima_lab.setText("")
        self.ima_lab.setObjectName("ima_lab")
        self.f15 = QtWidgets.QLabel(self.centralwidget)
        self.f15.setGeometry(QtCore.QRect(105, 122, 15, 77))
        self.f15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.f15.setText("")
        self.f15.setObjectName("f15")
        self.buy_info = QtWidgets.QLabel(self.centralwidget)
        self.buy_info.setGeometry(QtCore.QRect(370, 390, 211, 71))
        self.buy_info.setStyleSheet("border-image: url(:/game/infoframe.png);\n"
"font: 40pt \"appo paint\"")
        self.buy_info.setText("")
        self.buy_info.setObjectName("buy_info")
        self.yes = QtWidgets.QPushButton(self.centralwidget)
        self.yes.setGeometry(QtCore.QRect(630, 410, 71, 31))
        self.yes.setStyleSheet("border-image: url(:/figure/yes.png);")
        self.yes.setText("")
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QPushButton(self.centralwidget)
        self.no.setGeometry(QtCore.QRect(730, 410, 71, 31))
        self.no.setStyleSheet("border-image: url(:/figure/no.png);")
        self.no.setText("")
        self.no.setObjectName("no")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(370, 351, 451, 41))
        self.info.setStyleSheet("border-image: url(:/game/infoframe.png);\n"
"font: 40pt \"appo paint\"")
        self.info.setText("")
        self.info.setObjectName("info")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import picture_rc
