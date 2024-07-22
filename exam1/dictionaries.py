
def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for key in keylist:
        if key in datadict:
            del datadict[key]

    return datadict
    pass

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    if key in datadict.values():
        return True
    else:
        return False
    pass

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return min(ddd,key=ddd.get)
    pass

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return max(ddd,key=ddd.get)
    pass

def letterfreq(word):
    '''
    # Write a function that returns a dictionary of letter frequencies from a word
    '''
    result={}
    for cha in word:
        if cha in result:
            result[cha]+=1
        else:
            result[cha]=1

    return result
    pass