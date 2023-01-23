import random
from abstraction import *
num = range(1,12)
firstCard = random.choice(num)
secondCard = random.choice(num)


Dealer(firstCard, secondCard, num)

while True:
  again = input("Play again(yes/no)?").lower()
  if again == "no":
    print("Thank you for playing!")
    break
  else:
    Dealer(firstCard, secondCard, num)
  
      
  