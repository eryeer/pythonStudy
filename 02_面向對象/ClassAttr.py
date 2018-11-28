class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print("tool count %d" % cls.count)

    @staticmethod
    def tool_claim():
        print("tool claim")


tool1 = Tool("futou")
tool2 = Tool("futou")
tool3 = Tool("futou")
print(Tool.count)
Tool.show_tool_count()
Tool.tool_claim()
