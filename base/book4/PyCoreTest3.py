'''
   chap04 多线程编程
'''

import _thread
from time import sleep, ctime

loops = [4, 2]

def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

# def main():
#     print('starting at:', ctime())
#     _thread.start_new_thread(loop0, ())
#     _thread.start_new_thread(loop1, ())
#     sleep(6)
#     print('all done at:', ctime())

def loop(nloop, nsec, lock):
     print('start loop', nloop, 'at:', ctime())
     sleep(nsec)
     print('loop', nloop, 'done at:', ctime())
     lock.release()

def main():
     print('starting at:', ctime())
     locks = []
     nloops = range(len(loops))

     for i in nloops:
         lock = _thread.allocate_lock()
         lock.acquire()
         locks.append(lock)

     for i in nloops:
         _thread.start_new_thread(loop, (i, loops[i], locks[i]))

     # 等待所有的锁释放
     for i in nloops:
         while locks[i].locked(): pass

     print('all done at:', ctime())

if __name__ == '__main__':
    main()