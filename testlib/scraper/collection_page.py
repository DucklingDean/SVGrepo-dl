from unittest           import TestCase
from testlib.tools      import load_html , pp 
from svgrepo_dl.scraper import CollectionPage




class TestCollectionPage(TestCase):
    def test_class(self):
        for htmlfile in ['collection_page(1-page).html', 'collection_page(4-pages).html']:
    
            htmlcode = load_html(htmlfile)
            clss = CollectionPage(htmlcode)
            self.images_property(clss)
            self.collection_property(clss)
            self.nextpage_func_property(clss)

    def images_property(self, clss:CollectionPage) -> None:
        imgs   = clss.images
        self.assertTrue(len(imgs)>0, "empty image list [].")
        pp(imgs)

     
    def collection_property(self, clss:CollectionPage) -> None:
        title = clss.collection
        self.assertTrue(len(title)>0, "empty title.")
        pp(title)


    def nextpage_func_property(self, clss:CollectionPage) -> None:
        next_page_exists = clss.is_nextpage_exists()
        self.assertEqual(type(next_page_exists), bool)
        pp({"next page": next_page_exists})

        if next_page_exists:
            nextpage_url = clss.nextpage
            self.assertEqual(type(nextpage_url), str)
            self.assertEqual(clss.nextpage, clss.next_page)
        pp({"next page url":clss.nextpage})



