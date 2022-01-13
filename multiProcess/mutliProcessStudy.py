from time import sleep
from multiprocessing import Process, Queue


def crawling(name, q):
    if name == "a":
        for i in range(0, 10):
            print("{}초 경과".format(i))
            sleep(1)
            q.put(True)
        q.put(False)

    elif name == "c":
        while True:
            ch = q.get()
            print("-------------")
            sleep(1)
            if ch is False:
                break


if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=crawling, args=("a", q))
    p2 = Process(target=crawling, args=("c", q))

    p1.start()
    p2.start()

    q.close()
    q.join_thread()

    p1.join()
    p2.join()

    print("모든 작업 종료")
