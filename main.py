import random
import math
import os

dict_file_path = os.path.split(os.path.realpath(__file__))[0]
DICTIONARY_FILE = dict_file_path + os.sep + 'words.txt'



def get_random_word(length):
    try:
        with open(DICTIONARY_FILE, "r") as words:
            words = [word.strip() for word in words]
            filtered_words = [word for word in words if len(word) == length]
            return " ".join(random.choice(filtered_words))
    except:
        print_title("ERROR")
        print("Something went wrong when opening the dictionary file.")
        print("Please check {file} existence".format(file=DICTIONARY_FILE))
        quit()


def create_blank_word(length):
    return " ".join("_" * length)


def menu_options(live_number, length):
    print("Enter 1 to play")
    print(f"Enter 2 to set number of lives, currently {live_number}")
    print(f"Enter 3 to set number of character in word, currently {length}")
    print("Enter 0 to quit")


def print_title(text):
    print("-" * 50)
    length = 25 - math.floor(len(text) / 2)
    print(" " * length + text)
    print("-" * 50)


def game_options(word, guessed_characters, lives_left):
    print("The word is:")
    print(word)
    print(f"You have tried these options: {guessed_characters}")
    print(f"You currently have {lives_left} lives.")
    print("Enter a character (or word, if you think you know it)")
    print("Enter 0 to quit")


def get_user_menu_choice():
    user_choice = input("what is your choice: ")
    while not user_choice.isnumeric() or not -1 < int(user_choice) < 4:
        user_choice = input("what is your choice: ")
    if int(user_choice) == 0:
        quit()
    return int(user_choice)


def get_user_choice(length):
    user_input = ""
    while not user_input.isalpha() and not user_input.isnumeric():
        user_input = input("What is your choice: ")
        if user_input.isalpha():
            if len(user_input) == 1 or len(user_input) == length:
                return user_input
        if user_input.isnumeric() and int(user_input) == 0:
            quit()
        user_input = ""


def change_live_number(current_live_number):
    print(f"Currently you have {current_live_number} lives.")
    new_live_number = input("How many lives do you want: ")
    while not new_live_number.isnumeric() or not int(new_live_number) > 0:
        new_live_number = input("How many lives do you want: ")
    print(f"You now have {new_live_number} lives.")
    return int(new_live_number)


def change_word_length(current_word_length):
    print(f"The word length is {current_word_length} characters")
    new_length = input("How many characters do you want in your word: ")
    while not new_length.isnumeric() or not 3 < int(new_length) < 15:
        print("please enter a number larger than 3 and smaller than 15")
        new_length = input("How many characters do you want in your word: ")
    print(f"the word length is now {new_length} characters")
    return int(new_length)


def duplicate_character_text(duplicate_character, guessed_character):
    print(f"You have already guessed {duplicate_character}")
    print(f"You already guessed these {guessed_character}")
    new_choice = get_user_choice(word_length)
    return new_choice


def get_character_index(character, word):
    i = 0
    result = []
    while i < len(word):
        if character == word[i]:
            result.append(i)
        i += 1
    return result


def replace_character(index, word, character):
    replaced_word = ''
    i = 0
    while i < len(word):
        if i in index:
            replaced_word += character
        else:
            replaced_word += word[i]
        i += 1
    return replaced_word


def wrong_guess_text(wrong_char, lives):
    print(f"the character {wrong_char}, is not in the word")
    return lives - 1


def correct_guess_text(character):
    print("-" * 50)
    print(f"the character {character} is in the word")


def game_over_check(remaining_live):
    return remaining_live <= 0


def game_over_text_lose(correct_word, guessed_letters):
    print("-" * 50)
    print("-" * 50)
    print("Game Over, you Lost")
    print("The correct word is")
    print(correct_word)
    print(f"You have tried these options: {guessed_letters}")
    quit()


def game_over_text_win(remaining_lives, correct_word):
    print("-" * 50)
    print("-" * 50)
    print("Game Over, you Win")
    print("The correct word is")
    print(correct_word)
    print(f"you still have {remaining_lives} lives left")
    quit()


word_length = 6
live = 10

print_title("MAIN MENU")
menu_options(live, word_length)
user_choice = get_user_menu_choice()


while 1 < user_choice < 4:
    if user_choice == 3:
        print_title("LENGTH")
        word_length = change_word_length(word_length)
    else:
        print_title("LIVE")
        live = change_live_number(live)
    print_title("MAIN MENU")
    menu_options(live, word_length)
    user_choice = get_user_menu_choice()


word = get_random_word(word_length)
blank_word = create_blank_word(word_length)
letters_guessed = []

while True:
    print_title("GAME")
    game_options(blank_word, letters_guessed, live)
    user_choice = get_user_choice(word_length)

    while user_choice in letters_guessed:
        user_choice = duplicate_character_text(user_choice, letters_guessed)
    letters_guessed.append(user_choice)
    if len(user_choice) == 1:
        if user_choice in word:
            character_index = get_character_index(user_choice, word)
            blank_word = replace_character(character_index, blank_word, user_choice)
            correct_guess_text(user_choice)
        else:
            live = wrong_guess_text(user_choice, live)
            if not game_over_check(live):
                print(f"you now have {live} lives left.")
    else:
        if " ".join(user_choice) == word:
            blank_word = " ".join(user_choice)
        else:
            live = wrong_guess_text(user_choice, live)
            if not game_over_check(live):
                print(f"you now have {live} lives left.")

    if word == blank_word:
        game_over_text_win(live, word)

    elif game_over_check(live):
        game_over_text_lose(word, letters_guessed)
