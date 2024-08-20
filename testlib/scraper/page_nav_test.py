from unittest      import TestCase
from testlib.tools import  load_html ,pp , test_cases
from typing        import Type





class PageNavTest(TestCase):







    @test_cases
    def test_next_page_property(self, clss) -> None:        

        next_page_url = clss.next_page
        self.assertEqual(clss.nextpage, clss.next_page)

        pp({
            "next page" : next_page_url
        })

    
    @test_cases
    def test_prev_page_property(self, clss:Type) -> None:
        prev_page_url = clss.prev_page
        self.assertEqual(clss.prevpage, clss.prev_page)

        pp({
            "prev page" : prev_page_url
        })



    @test_cases
    def test_totalpages_property(self, clss:Type) -> None:
        total_pages = clss.total_pages
        self.assertEqual(type(total_pages), int, "`CollectionPage.pagecount` should be an 'int'.")
        self.assertGreater(total_pages, 0)
        pp({'total_pages':total_pages})


