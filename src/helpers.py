import itertools

##
#### helper functions for dictionaries
##

# get top n items of a sorted dictionary
def get_top_n(sorted_dict, n = None):
    if n is None:
        n = len(sorted_dict)

    return dict(itertools.islice(sorted_dict.items(), 0, n))

# sort a dictionary on its key
def sort_dict_by_key(unsorted_dict):
    sorted_dict = {}

    for key in sorted(unsorted_dict):
        sorted_dict[key] = unsorted_dict[key]

    return sorted_dict

# sort a dictionary on its value
def sort_dict_by_value(unsorted_dict):
    sorted_dict = {}

    for a in sorted(unsorted_dict, key=unsorted_dict.get, reverse=True):
        sorted_dict[a] = unsorted_dict[a]

    return sorted_dict