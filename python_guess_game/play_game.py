import functions_module as f

min = 0
max = 10

player_name = f.player_name()

player_profile = f.player_game_details()
player_profile.insert(0, player_name)


print(f"Welcome to the Number Guessing game\n\nHeres's your profile\n\nPlayername = {player_profile[0]}")
print(f"Balance = welcome bonus of ${player_profile[1]}\nLevel = {player_profile[2]}\nMaximum tries = {player_profile[3]}\nTries = {player_profile[4]}")

"""
player profile[0] = player name
player proflie[1] = balance
player profile[2] = level
player profile[3] = maximum_tries
player profile[4] = try
"""

set_bet = f.confirm_bet(player_profile[1])

print(f"\n\n{set_bet}")

#update balance after stake
player_profile[1] = set_bet[0]
print(player_profile)


#set_bet[0] = balance after bet
#set_bet[1] = amount staked


#computer generates random number
computer = f.computer_number(min, max)


#player enters a guess
guess = f.player_guess(min, max)


is_valid = f.validate_player_guess_within_range(guess, max)
print(is_valid)


#Ensuring guess is within the required guess range
while not is_valid:
    guess = f.player_guess(min, max)
    is_valid = f.validate_player_guess_within_range(guess, max)
    print(is_valid)


if_win = f.validate_if_win(guess, computer)
print("you win?",if_win, "computers's number = ", computer)

if not if_win:
    player_profile[4] += 1
    f.hint(guess, computer)
    print(f"tries: {player_profile[4]}")

    
while player_profile[4] != player_profile[3]:
    if if_win:
        print("Congratulations, you've guessed correctly")
        break;
    else:
        guess = f.player_guess(min, max)
        is_valid = f.validate_player_guess_within_range(guess, max)
        f.hint(guess, computer)
        player_profile[4] += 1
        print(f"tries: {player_profile[4]}") 
    

"""
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
"""
