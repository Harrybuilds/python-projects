#!/usr/bin/python3

#import all needed contents(variables,functions,e.t.c) in the blackjackfunction module

from blackjackfunctions import *


if __name__ == "__main__":
    play = True

    functions_organizer()
    while play:
        
        again = input('do you want to play again?: ')
        
        if again.lower() == 'y':
            functions_organizer()
        else:
            play = False
            
