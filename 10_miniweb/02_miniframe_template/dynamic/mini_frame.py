# _*_ coding:utf-8 _*_


def index():
    with open("./templates/index.html", "r", encoding="UTF-8") as file:  # 打开文件的相对路径全部以main方法所在模块的位置为基础路径
        content = file.read()
    return content


def center():
    with open("./templates/center.html", "r", encoding="UTF-8") as file:  # 打开文件的相对路径全部以main方法所在模块的位置为基础路径
        return file.read()


def application(environ, set_response_header):
    set_response_header('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    if file_name == '/index.py':
        return index()
    elif file_name == '/center.py':
        return center()
    else:
        return '<h1>我爱你中国!</h1>'
