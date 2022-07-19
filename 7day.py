#Step 1 
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random

random_words = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

input_guess = input("Guess a letter: ")
input_guess = input_guess.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if input_guess in random_words:
    print("Yes, it is in the word!", random_words)
else:
    print("No, it is not in the word!", random_words)
        
    