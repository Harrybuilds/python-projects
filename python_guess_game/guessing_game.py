from random import randint

def play():
    win = "Congratulations, you guessed right"
    loss = "oh...sorry...try again"

    
    replies = ["yes", "no"]
    number = randint(1 , 10)
    guess = int(input("Enter your guess : "))

    reply = input("Is that your final guess?")
    while reply not in replies:
        print("please enter a correct answer: (yes or no)")
        reply = input("is that your final guess: ")
#    if reply == "yes":
#       continue
#    else:
#       continue

    if number > guess: hint = "you are a bit lower"
    else: hint = "you're a bit higher"

    if guess == number: print(win)
    else: print(loss,  hint)

    play_again = input("want to play again")

    if play_again: play()
    else: quit()


play ()
