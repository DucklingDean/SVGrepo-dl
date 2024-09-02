from typing import Pattern
from reqio.pools import DefaultPool
from reqio       import ReadyRequest
from requests    import get as GET
from queue       import Queue
from svgrepo_dl.scraper import HomePage
from svgrepo_dl.toolkit import print_progress 



def extract_all_collections() -> list[dict]:
    headers = ReadyRequest.gen_headers()
    headers["host"] = "www.svgrepo.com"

    html = GET("https://www.svgrepo.com", headers=headers).content
    total_pages:int = HomePage(html).total_pages
    pool = DefaultPool(
        pool_size=5,
        save_files=False,
        save_in_dict=True,
    )
    
    tasks = Queue()
    for page in range(1, total_pages+1):
        tasks.put(pool.add(f"https://www.svgrepo.com/collections/all/{page}"))

    print_progress(tasks, total_pages, "pg")
    
    collections = []
    for html in pool.dict.values():
        collections += HomePage(html).all_collections
    return collections

        

        
                          









    




