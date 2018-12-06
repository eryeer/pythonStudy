import os
import execjs
import time

os.environ["EXECJS_RUNTIME"] = "Node"
print(execjs.get().name)
print(os.getcwd() + "\\node_modules")
os.environ["NODE_PATH"] = os.getcwd() + "\\node_modules"

ctx = execjs.compile("""
    var new_encpro2 = require("new-encpro2");
    function test(a,b) {
        return new_encpro2.getAuthKeyAndSalt(a, b);
    }
""")
start_time = time.time()
call = ctx.call('test', 'account1', '123456')
end_time = time.time()
print(end_time-start_time)

print(type(call))
print(call)
