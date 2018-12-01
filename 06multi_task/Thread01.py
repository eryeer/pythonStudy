import time
import threading

gl_num = 100


def sing():
    global gl_num
    gl_num += 1
    print(gl_num)
    for i in range(5):
        print("---sing 菊花茶")
        time.sleep(1)
        time_time = time.time()
        print(time_time)


def dance(num):
    for i in range(5):
        print("----dance %d args:%d" % (gl_num, num))
        time.sleep(1)


def main():
    a = 99
    t1 = threading.Thread(target=dance, args=(a,))
    t2 = threading.Thread(target=sing)
    t1.start()
    t2.start()
    print(threading.enumerate())


if __name__ == '__main__':
    main()
