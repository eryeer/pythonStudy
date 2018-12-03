import re


def main(name, regex):
    email = name
    ret = re.match(regex, email)
    if ret:
        print("变量名: %s 符合要求。。。%s" % (email, ret.group()))
    else:
        print("变量名: %s 不符合要求。。。" % email)


if __name__ == '__main__':
    # main("laowang@163.com", r"^([a-zA-Z0-9_]{4,20})@(163|126)\.com$")
    main("<body><h1>hello</h1></body>", r"<(\w*)><(\w*)>.*</\2></\1>")
