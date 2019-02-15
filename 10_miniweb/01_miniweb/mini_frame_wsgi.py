import time


def login():
    return "---login--- welcome to our website %s" % time.ctime()


def register():
    return "---register--- welcome to our website %s" % time.ctime()


def application(environ, set_response_header):
    set_response_header('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    else:
        return '<h1>我爱你中国!</h1>'
