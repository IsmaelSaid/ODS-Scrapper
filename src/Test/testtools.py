import unittest
import ScrappingPackage.tools as t
class Testwordprocessing(unittest.TestCase):

    def setUp(self):
        self.fictional_dict = {
            "region_region": ["THEME1", "thème2"],
            "region_paris": ["theme1", "THEME2"]
        }

    def test_convert_list(self):
        result = t.convert_dict_list_to_list(self.fictional_dict)
        expected = ['THEME1', 'thème2', 'theme1', 'THEME2']
        self.assertEqual(result, expected)


    def test_lower(self):
        result = t.lower(["THEME1", "thème2"])
        expected = ["theme1", "thème2"]
        self.assertEqual(result, expected)

    def test_remove_accents(self):
        result = t.remove_accents(["THEME1", "thème2"])
        expected = ["THEME1", "theme2"]
        self.assertEqual(result, expected)

        
    def test_transform(self):
        pass 