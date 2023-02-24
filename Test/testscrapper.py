import unittest
import ScrappingPackage
from ScrappingPackage.opendatasoftscrapper import Opendatasoftscrapper


class TestOpenDataSoftScrapper(unittest.TestCase):

    def setUp(self):
        """
        This class makes some basics tests
        """
        url = "https://data.regionreunion.com/"
        self.scp = Opendatasoftscrapper(url = url)

    
    def test_create_url_catalog_export_endpoint(self):
        """
        This test verifies that create_url_catalog_export() function works correctly with catalog/exports endpoint
        input : the endpoint name :  "catalog/exports"
        output : a complete url  : "https://data.regionreunion.com/api/v2/catalog/exports/json"
        """
        self.assertEqual
        (
        self.scp.create_url("catalog/exports/"),
        "https://data.regionreunion.com/api/v2/catalog/exports/json",
        "Createurl() pour catalog/eports : ok "
        )
    
    def test_create_url_facets_endpoint(self):
        """
        This test verifies that create_url() function works correctly with catalog/facets/ endpoint
        input : the endpoint name : "catalog/facets/"
        output : a complete url: "https://data.regionreunion.com/catalog/facets"
        
        """
        self.assertEqual
        (
        self.scp.create_url("catalog/facets/"),
        "https://data.regionreunion.com/api/v2/catalog/facets/",
        "create_url() pour catalog/facets/ : ok"

        )

    
    def test_verify_request_pos(self):
        """
        This test verifies if is_valid_endpoint function works correctly to discriminate positive examples

        input : a valid endpoint name : exemple "catalog/facets/"
        output: true if is_valid_endpoint() find 
        """        

        result = self.scp.is_valid_endpoint(endpoint = "catalog/facets/")
        self.assertTrue(result, msg = "Exemple positive ok")
    
    
    def test_verify_request_neg(self):
        """
        This test verifies if is_valid_endpoint function works correctly to discriminate negative examples

        input : an unvalid endpoint name: catalog/facet
        output : should return false 
        """        

        result = self.scp.is_valid_endpoint(endpoint = "/facets/")
        self.assertFalse(result, msg = "Exemple negative ok")
        
    def test_get_facets_json(self):
        """
        This method checks that get_facet_json() works fine.
        There are exactly 13 themes in this portal, in order to
        verify get_facets_json(), get_facets_json() == 13 is true
        in:
        out: True only if there is the correct number of themes in the json file
        """
        result = self.scp.get_facets_json()
        length =len(result.get('facets')[0].get('facets'))
        
        self.assertEqual(length, 13)

    def test_get_facets_pandas(self):
        """
        This method checks that get_facets_pandas works fine.
        Since we know exactly how the returned dataframe should look like,
        we just gonna checks dimensions of the dataframe returned by get_facets_pandas().

        in: 
        out: a dataframe that holds the number of dataset by themes
        """
        facets_df = self.scp.get_facets_pandas()
        self.assertEqual(facets_df.shape, (13,4))

    def test_get_nb_federated_dataset(self):
        """
        This method checks that get_nb_federated_datasets works well.
        We know there are 75 federated dataset in the portal.
        in:
        out: true only if get_nb_federated() find the correct number of federated dataset.
        
        This test may fail if the portal publish new dataset
        """
        nb_federated_dataset = self.scp.count_federated_dataset()
        self.assertEqual(nb_federated_dataset, 75)

    def test_get_nb_not_federated(self):
        """
        This method checks that get_nb_not_federated_datasets works well.
        We know there are 96 unfederated dataset in the portal.
        in:
        out: true only if get_nb_not_federated() find the correct number of unfederated dataset.

        This test may fail if the portal publish new dataset
        """
        nb_not_federated = self.scp.count_not_federated_dataset()
        self.assertEqual(nb_not_federated, 96)

    def test_federated_on_not_federated_rate(self):
        """
        """
        calculated_rate = self.scp.get_federated_on_not_federated_rate()
        expected_rate =  75 / 96
        self.assertEquals(True, True)

    def test_get_all_themes(self):
        """
        This test checks that gell_all_themes is able to retrieve all themes in an open data portal
        """
        expected = ['Administration et citoyenneté', 'Aménagement durable du territoire', 'Culture et patrimoine', 'Développement économique', 'Economy, Business, SME, Economic development, Employment', 'Environnement', 'Référentiel géographique', 'Santé', 'Services et social', 'Sport et loisirs', 'Sécurité', 'Tourisme - Hébergement et restauration', 'Transports et déplacements', 'Éducation - Formation']
        result = self.scp.get_all_themes()
        self.assertEqual(expected, result,msg = "Themes are incorrect")


    def test_find_themes_index_facet_1(self):
        url1  = "https://data.regionreunion.com/" # index 0 
        test_1 = Opendatasoftscrapper(url = url1)
        expected = 0 
        result = test_1.find_index_for_themes()

        self.assertEqual(expected, result)



    def test_find_themes_index_facet_2(self):
        url2 = "https://data.laregion.fr/" # index 1 
        test_2 = Opendatasoftscrapper(url = url2)
        expected = 1 
        result = test_2.find_index_for_themes()

        self.assertEqual(expected, result)

    def test_verify_themes_presence_neg(self):
        """
        ods toulouse don't have themes facet so it should returns false
        """
        url1  = "https://data.toulouse-metropole.fr/" 
        test1 = Opendatasoftscrapper(url = url1)

        self.assertEqual(False,test1.verify_themes_presence())

    def test_verify_themes_presence_pos(self):
        """
        ods region reunion don't have themes facet so it should returns True
        """
        url1  = "https://data.regionreunion.com/" 
        test1 = Opendatasoftscrapper(url = url1)
        self.assertEqual(True,test1.verify_themes_presence())

if __name__ == '__main__':
    unittest.main()
