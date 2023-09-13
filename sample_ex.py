# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring.

from multiprocessing import Pipe

def main():
    c1, c2 = Pipe()

    c2.send('text')
    print('data to be recived:', c1.poll())
    obj = c1.recv()
    print(obj)
    print('data to be recived:', c1.poll())



if __name__ == '__main__':

    main()
