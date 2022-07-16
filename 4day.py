import random;

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

choose_game=[rock,paper,scissors]

choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

computerChoose = random.randint(0,2)

if(choose==computerChoose):
    print("Please again")
elif(choose==0 and computerChoose==1):
    print(choose_game[choose])
    print("Computer choose")
    print(choose_game[computerChoose])
    print("You lose")
elif(choose==1 and computerChoose==2):
    print(choose_game[choose])
    print("Computer choose")
    print(choose_game[computerChoose])
    print("You lose")
elif(choose==2 and computerChoose==0):
    print(choose_game[choose])
    print("Computer choose")
    print(choose_game[computerChoose])
    print("You lose")
elif(choose==0 and computerChoose==2):
    print(choose_game[choose])
    print("Computer choose")
    print(choose_game[computerChoose])
    print("You win")
elif(choose==1 and computerChoose==0):
    print(choose_game[choose])
    print("Computer choose")
    print(choose_game[computerChoose])
    print("You win")
elif(choose==2 and computerChoose==1):
    print(choose_game[choose])
    print("Computer choose")
    print(choose_game[computerChoose])
    print("You win")
