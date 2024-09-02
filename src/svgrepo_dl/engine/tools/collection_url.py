from reqio       import ReadyRequest
from requests    import head as HEAD
from re          import match as is_pattern_matched
from svgrepo_dl.toolkit import Color as cl




def match_pattern(url:str, verbose:bool) -> bool:
    pattern   = r"^https://www\.svgrepo\.com/collection/[^/]+$"
    if is_pattern_matched(pattern, url): return True
    cl.p(cl.R, cl.BOLD,"Bad URL:", url)
    if verbose:
        cl.p(cl.BOLD, "   | doesn't match pattern:", cl.R, "\"https://www.svgrepo.com/collection/*\"")
    return False


    
def check_status_code(url:str, verbose:bool) -> bool:
    headers = ReadyRequest.gen_headers()
    headers["host"] = "www.svgrepo.com"

    stcode = HEAD(url, headers=headers).status_code

    if stcode == 200:
        cl.p(cl.G, cl.BOLD, "200:", url)
        return True
    elif stcode == 500:
        cl.p(cl.R, cl.BOLD, "404:", url)
        if verbose:
            cl.p(cl.BOLD, "   | doesn't exist in 'svgrepo.com':", cl.BOLD, 'status_code=', cl.R, '500')

    return False

    

def true_exists_collection_url(clltion_list:list[str], verbose:bool) -> list[str]:
    pure_list = []
  
    for url in clltion_list:   

        url = url.rstrip('/')

        if not match_pattern(url, verbose):continue 
        if check_status_code(url, verbose):pure_list.append(url)

    return pure_list

