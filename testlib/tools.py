from collections.abc import Callable
from .config        import PRINT_TEST
from rich.pretty    import pprint 
from typing         import Callable




def load_html(file_name:str) -> bytes:
    with open(f"testlib/assets/html/{file_name}", 'rb') as html_file:
        return html_file.read()

def pp(*args):
    if PRINT_TEST:
        pprint(
            *args,
            max_depth=4, 
            max_string=70, 
            max_length=4, 
            expand_all=True
        )


def test_cases(func:Callable) -> Callable:
    """Will loop through `self.cases and` pass the case as an args"""
    def wrapper(self) -> None:
        for case_ in self.cases:
            func(self, case_)
    return wrapper

# to avoid uplaoding html to the repo, & and easy to redownload those files. 
def download_html() -> None:
    from requests import get as GET
    from os.path  import exists as path_exists
    import json

    with open("testlib/htmlfiles.json", 'r') as jsonfile:
        htmlfiles:dict = json.load(jsonfile)

    for file_name, url in htmlfiles.items():
        path = f"testlib/assets/html/{file_name}"

        if not path_exists(path):
            with open(path, 'wb') as html_file:
                html_file.write(GET(url).content)


        





