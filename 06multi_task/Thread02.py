import threading
import time


class MyThread(threading.Thread):
    def run(self):
        while True:
            print("thread start")
            time.sleep(1)


if __name__ == '__main__':
    thread = MyThread()
    thread.start()
