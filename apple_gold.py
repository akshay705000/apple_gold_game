import time
from random import* 
global gold 
global apples
gold=0
apples=0
def start():
 global apples
 print("hello and welcome!")
 name=input("whay your name: ")
 print('welcome',name)
 print("the objective of game is  to collect apples")
 print('after collecting apples you can sell them')
 choice=input("do you want to play y/n: ")
 if choice == 'y':
  print('lets get started')
  print("you have currently %d apples"%(apples))
  beg()
 else:
  print("see you later")
  
  
def beg():
 global apples
 if apples > 20:
  print("you have won the game")
  print('do you wany to sell it y/n: ')
  r=input()
  if r == 'y'
   print("you have % daimonds"%(apples*10)
   print("congratulations")
   print("come again")
 else:  
  pick=input("do you want to pick the apple y/n: ")
  if pick == 'y':
   a=randint(1,10)
   b=randint(1,11)
   c=randint(1,11)
   m='a*b-a+b+c'
   print("evaluate and press answer ",a,'*',b,'-',a,'+',b,'+',c)
   v=int(input())
   d=eval(m)
   if d == v:
    time.sleep(1)
    print("you have picked a apple")
    apples=apples+1
    print("you have currently %d apples"%(apples))
    beg()
   else:
    print("you gave wrong answer")
    sell=input("do you want to sell apples y/n: ")
    if sell =='y':
     global gold
     print("you have currently %d apples"%(apples))
     print("you have sold your apples")
     gold=apples*10
     apples=0
     print("you have %d golds"%(gold))
    else:
     beg()	
start()  
 
