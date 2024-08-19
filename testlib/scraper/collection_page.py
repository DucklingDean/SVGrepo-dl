from unittest           import TestCase
from testlib.tools      import load_html , pp 
from svgrepo_dl.scraper import CollectionPage




class TestCollectionPage(TestCase):
    def test_get_images(self):
        for htmlfile in ['collection_page(1-page).html', 'collection_page(4-pages).html']:
            htmlcode = load_html(htmlfile)

            clss = CollectionPage(htmlcode)

            imgs   = clss.images
            self.assertTrue(len(imgs)>0, "empty image list [].")
            pp(imgs)

            title = clss.collection
            self.assertTrue(len(title)>0, "empty title.")
            pp(title)

            next_page_exists = clss.is_nextpage_exists()
            self.assertEqual(type(next_page_exists), bool)
            pp({"next page": next_page_exists})

            if next_page_exists:
                nextpage_url = clss.nextpage
                self.assertEqual(type(nextpage_url), str)
                self.assertEqual(clss.nextpage, clss.next_page)
            pp({"next page url":clss.nextpage})



