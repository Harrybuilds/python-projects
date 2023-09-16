from random import randint
lives = 3
score = 0
level = 1
minimum = 0
maximum = 10

name = input("Enter your name: ")
print(f"welcome {name}, Let the game begin")

def get_random():
    return randint(minimum, maximum)


def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("You've entered an invalid number, try again")


def validate(guess, maximum, minimum):
    if guess > maximum or guess < minimum:
        print(f"your guess shouldn't be less than {minimum} and"
                      f" it shouldn't be higher than {maximum}")
        return False
    return True


def drop_hint(number, guess):
    if guess > number:
        print("Try a higher number")
    else:
        print("Try a lower number")


def check_status(number, guess):
    print(number) 
    if guess == number:
        return True
    else:
        drop_hint(number, guessed)
        return False


def win():
        print("congrants, You guessed right")
        global score 
        score += 1
        global level 
        level += 1
        global minimum 
        minimum += 5
        global maximum
        maximum += 5
        play_again = input("want to play again? ")
        while play_again.lower()  != "yes" or play_again.lower() != "no":
            play_again = input("want to play again? ")
            
        if play_again == "yes": play()    


def play():
    print(f"Level {level}")
    print(f"guess a number between {minimum} and {maximum}")
    print(f"Score: {score}")
    number = get_random()
    
    guessed = get_guess()
    
    if not validate(guessed, maximum, minimum):
        status = check_status(number, guessed)
        if status:
            win()




play ()

