from random import sample

count=16
player_1=input("enter first player's name")
player_2=input("enter second player's name")
"""print("there are 16 sticks.you can pick 1,2,3 set of sticks ")
print(player_1,'pick set of sticks')
stick=int(input("enter the set of sticks"))
print(player_2,"pick your set of sticks")
stick_1=int(input("enter the set of sticks"))
while True:
      if stick==1:
          print("have remaining" ,count-stick)
          break
      elif stick==2:
          print('have remaining ',count-stick)
          break
      elif stick==3:
          print("have remaining ",count-stick)
          break
      else:
          print("invalid set of sticks")"""


while count!=0:

    if count>0:
        print(count)
        choice=int(input(f"{player_1} choice between 1,2 or 3:"))
        count=count-choice
        player=player_1

    if count>0:
        print(count)
        choice = int(input(f"{player_2} choice between 1,2 or 3:"))
        count = count - choice
        player=player_2

if count==0:

    print(f"{player} lost the match")