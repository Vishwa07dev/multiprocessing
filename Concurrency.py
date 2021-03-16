import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

COUNT = 200000000
SLEEP = 10


def io_bound(sec):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} ---> Start sleeping...")
    time.sleep(sec)
    print(f"{pid} * {processName} * {threadName} ---> Finished sleeping...")


def cpu_bound(n):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} ---> Start counting...")

    while n > 0:
        n -= 1

    print(f"{pid} * {processName} * {threadName} ---> Finished counting...")


if __name__ == "__main__":
    start = time.time()

    # YOUR CODE SNIPPET HERE
    # 1 demo
    '''
    io_bound(SLEEP)
    io_bound(SLEEP)
    '''

    # Code snippet for Part 2
    # 2 demo
    # t1 = Thread(target=io_bound, args=(SLEEP,))
    # t2 = Thread(target=io_bound, args=(SLEEP,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # 3 demo
    # cpu_bound(COUNT)
    # cpu_bound(COUNT)


    # 4 demo
    # t1 = Thread(target=cpu_bound, args=(COUNT,))
    # t2 = Thread(target=cpu_bound, args=(COUNT,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # 5 demo
    # p1 = Process(target=cpu_bound, args=(COUNT,))
    # p2 = Process(target=cpu_bound, args=(COUNT,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()


    # 6 demo
    # Code snippet for Part 6
    # p1 = Process(target=io_bound, args=(SLEEP,))
    # p2 = Process(target=io_bound, args=(SLEEP,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)