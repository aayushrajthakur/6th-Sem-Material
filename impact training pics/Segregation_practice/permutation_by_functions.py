import itertools as it
def concatenate_substring(words):
    li = list(it.permutations(words))
    permutated_list =  [list(p) for p in li]
    permutated_list = [li for li in permutated_list]
    substring = [''.join(letter) for letter in permutated_list]
    return substring

words = ["ab","cd","ef"]
print(concatenate_substring(words))