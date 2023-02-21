from random import randint

print('Nhap dam la keo: ')
player = input()
computer = randint(0, 2)

if computer == 0:
  computer = "dam"
if computer == 1:
  computer = "la"
if computer == 2:
  computer = "keo"

print("---")
print("You choose: " + player)
print("Computer chooses: " + computer)
print("---")

if player == computer:
  print("Draw")
else:
  if player == "keo":
    if computer == "dam":
      print("You lose")
    else:
      print('You win')
  elif player == "la":
    if computer == "keo":
      print("You lose")
    else:
      print("You win")
  elif player == "dam":
    if computer == "keo":
      print("You win")
    else:
      print('You lose')
  else:
    print("Pls enter again")
