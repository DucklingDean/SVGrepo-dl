from .scraper_core              import ScraperCore




class CollectionPage(ScraperCore):
    """
    page with URL like: 'svgrepo.com/collection/**'
    """
    _images    : list[dict]  = None
    _collection: str         = None



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





    @property
    def title(self) -> str: return self.collection










