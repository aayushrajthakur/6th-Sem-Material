#write a program that takes string as input and return the dictionary where the keys are the words and the values are their frequencies.
def word_seperate(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(".","")
    words = sentence.split()
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict


sentence = "My name is Aayush raj thakur. I am from Janakpur. Welcome to nepal."
print(word_seperate(sentence))