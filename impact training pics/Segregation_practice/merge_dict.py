#Write a program to merge two dictionary. if the key exists in both then add their value.
def merge_dict(dict1, dict2):
    dict = dict1.copy()
    for key, value in dict2.items():
        if key in dict:
            dict[key]  += value
        else:
            dict[key] =  value
    return dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}
print(merge_dict(dict1, dict2))