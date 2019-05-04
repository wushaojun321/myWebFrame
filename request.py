# encoding:utf8

class Request():
    def __init__(self, request_str):
        self.request_str = request_str
        self.parse()

    def parse(self):
        headers_lines, body = self.request_str.split("\r\n\r\n")  # 将headers与body分开
        headers_lines = headers_lines.split("\n")
        first_line, headers_lines = headers_lines[0], headers_lines[1:]
        self.method, self.route, _ = first_line.split()
        self.headers = {}
        for headers_line in headers_lines:
            k, v = headers_line.split(": ")
            self.headers[k] = v
        self.data = {}
        body = body.split("&")
        for line in body:
            if '=' in line:
                k, v = line.split("=")
                self.data[k] = v


if __name__ == '__main__':
    s = '''POST /todo HTTP/1.1
Host: 127.0.0.1:8080
Connection: keep-alive
Content-Length: 24
Pragma: no-cache
Cache-Control: no-cache
Origin: http://127.0.0.1:8080
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36                                                                        
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3                                                                               
Referer: http://127.0.0.1:8080/todo
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: _ga=GA1.1.542558113.1555076932; csrftoken=WSvXz7s96R0m4jyXDq1Z8LUqgzwWZ2Bq

datetime=asd&content=asd
'''
    r = Request(s)
    print r.__dict__
    print r.data