# encoding:utf8
import socket

response = '''
HTTP/1.1 200 OK
Date: Tue, 10 Jul 2012 06:50:15 GMT
Content-Type: text/html

<h1>hello world</h1>
'''

def run_server(host="localhost", port=8080):
    print u'服务器已经启动... \n访问地址：'+("http://"+host+":"+str(port))
    s = socket.socket()
    s.bind((host, port))
    while True:
        s.listen(5)  # 最多同时处理5个请求
        conn, addr = s.accept()
        r = ''
        while True:
            _r = conn.recv(1024)
            r += _r
            if len(_r) <= 1024:
                break
        print "接收到的信息如下："
        print "="*100
        print r
        print "="*100
        conn.sendall(response)

if __name__ == '__main__':
    run_server()
    