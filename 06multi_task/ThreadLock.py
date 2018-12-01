import threading
import time
gl_num = 0

mutex = threading.Lock()

def test1(num):
    global gl_num
    for i in range(num):
        mutex.acquire()
        gl_num += 1
        mutex.release()
    print("---in test1 gl_num = %d" % gl_num)


def test2(num):
    global gl_num
    for i in range(num):
        mutex.acquire()
        gl_num += 1
        mutex.release()
    print("---in test2 gl_num = %d" % gl_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print("--- in main gl_num = %d" % gl_num)
