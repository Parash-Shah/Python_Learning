#Used import random to generate random selections of the symbols.
#Used list to create list of the symbol and to convert symbols in items.
#used list to print symbols randomly.
#used if and elif statements to compare inputs and printout correct results.
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image= [rock,paper,scissors]
user_choice= int(input("Choose between rock, paper and scissor. Type number 0 to 2 respectively to choose your symbol\n"))
print(game_image[user_choice])
computer_choice= random.randint(0,2)
print(f"computer chose: {game_image[computer_choice]}")
if user_choice>= 3 and user_choice<0:
    print("you entered invalid input.")
elif user_choice==computer_choice:
    print("It's a draw!")
elif user_choice== 0 and computer_choice== 2:
    print("you win!")
elif user_choice==2 and computer_choice==0:
    print("You loose")
elif user_choice>computer_choice:
    print("You win!")
elif user_choice<computer_choice:
    print("You loose!")