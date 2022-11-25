# Booleans and Conditionals
# Using booleans for branching logic

# Booleans
# Python has a type of variable called bool. It has two possible values: True and False.

X = True
print(X)
print(type(X))

# Rather than putting True or False directly in our code, we usually get boolean values from boolean operators. 
# These are operators that answer yes/no questions. 

# Comparison Operations
# Operation	Description		         Operation	Description
# a == b	a equal to b		      a != b	a not equal to b
# a < b	    a less than b		      a > b 	a greater than b
# a <= b	a less or equal to b      a >= b	a greater than or equal to b

def Can_Run4_president_Election(age):
    return age>=35

print("Can a 19-year-old run for president?", Can_Run4_president_Election(19))
print("Can a 45-year-old run for president?", Can_Run4_president_Election(45))

# Comparisons frequently work like you'd hope

3.0 == 3
True
# But sometimes they can be tricky
'3' == 3
False

# Comparison operators can be combined with the arithmetic operators we've already seen to express a virtually limitless 
# range of mathematical tests. For example, we can check if a number is odd by checking that the modulus with 2 returns 1:

def CheckOdd(num):
    return (num%2)==1

print("Is the number 3 a odd number:",CheckOdd(3))
print("Is the number 4 a odd number:",CheckOdd(4))

# Remember to use == instead of = when making comparisons. If you write n == 2 you are asking about the value of n. 
# When you write n = 2 you are changing the value of n.

# Combining Boolean Values
# You can combine boolean values using the standard concepts of "and", "or", and "not". In fact, the words 
# to do this are: and, or, and not.

# With these, we can make our can_run_for_president function more accurate.

def can_run4Presiden(age,isNaturalBornCitizen):
    return (age>35) and isNaturalBornCitizen

print(can_run4Presiden(19, True))
print(can_run4Presiden(55, False))
print(can_run4Presiden(55, True))

# Quick, can you guess the value of this expression?
print("True or True and False=",True or True and False)

# Order of operations.
# For example, and is evaluated before or. That's why the first expression above is True. If we evaluated it from left to right,
#  we would have calculated True or True first (which is True), and then taken the and of that result with False, giving a 
#  final value of False.

# You could try to memorize the order of precedence, but a safer bet is to just use liberal parentheses. Not only does this 
# help prevent bugs, it makes your intentions clearer to anyone who reads your code.


# Conditionals
# Booleans are most useful when combined with conditional statements, using the keywords if, elif, and else.

# Conditional statements, often referred to as if-then statements, let you control what pieces of code are
#  run based on the value of some Boolean condition. Here's an example:

def Inspect(x):
    if (x == 0):
        print(x, "is zero")
    elif(x>0):
        print(x, "is +ve")
    elif(x<0):
        print(x,"is -ve")
    else:
        print(x,"i dont think its a number")

Inspect(-8)

# Note especially the use of colons (:) and whitespace to denote separate blocks of code. This is similar to what happens when we
#  define a function - the function header ends with :, and the following line is indented with 4 spaces. All subsequent 
#  indented lines belong to the body of the function, until we encounter an unindented line, ending the function definition.

def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)

# Boolean conversion
# We've seen int(), which turns things into ints, and float(), which turns things into floats, so you might not be surprised to 
# hear that Python has a bool() function which turns things into bools.

print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"

# We can use non-boolean objects in if conditions and other places where a boolean would be expected. Python will implicitly
#  treat them as their corresponding boolean value:

if 0:
    print(0)
elif "spam":
    print("spam")       # this output spam as if statement looks for trueness of the condition 

#----------------------------------------------------------------------------------
# Many programming languages have sign available as a built-in function. Python doesn't, but we can define our own!

# Define a function called sign which takes a numerical argument and returns -1 if it's negative, 
# 1 if it's positive, and 0 if it's 0.

def sign(x):
    if x<0:
        return -1
    elif x>0:
        return 1
    elif x ==0:
        return 0

# using a conditional expression:

totalCandy = 9
print("candy" if totalCandy ==1 else "Candies")

totalCandy = 1
print("candy" if totalCandy ==1 else "Candies")

# The function is_negative below is implemented correctly - it returns True if the given number is negative and False otherwise.

# However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this 
# function by 75% while keeping the same behaviour.

# def is_negative(number):
#     if number < 0:
#         return True
#     else:
#         return False

# Above code can be rewritten as

def is_negative(number):
    return number < 0

print(is_negative(89))

