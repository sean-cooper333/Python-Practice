import random

moves = ["r", "p", "s"]

while True:
  computer_move = random.choice(moves)
  player_move = input('Welcome to Rock, Paper, Scissors pick your move (r/p/s), or (q) to quit').lower()
  print(player_move)
  if player_move == "q":
    break
  elif player_move not in moves:
    print('You need to pick r p s')
    continue
  print(f"Computer Played: {computer_move}")
  if player_move == computer_move: 
    print("It's a tie!")
  elif(player_move == "r" and computer_move == "s") or \
    (player_move == "s" and computer_move == "p") or \
    (player_move == "p" and computer_move == "r"):
    print('You win!')
  else: 
    print('You Lose!')
