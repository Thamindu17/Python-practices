import random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level):
    if level=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return  HARD_LEVEL_ATTEMPTS

def check_number(guess_number,answer,attemps):
    if guess_number>answer:
        print("guess is too high")
        return attemps-1
    elif guess_number<answer:
        print("guess is too low")
        return attemps-1
    else:
        print(f" your guess is correct,the answer is {answer}.")
def game():
    print("let me think a number between 1 to 50.")
    answer=random.randint(1,50)
    print(answer)
    level=input("easy or hard:").lower()
    attemps=set_difficulty(level)

    guess_number=0
    while attemps!=answer:
        print(f"you have {attemps} attemps ")
        guess_number=int(input("guess the number between 1 to 50:"))
        attemps=check_number(guess_number,answer,attemps)
        if attemps==0:
            print("out of guesses")
            return
        #elif guess_number==answer:
            #return
        elif guess_number!=answer:
            print(f"try again.")
game()

