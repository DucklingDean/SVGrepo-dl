from svgrepo_dl.toolkit.globals import HTTPS_URL
from .scraper_core              import ScraperCore




class PageNav(ScraperCore):

    _images    : list[dict]  = None
    _next_page : str|None    = None
    _prev_page : str|None    = None
    _total_pages: int         = None


    _get_next_prev  = lambda self, index: self._tree.css(".style_pagingCarrier__NVbHL > div")[index].css_first("a")
    _get_total_pages = lambda self: int(self._tree.css_first(".style_pagingCarrier__NVbHL span").text().split("/")[-1].strip())








    @property
    def next_page(self) -> str|None:
        """Next Page URL or None"""
        if self._next_page is None:
            self._next_page = self._get_next_page_url()
        return self._next_page




    @property
    def prev_page(self) -> str|None:
        """Previous Page URL or None"""
        if self._prev_page is None:
            self._prev_page = self._get_prev_page_url()
        return self._prev_page




    @property
    def total_pages(self) -> int:
        """How many pages collection has"""
        if self._total_pages is None:
            self._total_pages = self._get_total_pages()
        return self._total_pages




    def _get_next_page_url(self) -> str|None:
        # i should not add this try catch, but some freaking nerds touch even "private fuctions"
        try:
            return HTTPS_URL + self._get_next_prev(-1).attributes['href'].strip()
        except AttributeError:
            return None




    def _get_prev_page_url(self) -> str|None:
        try:
            return HTTPS_URL + self._get_next_prev(0).attributes['href'].strip()
        except AttributeError:
            return None








# rename properties:

    @property
    def nextpage(self) -> str|None: return self.next_page

    @property
    def prevpage(self) -> str|None: return self.prev_page

    @property
    def totalpages(self) -> int: return self.total_pages
