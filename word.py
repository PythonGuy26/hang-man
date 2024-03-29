def opening_game():
    """
    print the opening of the game
    """
    print(r"""Welcome to Hang Man
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
Try to guess the word and save the man
Guess your first letter""")


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


def choose_word(file_path, index):
    """
    # פונקציה שבוחרת מילה מתוך רשימת המילים
    :param file_path: the list of word file path
    :param index: random number int
    :return: the random chosen word
    """
    open_file = open(file_path)
    file_content = open_file.read()
    word_list = file_content.split(",")
    number_of_words = len(word_list)
    while index > number_of_words:
        index = index - number_of_words
    return word_list[index]


def print_hangman(num_of_tries):
    """
    :param num_of_tries: int number represent the number of fails attempts
    :return: print of the hang man stage
    """
    global HANGMAN_PHOTOS
    print(HANGMAN_PHOTOS["stage_" + str(num_of_tries)])


def end_game(end_game_result):
    """
    :param end_game_result:use the return True or False of the function check_win
    :return:print if the user win or lose
    """
    if end_game_result:
        print("You were able to successfully save the man\n", r"""     /\
     /__\    \O/
    |____|    |
    |_||_|   / \ """)
    else:
        print("Your man is dead, try again in the next life!")
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
