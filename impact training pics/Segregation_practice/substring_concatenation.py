import itertools as it
def concatenate_substring(words):
    li = list(it.permutations(words))
    permutated_list =  [list(p) for p in li]
    print("Test : ",permutated_list)
    permutated_list = [li for li in permutated_list]
    substring = [''.join(letter) for letter in permutated_list]
    return substring
    
def findSubstring(s,word):
    words = concatenate_substring(word)
    m = len(s)
    n = len(words)
    res = []
    for i in range(m-n+1):
        for x in words:
            if s[i:i+n] == x:
                res.append(i)
    return res

if __name__ == "__main__":
    words = input("Enter the words : ")
    s = input("Enter the words of long length : ")
    words = words.split()
    print(findSubstring(s, words))

