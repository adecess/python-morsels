def count_words(sentence):
    word_mapping = dict()
    words = sentence.casefold().split(" ")
    for word in words:
        if word in word_mapping:
            word_mapping[word] += 1
        else:
            word_mapping[word] = 1
    
    return word_mapping
    

print(count_words("welcome to the jungle"))
print(count_words("oh what a day what a lovely day"))