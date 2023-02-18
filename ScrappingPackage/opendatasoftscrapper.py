import requests
import json
from pandas import DataFrame


class Opendatasoftscrapper:

    CATALOG_EXPORTS_ENDPOINT = "catalog/exports/"
    FACETS_ENDPOINT = "catalog/facets/"
    EXPORT_TYPE = "json"
    VERSION = "api/v2/"
    VALID_ENDPOINTS = [
        CATALOG_EXPORTS_ENDPOINT,
        FACETS_ENDPOINT
    ]

    def __init__(self, url : str):
        """
        This class holds various methods to scrap easily open data portals with few lines of code. 

        Args:
            url (str): url of the portal : ex https://data.regionreunion.com
        """
        self.url = url

    def get_catalog_json(self,params : dict) -> json:
        """
        a method to scrapp the catalog 

        Args:
            params (dict): this dict holds parameters for the get request. 
            cf: >>>help(requests) for more details 
            cf: Opendatasoft's Explore API Reference Documentation (V2) 

        Returns:
            json: return the result of the request 
        """
        created_url = self.create_url(endpoint = "catalog/exports/")
        response = requests.get(
            url = created_url,
            params=params)
        
        # You can check the error code here
        assert response.status_code == 200
        return response.json()
        
    def create_url(self, endpoint : str) -> str:
        """
        a method to create a complete url

        Args:
            endpoint (str): the name of the endpoint

        Returns:
            str: a complete url like https://data.regionreunion.com/api/v2/facets/ 
        """

        # check if the endpoint is valid and well written
        if self.is_valid_endpoint(endpoint):
            # le endpoint est valide on peut retourner l'URL 
            if (endpoint == self.CATALOG_EXPORTS_ENDPOINT):
                return self.url + self.VERSION + self.CATALOG_EXPORTS_ENDPOINT + self.EXPORT_TYPE
            elif (endpoint == self.FACETS_ENDPOINT):
                return self.url + self.VERSION + self.FACETS_ENDPOINT
        
        return None

    def is_valid_endpoint(self,endpoint : str) -> bool :
        """
        a method to check if an endpoint is valid
        Args:
            endpoint (str): endpoint name: ("catalog/exports/" | "catalog/facets/")

        Returns:
            bool: true only if the endpoint is valid
        """
        return endpoint in self.VALID_ENDPOINTS

    def get_facets_json(self, params : dict = {"timezone":"UTC"}, pos_facets : int = 0) -> json :
        created_url = self.create_url("catalog/facets/")
        response = requests.get(
            url = created_url,
            params = params
        )
        return response.json()

    def get_facets_pandas(self)-> DataFrame:
        """        
        Returns:
            DataFrame: return a datafram holding the number of dataset by theme
        """
        facet_json = self.get_facets_json()
        facets_df = DataFrame(
            facet_json.get('facets')[0].get('facets')
        )
        return facets_df

    def get_federated_dataset_json(self) -> json:
        """
        This method returns all federated dataset.
        # TODO rename this method and the test as well

        Returns:
            json: a json of federated dataset.
        """
        custom_params = dict(
            where = "federated = true",
            limit = -1,
            timezone = "UTC"
        )
        federated_dataset = self.get_catalog_json(params = custom_params)
        return federated_dataset
    
    
    def get_not_federated_dataset_json(self) -> json:
        """
        Thid method return all unfederated dataset.

        Returns:
            json: return a json file of all unfederated dataset
        """
        custom_params = dict(
            where = "federated = false",
            limit = -1,
            timezone = "UTC"
        )
        federated_dataset = self.get_catalog_json(params = custom_params)
        """_summary_

        Returns:
            _type_: _description_
        """
        return federated_dataset

    def count_federated_dataset(self) -> int:
        """
        this method returns the number federated dataset 

        Returns:
            int: the number of federated dataset
        """
        federated_dataset = self.get_federated_dataset_json()
        return len(federated_dataset)
    
    def count_not_federated_dataset(self) -> int:
        """
        this method returns the number of unfederated dataset 

        Returns:
            int: number of unfederated dataset
        """
        not_federated_dataset = self.get_not_federated_dataset_json()
        return len(not_federated_dataset)

    def count_dataset(self) -> int :
        """
        this method returns the total number of dataset

        Returns:
            int: _description_
        """
        return self.count_federated_dataset() + count_not_federated_dataset

    def get_federated_and_not_federated_df(self) -> DataFrame:
        """
        

        Returns:
            DataFrame: _description_
        """
        nb_federated = self.count_federated_dataset()
        nb_not_federated = self.count_not_federated_dataset()

        return DataFrame({
            "nb_dataset":[nb_federated,nb_not_federated, nb_federated + nb_not_federated],
            "type_dataset" : ["federated","not_federated","total"]
        })

    def get_federated_on_not_federated_rate(self) -> float:
        """
        this method returns the percentage of unfederated dataset 

        Returns:
            float: ratio
        """
        nb_federated = self.count_federated_dataset()
        nb_not_federated = self.count_not_federated_dataset()

        rate = nb_not_federated * 100 / (nb_federated + nb_not_federated)

        return rate

    def get_all_results(self) -> dict:
        """
        # TODO calculate the number of dataset/personn

        Returns:
            dict: return a dict holding, the number of federated/unfederated dataset and the rate of fed/unfed dataset.
        """
        results = dict()
        results['nb_federated_and_not_federated_df'] = self.get_federated_and_not_federated_df()
        results['nb_dataset_per_theme_df'] = self.get_facets_pandas()
        results['rate_federated_on_not_federated'] = self.get_federated_on_not_federated_rate()

        return results