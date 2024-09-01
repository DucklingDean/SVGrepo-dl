from typing import Pattern
from reqio.pools import DefaultPool
from reqio       import ReadyRequest
from requests    import get as GET, status_codes 
from requests    import head as HEAD
from queue       import Queue
from svgrepo_dl.scraper import HomePage
from svgrepo_dl.scraper.collection_page import CollectionPage
from svgrepo_dl.toolkit import print_progress 
from svgrepo_dl.toolkit import Color as cl


__all__ = ["extract_all_collections",]

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



def check_collection_url_list(clltion_list:list[str], verbose:bool) -> list[str]:
    from re import match as is_pattern_match

    pattern   = r"^https://www\.svgrepo\.com/collection/[^/]+$"
    pure_list = []

    headers = ReadyRequest.gen_headers()
    headers["host"] = "www.svgrepo.com"
 
    for url in clltion_list:   
        url = url.rstrip('/')
        if not is_pattern_match(pattern, url):
            cl.p(cl.R, cl.BOLD,"Bad URL:", url)
            if verbose:
                cl.p(cl.BOLD, "   | doesn't match pattern:", cl.R, "\"https://www.svgrepo.com/collection/*\"")
            continue 


        status_code = HEAD(url, headers=headers).status_code
        if status_code == 500:
            cl.p(cl.R, cl.BOLD, "404:", url)
            if verbose:
                cl.p(cl.BOLD, "   | doesn't exist in 'svgrepo.com':", cl.BOLD, 'status_code=', cl.R, '500')
        elif status_codes != 200:
            raise NotImplementedError
        else: 
            cl.p(cl.G, cl.BOLD, "200:")
            pure_list.append(url)

    return pure_list

        

        
                          









    




