"""
pipes are used to data sharing in python
->pipes is connected with two processes it is used to send data from one process to other process.
"""

from multiprocessing import Pipe

def main():
    c1, c2 = Pipe()

    c2.send('text')
    print('data to be recived:',c1.poll())
    obj  = c1.recv()
    print(obj)
    print('data to be recived:',c1.poll())

if __name__ == '__main__':
    main()