from card import Card


class Director:
    """This Class will manage the flow of the game
    and the update of the score in screen
    """

    def __init__(self):
        """ This is the constructor of class
        declaring the attributes to use in the game
        """
        self.score = 300
        self.is_playing = True
        self.user_guess = ""
        self.card_1 = 0
        self.card_2 = 0
        self.my_card_1 = Card()
        self.my_card_2 = Card()

    def start_game(self):
        """This Method will manage the flow of the 
        game
        """
        while self.is_playing:
            self.update_screen()
            self.update_score()
            self.play_again()

    def update_score(self):
        """This Method will update the score for
        the player and the total score
        """
        if self.user_guess.lower() == "h":
            # higher
            if self.card_2 > self.card_1:
                self.score += 100
                print(f"Correct! Your score is: {self.score}")
            elif self.card_2 < self.card_1:
                self.score -= 75
                print(f"Wrong! Your score is: {self.score}")
                if self.score <= 0:
                    print("Game Over")
                    print(f"Your score is {self.score}")
                    self.is_playing = False
            elif self.card_2 == self.card_1:
                print(f"It is a tie!")
        elif self.user_guess.lower() == "l":
            # lower
            if self.card_2 < self.card_1:
                self.score += 100
                print(f"Correct! Your score is {self.score}")
            elif self.card_2 > self.card_1:
                self.score -= 75
                print(f"Wrong! Your score is {self.score}")
                if self.score <= 0:
                    print("Game Over")
                    print(f"Your score is {self.score}")
                    self.is_playing = False
            elif self.card_2 == self.card_1:
                print(f"It is a tie!")
        else:
            print("Invalid input! please type [h/l]")

    def update_screen(self):
        """This Method will be printing on screen the
        output for the game and the update during the game.
        """
        self.card_1 = self.my_card_1.roll_card()
        self.card_2 = self.my_card_2.roll_card()
        print(f"\nThe first card is: {self.card_1}")
        self.user_guess = input("Higher or Lower? [h/l] ")
        print(f"The next card is: {self.card_2}")

    def play_again(self):
        """ Get User input for continue game
        Args:
            Director: Class
        Returns:
            nothing
        """
        self.next_game = input("\nWould you like to play again? [y/n] ")
        if self.next_game.lower() == 'y':
            self.is_playing
        else:
            self.is_playing = False
            print()
            print(
                f"Nice game, Thank you for playing!\nYour total score is: {self.score}")
