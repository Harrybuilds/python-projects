#!/usr/bin/python3

#import needed functions and data from their respective modules
from random import choice
import  game_art as art
from os import system

data = __import__ ('game_data').data



def pick_at_random(data):
    """
    function to pick an element at rondom
    and return the picked element
    """
    data = choice(data)
    return data



def play(first, second):
    
    score = 0
    play_on = True
    
    while play_on:
        system('clear')
        print(art.logo,'\n')
        print(f'Your score: {score}')
        print('Compare A: {}, a {}, from {}'.format(first['name'], first['description'], first['country']))

        print(art.vs)

        print('Compare B: {}, a {}, from {}'.format(second['name'], second['description'], second['country']))

        player_choice = input("Who has more followers? Type 'A' or 'B': ")

        if player_choice.upper() == 'A':
            play_on = first['follower_count'] > second['follower_count']

        elif player_choice.upper() == 'B':
            play_on = second['follower_count'] > first['follower_count']
        else:
            play_on = False

        if play_on == True:
            score += 1
            first = second
            second = pick_at_random(data)
        else:
            system('clear')
            print(art.logo,'\n')
            print(f"your final score: {score}")


def main ():
    
    first = pick_at_random(data)
    second = pick_at_random(data)
    play(first, second)

if __name__ == '__main__':
    main()
