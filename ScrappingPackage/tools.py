import numpy as np
import unidecode as u
import pandas as pd 
import collections

def flatten(l):
    return [item for sublist in l for item in sublist]

def convert_dict_list_to_list(dict)-> list:
    """
    convert a dict of words into a list
    Returns:
        list: a list of words 
    """
    # First convert the dictionary into a list of list 
    l = dict.values()
    return flatten(l=l)

def lower(list_words : list) -> list:

    """
    Converts all words containing upper case letters to words containing only lower case letters

    Returns:
        list: a list containing only words with lower case letters
    """
    result = [item.lower() for item in list_words]
    return result

def remove_accents(list_words : list) -> list:
    results = [u.unidecode(item) for item in list_words]
    return results
    
def remove_stop_words(list_words)-> list: 
    stopwords = [",","&","-","du","/"]
    """
    remove all stop words

    Returns:
        list: 
    """
    pass

def get_words_counts_df(list_words):
    """
    Args:
        self (list_words): _description_

    Returns:
        _type_: _description_
    """
    # results = self.transform()
    count_results = collections.Counter(results)
    resutls_df = pd.DataFrame({"theme":count_results.keys(),"compte":count_results.values()})
    return resutls_df
