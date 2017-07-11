import random

# Name: Trey Owen
# Date: July 2017

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21

# Introduction
print ""
a = raw_input("Welcome to the Number Game!\nPress ENTER")
a = raw_input("The goal is to chose random numbers, and when you are done, guess the sum of them.\nPress ENTER")
print " "
name = raw_input("Please enter a username: ")
print " "
print "Welcome, " + name + "!"
print ""

# Test loop
loop_control = True
total = 0


while loop_control == True:
    num = int(raw_input("Enter a number (enter 0 to end game): "))
    if num > 0:
        num = raw_input("Enter a number (enter 0 to end game): ")
    else:

        if num < 1:
            loop_control = False
            print ""
            print "Game over."
            guess = raw_input("What is your guess: ")
            total = num + 
            print name, ", the correct answer is", total, "."
