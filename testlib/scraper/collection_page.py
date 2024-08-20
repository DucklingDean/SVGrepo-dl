from testlib.tools      import load_html , pp , test_cases
from svgrepo_dl.scraper import CollectionPage
from .page_nav_test     import PageNavTest


class TestCollectionPage(PageNavTest):
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



    



