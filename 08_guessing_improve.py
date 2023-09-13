# Guessing Game (without Loop)
import random

is_play = True

while is_play :

    secert_num = random.randint(0,5)
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit :
        guess_num = int(input("Guess a number between (0-5) : "))
        guess_count += 1

        if (secert_num == guess_num) :
            print("You win!")
            break

        print(f"Wrong guess. Guess count [{guess_count}-{guess_limit}]")

    else :
        print("Too bad! You lose T-T")
        user_play = input("Want to try again ? [ Yes | No ] : ").lower()

        if (user_play != "yes") :
            is_play = False
