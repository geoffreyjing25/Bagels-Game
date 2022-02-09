# Bryan Yang and Geoffrey Jing, CS 111 Final Project Guesser class, 19 November 2021
import random
import Bagels

class Guesser:

    # Constructor initiates an instance of the Bagels class called self.guesserGame, and initiates a self.num variable and 
    # sets it equal to output of the createNum method. It also initiates a nested list of numbers for the computer
    # to create a 3 digit number.  
    def __init__(self):
        self.guesserGame = Bagels.Bagels()
        self.num = ""
        self.guesslist = [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        self.count = 0
        self.num = self.createNum()

    # Randomly creates a 3 digit number based on what is in self.guesslist.
    def createNum(self):
        firstNum = random.choice(self.guesslist[0])
        secondNum = random.choice(self.guesslist[1])
        while firstNum == secondNum:
            secondNum = random.choice(self.guesslist[1])
        thirdNum = random.choice(self.guesslist[2])
        while firstNum == thirdNum or secondNum == thirdNum:
            thirdNum = random.choice(self.guesslist[2])
        self.num = firstNum + secondNum + thirdNum
        self.count += 1
        
    def getNum(self):
        return self.num

    def getCount(self):
        return self.count

    # if the output is bagels, this method will remove the element that the computer guessed for bagels so that the computer
    # learns the number that it guesses is not in the number being guessed. 
    # Basiclly, if the output is Bagels, it won't guess any number in that guess in any future guesses. 
    def calcNum(self, output):
        if "Bagels" in output:
            print("test1")
            self.guesslist[0].pop(self.guesslist[0].index(self.num[0]))
            self.guesslist[1].pop(self.guesslist[1].index(self.num[1]))
            self.guesslist[2].pop(self.guesslist[2].index(self.num[2]))
            self.createNum()

    
    
