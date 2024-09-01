from queue import Queue
from sys   import stdout
from tqdm  import tqdm

__all__ = ["print_progress",]

def print_progress(tasks_queue:Queue, length:int, unit:str="") -> None:
    progress_bar = tqdm(total=length, unit=unit, file=stdout)
    while not tasks_queue.empty():
        t = tasks_queue.get()
        if t.is_alive():tasks_queue.put(t)
        else:progress_bar.update(1)

    progress_bar.close()

    
