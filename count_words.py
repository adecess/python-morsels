from collections import Counter

def count_words(sentence):
    words = Counter(
                word.casefold().strip("¿.,!?\"'")
                for word in sentence.split()
            )
    return words

print(count_words("welcome to the jungle"))
print(count_words("oh what a day what a lovely day"))
print(count_words("Oh what a day, what a lovely day!"))
