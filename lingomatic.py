import random
import functools


def debug(function):
    @functools.wraps(function)
    def _debug(*args, **kwargs):
        output = function(*args, **kwargs)
        print('%s(%r, %r): %r' % (function.__name__, args, kwargs, output))
        return output
    return _debug


class Language:
    PHONEMES = ['a', 'e', 'i', 'o', 'u', 't', 'g', 's', 'f']
    SOFT = ['f', 'h', 'l', 's', 'm', 'n', 'w', 'y', 'j']
    HARD = ['t', 'q', 'd', 'k', 'g', 'c', 'b', 'z', 'x']
    VOWELS = ['a', 'i', 'o', 'u', 'e']

    def __init__(self, size_of_vocab):
        self.phoneme = self.PHONEMES
        self.vocabulary = self.create_vocabulary(size_of_vocab, random.randint(1, 20))

    def create_word(self, length):
        '''
        Create a random word of a given length.

            Parameters:
                length (int): Number of characters for word.

            Returns:
                word (str): Randomly made word.
        '''
        word = ''
        for letter in range(0, length):
            word = word + self.phoneme[random.randint(0, len(self.phoneme) - 1)]
        return word

    def create_sentence(self, no_of_words, word_length):
        '''
        Create a random sentence of a given length with words of a given range of lengths.

            Parameters:
                no_of_words (int): Number of words to create for the sentence.
                word_length (int): Maximum length of words.

            Returns:
                sentence (str): Randomly created sentence.
        '''
        sentence = ''
        for word in range(no_of_words):
            sentence = sentence + self.create_word(random.randint(1, word_length)) + ' '
        return sentence[:-1]

    def sentencify(self, sentence):
        sentence = sentence[0].upper() + sentence[1:]
        return sentence + "."

    def create_vocabulary(self, number_of_words, word_length):
        '''
        Create a randomly made dictionary of words.

            Parameters:
                number_of_words (int): Number of words to create.
                word_length (int): Maximum length of words.

            Returns:
                vocab_list (dict): Dictionary of words.
        '''
        vocab_list = {}
        for word in range(number_of_words):
            vocab_list['Word {}'.format(str(word))] = self.create_word(random.randint(1, word_length))
        return vocab_list


class CustomPhoneme(Language):
    def __init__(self, rating, size_of_vocab):
        super().__init__(size_of_vocab)
        self.rating = rating
        self.phoneme = self.create_custom_phonemes()
        self.vocabulary = self.create_vocabulary(size_of_vocab, random.randint(1, 20))

    def create_custom_phonemes(self):
        custom_phoneme = []
        for letter in self.HARD:
            if random.uniform(0, 1) < float(self.rating):
                custom_phoneme.append(letter)
        for letter in range(len(custom_phoneme), len(self.SOFT)):
            custom_phoneme.append(self.SOFT[letter])
        custom_phoneme.extend(self.VOWELS)
        return custom_phoneme


example = Language(50)
example_subclass = CustomPhoneme(0, 50)


'''
print(example.phoneme)
print(example.create_word(12))
print(example_subclass.phoneme)
print(example_subclass.create_word(12))
#print(example.create_sentence(25, 9))
#print(example_subclass.sentencify(example_subclass.create_sentence(12, 17)))
print(example.vocabulary)
print(example_subclass.vocabulary)
'''
