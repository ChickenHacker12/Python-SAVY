import random

# Name: Trey & Laila
# Date: July 2017


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

counter = 0
points = 0

print ""
print "Welcome to the Guessing Game!"
enter = raw_input("Press ENTER")
print ""
number = random.randint(1,9)
#guess = raw_input("Guess my number, 1 to 9(enter 0 to end game):")
number = int(number)
#True = guess != number
loop = True
#if guess == number:
   # print "Congratulations, you guessed my number!"




while loop == True:
    guess = raw_input("Guess my number, 1 to 9 (enter 0 to end game): ")
    guess = int(guess)
    if guess > number:
        print ""
        print "Your guess is too high."
        counter = counter + 1
        points = points - 1

    elif guess < number:
        if guess == 0:
            loop = False
            print "\nYou exited the game."
            print "Your total points: ", points
        elif guess < number:
            print ""
            print "Your guess is too low."
            counter = counter + 1
            points = points - 1

    elif guess == number:
        points = points + 5
        print "\nYou guessed my number! Congratulations!"
        print "You total points: ", points
        print ""
        number = random.randint(1,9)

        #loop = False












