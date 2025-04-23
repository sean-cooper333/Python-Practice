import random

total_score = 0

while True:
  player_choice = input('Do you want to roll the dice?: (y/n)').lower()
  if player_choice == 'y':
    while True:
      try:
          min_val = int(input('Enter a minimum value: '))
          max_val = int(input('Enter a maximum value: '))
          if min_val >= max_val:
            raise ValueError("Minimum value must be less than the Maximum value")
          break
      except ValueError as e:
          print(f"Invalid input: {e}")
          
    dice1 = random.randint(min_val, max_val)
    dice2 = random.randint(min_val, max_val)
    round_score = dice1 + dice2
    total_score += round_score
    print(f'{dice1}, {dice2}')
    print(f'You scored {round_score} this round!')
    print(f'Total Score: {total_score}')
    
  elif player_choice == 'n':
      print("Thanks for playing")
      print(f"Your final score is: {total_score}")
      break
  else:
      print("Sorry try another input!")
      