from unicodedata import name


def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    name = list(people)
    age = list(people.values())
    mage = max(age)
    index = age.index(mage)

    
    return name[index]