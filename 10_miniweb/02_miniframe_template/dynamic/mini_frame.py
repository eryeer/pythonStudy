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


@route("/index.html")
def index():
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
                <input type="button" value="add" id="toAdd" name="toAdd" systemidvalue="000007">
            </td>
        </tr>
        """

        html = ""
        for line_info in my_stock_info:
            html += tr_template % line_info
        content = re.sub(r"{%content%}", html, content)
    return content


@route("/center.html")
def center():
    with open("./templates/center.html", "r", encoding="UTF-8") as file:  # 打开文件的相对路径全部以main方法所在模块的位置为基础路径
        content = file.read()
    conn = connect(host='localhost', port=3306, user='root', password='root', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute("select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i left join focus as f on f.info_id = i.id;")
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
            <a type="button" href="/update/300268.html">
            <span></span> 修改</a>
        </td>
        <td>
            <input type="button" value="delete" id="toAdd" name="toAdd" systemidvalue="000007">
        </td>
    </tr>
    """
    html = ""
    for line_info in focus_info:
        html += tr_template % line_info
    content = re.sub(r"{%content%}", html, content)
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
    try:
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常: %s" % str(ret)
