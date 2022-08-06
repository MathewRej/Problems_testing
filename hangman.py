import random
CONTINUE = 1
ALREADY_GUESSED = 2

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
def get_status(secret_word, guessed_letters, turns_left):
    return f"""{mask_word(secret_word, guessed_letters)}
    Guessed Letters: {" ".join(guessed_letters)}
    Turns Left: {turns_left}"""

def process_turn(secret_word, current_guess, guessed_letters, turns_left):
    if current_guess in guessed_letters:
        return f"You have already Guessed {current_guess}", turns_left, ALREADY_GUESSED
