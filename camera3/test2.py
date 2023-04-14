import serial


# 端口号，根据自己实际情况输入，可以在设备管理器查看
port = "COM6"
# 串口波特率，根据自己实际情况输入
bps = 9600
# 超时时间,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
time = 5
# 打开串口，并返回串口对象
uart = serial.Serial(port, bps, timeout=time)
uart.write("hello serial".encode('utf-8'))

# com = serial.Serial('COM7', 9600)
print(uart)

# uart = serial.Serial('COM3', 9600)
success_bytes = uart.write('This is data for test'.encode('utf-8'))
print(success_bytes)    #打印成功发送的位数
# 关闭串口
# uart.close()
print(serial.Serial.read_all)


# 接收数据(固定长度)
com = serial.Serial('COM7', 9600, timeout=time)
print(com)
len=21
# data = com.read(10)

# 串口接收一个字符串
str = ''
for i in range(len):
    str += com.read().decode('utf-8')
    # str = uart.read().hex()
print("receive data: ", str)

print(str)


