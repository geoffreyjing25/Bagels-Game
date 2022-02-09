# Bryan Yang and Geoffrey Jing, CS 111 Final Project main file, 19 November 2021
import Bagels
import Input
import Guesser


def main():

    baglesGame = Bagels.Bagels()
    # print(baglesGame.num)
    count = 1

    print("")
    print("***************************************************************************************************************".center(150))
    print("")
    print(" Hello, this is the Bagels Game. The rules are as follows: \n".center(150))
    print(" The computer will randomly generate a non-repeating three digit number. ".center(150))
    print(" Your goal is to try and guess the number. Based on what you guess, the computer will ouput certain phrases. ".center(150))
    print(" 'Bagels' means none of the numbers in your guess are present in the correct number. ".center(150))
    print(" A 'Pico' means that a number in your guess is present in the correct number, but it is in the wrong position. ".center(150))
    print(" A 'Fermi' means that a number in your guess is present and in the correct position. ".center(150))
    print(" You can input only numbers to guess, but also be careful to only input three digit numbers that do not contain repeating digits. ".center(150))
    print(" Good game and good luck.".center(150))
    print("")
    print("***************************************************************************************************************".center(150))
    print("")


    # Code below allows user to choose gamemode.
    choice = input("Do you want to watch a computer play? Press 1 to see the computer try and guess, Press 2 to play by yourself: ")

    # Starts gamemode where computer guesses.
    if choice == str(1):
        computer = Guesser.Guesser()
        computer.createNum()
        print(computer.num)
        while computer.num != baglesGame.num:
            computer.createNum()
            computerGuess = computer.getNum()
            computer.calcNum(baglesGame.checkNum(computerGuess))
            print(baglesGame.checkNum(computerGuess))
            print(computerGuess)

        print("")
        print("*******************************************")
        print("The computer took " + str(computer.getCount()) + " tries.")
        print("*******************************************")
        print("")

    # Starts gamemode where user guesses.
    elif choice == str(2):

        inputGame = Input.Input()

        while not baglesGame.isCorrect(inputGame.guess):
            # Checks to make sure user's guess is within the rules.
            if not inputGame.guess.isdecimal():
                print("Your guess must only contain numbers. Please try again.")
                inputGame.getGuess()
            elif len(inputGame.guess) != 3:
                print("Your guess must be 3 digits long. Please try again.")
                inputGame.getGuess()
            elif not inputGame.isUnique(inputGame.guess):
                print("Make sure there are no repeating numbers. Please try again.")
                inputGame.getGuess()
            else:
                print(baglesGame.checkNum(inputGame.guess))
                print("Please try again.")
                inputGame.getGuess()
                count += 1
                
        print("")    
        print("*********************************************************")    
        print("Congratulations, you guessed the correct number!")
        print("You took " + str(count) + " tries!")
        print("*********************************************************")    
        print("")

if __name__=="__main__":
    main()