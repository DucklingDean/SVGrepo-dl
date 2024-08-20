from .scraper_core              import ScraperCore
from svgrepo_dl.toolkit.globals import HTTPS_URL




class CollectionPage(ScraperCore):
    """
    page with URL like: 'svgrepo.com/collection/**'
    """
    _images    :list[dict]  = None
    _collection:str         = None
    _nextpage  :str|None    = None
    _pagecount :int         = None
    

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
            self._collection = self._get_collection_title()
        return self._collection

    
    @property
    def next_page(self) -> str|None:
        """Next Page URL or None"""
        return self.nextpage
    

    @property
    def nextpage(self) -> str|None:
        """Next Page URL or None"""
        if self._nextpage is None:
            if self.is_nextpage_exists():
                self._nextpage = self._get_nextpage_url()
            else:
                return None
        return self._nextpage
                           

    @property
    def pagecount(self) -> int:
        """How many pages collection has"""
        if self._pagecount is None:
            self._pagecount = self._get_pagecount()
        return self._pagecount



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


    def _get_collection_title(self) -> str:
        "Scrape Collection Title."
        return self._tree.css(".style_breadCrumbsScroller__93Cu8 div a")[-1].text().strip()


    def is_nextpage_exists(self) -> bool:
        return bool(
            self._tree.css(".style_pagingCarrier__NVbHL div")[-1].css_first("a")
        )

    def _get_nextpage_url(self) -> str|None:
        # i should not add this try catch, but some freaking nerds touch even "private fuctions"
        try:
            return HTTPS_URL + self._tree.css(".style_pagingCarrier__NVbHL div")[-1].css_first("a").attributes['href'].strip()

        except AttributeError:
            return None


    def _get_pagecount(self) -> int:
        return int(
            self._tree.css_first(".style_pagingCarrier__NVbHL span").text()\
            .split("/")[-1].strip() 
        )
