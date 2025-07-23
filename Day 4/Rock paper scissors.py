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

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number, you lose!")

elif your_choice == 0:
    print(rock)
    print("you chose Rock")

elif your_choice == 1:
    print(paper)
    print("you chose Paper")

elif your_choice == 2:
    print(scissors)
    print("you chose Scissors")

computers_choice = random.randint(0,2)
print(f"Computers choice: {computers_choice}")

if computers_choice == 0:
    print(rock)

elif computers_choice == 1:
    print(paper)

elif computers_choice == 2:
    print(scissors)

if your_choice == computers_choice:
    print("it's a draw")

elif (your_choice == 0 and computers_choice == 2) or \
     ( your_choice ==1 and computers_choice == 0) or \
     (your_choice == 2 and computers_choice == 1):
    print("you win!")

else:
    print("You lose!")