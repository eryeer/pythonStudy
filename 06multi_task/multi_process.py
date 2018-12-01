import multiprocessing
import time


def sing():
    for i in range(50000):
        print("---sing 菊花茶")
        time.sleep(1)


def dance():
    for i in range(50000):
        print("----dance args:d")
        time.sleep(1)


def main():
    a = 99
    t1 = multiprocessing.Process(target=dance)
    t2 = multiprocessing.Process(target=sing)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
