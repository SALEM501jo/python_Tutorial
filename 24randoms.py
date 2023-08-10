import random 

x=random.randint(1,10)
  #* this will return a random number between (a,b) including the endings 
print(x)

y=random.random()
 #* this will return a random float number between (0,1) 
#print(y)

guess=["paper","rock","scissors"]
z=random.choice(guess)
#* this will choose a random item from the list
#print(z)

cards=[1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
#* this will mix the list and gives new order every time
#print(cards)
