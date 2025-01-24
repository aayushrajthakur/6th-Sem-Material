import itertools as it
def concatenate_substring(words):
    li = list(it.permutations(words))
    permutated_list =  [list(p) for p in li]
    permutated_list = [li for li in permutated_list]
    substring = [''.join(letter) for letter in permutated_list]
    return substring
    

def findSubstring(s,word):
    words = concatenate_substring(word)
    m = len(s)
    n = len(word)
    res = []
    for i in range(m-n+1):
        for word in words:
            if s[i:i+n] == word:
                res.append(i)
    return res
    


if __name__ == "__main__":
    words = input("Enter the words : ")
    s = input("Enter the words of long length : ")
    words = words.split()
    # words = ["ab","cd","ef"]
    # s = "wordgoodgoodgoodbestword"
    print(findSubstring(s, words))







def concatenate_words(words):
    return ''.join(words)

def findSubstring(s, words):
    if not s or not words:
        return []

    word_length = len(words[0])
    num_words = len(words)
    total_length = word_length * num_words
    word_count = {}

    # Count occurrences of each word in the list
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    res = []
    
    # Iterate through the string with a sliding window
    for i in range(len(s) - total_length + 1):
        seen_words = {}
        for j in range(num_words):
            # Get the current word from the string
            start_index = i + j * word_length
            current_word = s[start_index:start_index + word_length]
            
            if current_word in word_count:
                seen_words[current_word] = seen_words.get(current_word, 0) + 1
                
                # If the count of the current word exceeds the expected count, break
                if seen_words[current_word] > word_count[current_word]:
                    break
            else:
                break
        
        # If we have seen all words the correct number of times, add the starting index
        if seen_words == word_count:
            res.append(i)

    return res

if __name__ == "__main__":
    words = input("Enter the words (space-separated): ")
    s = input("Enter the long string: ")
    words = words.split()
    print(findSubstring(s, words))