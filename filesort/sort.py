import os
import re
import shutil


def sort(dir):
    listdir = os.listdir(dir)
    print(listdir)
    for file in listdir:
        path = dir + "\\" + file
        if os.path.isdir(path):
            sort(path)
        else:
            match1 = re.match("^.*\.(mp4|MP4|MPG|avi|AVI|mpg)$", path)
            match2 = re.match("^.*\.(jpeg|jpg|png)$", path)
            match3 = re.match("^.*\.(rar|zip)$", path)
            if match1:
                print(match1.group())
                shutil.move(path, "D:\\thunderdownload\\" + file)
            elif match2:
                print(match2.group())
                shutil.move(path, "D:\\thunderdownload\\pic\\" + file)
            # elif match3:
            #     print(match3.group())
            #     shutil.move(path, "D:\\thunderdownload\\zip\\" + file)


def mycopy(src_file, dst_file):
    """此函数的功以实现复制文件
    src_file : 源文件名
    dst_file : 目标文件名
    """
    try:
        fr = open(src_file, "rb")  # fr读文件
        try:
            try:
                fw = open(dst_file, 'wb')  # fw写文件
                try:
                    while True:
                        data = fr.read(4096)
                        if not data:
                            break
                        fw.write(data)
                except:
                    print("可能U盘被拔出...")
                finally:
                    fw.close()  # 关闭写文件
            except OSError:
                print("打开写文件失败")
                return False
        finally:
            fr.close()  # 关闭读文件
    except OSError:
        print("打开读文件失败")
        return False
    return True


if __name__ == '__main__':
    dest = "D:\\thunderdownload\zip"
    sort(dest)
