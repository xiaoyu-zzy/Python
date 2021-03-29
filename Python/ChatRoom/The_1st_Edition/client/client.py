import socket
from threading import Thread
class Client(Thread):
    def __init__(self,name):
        localhost = input("localhost:")
        while True:
            try:
                password = int(input("password:"))
                if password > 65535 or password < 0:
                    print("错误，请重试！")
                    continue
                break
            except:
                print("错误，请重试！")
        super(Client, self).__init__()
        self.name = name
        self.ip_port = (localhost,password)
        self.sk = socket.socket()
        self.sk.connect(self.ip_port)
        print("连接成功！！！")

    def run(self):#负责接收服务器端发来的消息打印处理
        try:
            while True:
                data = str(self.sk.recv(1024), encoding='utf-8')
                print(data)
        except Exception as e:
            print("服务端已关闭..")
            return
 
    def send(self):#负责本客户端输入信息发送到服务器端
        try:
            while True:
                inp = input("\n")
                self.sk.sendall(bytes(inp, encoding='utf-8'))
        except Exception as e:
            print("服务端已关闭..")
            return
 
    def close(self):
        self.sk.close()

if __name__=="__main__":
    client1 = Client("client1")
    client1.start()#数据接收与数据发送并行执行
    client1.send()#数据接收与数据发送并行执行
