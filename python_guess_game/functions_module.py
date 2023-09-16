# This module should contain all functions needed to play the gusessing game


# involking the python interpreter
#!/usr/bin/python3


#get player name
#set player default balance, max_tries, default_player_try = 0
#comfirm player bet
#computer generates a random number within a certain range
#get player guess
#validate player guess is within the certain range
#validate if player guess equals computer randomly generated number, if false, drop hint

#player tries guessing again, until max tries is reached, if after max tries reached and player guess is still failed, bet is deducted from balance, but if before max tries is reached and player guess equals computer randomly generated number, "player bet" + 100% of the player bet is added to the player balance


#/* version 2 */
#save player details in a file
#fetch player details in a file



#/* version 3 */
#save player game_histroy into  a file
#secure player details and game history file




######################################################
from random import randint

def player_name():
    name = input("Enter your name: ")
    return name


def player_game_details():
    balance = 1000
    level = 1
    maximum_tries = 3
    default_try = 0
    return [balance,
            level,
            maximum_tries,
            default_try]


def confirm_bet(balance):
    while True:
        try:
            bet = int(input("Enter your bet($): "))

            if bet <= balance:
                balance = balance - bet
                return [balance, bet]
            else:
                print("insufficient fund, please fund your account")
        except ValueError:
            print("please, Enter a valid amount to stake")



def computer_number(minimum, maximum):
    computer_guess = randint(minimum, maximum)
    return computer_guess



def player_guess(min, max):
    while True:
        try:
            guess = int(input(f"Enter your guess between range {min} and {max}: "))
            return guess
        except ValueError:
            print("Enter a valid guess number")


def validate_player_guess_within_range(player_guess, max_number):
    if player_guess in range(max_number):
        return True
    else:
        print(f"Enter a number within the range {max_number}")
        return False


def validate_if_win(player_guess, computer_number):
    if player_guess == computer_number:
        return True
    else: return False


def hint(player_guess, computer_number):
    if player_guess > computer_number:
        print("Your guess is a bit higher")
    else: print("You want to try something higher")


def update_details_in_game(balance, stake, max_tries, tries, level):
    if tries < max_tries:
        pass

    elif tries <= max_tries and validate_if_win():
        balance += stake + (stake * 100/100)
        level += 1
        return [balance, 0, max_tries, 0, level]
    else:
        balance -= stake
        print(f"oh oh...You just lost ${stake},try again, you just might be lucky next time")
        return [balance, 0, max_tries, 0, level]


