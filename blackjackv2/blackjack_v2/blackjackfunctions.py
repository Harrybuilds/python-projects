#!/usr/bin/python3

#import choice and system function from their respective modules
from random import choice
from os import system


art = logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   


#global variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

target = 21




def pick_number(sequence):
    """
    function to randomly pick a number
    from a sequence and return the randomly picked number

    """
    number = choice(sequence)
    return number

def fill_list():
    """
    function to fill the player and computer
    list with randomly picked numbers and return
    sum of player numbers and sum of computer numbers
    """
    player_numbers = []
    computer_numbers = []
    turn = 0
    
    while len(player_numbers) < 2:
        picked_number = pick_number(cards)
        if turn % 2 == 0:
            computer_numbers.append(picked_number)
        else:player_numbers.append(picked_number)
        turn += 1
    return player_numbers, computer_numbers

def verify_if_blackjack(player_numbers, computer_numbers):
    """
    function to verify if player or
    computer has a blackjack or if to continue the game
    """
    winner = None
    play_on = True
    
    if sum(player_numbers) == target:
        if computer_numbers != target:
            winner = 'player'

        elif computer_numbers == target:
            winner = 'draw'

        return winner

            
    elif sum(computer_numbers) == target:
        if player_numbers != target:
            winner = 'computer'

        elif player_numbers == target:
            winner = 'draw'

        return winner


    else:
        comp_options = ['y', 'n']
        while play_on:
            print(f'Your cards {player_numbers}, your current score: {sum(player_numbers)}')
            print(f'computer first card: {computer_numbers[0]}')

            
            player_reply = input('do you want another card?: ')
            if player_reply.lower() == 'y':
                picked = choice(cards)
                player_numbers.append(picked)

                comp_reply = choice(comp_options)
                if comp_reply == 'y':
                    picked = choice(cards)
                    computer_numbers.append(picked)
                    


                if 11 in player_numbers:
                    if sum(player_numbers) > target:
                        for ind, num in enumerate(player_numbers):
                            if num == 11:
                               player_numbers[ind] = 1
                elif 11 in computer_numbers:
                    if sum(computer_numbers) > target:
                        for ind, num in enumerate( computer_numbers):
                            if num == 11:
                                computer_numbers[ind] = 1



                if sum(player_numbers) > target or sum(computer_numbers) > target:
                    play_on = False
                
            else:
                play_on = False
                
        return winner



def decide_winner(player_numbers, computer_numbers, winner=None):
     """
     function to decide winner of the game

     """
     
     print(f'Your cards {player_numbers}, your final score: {sum(player_numbers)}')
     print(f'computer cards: {computer_numbers}, computer final score: {sum(computer_numbers)}')
     
     if winner:
         if winner == 'player':
             print('You win, got a black jack 😎')
         elif winner == 'computer':
             print('You lose, your opponent got a black jack 😱')
         else: print("it's a draw 🙃")

     else:
         if sum(player_numbers) > target:
             print(f'You lose, you scored over {target} 😭')
         elif sum(computer_numbers) > target:
             print(f'You win, your opponent scored over {target} 😎')
         else:
             if target - sum(player_numbers) > target - sum(computer_numbers):
                 print('You lose 😤')
             
             elif target - sum(player_numbers) < target - sum(computer_numbers):
                 print('You win 😎')

             else: print("it's a draw 🙃")
         


def functions_organizer():
    """
    function to organize all other functions
    in order for them to work together and get
    the expected result
    returns nothing
    """
    system('clear')

    print(art)
    
    player, computer = fill_list()
    who_is_the_winner = verify_if_blackjack(player, computer)
    decide_winner(player, computer, who_is_the_winner)
    return
