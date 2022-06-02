import random
from hangman_images import hangman_stages, logo
from hangman_words import word_list

play_again = 'y'
while play_again == 'y':
    chosen_word = random.choice(word_list)
    lives = 6
    #Create blanks
    display = ["_" for _ in range(len(chosen_word))]
    end_of_game = False
    print(logo)

    while not end_of_game:
        guess = input("Guess a letter: ")
        # check if the entered character is a letter
        if not guess.isalpha():
            print("It's not a letter. Please, try again.")
            print(*display)
            print(hangman_stages[lives])
            continue
        guess = guess.lower()
        # check if the entered character hasn't already guessed
        if guess in display:
            print("You've already guessed the letter.\nIt's displayed below ⬇⬇⬇")
            print(*display)
            print(hangman_stages[lives])
            continue
        if guess not in chosen_word:
            print(f"You are wrong. Letter -{guess}- is not in the word. You lose a live")
            lives -= 1
            if lives == 0:
                print(*display)
                print(hangman_stages[lives])
                print("You lose!")
                break
        else:
            print(f"Well done. Letter -{guess}- is in the word.")
            # changing displayed _ to matching letters
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess

        print(*display)
        print(hangman_stages[lives])
        if "_" not in display:
            print("You win!")
            end_of_game = True

    play_again = input("Wanna play again? y/n: ").lower()
    while play_again != "y" and play_again != "n":
        print("Incorrect answer :(")
        play_again = input("Wanna play again? y/n: ").lower()



