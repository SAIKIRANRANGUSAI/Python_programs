import threading
import time

lock = threading.Lock()

def counter(limit: int,name: str):
    for i in range(limit):
        time.sleep(0.5)
        print(name,i + 1, sep=':')

def task1():
    counter(5,'t-1')

def task2():
    counter(5,'t-2')

def task3():
    counter(5,'t-3')

def main():
    thread = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    thread.start()
    thread.join()
    thread2.start()
    thread2.join()
