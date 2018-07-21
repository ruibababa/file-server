# @Author  : ShiRui


import socket
import os


client = socket.socket()  # 创建客户端实例
client.connect(('127.0.0.1', 9999))    # 连接到服务器

while True:

    input_data = input("path:")  # 输入要下载的文件
    cmd, path = input_data.split('|')  # 分割命令和文件路径
    file_name = os.path.basename(path)  # basename是返回最后一个文件名，如：path='D:/CSDN',会返回CSDN
    file_size = os.stat(path).st_size  # 文件的大小
    client.send((cmd + "|" + file_name + "|" + str(file_size)).encode())  # 发送给服务器端
    send_size = 0  # 初始发送的大小为0
    f = open(path, "rb")  # 打开文件的路径
    Flag = True
    while Flag:

        if send_size + 1024 > file_size:   # 如果发送的大小大于文件本身的大小

            data = f.read(file_size - send_size)  # 就读取文件
            Flag = False

        else:

            data = f.read(1024)
            send_size += 1024
        client.send(data)

    f.close()

client.close()
