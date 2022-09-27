def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    k=len(key)
    dic={}
    for i in range(1,k+1):
        dic[i]=value[i-1]
    return dic