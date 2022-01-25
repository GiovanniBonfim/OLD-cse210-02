# import card

# class Director:
#     """This Class will manage the flow of the game
#     and the update of the score in screen
#     """
#     def __init__(self) -> None:
#         """ This is the constructor of class
#         declaring the attributes to use in the game
#         """
#         self.total_score = 0
#         self.score = 300
#         self.is_playing = True
#         self.card = 0

#     def start_game(self):
#         """This Method will manage the flow of the
#         game
#         """
#         while self.is_playing:
#             self.update_point()
#             self.update_screen()


#     def update_point(self):
#         """This Method will update the score for
#         the player and the total score
#         """
#         pass

#     def update_screen():
#         """This Method will be printing on screen the
#         output for the game and the update during the game.
#         """
#         pass

#     pass

# # The n-player b-starts the game with 300 points.
# # Individual n-cards are represented as a number from 1 to 13.
# # The current n-card is displayed.
# # The player guesses if the next one will be higher or lower.
# # The the next card is displayed.
# # The player earns 100 points if they guessed correctly.
# # The player loses 75 points if they guessed incorrectly.
# # If a player reaches 0 points the game is over.
# # If a player has more than 0 points they decide if they want to keep playing.
# # If a player decides not to play again the game is over.

from card import Card
import random


class Director:
    """This Class will manage the flow of the game
    and the update of the score in screen
    """

    def __init__(self):
        """ This is the constructor of class
        declaring the attributes to use in the game
        """
        self.total_score = 0
        self.score = 300
        self.is_playing = True
        self.card_1 = 0
        self.card_2 = 0
        self.user_guess = ""

    def start_game(self):
        """This Method will manage the flow of the 
        game
        """
        while self.is_playing:

            self.update_screen()
            self.update_score()
            self.play_again()

    def update_screen(self):
        """This Method will be printing on screen the
        output for the game and the update during the game.
        """

        self.card_1 = random.randint(1, 13)
        self.card_2 = random.randint(1, 13)
        print(f"The first card is: {self.card_1}")
        self.user_guess = input(" Higher or Lower? [h/l] ")
        print(f"The next card is: {self.card_2}")

    def update_score(self):
        """This Method will update the score for
        the player and the total score
        """

        if self.user_guess.lower() == "h":
            # higher
            if self.card_1 <= self.card_2:
                self.score += 100
                print(f"Correct! Your score is {self.score}")
            elif self.card_1 > self.card_2:
                self.score -= 75
                print(f"Wrong! Your score is {self.score}")
                if self.score <= 0:
                    print("Game Over")
                    print(f"Your score is {self.score}")
                    self.is_playing = False
        elif self.user_guess.lower() == "l":
            # lower
            if self.card_1 >= self.card_2:
                self.score += 100
                print(f"Correct! Your score is {self.score}")
            elif self.card_1 > self.card_2:
                self.score -= 75
                print(f"Wrong! Your score is {self.score}")
                if self.score <= 0:
                    print("Game Over")
                    print(f"Your score is {self.score}")
                    self.is_playing = False

    def play_again(self):
        """ Get User input for continue game
        Args:
            Director: Class
        Returns:
            nothing
        """
        # self.next_game = input("Would you like to play again? [y/n] ")
        # self.is_playing = (self.next_game.lower() == 'y')

        self.ask_user = input("Would you like to play again? [y/n] ")
        while self.ask_user.lower() == "y":
            if self.ask_user == "y":
                return
            elif self.ask_user == "n":
                print("Game Over!")
