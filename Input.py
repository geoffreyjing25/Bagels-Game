# Geoffrey Jing, Project Input class, 19 November 2021
import Bagels

class Input:

    # Constructor initiates self.guess which is inputed by the user.
    def __init__(self):
        self.guess = input("Enter Guess: ")

    # Checks if the 3 digit number is non repeating. 
    def isUnique(self, guess):
        # self.count += 1
        if guess[0] != guess[1] and guess[1] != guess[2] and guess[0] != guess[2]:
            return True
        else:
            return False

    # Everytime this function is called it has the user input a new guess and assigns it to self.guess.
    def getGuess(self):
        self.guess = input("Enter another guess:")


    


