# Name: Trey Owen
# Date: July 2017

# 01: A Simple Program
# This program asks the user for his/her name and age.

print " "
print "Welcome to Age Calculator! Last updated July 2017. \nBy Trey Owen"
print " "
t = raw_input("You need to answer a few questions in order to continue.\nPress ENTER")
c = 0
# Name
print " "
n = raw_input("Please tell me your first name: ")

# Get age with var a
a = int(raw_input("Please tell me your age: "))

# Have you had a birthday yet this year?
#z = raw_input("Have you had a birthday yet this year (yes or no):")
#if z == "yes":
#c = int(a) + 1
#elif z == "no":
#    c = int(a)
#else:



# Get new name
my_str1 = str(n)
my_str2 = my_str1[0]
my_str3 = my_str2.upper()
my_str4 = my_str1[1]
my_str5 = my_str4 + my_str1[2]
my_str6 = my_str5 + my_str1[3]
my_str7 = my_str3 + my_str6
m = my_str7
print " "
print "Welcome, " + my_str7 + "!"

# Tell the age
print " "
print m + " will be 100 years old in the year:"
print (100 - int(a)) + 2017

print m + " was born around the year:"
print 2017 - int(a)

# a = age before b-day
# n = name before m
# m = name after m
