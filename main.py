from asset import hangman_art as hma
import random

# 13 Dec 2025, hangman guessing game V1 guessing the whole word with hint

guess_dict = {
    "dog": "opposite of cat",
    "fish": "can not live without water",
    "bird": "have wings",
    "cat": "opposite of dog",
    "giraffe": "long neck",
    "elephant": "long nose",
    "panda": "china",
    "worm": "disgusting",
    "lion": "king of the jungle"
}

random_pair = random.choice(list(guess_dict.items()))
random_key = random_pair[0]
random_value = random_pair[1]
hint = random_value
com = random_key

def main():
    stages = 6

    print(hma.logo)

    while True:

        if stages < 0:
            print("YOU LOSE!!")
            break

        print(f"hint: {hint}")
        user_guess = input("enter your guess words: ")

        if com == user_guess:
            print("that's correct!")
            break
        else:
            print("Incorrect Guess Again!")
            print(hma.stages[stages])
            print(f"number of guesses left {stages}")
            stages -= 1
     
if __name__ == "__main__":
    main()
