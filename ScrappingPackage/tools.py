import numpy as np
import unidecode as u
import pandas as pd 
import collections

class Wordprocessing:
    def __init__(self, dict_words):
        self.dict_words = dict_words
        self.list_words = self.convert_list()

    
    def flatten(self,l):
        return [item for sublist in l for item in sublist]

    def convert_list(self)-> list:
        """
        convert a dict of words into a list

        Returns:
            list: a list of words 
        """
        # First convert the dictionary into a list of list 
        l = self.dict_words.values()
        return self.flatten(l)

    def lower(self, list_words : list) -> list:

        """
        Converts all words containing upper case letters to words containing only lower case letters

        Returns:
            list: a list containing only words with lower case letters
        """
        result = [item.lower() for item in list_words]
        return result

    def remove_accents(self, list_words : list) -> list:
        results = [u.unidecode(item) for item in list_words]
        return results
    
    def remove_stop_words(self)-> list: 
        stopwords = [",","&","-","du","/"]
        """
        remove all stop words

        Returns:
            list: 
        """
        pass

    def transform(self) -> list :
        result = self.remove_accents(self.lower(self.list_words))
        return result

    def get_words_counts_df(self):
        results = self.transform()
        count_results = collections.Counter(results)
        resutls_df = pd.DataFrame({"theme":count_results.keys(),"compte":count_results.values()})
        return resutls_df