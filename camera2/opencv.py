import cv2 as cv

if __name__ == '__main__':
    # 创建视频读取/捕获对象
    vedioRead = "../images/nasa_m420p.mov"  # 读取视频文件的路径
    capRead = cv.VideoCapture(vedioRead)  # 实例化 VideoCapture 类
    capWrite=cv.VideoCapture()
    # 读取视频文件
    frameNum = 0  # 视频帧数初值
    while capRead.isOpened():  # 检查视频捕获是否成功
        ret, frame = capRead.read()  # 读取下一帧视频图像
        if ret is True:
            cv.imshow(vedioRead, frame)  # 播放视频图像
            if cv.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 退出
                break
        else:
            print("Can't receive frame at frameNum {}".format(frameNum))
            break

    capRead.release()  # 关闭读取视频文件
    capWrite.release()  # 关闭视频写入对象
    cv.destroyAllWindows()  # 关闭显示窗口
