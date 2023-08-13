word_list = ['advark', 'baboon', 'camel']

import random

chosen_word = random.choice(word_list)
guess = input("Guess a Letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print('False')
