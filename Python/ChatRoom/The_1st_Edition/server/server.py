import socket
from threading import Thread
import threading
import datetime
 
clientSocket=[]#一个列表，内部存储元组元素（所有参与链接的客户端），(conn,字符串(address),例如(127.0.0.1,"127.0.0.1"，9000)
 
class Server(Thread):#继承多线程
    def __init__(self,name):
        localhost = input("localhost:")
        while True:
            try:
                password = int(input("password:"))
                if password > 65535 or password < 0:
                    print("密码只能在0-65535，请重试！")
                    continue
                break
            except:
                print("密码只支持数字，请重试！")
            
        super().__init__()
        self.name = name
        self.ip_port = (localhost,password)
        self.init()
        print("服务端开启...")
    def init(self):
        self.sk = socket.socket()
        self.sk.bind(self.ip_port)
        self.sk.listen(10)
 
    def run(self):
        while True:
            try:
                conn, address = self.sk.accept()
                clientSocket.append((conn, str(address)))
                nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 当前时间
                str1 = "[" + str(nowTime) + "]>>" + str(address) + ":加入群聊"  # 某IP,port的某用户x加入群聊
                print(str1)
                for con in clientSocket:
                    con[0].sendall(bytes(str1, encoding='utf-8'))  # 向每个客户端发送某人加入群聊的通知信息
                client_thread = threading.Thread(target=self.handle_ac,args=(conn, str(address)))  # 把sock加入线程内
                client_thread.start()  # 启动线程
            except Exception as e:
                print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]>>:",e.args)
 
    def handle_ac(self,conn,address):
        while True:
            connection=()
            try:
                data = str(conn.recv(1024), encoding='utf -8')
                nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 当前时间
                str1 = "[" + str(nowTime) + "]>>" + str(address) + ":" + data  # 某IP,port的某用户x当前时间发送的消息data
                print(str1)  # 服务器端也打印群聊信息消息记录  log
                for con in clientSocket:
                    try:
                        con[0].sendall(bytes(str1, encoding='utf-8'))  # 服务器将用户x(address:(IP,port))发送出来的群聊数据发送给每个客户端用户
                    except Exception as e:
                        clientSocket.remove(con)#若该客户端连接不通，说明客户端存在问题或者关闭，直接从客户端存储列表里剔除该客户端
            except Exception as e:
                print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]>>:",e.args)
                self.join()
 
    def close(self):
        for con in clientSocket:
            con[0].close()#将列表里每个元组第一个conn链接全部关闭
        self.sk.close()
 
if __name__=="__main__":
    server = Server("server1")
    server.start()
