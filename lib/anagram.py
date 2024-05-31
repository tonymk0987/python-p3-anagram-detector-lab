# your code goes here!
class Anagram:
    def __init__(self, word):#instantiates with a single argument, a word. .  
        self.word = word.lower()

    def match(self, word_list):#contains a method called "match". .
        # Filters the word list to include only words that are anagrams of self.word
        return [word for word in word_list if sorted(word.lower()) == sorted(self.word)]
