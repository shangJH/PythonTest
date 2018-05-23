'''
   chap04 多线程编程 Thread类
'''
import threading
from time import ctime, sleep

loops = [4, 2]
def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()     # 等待所有的线程结束

    print('all done at:', ctime())

if __name__ == '__main__':
    main()