# Name: Zeke Cook and Trey Owen
# Date: July 2017


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
a = choose_word(wordlist)

# your code begins here!
z = "_ "
already_guessed = []
guesses = 10
word = []
spaces = []
for letter in a:
    word.append(letter)

print "\nWelcome to HangmanPro! By Zeke Cook & Trey Owen."
eeee = raw_input("Press ENTER")
print ""


loop_control = True

while loop_control == True:

    word.append(random)
    # Print spaces
    spaces = len(word)
    spaces2 = spaces*z
    space_list = [spaces2]
    print space_list
    print word
    # Question & info
    print "\nNumber of guesses left: ", guesses
    print "Letters guessed: ", already_guessed

    user_guess = raw_input("What letter would you like to guess: ")
    if user_guess in word:
        print "\nThat is correct! There is a(n)", user_guess, "."
    elif guesses == 1:
        loop_control = False
        print "\nSorry, you ran out of guesses. Please try again."
    else:
        guesses = guesses - 1
        print "\nSorry, inncorrect."