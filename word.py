def category_choosing():
    """
    Print the opening of the game and choose the category of the word
    :return: The category key to the words_dir directory
    """
    string = """Welcome to Hang Man
      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/"""

    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.01)
    try:
        category_num = int(input("select the category:\n1 - Food\n2 - Animals\n3 - Programming languages\n4 - super heroes\n"))
    except:
        category_num = 1
    if category_num == 1:
        category = "food"
    elif category_num == 2:
        category = "animals"
    elif category_num == 3:
        category = "Programming languages"
    elif category_num == 4:
        category = "super heroes"
    else:
        category = "food"
    print("Try to guess the word and save the man\nGuess your first letter")
    return category


def choose_word(word_list, index):
    """
    # פונקציה שבוחרת מילה מתוך רשימת המילים
    :param word_list: list of words from the dictionary
    :param index: random number int
    :return: the random chosen word
    """

    number_of_words = len(word_list)
    while index >= number_of_words:
        index = index - number_of_words
    return word_list[index]


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    #  פונקציה לבדיקת תקינות קלט
    :param letter_guessed: אות שהשחקן ניסה לנחש
    :param old_letters_guessed: רשימת האותיות שנוחשו כבר
    :return: False - אם האות לא חוקית או קיימת כבר True אם האות תקינה
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    # פונקציה שבודקת אם התו תקין באמצעות אפליקצייה קודמת ואם כן מוסיפה לרשימת המילים שנוחשו
    :param letter_guessed: the letter the user have try to guess
    :param old_letters_guessed: list of already guessed letters
    :return: True if the letter is valid, False if not and also show the letters that already guessed
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("already guessed letter")
        show_list = " -> ".join(sorted(old_letters_guessed))
        print("the letters you have guessed are\n", show_list)
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    # פונקציה שלוקחת את המילה והאותיות שנוחשו ומחזירה אותיות וקויים עבור אותיות שלא נוחשו עדיין
    :param secret_word: the word the user need to guess
    :param old_letters_guessed: list of already guessed letters
    :return: the letters that already guessed in their right place and _ where letters not guessed yet
    """
    hidden_letter = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_letter = hidden_letter + letter
            hidden_letter = hidden_letter + " "
        else:
            hidden_letter = hidden_letter + "_ "
    return hidden_letter


def check_win(secret_word, old_letters_guessed):
    """
    #פונקציה שבודקת אם המשתמש ניצח
    :param secret_word: the secret word that chosen to the game
    :param old_letters_guessed: list of already guessed letters
    :return:True if al letter of the word in the list, False if not all letter of the word in list
    """
    win_word = ""
    for letter in secret_word:
        if letter not in old_letters_guessed:
            win_word = win_word + "n"
    if "n" in win_word:
        return False
    else:
        return True


def print_hangman(num_of_tries):
    """
    :param num_of_tries: int number represent the number of fails attempts
    :return: print of the hang man stage
    """
    global HANGMAN_PHOTOS
    print(HANGMAN_PHOTOS["stage_" + str(num_of_tries)])


def end_game(end_game_result, chosen_word):
    """
    :param end_game_result:use the return True or False of the function check_win
    :param chosen_word: the word that was chosen to the game
    :return print if the user win or lose
    """
    if end_game_result:
        print("You were able to successfully save the man\n", r"""     /\
     /__\    \O/
    |____|    |
    |_||_|   / \ """)
    else:
        print("Your man is dead, try again in the next life!\nthe word was", chosen_word)
        print(r"""    x-------x
    |       |
    |       0
    |       
    |      /|\ 
    |      / \ 
        """)


HANGMAN_PHOTOS = {
    'stage_0': """    |
    |
    |
    |
    |""",
    'stage_1': """    x-------x
    |
    |
    |
    |
    |""",
    'stage_2': """    x-------x
    |       |
    |       0
    |       
    |       
    |       """,
    'stage_3': """    x-------x
    |       |
    |       0
    |       |
    |       
    |       """,
    'stage_4': r"""    x-------x
    |       |
    |       0
    |      /|  
    |       
    |       """,
    'stage_5': r"""    x-------x
    |       |
    |       0
    |      /|\ 
    |       
    |       """,
    'stage_6': r"""    x-------x
    |       |
    |       0
    |      /|\ 
    |      / 
    |       """,
    'stage_7': r"""    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |       """}

words_dir = {"food": ["lemon", "banana", "orange", "milk", "agg"],
             "animals": ["cow", "lion", "dog", "cat", "elefant"],
             "Programming languages": ["python", "javascript", "java", "html", "ruby", "swift"],
             "super heroes": ["batman", "superman", "spiderman", "ironman", "captainamerica", "thor",]}
