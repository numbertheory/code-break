#!/usr/bin/python3

import random


def colorize(color, text):
    color_table = {
        "yellow": "\033[1;33;40m",
        "red": "\033[1;31;40m",
        "green": "\033[1;32;40m",
        "blue": "\033[1;34;40m",
        "purple": "\033[1;35;40m",
        "standard": "\033[0;37;40m"
    }
    return "{}{}{}".format(color_table[color], text, color_table["standard"])


def create_game():
    game = list()
    for i in range(0, 5):
        game.append(
            random.choice(['y', 'r', 'g', 'b', 'p'])
            )
    return game


def verify_guess(guess):
    if len(guess) != 5:
        return False
    else:
        for i in guess:
            if i not in ['y', 'r', 'g', 'b', 'p']:
                return False
        return True


def find_intersection(guess, game):
    # Take in two lists and find if they have an intersection or not
    for i in guess:
        if i in game:
            return True
    return False


def declare_winner(guesses):
    return "You win! It only took you {} tries.".format(guesses)


def give_hints(rc_rp, rc_wp):
    rc_rp_hints = ["C" for x in range(0, rc_rp)]
    rc_wp_hints = ["W" for x in range(0, rc_wp)]
    return rc_rp_hints + rc_wp_hints


guess = 1

maximum_guesses = 12

game = create_game()

guess_history = list()

while guess < (maximum_guesses + 1):
    # right color, right position
    rc_rp = 0
    # right color, wrong position
    rc_wp = 0

    wrong_place = list()

    remaining_game = list()

    guess_text = input('#{} Guess? '.format(guess))
    if guess_text.lower() in ['q', 'c']:
        if guess_text.lower() == 'q':
            break
        # Cheat mode, this reveals the answer
        # uncomment these three lines to enable.
        elif guess_text.lower() == 'c':
            print("".join(game))
            continue

    if len(guess_text.lower()) != 5:
        print('Invalid guess.')
        continue

    if find_intersection([x for x in guess_text.lower()], game):
        list_guess = [x for x in guess_text.lower()]
        for j in range(0, 5):
            if list_guess[j] == game[j]:
                rc_rp += 1
            else:
                wrong_place.append(list_guess[j])
                remaining_game.append(game[j])

        for place in wrong_place:
            if place in remaining_game:
                rc_wp += 1

        if rc_rp == 5:
            print(declare_winner(guess))
            break
        else:
            guess_history.append(
                {"guess": list_guess, "hints": give_hints(rc_rp, rc_wp)})
            print(guess_history)
            guess += 1

    elif verify_guess(guess_text.lower()):
        list_guess = [x for x in guess_text.lower()]
        guess_history.append(
            {"guess": list_guess, "hints": give_hints(rc_rp, rc_wp)})
        print(guess_history)
        guess += 1
    else:
        print('Invalid guess.')
