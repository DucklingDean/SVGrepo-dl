import collections
from collections.abc import Collection
from re import split
from svgrepo_dl.toolkit.globals import HTTPS_URL
from selectolax.parser          import Node
from .page_nav                  import PageNav




class HomePage(PageNav):
    """
    Works for homepages like:
    'https://www.svgrepo.com/'
    'https://www.svgrepo.com/collections/'
    'https://www.svgrepo.com/collections/all/*'(what ever the page number)
    """


    _all_images     :list[dict] = None
    _all_collections:list[dict] = None




    @property
    def all_images(self) -> list[dict]:
        if self._all_images is None:
            self._all_images = [{
                "title"     :img_element.attributes['alt'].strip(),
                "url"       :HTTPS_URL+img_element.attributes['src'].strip(),
                "file-name" :img_element.attributes['src'].strip().split("/")[-1]
            } for img_element in self._tree.css(".style_collectionListing__7_icr .style_CollectionImages__HaFfn img")]

        return self._all_images
    

    @property
    def all_collections(self) -> list[dict]:
        if self._all_collections is None:
            self._all_collections = self._get_all_collections()
        return self._all_collections 




    def _get_all_collections(self):
        """
        Get all collections in page with there images.
        [
            {
            "title" :"...",
            "url"   :"...",
            "images":[],
            "total-images":"..."
            }
        ]
        """
        # You should call this before before title
        def total_images(crd:Node) -> int:
            span  = crd.css_first('.style_title__556fI span')
            total = int(span.text().strip())
            span.decompose()
            return total

        
        card2imgs = lambda crd:[{
            "title"     :img.attributes["alt"].strip(),
            "url"       :HTTPS_URL+img.attributes["src"].strip(), 
            "file-name" :img.attributes["src"].strip().split("/")[-1]
        }for img in crd.css('img')]

        cards = self._tree.css(".style_collectionListing__7_icr .style_Collection__pbtoU")
        return [
            {
                "total-images" :total_images(crd),
                "title"        :crd.css_first('.style_title__556fI').text().strip(),
                "url"          :HTTPS_URL+crd.css_first('a').attributes["href"].strip(),
                "images"       :card2imgs(crd)
            }
        for crd in cards]




    



