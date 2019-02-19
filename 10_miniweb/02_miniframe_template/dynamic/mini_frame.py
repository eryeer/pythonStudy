# _*_ coding:utf-8 _*_
import re
from pymysql import *

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route(r"/index.html")
def index(ret):
    with open("./templates/index.html", "r", encoding="UTF-8") as file:  # 打开文件的相对路径全部以main方法所在模块的位置为基础路径
        content = file.read()
        # my_stock_info = "這是本月名稱"
        # content = re.sub(r"{%content%}", my_stock_info, content)
    conn = connect(host='localhost', port=3306, user='root', password='root', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute("select * from info;")
    my_stock_info = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="add" id="toAdd" name="toAdd" systemIdVaule="%s">
        </td>
    </tr>
    """

    html = ""
    for line_info in my_stock_info:
        html += tr_template % (
            line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6],
            line_info[7],
            line_info[1])
    content = re.sub(r"{%content%}", html, content)
    return content


@route(r"/center.html")
def center(ret):
    with open("./templates/center.html", "r", encoding="UTF-8") as file:  # 打开文件的相对路径全部以main方法所在模块的位置为基础路径
        content = file.read()
    conn = connect(host='localhost', port=3306, user='root', password='root', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute(
        """
        select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i inner join focus as f on f.info_id = i.id;
        """)
    focus_info = cs.fetchall()
    cs.close()
    conn.close()

    # my_stock_info = "mysql查询出来的数据"
    # content = re.sub(r"{%content%}", my_stock_info, content)
    tr_template = """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
        </td>
        <td>
            <input type="button" value="delete" id="totoDel" name="toDel" systemIdVaule="%s">
        </td>
    </tr>
    """
    html = ""
    for line_info in focus_info:
        html += tr_template % (
            line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6],
            line_info[0], line_info[0])
    content = re.sub(r"{%content%}", html, content)
    return content


@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """
    显示修改的那个页面
    :param ret:
    :return:
    """
    stock_code = ret.group(1)
    with open("./templates/update.html", "r", encoding="UTF-8") as file:  # 打开文件的相对路径全部以main方法所在模块的位置为基础路径
        content = file.read()
    conn = connect(host='localhost', port=3306, user='root', password='root', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute("select f.note_info from info as i inner join focus as f on f.info_id = i.id where i.code = %s;",
               (stock_code,))
    stock_info = cs.fetchone()
    note_info = stock_info[0]
    cs.close()
    conn.close()

    content = re.sub(r"{%note_info%}", note_info, content)
    content = re.sub(r"{%code%}", stock_code, content)
    return content


@route(r"/update/(\d+)/([^.]+)\.html")
def save_update_page(ret):
    """保存修改的信息"""
    stock_code = ret.group(1)
    comment = ret.group(2)
    conn = connect(host='localhost', port=3306, user='root', password='root', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute(
        """update focus set note_info = %s where info_id = (select id from info where code=%s);
        """, (comment, stock_code))
    conn.commit()
    cs.close()
    conn.close()
    return "修改成功"


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    stock_code = ret.group(1)

    conn = connect(host='localhost', port=3306, user='root', password='root', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute(
        """
        select * from info where code = %s;
        """, stock_code)
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "请手下留情"
    sql = """select * from info as i inner join focus as f on f.info_id = i.id where i.code=%s;"""
    cs.execute(sql, stock_code)
    if cs.fetchone():
        cs.close()
        conn.close()
        return "已经关注过了。。。"
    sql = "insert into focus (info_id) select id from info where code=%s;"
    cs.execute(sql, stock_code)
    conn.commit()
    cs.close()
    conn.close()
    return "add ok %s ..." % stock_code


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    stock_code = ret.group(1)

    conn = connect(host='localhost', port=3306, user='root', password='root', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute(
        """
        select * from info where code = %s;
        """, stock_code)
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "请手下留情"
    sql = """select * from info as i inner join focus as f on f.info_id = i.id where i.code=%s;"""
    cs.execute(sql, stock_code)
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "之前未关注，请勿取消"
    sql = "delete from focus where info_id = (select id from info where code=%s);"
    cs.execute(sql, stock_code)
    conn.commit()
    cs.close()
    conn.close()
    return "del ok %s ..." % stock_code


def application(environ, set_response_header):
    set_response_header('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    # if file_name == '/index.py':
    #     return index()
    # elif file_name == '/center.py':
    #     return center()
    # else:
    #     return '<h1>我爱你中国!</h1>'
    try:
        for url, func in URL_FUNC_DICT.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            return "请求的url(%s)没有对应的函数...." % file_name
    except Exception as ret:
        return "产生了异常: %s" % str(ret)
