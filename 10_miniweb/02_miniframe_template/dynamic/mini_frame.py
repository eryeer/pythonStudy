# _*_ coding:utf-8 _*_
import re

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.py")
def index():
    with open("./templates/index.html", "r", encoding="UTF-8") as file:  # 打开文件的相对路径全部以main方法所在模块的位置为基础路径
        content = file.read()
        my_stock_info = "這是本月名稱"
        content = re.sub(r"{%content%}", my_stock_info, content)
    return content


@route("/center.py")
def center():
    with open("./templates/center.html", "r", encoding="UTF-8") as file:  # 打开文件的相对路径全部以main方法所在模块的位置为基础路径
        content = file.read()
    my_stock_info = "mysql查询出来的数据"
    content = re.sub(r"{%content%}", my_stock_info, content)
    return content


def application(environ, set_response_header):
    set_response_header('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    # if file_name == '/index.py':
    #     return index()
    # elif file_name == '/center.py':
    #     return center()
    # else:
    #     return '<h1>我爱你中国!</h1>'
    func = URL_FUNC_DICT[file_name]
    return func()
