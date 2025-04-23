import random


def play_game():
    print("Welcome to Hangman")
    print("You get 5 guesses")
    one_piece = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji",
                 "Nico Robin", "Chopper", "Franky", "Brook"]

    random_word = random.choice(one_piece).lower()

    empty_list = []

    guess_limit = 5

    game_over = False

    for letter in random_word:
        empty_list += "_"
    print(empty_list)

    while not game_over:

        guess = input("Pick a letter: ").lower()
    # study this part more [position]
        for position in range(len(random_word)):
            letter = random_word[position]
            if letter == guess:
                empty_list[position] = letter
        if guess not in random_word:
            guess_limit -= 1
            if guess_limit == 0:
                print("Sorry you lose! ")
                play_again = str(input("Play again? (y/n) ")).lower()
                if play_again == "y":
                    game_over = False
                    play_game()
                elif play_again == "n":
                    game_over = True

        print(empty_list)
        print(f"You have {guess_limit} left! ")

        if "_" not in empty_list:
            print("You win!")
            play_again = str(input("Play again? (y/n) ")).lower()
            if play_again == "y":
                game_over = False
                play_game()
            elif play_again == "n":
                game_over = True


play_game()
