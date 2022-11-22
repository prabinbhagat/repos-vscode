# How tall am I, in meters, when wearing my hat?

hat_height_cm = 25
my_height_cm = 190

heightwithCap_cm  = my_height_cm+hat_height_cm
heightInMeter = heightwithCap_cm/100


print("Your are {}cm tall and  {} in metre".format(heightwithCap_cm,heightInMeter))

# Builtin functions for working with numbers
# min and max return the minimum and maximum of their arguments, respectively...

print(min(5,3,1.2,5,8.2,1/2))
print(max(54,589,32,54,7896,321,45,3.21,.3255,.35,123.20))

#abs returns the absolute value of an argument: means postive value

print(abs(-45.60))
print(abs(-86))

#In addition to being the names of Python's two main numerical types, 
#int and float can also be called as functions which convert their arguments to the corresponding type:
print(float(8/9))
# They can even be called on strings!
print(int("56")+50)

# --------------------------------
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter/2

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi*radius**2
#-----------------------------------

########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.
c = a
d = b
b = c
a = d

######################################################################

# Check your answer
#The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:

tmp = a
a = b
b = tmp
#If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:

a, b = b, a
#We'll demystify this bit of Python magic later when we talk about tuples.

#Add parentheses to the following expression so that it evaluates to 1.
5 - 3 // 2
x = (5-3)//2
print(x)

#Add parentheses to the following expression so that it evaluates to 0.
8 - 3 * 2 - 1 + 1
x = (8-3)*(2-(1+1))
print(x)

# # 4. 
# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves.
# For the sake of their friendship, any candies left over will be smashed. For example, if they collectively
# bring home 91 candies, they'll take 30 each and smash 1.

# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = -1
to_smash = (alice_candies+bob_candies+carol_candies)%3
print(to_smash)

#<--------------------------------------help()-------------------------------------->
# Help function
help(round)
# help() displays two things:
# the header of that function round(number, ndigits=None). In this case, this tells us that round() takes an argument we can describe as number. Additionally, we can optionally give a separate argument which could be described as ndigits.
# A brief English description of what the function does.

# Common pitfall: when you're looking up a function, remember to pass in the name of the function itself, and not the result of calling that function.
# What happens if we invoke help on a call to the function round()? Unhide the output of the cell below to see.
help(round(-2.01))

# Python evaluates an expression like this from the inside out. First it calculates the value of round(-2.01), 
# then it provides help on the output of that expression.

# (And it turns out to have a lot to say about integers! After we talk later about objects, methods, 
# and attributes in Python, the help output above will make more sense.)

# round is a very simple function with a short docstring. help shines even more when dealing with more complex, 
# configurable functions like print. Don't worry if the following output looks inscrutable... for now, just 
# see if you can pick anything new out from this help.

help(print)
# If you were looking for it, you might learn that print can take an argument called sep, and that this
# describes what we put between all the other arguments when we print them.
#</--------------------------------------help()--------------------------------------