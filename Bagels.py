# Bryan Yang and Geoffrey Jing, CS 111 Final Project Bagels class, 19 November 2021
import random

class Bagels:

    # Constructor randomly initiates self.num, a non-reapeating 3 digit number, and self.guess
    def __init__(self):
        self.guess = "" 
        
        self.num = ""
        while len(self.num) < 3 :
            newNum = random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
            if newNum not in self.num:
                self.num = self.num + newNum
    
    def get_num(self):
        return self.num

    # Checks if guess equals to self.num
    def isCorrect(self, guess):
        if self.num == guess:
            return True
        else:
            return False

    # Returns correct combination of "Bagels", "Picos", and "Fermis" based on the guess.
    def checkNum(self, guess):

        fermiCount = 0
        picoCount = 0
        baglesCount = 0

        returnStr = ""

        for x in range(len(guess)):
            if guess[x] not in self.num:
                baglesCount += 1
                if baglesCount == 3:
                    return "Bagels"
            elif guess[x] in self.num[x]:
                fermiCount += 1
            elif guess[x] in self.num:
                picoCount += 1
            
        for picos in range(picoCount):
            returnStr += "Pico, "
        
        for fermis in range(fermiCount):
            returnStr += "Fermi, "
        
        if len(returnStr) > 8:
            returnStr = returnStr[:-2] + "."
        else:
             returnStr = returnStr[:-2]

        return returnStr



    
