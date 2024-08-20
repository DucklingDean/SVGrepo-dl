from unittest           import TestCase
from testlib.tools      import load_html , pp , test_cases
from svgrepo_dl.scraper import CollectionPage



class TestCollectionPage(TestCase):
    files = [
        'collection_page(1-page).html',
        'collection_page(4-pages).html',
        'collection_page(21-pages).html',
        'collection_page(4-pages)(page=3).html'
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
        self.assertEqual(clss.collection, clss.title)
        pp(title)


    @test_cases
    def test_next_page_property(self, clss:CollectionPage) -> None:        

        next_page_url = clss.next_page
        self.assertEqual(clss.nextpage, clss.next_page)

        pp({
            "next page" : next_page_url
        })

    
    @test_cases
    def test_prev_page_property(self, clss:CollectionPage) -> None:
        prev_page_url = clss.prev_page
        self.assertEqual(clss.prevpage, clss.prev_page)

        pp({
            "prev page" : prev_page_url
        })



    @test_cases
    def test_totalpages_property(self, clss:CollectionPage) -> None:
        total_pages = clss.total_pages
        self.assertEqual(type(total_pages), int, "`CollectionPage.pagecount` should be an 'int'.")
        self.assertGreater(total_pages, 0)
        pp({'total_pages':total_pages})


    



