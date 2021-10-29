import random
import os

def GachaRoll():
  gamblingaddiction = True
  count = 0
  primogems = 20000
  list1 = ["Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "QiQi *****", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Harbinger of Dawn", "Slingshot", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Jean *****", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Slingshot", "Cool Steel", "Halberd", "Cool Steel", "Bloodtainted Greadsword", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Slingshot", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "QiQi *****", "Cool Steel", "Bloodtainted Greadsword", "Mona *****", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Slingshot", "Cool Steel", "Cool Steel", "Halberd", "Bloodtainted Greadsword", "Diluc *****", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Keqing *****", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Halberd", "Slingshot", "Cool Steel", "Paimon *", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Urmom ************", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Halberd", "Slingshot", "Cool Steel", "Slingshot", "Cool Steel", "Cool Steel", "Halberd", "Bloodtainted Greadsword", "Mona *****", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Halberd", "Slingshot", "Cool Steel", "Emergency food", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Halberd", "Slingshot", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Cool Steel", "Messenger", "Magic Guide", "Harbinger of Dawn", "Halberd", "Slingshot", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Ganyu *****", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Cool Steel", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword", "Cool Steel", "Cool Steel", "Harbinger of Dawn", "Cool Steel", "Cool Steel", "Cool Steel", "Bloodtainted Greadsword"]

  list2 = ["Keqing *****", "QiQi *****", "ZhongLee *****", "Mona *****", "Keqing *****", "QiQi *****", "ZhongLee *****", "Mona *****", "Diluc ******", "Keqing ******", "QiQi *****", "ZhongLee *****", "Mona *****", "Ganyu *****"]

  list3 = ["Fischl ****", "Bennett ****", "ChongYun ****", "Xin Yang ****", "Lisa ****", "Kaeye ****", "Amber ****", "Ganyu *****"]

  list4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1]

  n = list4[random.randint(0,27)]
  while gamblingaddiction == True:
    print('')
    print("------------------------------")
    print("Type 1 for roll ")
    print("Type 10 for 10 rolls ")
    print("Type 0 to go back to Menu")
    print('')

    Roll = int(input())
    
    #Function for Roll 1
    if Roll == 1:
      print('')
      print("------------------------------")
      count += 1
      primogems = primogems - 160
      print("primogems used| ", primogems)
      print('')
      if count == 90:
        print(list2[random.randint(0, 13)])
        print('')
        count = 0
      else: 
        print(list1[random.randint(0, 95)])
        print('')

    
    #Function for Roll 10
    elif Roll == 10:
      print('')
      print("------------------------------")
      count += 10
      primogems = primogems - 1600
      print("primogems used| ", primogems)
      print('')
      if count == 90:
        print(list2[random.randint(0, 13)])
        for i in range(9):
          print(list1[random.randint(0, 95)])
          print('')
        print('')
        count = 0
      else:
        for x in range(n):
          print(list3[random.randint(0,6)])
          print('')
        for i in range(10-n):
          print(list1[random.randint(0, 95)])
          print('')

    #Function to go back to Menu
    elif Roll == 0:
      gamblingaddiction = False
      os.system('clear')
      print("you can never go back...")

def Exit():
  exit()

def menu(): 
  print("GACHA GAME THE GAME")
  print("")
  choose = input("Type Y to play: ")
  print("")

  if choose.lower() == 'y':
    os.system('clear')
    GachaRoll()

menu()



