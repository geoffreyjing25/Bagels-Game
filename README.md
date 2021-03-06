# Bagels-Game
Code of working Bagels implementation programmed from scratch with Python

My project is a game. The basics of how the Bagels game works are described below:
There are two players, player 1 and player 2.
Player 1 will think of a three digit non-repeating number, and the player 2 will attempt to guess it by guessing 
a three digit non-repeating number of its own. If none of the three digits in player 2's guess are in 
player 1's number then player 1 will say "Bagels". If there is one digit that is the same as
player 1's number, player 1 will say "Pico", and if the number is in the same spot as player 1's number,
player 1 will say Fermi, for each individual number in the guess that matches player 1's number. 
Based on these hints, Player 2 will eventually be able to guess the number. This project works in a similar
fashion, but instead of two players, there will be a computer generate a random three digit non-repeating 
number, and the user can input numbers to try and guess the number. The user is only allowed to input
3 digit numbers that do not repeat and will be prompted to re-guess if it is not. It will keep track of how many times the 
user guesses so they can see how many tries it took them. I also implemented some computer intelligence 
in the game by creating a Guesser class that is basically a computer continually generating three digit
non-repeating numbers until it guesses the number. As the computer guesses, it will note when the output
is "Bagels" and will no longer guess the numbers from that guess for any future guesses. 
There are no bugs to the program, but it should be noted that each run of the code will produce
one game, and to play again the user will need to run the program again. This is also the case if the user 
wants to watch the computer guess the number, each time the code is run is one completed game by the computer. 
