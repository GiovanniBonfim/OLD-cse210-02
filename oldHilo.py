import random


def main():
    playAgain = "y"
    score = 300
    while playAgain.lower() == "y":
        r1 = randomNum()
        r2 = randomNum()
        print(f"The card is : {r1}")
        guess = input("Higher or Lower? [h/l] : ")

        # higher
        if guess.lower() == "h":
            if r2 > r1:
                print(f"Correct! Next Card was: {r2}")
                score += 100
                print(f"Your score is: {score}")
                playAgain = input("Play again? [y/n]: ")
                if score <= 0:
                    playAgain = "n"
            elif r2 < r1:
                print(f"Wrong! Next Card was: {r2}")
                score -= 75
                print(f"Your score is: {score}")
                playAgain = input("Play again? [y/n]: ")
                if score <= 0:
                    playAgain = "n"
            elif r1 == r2:
                print(f"It's a tie : {r2}")
                print(f"Your score is: {score}")
                playAgain = input("Play again? [y/n]: ")
                if score <= 0:
                    playAgain = "n"

        # lower
        elif guess.lower() == "l":
            if r2 < r1:
                print(f"Correct! Next Card was: {r2}")
                score += 100
                print(f"Your score is: {score}")
                playAgain = input("Play again? [y/n]: ")
                if score <= 0:
                    playAgain = "n"
            elif r2 > r1:
                print(f"Wrong! Next Card was: {r2}")
                score -= 75
                print(f"Your score is: {score}")
                playAgain = input("Play again? [y/n]: ")
                if score <= 0:
                    playAgain = "n"
            elif r1 == r2:
                print(f"It's a tie : {r2}")
                print(f"Your score is: {score}")
                playAgain = input("Play again? [y/n]: ")
                if score <= 0:
                    playAgain = "n"
        else:
            print()

    print(f"The game is finished!\nYour score is: {score}")


def randomNum():
    return random.randint(1, 13)


if __name__ == "__main__":
    main()
