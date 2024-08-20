import collections
from .page_nav_test     import PageNavTest
from testlib.tools      import load_html , pp , test_cases
from svgrepo_dl.scraper import HomePage



class TestHomePage(PageNavTest):
    files = [
        "home_page(page=1).html",
        "home_page(page=10).html"
    ]
    cases = [HomePage(load_html(fl)) for fl in files]
    del files
    


    @test_cases
    def test_all_images_property(self, clss:HomePage) -> None:
        images = clss.all_images
        self.assertTrue(len(images)>0)
        pp(images)


    

    @test_cases 
    def test_all_collections_property(self, clss:HomePage) -> None:
        collections = clss.all_collections
        self.assertTrue(len(collections)>0)
        pp(collections)



    
