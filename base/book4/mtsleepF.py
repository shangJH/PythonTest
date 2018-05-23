'''
   chap04 多线程编程
'''
from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import ctime, sleep

class ClearoutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

loops = (randrange(2, 5) for x in range(randrange(3, 7)))

remaining = ClearoutputSet()
lock = Lock()

def loop(nsec):
    myname = current_thread().name
    # lock.acquire()
    # remaining.add(myname)      # 操作公共资源，尽量加锁
    # lock.release()
    # print('[%s] Started %s' % (ctime(), myname))
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    sleep(nsec)
    # lock.acquire()
    # remaining.remove(myname)   # 操作公共资源，尽量加锁
    # lock.release()
    with lock:
        remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
    print('    (remaining: %s)' % (remaining or 'NONE'))

def main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print('all done at:', ctime())


if __name__ == '__main__':
    main()
