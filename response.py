# encoding:utf8

class Response(object):
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body
        self.result = """
HTTP/1.1 {status_code} OK
Date: Tue, 10 Jul 2012 06:50:15 GMT
Content-Type: text/html

<html>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<body>
{body}
<form method="post" action="/todo">
    日期:<input name="datetime"></input>
    内容:<input name="content"></input>
    <input type="submit"></input>
</form>
</body>
</html>
""".format(status_code= self.status_code, body=self.body)

        