# @Author  : ShiRui


import socketserver   # 博主用的是scoetserver，socket服务器端。
import os


class Server(socketserver.BaseRequestHandler):

    def handle(self):

        base_path = "D:\\"   # 这个下载东西存储的路径
        conn = self.request     # 相当于conn， addr = socket.socket.accpet()中的conn
        print("正在连接...")
        while True:

            recv_data = conn.recv(1024).decode()  # 接受客户端的消息，decode是解码
            cmd, file_name, file_size = recv_data.split("|")  # 收到的消息按照‘|’划分，得到命令、文件名、文件大小。
            recv_size = 0  # 设置收到的大小为0
            file_dir = os.path.join(base_path, file_name)  # 拼接文件的的具体位置信息，比如：D://xx.png
            f = open(file_dir, "wb")  # 打开文件，并以写入的方式
            Flag = True  # 设置标志
            while Flag:

                if int(file_size) > recv_size:  # 如果文件大小大于收到的初始大小，未上传完毕就继续接受。
                    data = conn.recv(1024)  # 接收文件，每次1024大小
                    recv_size += len(data)  # 初始收到的大小+1024
                else:
                    recv_size = 0
                    Flag = False
                    continue
                f.write(data)  # 写入文件
            print("下载成功!")
            f.close()

if __name__ == "__main__":

    instance = socketserver.ThreadingTCPServer(("127.0.0.1", 9999), Server)  # 以多线程的方式运行，可以防止堵塞
    instance.serve_forever()
