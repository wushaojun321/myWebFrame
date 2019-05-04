# encoding:utf8
import socket
from request import Request
from response import Response
from app import todo


route_map = {
    "/todo": todo
}

def make_response(request):
    '''根据请求内容返回相应的内容'''
    view_function = route_map.get(request.route, None)
    if view_function is None:
        result = Response(404, "").result
        return result
    return view_function(request)



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
        if not r:
            continue
        print "接收到的信息如下："
        print "="*100
        print r
        print "="*100
        request = Request(r)
        response = make_response(request)
        conn.sendall(response)
        conn.close()

if __name__ == '__main__':
    run_server()
    