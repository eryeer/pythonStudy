import re

ret = re.match("[A-Z][a-z]*","MnnM")
print(ret.group())