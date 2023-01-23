import random
from abstraction import *
num = range(1,12)
firstCard = random.choice(num)
secondCard = random.choice(num)

Dealer(firstCard, secondCard, num)

