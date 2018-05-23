'''
    chap04 多线程编程   
           生产者-消费者文件简单示例
'''
from random import randint
from time import sleep
from queue import Queue
from myThread import MyThread

def writeQ(queue):
    print('producing object for Q...')
    queue.put('xxx', 1)
    print('Size now', queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q...size now', queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(1, 3))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all done')


if __name__ == '__main__':
    main()