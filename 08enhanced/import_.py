import sys
from imp import reload
import private_

sys.path.insert(0, "/home/xxx/xxx")
sys.path.append("/home/xxx/xxx")
print(sys.path)

reload(private_)  # 热更新模块 能够reload模块名，用于import 模块名写法
