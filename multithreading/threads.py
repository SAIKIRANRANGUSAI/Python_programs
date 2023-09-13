"""
we can create multipul threads at a time
it decides which tasks should switch
"""

#Creating a program that that will execute two threads by printing first 3 threads and then second thread next 1st next 2nd ....

import threading
import time


def sai_t(name: str, count: int):
    print(f'starting  {name}')

    for i in range(count):
        print(name, i + 1, sep=':')  # sap= is used to saparte the things
        time.sleep(1)


if __name__ == '__main__':
    thread_one = threading.Thread(target=sai_t,args=('thread-1', 10))
    thread_two = threading.Thread(target=sai_t,args=('thread-2', 5))
    thread_one.start()
    time.sleep(3)
    thread_two.start()

    thread_one.join()
    thread_two.join()




