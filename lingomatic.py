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

    def create_sentence(self, no_of_words, word_length):
        sentence = ''
        for word in range(no_of_words):
            sentence = sentence + self.create_word(random.randint(1, word_length)) + ' '
        return sentence[:-1]

    def sentencify(self, sentence):
        sentence = sentence[0].upper() + sentence[1:]
        return sentence + "."


class CustomPhoneme(Language):
    def __init__(self, rating):
        super().__init__()
        self.rating = rating
        self.phoneme = self.create_custom_phonemes()

    def create_custom_phonemes(self):
        custom_phoneme = []
        for letter in self.HARD:
            if random.uniform(0, 1) < float(self.rating):
                custom_phoneme.append(letter)
        for letter in range(len(custom_phoneme), len(self.SOFT)):
            custom_phoneme.append(self.SOFT[letter])
        custom_phoneme.extend(self.VOWELS)
        return custom_phoneme


example = Language()
example_subclass = CustomPhoneme(0)



print(example_subclass.PHONEMES)
print(example_subclass.phoneme)
print(example_subclass.create_word(12))
print(example.create_sentence(25, 9))
print(example_subclass.sentencify(example_subclass.create_sentence(12, 17)))

