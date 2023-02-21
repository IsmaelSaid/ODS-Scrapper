import unittest
from ScrappingPackage.tools import Wordprocessing

class Testwordprocessing(unittest.TestCase):

    def setUp(self):
        fictional_dict = {
            "region_region": ["THEME1", "thème2"],
            "region_paris": ["theme1", "THEME2"]
        }
        self.wp = Wordprocessing(fictional_dict)
        self.list_words = self.wp.list_words


    def test_convert_list(self):
        """
        This method checks if convert_list works

        """
        expected_value = 4
        calculated_value = len(self.wp.convert_list())
        self.assertEqual(expected_value,calculated_value)


    def test_lower(self):
        print(self.wp.lower(self.list_words))
        self.assertTrue(True)

    def test_remove_accents(self):
        print(self.wp.remove_accents(self.list_words))

        self.assertTrue(True)


    def test_transform(self):
        print(self.wp.transform())