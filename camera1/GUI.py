# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 971)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wgt_video = myVideoWidget(self.centralwidget)
        self.wgt_video.setGeometry(QtCore.QRect(110, 60, 1181, 541))
        self.wgt_video.setObjectName("wgt_video")
        self.formLayout = QtWidgets.QFormLayout(self.wgt_video)
        self.formLayout.setObjectName("formLayout")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(340, 790, 171, 101))
        self.btn_open.setObjectName("btn_open")
        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play.setGeometry(QtCore.QRect(610, 790, 161, 101))
        self.btn_play.setObjectName("btn_play")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(850, 790, 191, 91))
        self.btn_stop.setObjectName("btn_stop")
        self.lab_video = QtWidgets.QLabel(self.centralwidget)
        self.lab_video.setGeometry(QtCore.QRect(990, 690, 81, 18))
        self.lab_video.setObjectName("lab_video")
        self.sld_video = QtWidgets.QSlider(self.centralwidget)
        self.sld_video.setGeometry(QtCore.QRect(350, 660, 511, 61))
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.btn_shot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_shot.setGeometry(QtCore.QRect(1130, 790, 171, 91))
        self.btn_shot.setObjectName("btn_shot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_open.setText(_translate("MainWindow", "打开视频文件"))
        self.btn_play.setText(_translate("MainWindow", "播放"))
        self.btn_stop.setText(_translate("MainWindow", "暂停"))
        self.lab_video.setText(_translate("MainWindow", "TextLabel"))
        self.btn_shot.setText(_translate("MainWindow", "截图"))
from myVideoWidget import myVideoWidget
