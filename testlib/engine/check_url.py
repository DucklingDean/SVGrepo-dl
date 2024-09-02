from svgrepo_dl.engine import true_exists_collection_url
from unittest          import TestCase, result




class TestURLCheckers(TestCase):
    
    def test_check_collection_url(self):
        inputs = [
            'hello', 
            'some_collection',
            'https://www.svgrepo.com/collection/chunk-16px-thick-interface-icons/',
            'https://www.svgrepo.com/collection/wrong_url/',
            'https://www.svgrepo.com/collection/business-sharp-line-duotone-icons/',
            'https://www.svgrepo.com/svg/530576/calendar'
        ]
        result = [
            'https://www.svgrepo.com/collection/chunk-16px-thick-interface-icons',
            'https://www.svgrepo.com/collection/business-sharp-line-duotone-icons',
        ]
        for bl in [False,True]:
            print("\n","\033[33m="*3,f'verbose={bl}',"=\033[0m"*3)
            self.assertListEqual(
                true_exists_collection_url(inputs,bl),
                result 
            )



