# encoding:utf8
from response import Response

def todo(request):
    if request.method == "GET":
        with open("todo.txt", "r") as f:
            body = f.read()
        result = Response(200, body).result
        return result
    elif request.method == "POST":
        new_item = request.data["datetime"] + " " + request.data["content"] + "\n"
        with open("todo.txt", "a") as f:
            f.write(new_item)
        return Response(200, "添加成功").result

