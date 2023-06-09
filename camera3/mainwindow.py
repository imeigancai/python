# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import serial  # 导入模块
import serial.tools.list_ports
import tkinter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1475, 930)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(13, 13, 360, 82))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(470, 10, 321, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(900, 40, 411, 41))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(30, 130, 261, 291))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 81, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 174, 181, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 260, 181, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 340, 211, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1220, 370, 211, 51))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1260, 204, 181, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1220, 260, 81, 18))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1220, 170, 81, 20))
        self.label_7.setObjectName("label_7")
        self.quickWidget_2 = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget_2.setGeometry(QtCore.QRect(1190, 160, 261, 311))
        self.quickWidget_2.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget_2.setObjectName("quickWidget_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1250, 310, 181, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1220, 180, 81, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(2360, 350, 181, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(1250, 220, 181, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1220, 280, 81, 18))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1220, 370, 81, 18))
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1250, 400, 181, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(1280, 750, 111, 51))
        self.pushButton_44.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_44.setAutoFillBackground(False)
        self.pushButton_44.setStyleSheet("\n"
"background-color: rgb(66, 240, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/jpg/sezhi.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_44.setIcon(icon)
        self.pushButton_44.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(770, 530, 112, 71))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(371, 404, 112, 71))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(950, 530, 112, 71))
        self.pushButton_43.setMinimumSize(QtCore.QSize(0, 34))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(590, 530, 112, 71))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(950, 314, 112, 50))
        self.pushButton_11.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(950, 191, 112, 71))
        self.pushButton_10.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(591, 312, 112, 61))
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(591, 406, 112, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(371, 312, 112, 61))
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(770, 191, 112, 81))
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(370, 530, 112, 71))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(950, 400, 112, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gg = QtWidgets.QPushButton(self.centralwidget)
        self.gg.setGeometry(QtCore.QRect(591, 191, 111, 81))
        self.gg.setSizeIncrement(QtCore.QSize(100, 100))
        self.gg.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.gg.setIconSize(QtCore.QSize(44, 24))
        self.gg.setObjectName("gg")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(770, 314, 112, 50))
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.btn_backup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_backup.setEnabled(True)
        self.btn_backup.setGeometry(QtCore.QRect(371, 191, 112, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.btn_backup.sizePolicy().hasHeightForWidth())
        self.btn_backup.setSizePolicy(sizePolicy)
        self.btn_backup.setMinimumSize(QtCore.QSize(112, 81))
        self.btn_backup.setMaximumSize(QtCore.QSize(16777215, 34))
        self.btn_backup.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.btn_backup.setIconSize(QtCore.QSize(24, 44))
        self.btn_backup.setObjectName("btn_backup")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(770, 406, 112, 71))
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1475, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 信号
        self.btn_backup.clicked.connect(self.backup)  # 背升elevation
        self.gg.clicked.connect(self.backdown)  # 背升elevation

        # 槽

    def backup(self):
        # self.sld_video_pressed = True
        print("pressed backup")
        # port_list = list(serial.tools.list_ports.comports())
        # print(port_list)
        # if len(port_list) == 0:
        #     print('无可用串口')
        # else:
        #     for i in range(0, len(port_list)):
        #         print(port_list[i])

        try:
            # 端口号，根据自己实际情况输入，可以在设备管理器查看
            port = "COM6"
            # 串口波特率，根据自己实际情况输入
            bps = 9600
            # 超时时间,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
            time = 5
            # 打开串口，并返回串口对象
            uart = serial.Serial(port, bps, timeout=time)
            # 串口发送一个字符串
            len = uart.write(
                "hello worldmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm".encode('utf-8'))
            print("send len: ", len)
            # str1 = uart.write().hex
            # print("send informaton:", str1)

            #接收
            # 接收数据(固定长度)
            com = serial.Serial('COM7', 9600, timeout=time)
            print(com)

            # 进入消息循环
            top = tkinter.Tk()
            top.mainloop()
            # 串口接收一个字符串
            str = ''
            for i in range(len):
                str += uart.read().decode("utf-8")
                # str = uart.read().hex()
            print("receive data: ", str)


            # 关闭串口
            # uart.close()
        except Exception as result:
            print("******error******：", result)

    def backdown(self):
        # self.sld_video_pressed = True
        print("pressed backdown")
        # port_list = list(serial.tools.list_ports.comports())
        # print(port_list)
        # if len(port_list) == 0:
        #     print('无可用串口')
        # else:
        #     for i in range(0, len(port_list)):
        #         print(port_list[i])

        try:
            # 端口号，根据自己实际情况输入，可以在设备管理器查看
            port = "COM6"
            # 串口波特率，根据自己实际情况输入
            bps = 9600
            # 超时时间,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
            time = 5
            # 打开串口，并返回串口对象
            uart = serial.Serial(port, bps, timeout=time)

            # 串口发送一个字符串
            len = uart.write(
                "hello worldmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm".encode('utf-8'))
            print("send len: ", len)

            # 串口接收一个字符串
            str = ''
            for i in range(len):
                str += uart.read().decode("utf-8")
                # str = uart.read().hex()
            print("receive data: ", str)

            # 关闭串口
            uart.close()

        except Exception as result:
            print("******error******：", result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ff5500;\">遥控器界面</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "设置水温"))
        self.label_3.setText(_translate("MainWindow", "实际水温"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffaaff;\">运行状态</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffaaff;\">运行状态</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "实际水温"))
        self.label_7.setText(_translate("MainWindow", "设置水温"))
        self.label_8.setText(_translate("MainWindow", "设置风温"))
        self.label_9.setText(_translate("MainWindow", "实际风温"))
        self.label_10.setText(_translate("MainWindow", "背框角度"))
        self.pushButton_44.setText(_translate("MainWindow", "设置"))
        self.pushButton_42.setText(_translate("MainWindow", "椅子\n"
"状态"))
        self.pushButton_12.setText(_translate("MainWindow", "水温\n"
"设置"))
        self.pushButton_43.setText(_translate("MainWindow", "复位"))
        self.pushButton_27.setText(_translate("MainWindow", "自动\n"
"翻身\n"
"关"))
        self.pushButton_11.setText(_translate("MainWindow", "背平\n"
"腿升"))
        self.pushButton_10.setText(_translate("MainWindow", "右翻"))
        self.pushButton_5.setText(_translate("MainWindow", "腿降"))
        self.pushButton_6.setText(_translate("MainWindow", "清洗"))
        self.pushButton_4.setText(_translate("MainWindow", "腿升"))
        self.pushButton_8.setText(_translate("MainWindow", "左翻"))
        self.pushButton_13.setText(_translate("MainWindow", "静止"))
        self.pushButton_3.setText(_translate("MainWindow", "风温\n"
"设置"))
        self.gg.setText(_translate("MainWindow", "背降"))
        self.pushButton_7.setText(_translate("MainWindow", "背升\n"
"腿曲"))
        self.btn_backup.setText(_translate("MainWindow", "背升"))
        self.pushButton_9.setText(_translate("MainWindow", "烘干"))
from PyQt5 import QtQuickWidgets
# import img_rc


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程