import multiprocessing as mp
from time_stuff import get_time, timestamp, kill_time
import os


def func(param):
    print(f'starting:  {mp.current_process().name}({os.getpid()})...({timestamp})')
    kill_time
    print(f'{os.getpid()}  finished ({timestamp()})')


@get_time
def main():
    process = mp.main_process(name='process-1', target=func(), args=('sample,'))
    process2 = mp.main_process(name='process-2', target=func(), args=('sample2,'))

    process.start()
    process2.start()

    process.join()
    process2.join()

if __name__ == '__main__':
    main()
