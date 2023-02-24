import random 

stone = '''
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

sizzer = '''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image_choice =[stone, paper, sizzer ]

attempts = 0




print("Stone Paper and Sizzer Game Started! /nChoose : 0-Stone, 1-Paper, 2-Sizzer") 

User_Choice = int(input("Enter your choice : "))
print("Your choice:/n")
print(image_choice[User_Choice])

Computer_Choice = random.randint(0,2) #computer choices2

print("Computer Choice : \n")
print(image_choice[Computer_Choice])




while True :
      attempts += 1
      User_Choice = int(input("Enter your choice : "))
      if User_Choice > 2 or User_Choice < 0:
            print("You lose !! ")
      elif User_Choice == 0 and Computer_Choice == 2:
            print("You Win !!")
      elif Computer_Choice == 0 and User_Choice == 2:
            print("You lose again !!")
      elif Computer_Choice > User_Choice:
            print("You Lose!!")
      elif User_Choice > Computer_Choice:
            print("You win !!")
      elif User_Choice == Computer_Choice:
            print("It's Draw !!!")



# if User_Choice >2 or User_Choice <0:
#       print("You lose !! ")
# elif User_Choice ==0 and Computer_Choice ==2:
#       print("You Win !!")
# elif Computer_Choice == 0 and User_Choice ==2:
#       print("You lose again !!")
# elif Computer_Choice>User_Choice:
#       print("You Lose!!")
# elif User_Choice>Computer_Choice:
#       print("You win !!")
# elif User_Choice == Computer_Choice:
#       print("It's Draw !!!")
