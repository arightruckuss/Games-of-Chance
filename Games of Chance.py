import random
import time
from random import randint

#enter starting balance
money = 100
starting_balance = money
#Write your game of chance functions here

print('\n')
print('Weclome to **AJAY\'S CASNIO ROYLE**')
time.sleep(2)
print('\n')
print('The tables you can play are: \nCOIN FLIP\nCHO-HAN\nTWO CARD\nROULETTE')
time.sleep(2)
print('\nYou walk in with £' + str(money) + '\n')
time.sleep(2)
print('You walk over to the Coin Flip table....')

#coin_flip
coin_flip_balance = starting_balance
def coin_flip(guess, bet):
  global coin_flip_balance
  print('\n')

  #Check the player wants to play this table
  coin_flip_question = input('Press Y to play the Coin Flip table: ')
  if coin_flip_question.lower() == 'y':
    print('\n')
    if bet < 0:
      return print('*Please use a positive betting amount next time*')
    if guess != 'heads' and guess != 'tails':
      return print('*Please use heads or tails next time*')
    print('You have bet: £' + str(bet))
    print('Your choice is "' + guess + '"')
    print('\n')

    #Random coin flip answer
    coin = random.randint(1, 2)
    if coin == 1:
      coin = 'Heads'
    if coin == 2:
      coin = 'Tails'
    print('Random choice is....')
    time.sleep(2)
    print(coin)
  else:
    print('\n')
    return print('Press Y next time to play the Coin Flip table')
  time.sleep(2)
  print('\n')

  #Coin flip winner checker
  if guess.lower() == coin.lower():
    coin_flip_balance = coin_flip_balance + int(bet)
    print('Your prediction of "' + guess + '" was correct')
    print('You win £' + str(bet) + '!')
  if guess.lower() != coin.lower():
    coin_flip_balance = coin_flip_balance - int(bet)
    print('Your prediction of "' + guess + '" was wrong')
    print('You lose £' + str(bet) + '!')
    
  print('Thank you for playing the Coin FLip table')
  time.sleep(2)

global cho_han_balance
cho_han_balance = coin_flip_balance
  
#Cho-Han table
def cho_han(guess, bet):
    global cho_han_balance

    cho_han_balance = coin_flip_balance
    print('\n')
    print('You walk over to the Cho-Han table')
    print('Your money is now ' + str(cho_han_balance))
    print('\n')

    #Check the player wants to play this table
    cho_han_question = input('Press Y to play the Cho-Han game: ')
    if cho_han_question.lower() == 'y':
      if bet < 0:
        return print('*Please use a positive betting amount next time*')
      if guess != 'even' and guess != 'odd':
        return print('*Please use odd or even next time*')
    else:
        print('\n')
        return print('Press Y to play Cho-Han next time')

    print('\n')
    print('Your choose an "' + guess + '" number')
    print('You have bet: ' + str(bet))
    print('\n')

    #Random dice numbers
    dice_number1 = randint(1,6)
    print('Dice number 1 is rolling a....')
    time.sleep(2)
    print(dice_number1)
    dice_number2 = randint(1,6)
    print('Dice number 2 is rolling a....')
    time.sleep(2)
    print(dice_number2)
    #Total of two dices plus prediction
    total = str(dice_number1 + dice_number2)
    print('These dice comes to: ' + total)

    time.sleep(2)
    print('\n')

    #Odd or even check against guess
    if (int(total) % 2) == 0 and guess.lower() == 'even':
        cho_han_balance += int(bet)
        print('Your prediction of an "' + guess + '" number was correct!')
        print('You win: £' + str(bet))
    elif (int(total) % 2) == 1 and guess.lower() == 'odd':
        cho_han_balance += int(bet)
        print('Your prediction of an "' + guess + '" number was correct!')
        print('You win £' + str(bet))
    else:
        cho_han_balance = cho_han_balance - int(bet)
        print('Your prediction of an "' + guess + '" numer was wrong')
        print('You lose: £' + str(bet))
        
    print('\n')
    print('Thank you playing the Cho-Han Table')
    time.sleep(2)

global two_card_balance
two_card_balance = cho_han_balance
    
#Two Card table
def two_card(bet):
    global two_card_balance
    two_card_balance = cho_han_balance
    print('\n')
    print('Your money is now ' + str(two_card_balance))
    print('You walk over to the Two Card table')
    print('\n')
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace']*4
    two_card_question = input('Press Y to play the Two Card game: ')

    #Check the player wants to play this table
    if two_card_question.lower() == 'y':
        if bet < 0:
          return print('*Please use a positive betting amount next time*')
        
        print('\n')
        print('You have bet: £' + str(bet))
        print('\n')

        #Random card choice's
        time.sleep(2)
        player_one_pick = random.choice(deck)
        if player_one_pick in deck:
            deck.remove(player_one_pick)
        print('The card drawn for you is...' )
        print('"' + player_one_pick + '"')

        time.sleep(2)
        player_two_pick = random.choice(deck)
        print('The house\'s card drawn is....')
        print(player_two_pick)
    else:
        print('\n')
        return print('Press Y next time to play the Two Card table')    

    # Check who wins
    time.sleep(1)
    print('\n')
    if(player_one_pick == player_two_pick):
        return print('Game is tied £' + str(bet) + ' is returned to player')
    if(player_one_pick > player_two_pick):
        two_card_balance += int(bet)
        print('Player wins £' + str(bet) + '!')
    else:
        two_card_balance = two_card_balance - int(bet)
        print('The house wins you lose £' + str(bet) + '!')

    print('Your have a balance of £' + str(two_card_balance))    
    time.sleep(2)
    print('\n')    
    print('Thank you playing the Two Card Table')
    time.sleep(2)

global roulette_balance
roulette_balance = two_card_balance
    
#Roulette table
def roulette(number, colour, odd_or_even, bet):
    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    global roulette_balance
    roulette_balance = two_card_balance
    print('\n')
    print('Your money is now ' + str(roulette_balance))
    print('You walk over to the Roulette table')
    print('\n')
    #Roulette numbers question
    roulette_numbers_question = input('Press Y to play Roulette Numbers: ')
    if roulette_numbers_question.lower() == 'y':
        if bet < 0:
          return print('*Please use a positive betting amount next time*')
        player_roulette_choice = number
        if number in black_numbers or number in red_numbers or number == 0:
            print('You choose the number: ' + str(number))
        else:
            print('*Unable to play please use a number between 0 - 36*')
    else:
        print('Please press Y next time to play Roulette Numbers')

    print('\n')
    #Red or Black quesiton
    red_or_black_question = input('Press Y to play Red or Black: ')
    if red_or_black_question.lower() == 'y':
        red_or_black_choice = colour
        if colour != 'red' and colour != 'black':
            print('*Unable to play use red or black next time!*')
        else:
            print('You choose the colour: ' + str(colour))
    else:
        print('Please press Y next time to play Red or Black Numbers')

    print('\n')
    #Odd or Even question
    odd_or_even_question = input('Press Y to play Odd or Even: ')
    if odd_or_even_question.lower() == 'y':
        player_odd_even_choice = odd_or_even
        if odd_or_even != 'odd' and odd_or_even != 'even':
            print('*Unable to play please use odd or even next time!*')
        else:
            print('You choose: ' + str(odd_or_even))
    else:
        print('Please press Y to play Odd or Even next time')

    print('\n')
    #roulette number spin
    roulette_wheel = [randint(0, 36)]
    roulette_number = random.choice(roulette_wheel)
 
    #Show roulette number
    print('Roulette number is....')
    time.sleep(2)
    print('\n')
    if roulette_number in black_numbers:
        print(str(roulette_number) + ' Black')
    elif roulette_number in red_numbers:
        print(str(roulette_number) + ' Red')
    else:
        print(roulette_number)

    time.sleep(2)

    #Roulette numbers answer
    if roulette_numbers_question.lower() == 'y':
        time.sleep(2)
        print('\n')
        if player_roulette_choice == roulette_number:
            print('Well done you guessed the correct number')
            print('You won £' + str(int(bet)* 35))
            roulette_balance += int(bet) * 35
            print('Your have a balance of £' + str(roulette_balance))
        else: 
            print('Number ' + str(player_roulette_choice) + ' was the wrong number')
            print('You lost £' + str(bet))
            roulette_balance -= int(bet)
            print('Your have a balance of £' + str(roulette_balance))
    time.sleep(2)   
    #Red or Black answer
    if roulette_number == 0:
        print('Your guess of "' + red_or_black_choice + '" for red or black was incorrect')
        print('You lost £' + str(bet))
        roulette_balance = roulette_balance - int(bet)
        return print('Your have a balance of £' + str(roulette_balance))
    if red_or_black_question.lower() == 'y':
        time.sleep(2)
        print('\n')
        if red_or_black_choice.lower() == 'red' and roulette_number in red_numbers:
           print('Well done you won on red!')
           print('You won £' + str(bet))
           roulette_balance += int(bet)
           print('Your have a balance of £' + str(roulette_balance))
        elif red_or_black_choice.lower() == 'black' and roulette_number in black_numbers:
            print('Well done you won on ' + red_or_black_choice + '!')
            print('You won £' + str(bet))
            roulette_balance += + int(bet)
            print('Your have a balance of £' + str(roulette_balance))
        else:
            print('Your guess of "' + red_or_black_choice + '" for red or black was incorrect')
            print('You lost £' + str(bet))
            roulette_balance -= int(bet)
            print('Your have a balance of £' + str(roulette_balance))

    time.sleep(2) 
    #Odd or Even answer
    if roulette_number == 0:
       print('Your guess of "' + player_odd_even_choice + '" for odd or even was incorrect')
       print('You lost £' + str(bet))
       roulette_balance -= int(bet)
       return print('Your have a balance of £' + str(roulette_balance))
    if odd_or_even_question.lower() == 'y':
        time.sleep(2)
        print('\n') 
        if(roulette_number % 2) == 0 and player_odd_even_choice.lower() == 'even':
             print('Well done you correctly guess even')
             print('You won £' + str(bet))
             roulette_balance += int(bet)
             print('Your have a balance of £' + str(roulette_balance))
        elif(roulette_number % 2) == 1 and player_odd_even_choice.lower() == 'odd':
            print('Well done "' + player_odd_even_choice + '" was the correct guess!')
            print('You won £' + str(bet))
            roulette_balance += int(bet)
            print('Your have a balance of £' + str(roulette_balance))
        else:
            print('Your guess of "' + player_odd_even_choice + '" for odd or even was incorrect')
            print('You lost £' + str(bet))
            roulette_balance -= int(bet)
            print('Your have a balance of £' + str(roulette_balance))
            
# Winner or loser balance checker 
def end_balance():        
  time.sleep(2) 
  print('\n')
  if roulette_balance == money:
     print('You walk away with the same amount: £' + str(roulette_balance))
  elif roulette_balance <= 0:
    print('Unlucky you lost all of your money!')
  elif roulette_balance > money:
    money_won = roulette_balance - money
    print('Well done you won £' + str(money_won) + ' and walk away with £' + str(money + int(money_won)))
  else:
    money_lost = money - roulette_balance
    print('Unlucky you lost £' + str(money_lost) + ' and walk away with £' + str(money - int(money_lost)))

    print('Thank you playing the Roulette Table')

    time.sleep(2)
    print('\n')
    print('Come again to AJAY\'S CASINO ROYLE!!')
    
#enter(heads ot tails, bet amount)
coin_flip('heads', 10)
#enter(odd or even, bet amount)
cho_han('odd', 10)
#enter(bet amount)
two_card(20)
#enter(roulette number, red or black, odd or even, amount to bet)
roulette(23, 'black', 'odd', 30)
end_balance()
