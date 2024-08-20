from unittest           import TestCase
from testlib.tools      import load_html , pp , test_cases
from svgrepo_dl.scraper import CollectionPage




class TestCollectionPage(TestCase):
    files = [
        'collection_page(1-page).html',
        'collection_page(4-pages).html',
        'collection_page(21-page).html'
    ]
    cases = [CollectionPage(load_html(f)) for f in files]
    del files




    @test_cases
    def test_images_property(self, clss:CollectionPage) -> None:
        imgs   = clss.images
        self.assertTrue(len(imgs)>0, "empty image list [].")
        pp(imgs)

    @test_cases
    def test_collection_property(self, clss:CollectionPage) -> None:
        title = clss.collection
        self.assertTrue(len(title)>0, "empty title.")
        pp(title)

    @test_cases
    def test_nextpage_func_property(self, clss:CollectionPage) -> None:
        next_page_exists = clss.is_nextpage_exists()
        self.assertEqual(type(next_page_exists), bool)
        

        if next_page_exists:
            nextpage_url = clss.nextpage
            self.assertEqual(type(nextpage_url), str)
            self.assertEqual(clss.nextpage, clss.next_page)

        pp({
            "next page url" :clss.nextpage,
            "next page"     :next_page_exists
        })


    @test_cases
    def test_pagecount_property(self, clss:CollectionPage) -> None:
        pagecount = clss.pagecount
        self.assertEqual(type(pagecount), int, "`CollectionPage.pagecount` should be an 'int'.")
        self.assertGreater(pagecount, 0)
        pp({'page count':pagecount})



