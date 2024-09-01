from queue import Queue
from sys   import stdout
from tqdm  import tqdm

__all__ = [
    "print_progress",
    "Color",
]


class Color:
    _ALL = {"\033[30m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m", "\033[38m" }
    GREY = '\033[30m' 
    BOLD = '\033[1m'
    DEF  = '\033[0m'

    R = '\033[31m'
    G = '\033[32m'
    Y = '\033[33m'
    B = '\033[34m'
    P = '\033[35m'
    C = '\033[36m'
    W = '\033[38m'



    def p(*args, end:str='\n') -> None:
        p = lambda txt: print(txt, end="")

        for a in args:
            if a in Color._ALL: 
                p(a)
            else: 
                p(a+" "+Color.DEF)

        print(Color.DEF, end=end)




def print_progress(tasks_queue:Queue, length:int, unit:str="") -> None:
    progress_bar = tqdm(total=length, unit=unit, file=stdout)
    while not tasks_queue.empty():
        t = tasks_queue.get()
        if t.is_alive():tasks_queue.put(t)
        else:progress_bar.update(1)

    progress_bar.close()





