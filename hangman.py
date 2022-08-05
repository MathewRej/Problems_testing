import random

def get_random_word(path='/usr/share/dict/words'):
    good_words = []
    with open(path) as words:
        for word in words:
            word = word.strip()
            if len(word) < 6:
                continue
            if not word.isalpha():
                continue
            if word[0].isupper():
                continue
            good_words.append(word)
    return random.choice(good_words)

def mask_word(secret_word, guessed_letters):
    masked_word = ''
    for char in secret_word:
        if char in guessed_letters:
            masked_word += char
        else:
            masked_word += '-'
    return masked_word
