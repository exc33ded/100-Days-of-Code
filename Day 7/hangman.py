word_list = ['advark', 'baboon', 'camel']

import random

chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}')
guess = input("Guess a Letter: ").lower()

word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(display)

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
