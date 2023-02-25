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
    

def words_summary(dict_of_list : dict):
    """
    Args:
        self (list_words): _description_

    Returns:
        _type_: _description_
    """
    tmp = convert_dict_list_to_list(dict_of_list)
    results = remove_accents(lower(tmp))
    join_result = " ".join(results)

    # TODO:Could be better, but it's fine. cf import re, re.sub()
    stopwords = [",","&","-","/"]
    for word in stopwords:
        join_result = join_result.replace(word," ")
    
    
    count_results = collections.Counter(join_result.split(" "))
    resutls_df = pd.DataFrame(
                            {"theme":count_results.keys(),
                            "compte":count_results.values()})

    # TODO: Could be better but it's fine, create 1 function to create a big string of themes,1 function to count words and a
    # another to remove stop words.
    return resutls_df, join_result
