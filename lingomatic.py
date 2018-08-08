import random

phonemes = ['a', 'e', 'i', 'o', 'u', 't', 'g', 's', 'f']

soft = ['f', 'h', 'l', 's', 'm', 'n', 'w', 'y', 'j']
hard = ['t', 'q', 'd', 'k', 'g', 'c', 'b', 'z', 'x']
vowels = ['a', 'i', 'o', 'u', 'e']

def create_word(length):
    word = ''
    for letter in range(0, length):
        word = word + phonemes[random.randint(0, len(phonemes)-1)]
    return word

print(create_word(3))


def create_sentence(no_of_words, range_of_word_lengths):
    sentence = ''
    for word in range(0, no_of_words):
        sentence = sentence + create_word(random.randint(range_of_word_lengths[0], range_of_word_lengths[1])) + ' '
    return sentence


print(create_sentence(15, [2, 9]))

def create_custom_phonemes():
    rating = input("Enter an amount of harshness from 0 to 1")
    custom_phoneme = []
    for letter in hard:
        if random.uniform(0, 1) < float(rating):
            custom_phoneme.append(letter)
    for letter in range(len(custom_phoneme), len(soft)):
        custom_phoneme.append(soft[letter])
    custom_phoneme.extend(vowels)

    return custom_phoneme

print(create_custom_phonemes())

custom = create_custom_phonemes()

def create_varied_word(length):
    word = ''
    for letter in range(0, length):
        word = word + custom[random.randint(0, len(custom)-1)]
    return word



def create_varied_sentence(no_of_words, range_of_word_lengths):
    sentence = ''
    for word in range(0, no_of_words):
        sentence = sentence + create_varied_word(random.randint(range_of_word_lengths[0], range_of_word_lengths[1])) + ' '
    return sentence

print(create_varied_sentence(30, [2, 9]))