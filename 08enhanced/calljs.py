import execjs

ctx = execjs.compile("""
    function add(x, y) {
    return x + y;
    }
    """)
call = ctx.call("add", 1, 2)
print(call)




