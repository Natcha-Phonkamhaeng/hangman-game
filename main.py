from asset import hangman_art as hma
from asset import hangman_word as hmw
import random

random_words = random.choice(hmw.word_list)
split_text = " ".join(random_words)
com = random_words

def main():
    print(split_text)
    guess = []
    stages = 6

    print(hma.logo)

    while True:

        if stages < 0:
            print("YOU LOSE!!")
            break

        user_guess = input("enter your guess letter: ")

        if user_guess in split_text:
            guess.append(user_guess)
            print("that's is correct")
            print(guess)
        elif random_words == user_guess:
            print("you won")
            break
        else:
            print("Nope Try another letter!!")
            print(hma.stages[stages])
            stages -= 1
    
if __name__ == "__main__":
    main()