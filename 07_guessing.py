# Guessing Game (without Loop)
import random
secert_num = random.randint(0,5)
guess_num = int(input("Guess a number between (0-5)"))

if (secert_num == guess_num) :
    print("You win!")
else :
    print("You lose")