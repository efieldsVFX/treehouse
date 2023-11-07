"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    high_score = 999999
    
    while True:
        print("Welcome to the random number game!")
        
        if high_score!= 999999:
            print("Current high score is: {} attempt(s)".format(high_score))
            
        else:
            print("No high score yet. Play along to set the high score!"  )
        
        solution = random.randint(1, 10)
        attempts = 0
        
        while True:
            try: 
                guess = int(input("Guess a number 1-10.   "))
                attempts += 1
                
                if guess < 1 or guess > 10:
                    print("Your guess is out of bounds. Please pick a number 1-10")
                    continue
                    
                if guess < solution:
                    print("It's higher")
                    
                elif guess > solution:
                    print("It's lower")
                    
                else:
                    print("Got it! The number was {} and it only took you {} attempt(s)! ".format(solution, attempts))
                    
                    if attempts < high_score:
                        high_score = attempts
                        
                        print("Congrats! You set a new High Score! {} attempt(s)".format(high_score))
                        
                    elif attempts > high_score:
                        print("I'm sorry you did not beat the High Score of {} attempt(s). Try again to beat it!  ".format(high_score))
                        
                    elif attempts == high_score:
                        print("You matched the high score of {} attempt(s)! Keep playing to beat it!  ".format(high_score))
                        
                    print("Thanks so much for playing. We hope you play again soon.  ")
                    
                    break
                    
            except ValueError:
                print("Please enter a valid number 1-10 please")
        play_again = input("Would you like to play again? Y/N ")
        if play_again.lower() != "y":
            print("The game is now over. Thanks for playing!  ")
            break
            
        
# Kick off the program by calling the start_game function.
start_game()
