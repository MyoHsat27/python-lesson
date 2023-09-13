# Rock | Paper | Scissor Program
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = [rock, paper, scissor]
user_choice = int(input("Enter your choice [ 0 - Rock | 1 - Paper | 2 - Scissor ] : "))
computer_choice = random.randint(0,2)

if (user_choice >= 0 and user_choice <= 2) :
    print("Your choice :")
    print(choice[user_choice])
    print("Computer choice : ")
    print(choice[computer_choice])

    if (user_choice == 0 and computer_choice == 2) :
        print("You win!")
    elif (user_choice == 1 and computer_choice == 0) :
        print("You win!")
    elif (user_choice == 2 and computer_choice == 1) :
        print("You win!")
    elif (user_choice == 0 and computer_choice == 1) :
        print("You lose)")
    elif (user_choice == 1 and computer_choice == 2) :
        print("You lose)")
    elif (user_choice == 2 and computer_choice == 0) :
        print("You lose)")
    else :
        print("It is tie")
else : 
    print("Invalid Choice")