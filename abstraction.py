import random

def Dealer(firstCard,secondCard, num):
  dealersHand = firstCard + secondCard
  if dealersHand == 21:
    print(firstCard, secondCard)
    print("House wins! :(")
    return
  else:
    print(f'Dealers hand: {firstCard}')
    Player(firstCard,secondCard, num, dealersHand)
   

def Player(firstCard,secondCard, num, dealersHand):
#  timesDrawn = 0
  firstHand = firstCard + secondCard
  list = [firstCard, secondCard]
  print(f'Your hand: {firstCard, secondCard}')
  if firstHand == 21:
    print("Blackjack :)")
    return
  while True:
    choice = input("Do you want to draw another card(yes/no)? ").lower()
    if choice == "no":
        if firstHand > 21:
          print("Bust! :(")
          return
        elif firstHand == 21:
          print("Blackjack! :)")
          return      
        elif firstHand < dealersHand:
          print(dealersHand)
        print("You lost! :(")
        break
    if choice == "yes":
      while True:
        card = random.choice(num)
        if firstHand + card < 21 and card == 11:
          list.append(card)
          firstHand += card
          print(list)
          break
        elif firstHand + card > 21 and card == 11:
          firstHand += 1
          list.append(1)
          print(list)
          break
        else:
          firstHand += card
          list.append(card)
          print(list)
          break
        if firstHand > 21:
          print("Bust! :(")
          return
        elif firstHand == 21:
          print("Blackjack! :)")
          return      
        elif firstHand < dealersHand:
          print(f'The Dealers hand was {dealersHand}')
          print("You lost! :(")
          return



  # timesDrawn += 1
      # if timesDrawn == 1:
      #   card = random.choice(num)
      # if timesDrawn == 2:
      #   card2 = random.choice(num)
      # if firstHand + card < 21 and card == 11:
      #   firstHand += card
      #   print(f"Your hand: {firstCard, secondCard, card}")
      # if timesDrawn == 2:
      #   print(f"Your hand: {firstCard, secondCard, card, card2}")
      # elif firstHand + card > 21 and card == 11:
      #   firstHand += 1
      #   print(f"Your hand: {firstCard, secondCard, card}")
      #   if timesDrawn == 2:
      #     print(f"Your hand: {firstCard, secondCard, card, card2}")
      # else:
      #   print(f"Your hand: {firstCard, secondCard, card}")

      


      
    
      
      
      
    