from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from GUI import Ui_MainWindow
from myVideoWidget import myVideoWidget
# from what import screenshot
import sys
import cv2 as cv
# import what
import cv2
from PIL import Image
import numpy as np
import os
import cv2




address = 1

# def screenshot(videourl,imageurl):
#     cap = cv2.VideoCapture('E:\\videourl')  # 获取视频对象
#     # "F:\test1\Video.avi"
#     isOpened = cap.isOpened  # 判断是否打开
#     # 视频信息获取
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     imageNum = 0
#     sum = 0
#     timef = 15  # 隔15帧保存一张图片
#     while (isOpened):
#         sum += 1
#         (frameState, frame) = cap.read()  # 记录每帧及获取状态
#         # print(cap.read())
#         if frameState == True and (sum % timef == 0):
#             # 格式转变，BGRtoRGB
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             # 转变成Image
#             frame = Image.fromarray(np.uint8(frame))
#             frame = np.array(frame)
#             # RGBtoBGR满足opencv显示格式
#             frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#             imageNum = imageNum + 1
#             fileName = "E:\\imageurl\\" + str(imageNum) + '.jpg'  # 存储路径
#             # F:\test1
#             cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
#             print(fileName + " successfully write in")  # 输出存储状态
#         elif frameState == False:
#             break
#     print('finish!')
#
#     cap.release()


class myMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.sld_video_pressed = False  # 判断当前进度条识别否被鼠标点击
        self.videoFullScreen = False  # 判断当前widget是否全屏
        self.videoFullScreenWidget = myVideoWidget()  # 创建一个全屏的widget
        self.videoFullScreenWidget.setFullScreen(1)
        self.videoFullScreenWidget.hide()  # 不用的时候隐藏起来
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出的widget，就是上面定义的
        self.btn_open.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.btn_play.clicked.connect(self.playVideo)  # play
        self.btn_stop.clicked.connect(self.pauseVideo)  # pause
        self.btn_shot.clicked.connect(self.shotVideo)   #shot
        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.videoFullScreenWidget.doubleClickedItem.connect(self.videoDoubleClicked)  # 双击响应
        self.wgt_video.doubleClickedItem.connect(self.videoDoubleClicked)  # 双击响应
        self.sld_video.setTracking(False)
        self.sld_video.sliderReleased.connect(self.releaseSlider)
        self.sld_video.sliderPressed.connect(self.pressSlider)
        self.sld_video.sliderMoved.connect(self.moveSlider)


    def moveSlider(self, position):
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText(str(round(position, 2)) + '%')

    def pressSlider(self):
        self.sld_video_pressed = True
        print("pressed")

    def releaseSlider(self):
        self.sld_video_pressed = False

    def changeSlide(self, position):
        if not self.sld_video_pressed:  # 进度条被鼠标点击时不更新
            self.vidoeLength = self.player.duration() + 0.1
            self.sld_video.setValue(round((position / self.vidoeLength) * 100))
            self.lab_video.setText(str(round((position / self.vidoeLength) * 100, 2)) + '%')

    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件

        # print('zz')
        # print(QFileDialog.getOpenFileUrl())
        # print('zz1')
        # global address
        # address=str(QFileDialog.getOpenFileUrl())
        # print(address)
        # print("123")
        # # addre=address[5:400]
        #
        # a=print(address)
        # b=a[:-3]
        # print(b)

        self.player.play()  # 播放视频


    def playVideo(self):
        self.player.play()

    # def shotVideo(self):
    #     self.player.play()


    def shotVideo(player,imageurl):
        # SaveVideo.VideoURL(String)
        # VideoURL.
        address1 = QFileDialog.getExistingDirectory()
        # address = '\/'.join(address.split('\\\\'))
        # address2 = '//'.join(address1.split('/'))
        address = '//'.join(address1.split('/'))
        address=address+'//'
        print(address)
        # video_path = r'E:\\test4\\'  # 视频所在的路径
        video_path = r'%s'%address  # 视频所在的路径

        f_save_path = r'E:\\test3\\'  # 保存图片的上级目录
        mask = 1  # 不同方法：1 按照帧率截取；2 按照时间截取(单位：s)；
        frame_interval = 40  # 设置帧率间隔
        time_interval = 1  # 设置时间间隔(单位：s)

        if (mask == 1):
            print("当前模式：按照帧率截取视频\n帧率间隔：" + str(frame_interval))
        elif (mask == 2):
            print("当前模式：按照时间截取视频\n时间间隔：" + str(time_interval) + "s")

        videos = os.listdir(video_path)
        for video_name in videos:
            file_name = video_name.split('.')[0]  # 拆分视频文件名称 ，剔除后缀
            folder_name = f_save_path + file_name  # 保存图片的上级目录+对应每条视频名称 构成新的目录存放每个视频
            os.makedirs(folder_name, exist_ok=True)  # 创建存放视频的对应目录
            vc = cv2.VideoCapture(video_path + video_name)  # 读入视频文件
            fps = vc.get(cv2.CAP_PROP_FPS)  # 获取当前视频帧率
            rval = vc.isOpened()  # 判断视频是否打开
            c = 1
            while rval:  # 循环读取视频帧
                rval, frame = vc.read()  # videoCapture.read() 函数，第一个返回值为是否成功获取视频帧，第二个返回值为返回的视频帧；
                pic_path = folder_name + '/'
                if rval:
                    if (mask == 1):
                        if (c % round(frame_interval) == 0):  # 每隔frame_interval帧存储一次

                            cv2.imencode('.jpg', frame)[1].tofile(
                                pic_path + file_name + '_' + str(round(c / frame_interval)) + '.jpg')  # 中文路径也可以保存

                            print(file_name + '_' + str(round(c / frame_interval)) + '.jpg')
                        cv2.waitKey(1)
                        c = c + 1
                    elif (mask == 2):
                        if (c % (round(fps) * time_interval) == 0):  # 每隔time_interval秒存储一次
                            cv2.imencode('.jpg', frame)[1].tofile(
                                pic_path + file_name + '_' + str(round(c / fps)) + '.jpg')
                            print(file_name + '_' + str(round(c / fps)) + '.jpg')
                        cv2.waitKey(1)
                        c = c + 1
                else:
                    break
            vc.release()
            print('save_success' + folder_name)

            # cut_video()



    def pauseVideo(self):
        self.player.pause()

    def videoDoubleClicked(self, text):

        if self.player.duration() > 0:  # 开始播放后才允许进行全屏操作
            if self.videoFullScreen:

                self.player.pause()
                self.videoFullScreenWidget.hide()
                self.player.setVideoOutput(self.wgt_video)
                self.player.play()
                self.videoFullScreen = False
            else:
                self.player.pause()
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.player.play()
                self.videoFullScreen = True


if __name__ == '__main__':
    print(address)
    app = QApplication(sys.argv)
    video_gui = myMainWindow()
    video_gui.show()
    # openVideoFile()
    print(address)
    print('hello world1')
    print(address)
    # screenshot()

    sys.exit(app.exec_())

    # print(capp)