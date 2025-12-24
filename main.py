from asset import hangman_art as hma
import random

# 13 Dec 2025, hangman guessing game V1 guessing the whole word with hint

words = [
    "python", "hangman", "programming", "developer",
    "computer", "algorithm", "function", "variable"
]

random_words = random.choice(words)
split_text = " ".join(random_words)
com = random_words

def game_logic():

     while True:

        if stages < 0:
            print("YOU LOSE!!")
            break

        user_guess = input("enter your guess letter: ")
        guess.append(user_guess)

        if user_guess in split_text:
            print("that's is correct")
            print(guess)
        else:
            print("Nope Try another letter!!")
            print(hma.stages[stages])
            stages -= 1


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
        guess.append(user_guess)

        if user_guess in split_text:
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
