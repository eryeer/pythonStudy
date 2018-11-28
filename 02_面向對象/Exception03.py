def input_password():
    passwd = input("input passwd len >=8")
    if len(passwd) >= 8:
        return passwd
    else:
        exception = Exception("密码长度不够")
        raise exception


try:
    input_password()
except Exception as result:
    print(result)
