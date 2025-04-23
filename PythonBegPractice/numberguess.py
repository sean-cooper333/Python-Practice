import random 

random_int = random.randint(1, 100)

while True:
  try:
    random_input = int(input('Guess the number between 1 and 100: '))
    
    if random_int < random_input:
      print('Too High! Lower!!')
    elif random_int > random_input:
      print('Too Low!! Go Higher!!')
    else:
      print(f'Good Job!! The number was: {random_int}')
      break
  except ValueError:
    print('Please enter a valid number')

    
    
      

    
 
    
