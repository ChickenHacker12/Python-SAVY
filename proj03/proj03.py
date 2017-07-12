import random

# Name: Trey O. & Laila S.
# Date: July 2017

points = 5

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
        #Too high
        print ""
        print "Your guess is too high."
        points = points - 1

    elif guess < number:
        #End game
        if guess == 0:
            loop = False
            print "\nYou exited the game."
            print "Your total points: ", points
        #Too low
        elif guess < number:
            print ""
            print "Your guess is too low."

            points = points - 1

    elif guess == number:
        points = points + 5
        print "\nYou guessed my number! Congratulations!"
        print "You total points: ", points
        print ""
        number = random.randint(1,9)













