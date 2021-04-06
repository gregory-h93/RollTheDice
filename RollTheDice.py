##This program will pit you against the computer and whoever comes closest to
##21 without going over wins

import random

random.seed()   #Prepare random number generator

userScore = 0
compScore = 0
userTotal = 0
compTotal = 0
print("Welcome to the game Roll The Dice! Please select which you would like to do: ")
print("1. Play the game")
print("2. Quit the game")
choice = int(input())
while choice < 1 or choice > 2:
    print("Invalid input! Please select which you would like to do: ")
    print("1. Play the game")
    print("2. Quit the game")
    choice = int(input())
if choice == 1:
    while True:    #This simulates a Do Loop
        print("Rolling dice...")
        value1 = int(random.random() * 6) + 1
        value2 = int(random.random() * 6) + 1
        userTotal = value1 + value2
        print("Your Total: " + str(userTotal))
        while True:    #This simulates a Do Loop
            print("Rolling again...")
            value3 = int(random.random() * 6) + 1
            userTotal = userTotal + value3
            print("Your Total: " + str(userTotal))
            if userTotal < 21:
                print("Would you like to roll again? (Y/N)")
                keepRolling = input()
                while keepRolling != "Y" and keepRolling != "y" and keepRolling != "N" and keepRolling != "n":
                    print("Please enter in (Y/N). Would you like to run the program again? (Y/N)")
                    keepRolling = input()
            else:
                keepRolling = "N"
            if not(keepRolling == "Y" or keepRolling == "y"): break   #Exit loop
        value1 = int(random.random() * 6) + 1
        value2 = int(random.random() * 6) + 1
        compTotal = value1 + value2
        while compTotal < 18:
            value3 = int(random.random() * 6) + 1
            compTotal = compTotal + value3
        print("Your score: " + str(userTotal))
        print("Computer score: " + str(compTotal))
        if compTotal > 21 and userTotal > 21:
            print("You both went over 21")
        else:
            if compTotal > 21 and userTotal < 21:
                print("User wins")
                userScore = userScore + 1
            else:
                if compTotal < 21 and userTotal > 21:
                    print("Computer wins")
                    compScore = compScore + 1
                else:
                    if compTotal > userTotal:
                        print("Computer wins")
                        compScore = compScore + 1
                    else:
                        if compTotal < userTotal:
                            print("User wins")
                            userScore = userScore + 1
                        else:
                            if compTotal == userTotal:
                                print("You tied")
                            else:
                                if compTotal == 21 and userTotal > 21:
                                    print("Computer wins")
                                else:
                                    print("User wins")
        print("Computer wins: " + str(compScore))
        print("User wins: " + str(userScore))
        print("Would you like to play again? (Y/N)")
        keepPlaying = input()
        while keepPlaying != "Y" and keepPlaying != "y" and keepPlaying != "N" and keepPlaying != "n":
            print("Please enter in (Y/N). Would you like to run the program again? (Y/N)")
            keepPlaying = input()
        userTotal = 0
        compTotal = 0
        if not(keepPlaying == "Y" or keepPlaying == "y"): break   #Exit loop
print("You have chosen to quit the game!")
