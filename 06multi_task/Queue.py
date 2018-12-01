import multiprocessing


def download_from_web(q):
    data = [11, 22, 33, 44]

    for datum in data:
        q.put(datum)
    print("--download and save")


def analysis_data(q):
    waitting_analysis_data = list()
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        if q.empty():
            break
    print("analysis_data: %s" % waitting_analysis_data)


def main():
    # create a queue
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
