from .scraper_core              import ScraperCore
from svgrepo_dl.toolkit.globals import HTTPS_URL




class CollectionPage(ScraperCore):
    """
    page with URL like: 'svgrepo.com/collection/**'
    """
    _images    : list[dict]  = None
    _collection: str         = None
    _next_page : str|None    = None
    _prev_page : str|None    = None
    _page_count: int         = None
    

    _get_next_prev  = lambda self, index: self._tree.css(".style_pagingCarrier__NVbHL > div")[index].css_first("a")
    _get_page_count = lambda self: int(self._tree.css_first(".style_pagingCarrier__NVbHL span").text().split("/")[-1].strip())


    @property 
    def images(self) -> list[dict]:
        """
        Get All SVGs(title, file-name, url).
        format:
        {
            "title"     :"...",
            "url"       :"https://...",
            "file-name" :"*.svg"
        }
        """
        if self._images is None:
            self._images = self._get_images()
        return self._images




    @property
    def collection(self) -> str:
        """Collection Title"""
        if self._collection is None:
            self._collection = self._tree.css(".style_breadCrumbsScroller__93Cu8 div a")[-1].text().strip()
        return self._collection



    
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
    def page_count(self) -> int:
        """How many pages collection has"""
        if self._page_count is None:
            self._page_count = self._get_page_count()
        return self._page_count




    def _get_images(self) -> list[dict[str,str]]:
        """Extract all SVGs in the page (inside collection)"""
        elements = self._tree.css(".style_nodeListing__7Nmro img")
        return list(
            {
                "title"     :img_element.attributes["alt"].strip(),
                "url"       :img_element.attributes["src"].strip(),
                "file-name" :img_element.attributes["src"].split("/")[-1].strip()
            } for img_element in elements
        )




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
    def pagecount(self) -> int: return self.page_count

    @property
    def title(self) -> str: return self.collection


