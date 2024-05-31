import time
import random
import word
category = word.category_choosing()
random_index = random.randint(1, 10)
chosen_word = word.choose_word(word.words_dir[category], random_index)  # the game pick a word to guess
number_of_fails = 0
list_of_already_guessed_letters = []
while number_of_fails <= 7:
    word.print_hangman(number_of_fails)
    print(word.show_hidden_word(chosen_word, list_of_already_guessed_letters))
    guessed_letter = input("Guess a letter:")  # the user try to guess a letter
    guessed_letter = guessed_letter.lower()
    if guessed_letter in chosen_word:
        print("Well done!")
    elif guessed_letter in list_of_already_guessed_letters:
        pass
    else:
        number_of_fails = number_of_fails + 1
    word.try_update_letter_guessed(guessed_letter, list_of_already_guessed_letters)
    if word.check_win(chosen_word, list_of_already_guessed_letters):
        break
word.end_game(word.check_win(chosen_word, list_of_already_guessed_letters), chosen_word)
c = input("Press Enter to Exit")
