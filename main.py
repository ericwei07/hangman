import random


def get_random_word():
    with open("words.txt", "r") as words:
        return random.choice(words.readlines()).strip()


def create_blank_word(word):
    return " ".join("_" * len(word))


def menu_text(live_number):
    print("-" * 51)
    print(" " * 21 + "MAIN MENU")
    print("-" * 51)
    print("Enter 1 to play")
    print(f"Enter 2 to set number of lives, currently {live_number}")
    print("Enter 0 to quit")


def live_text():
    print("-" * 51)
    print(" " * 23 + "LIVES")
    print("-" * 51)


def game_text():
    print("-" * 50)
    print(" " * 23 + "GAME")
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
    while not user_choice.isnumeric() or not -1 < int(user_choice) < 3:
        user_choice = input("what is your choice: ")
    if int(user_choice) == 0:
        quit()
    return int(user_choice)


def get_user_choice(length):
    user_input = "a1"
    while not user_input.isalpha() and not user_input.isnumeric():
        user_input = input("What is your choice: ")
        if user_input.isalpha():
            if len(user_input) == 1 or len(user_input) == length:
                return user_input
        if user_input.isnumeric() and int(user_input) == 0:
            quit()
        user_input = "a1"


def change_live_number(current_live_number):
    print(f"Currently you have {current_live_number} lives.")
    new_live_number = input("How many lives do you want: ")
    while not new_live_number.isnumeric() or int(new_live_number) <= 0:
        new_live_number = input("How many lives do you want: ")
    print(f"You now have {new_live_number} lives.")
    return int(new_live_number)


def duplicate_character_text(duplicate_character, guessed_character):
    print(f"You have already guessed {duplicate_character}")
    print(f"You already guessed these {guessed_character}")
    new_choice = get_user_choice()
    return new_choice


def get_character_position(character, word):
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


word = get_random_word()
blank_word = create_blank_word(word)
word_length = len(word)
word = " ".join(word)
live = 10
valid_user_choice = [1, 2, 0]
letters_guessed = []
character_user_guess = ""
word_user_guess = ""

menu_text(live)
user_choice = get_user_menu_choice()
print(word)

while user_choice == 2:
    live_text()
    live = change_live_number(live)
    menu_text(live)
    user_choice = get_user_menu_choice()

while True:
    game_text()
    game_options(blank_word, letters_guessed, live)
    user_choice = get_user_choice(word_length)

    while user_choice in letters_guessed:
        user_choice = duplicate_character_text(user_choice, letters_guessed)
    letters_guessed.append(user_choice)
    if len(user_choice) == 1:
        if user_choice in word:
            character_position = get_character_position(user_choice, word)
            blank_word = replace_character(character_position, blank_word, user_choice)
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
