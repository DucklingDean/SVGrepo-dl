from selectolax.parser import HTMLParser



class ScraperCore:
    """
    - all the scrapers need to convert htmlcode -> HTMLParser.
    """
    def __init__(self, htmlcode:str|bytes) -> None:
        self._tree = HTMLParser(htmlcode)
