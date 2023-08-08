print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island! \nYour mission is to find the treasure")
level1 = input("You are at a cross road. where would you like to go? left or right?\n").lower()
if level1 == "right":
  level_2 = input("You came to a lake. how would you like to go? swim or boat?\n").lower()
  if level_2 == "boat":
    doors = input("There are three doors. where would you like to go? red, yellow or blue?\n").lower()
    if doors == "blue":
      print("You found the treasure! congratulations!!")
    elif doors == "red":
      print("this is a room full on fire! you lost!")
    elif doors == "yello":
      print("This room has a tiger! You lost!!")
    else:
      print("please choose correctly!!!")
  elif level_2 == "swim":
    print("bro there are crocodiles in the river. You died!!")
  else:
    print("please choose well, Motherfucker")
elif level1 == "left":
  print("you chose a wrong path and you fell in a gutter, You lost!!")
else:
  print("Choose well, ASSHOLE!")
