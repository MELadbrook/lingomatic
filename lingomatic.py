import random


class Language:
    PHONEMES = ['a', 'e', 'i', 'o', 'u', 't', 'g', 's', 'f']
    SOFT = ['f', 'h', 'l', 's', 'm', 'n', 'w', 'y', 'j']
    HARD = ['t', 'q', 'd', 'k', 'g', 'c', 'b', 'z', 'x']
    VOWELS = ['a', 'i', 'o', 'u', 'e']

    def __init__(self):
        pass

    def create_word(self, length):
        word = ''
        for letter in range(0, length):
            word = word + self.PHONEMES[random.randint(0, len(self.PHONEMES) - 1)]
        return word

'''    def create_word(self, length):
        word = ''
        for letter in range(0, length):
            word = word + Language.PHONEMES[random.randint(0, len(Language.PHONEMES)-1)]
        return word

    def create_sentence(self, no_of_words, range_of_word_lengths):
        sentence = ''
        for word in range(0, no_of_words):
            sentence = sentence + Language.create_word(random.randint(range_of_word_lengths[0], range_of_word_lengths[1])) + ' '
        return sentence

    def create_custom_phonemes(self, rating):
        #rating = input("Enter an amount of harshness from 0 to 1")
        custom_phoneme = []
        for letter in Language.HARD:
            if random.uniform(0, 1) < float(rating):
                custom_phoneme.append(letter)
        for letter in range(len(custom_phoneme), len(Language.SOFT)):
            custom_phoneme.append(Language.SOFT[letter])
        custom_phoneme.extend(Language.VOWELS)
        return custom_phoneme

    def create_varied_word(self, length):
        word = ''
        for letter in range(0, length):
            word = word + custom[random.randint(0, len(custom)-1)]
        return word

    def create_varied_sentence(self, no_of_words, range_of_word_lengths):
        sentence = ''
        for word in range(0, no_of_words):
            sentence = sentence + create_varied_word(random.randint(range_of_word_lengths[0], range_of_word_lengths[1])) + ' '
        return sentence'''

example = Language()



print(example.VOWELS)
print(example.create_word(12))

