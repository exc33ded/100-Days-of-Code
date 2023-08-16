word_list = ['advark', 'baboon', 'camel']

import random

chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}')

end_of_game = False
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a Letter: ").lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win!!")
