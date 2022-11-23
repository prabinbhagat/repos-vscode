# Defining functions
# Builtin functions are great, but we can only get so far with them before we need to start defining our own functions. 
# Below is a simple example.

def Least_Difference(a,b,c):
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1,diff2,diff3)

x= Least_Difference(50,60,70)
print(x)

# This creates a function called least_difference, which takes three arguments, a, b, and c.

# Functions start with a header introduced by the def keyword. The indented block of code 
# following the : is run when the function is called.

# return is another keyword uniquely associated with functions. When Python encounters a return statement, 
# it exits the function immediately, and passes the value on the right hand side to the calling context.

print(
    Least_Difference(1, 10, 100),
    Least_Difference(1, 10, 10),
    Least_Difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)

help(Least_Difference)

# Python isn't smart enough to read my code and turn it into a nice English description.
#  However, when I write a function, I can provide a description in what's called the docstring.

#<------------------------------------DocString---------------------------------------

def Least_Difference(a,b,c):
    '''
    Return the smallest difference between any two numbers
    among a, b and c.
    >>> least_difference(1, 5, -5)
    4
    '''
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1,diff2,diff3)

x= Least_Difference(50,60,70)
print(x)

help(Least_Difference)

# The docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function.
# When we call help() on a function, it shows the docstring.

# Aside: The last two lines of the docstring are an example function call and result. 
# (The >>> is a reference to the command prompt used in Python interactive shells.) 
# Python doesn't run the example call - it's just there for the benefit of the reader.

#<------------------------------------DocString---------------------------------------

# Functions that don't return
# What would happen if we didn't include the return keyword in our function?


def Least_Difference(a,b,c):
    '''
    Return the smallest difference between any two numbers
    among a, b and c.
    >>> least_difference(1, 5, -5)
    4
    '''
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    #return min(diff1,diff2,diff3)

x= Least_Difference(50,60,70)
print(x)            # Output will be None

# Python allows us to define such functions. The result of calling them is the special value None. 
# (This is similar to the concept of "null" in other languages.)

# Without a return statement, least_difference is completely pointless, but a function with side effects may do something 
# useful without returning anything. We've already seen two examples of this: print() and help() don't return anything. 
# We only call them for their side effects (putting some text on the screen). Other examples of useful side effects 
# include writing to a file, or modifying an input.

mystery = print()
print(mystery)      # Output will be None

# Default arguments:
# When we called help(print), we saw that the print function has several optional arguments. For example, we can specify a 
# value for sep to put some special string in between our printed arguments:

print(1, 2, 3, 4, sep='<')
# But if we don't specify a value, sep is treated as having a default value of ' ' (a single space).
print(1, 2, 3, 4, )

# Optional Arguments:
# Adding optional arguments with default values to the functions we define turns out to be pretty easy:

def Greet(whom = "Prabin"):
    print("Hello!",whom)

Greet()
Greet(whom="Kaggle") # (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
Greet('World')

# Functions Applied to Functions:
# Here's something that's powerful, though it can feel very abstract at first. You can supply functions as arguments to other
#  functions. Some example may make this clearer:

def MulByFive(x):
    return 5 * x

def Call(fn,arg):
    """Call fn on arg"""
    return fn(arg)

def SquredCall(fn,arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(Call(MulByFive,1), SquredCall(MulByFive,1),sep='\n')

# Functions that operate on other functions are called "higher-order functions."

# By default, max returns the largest of its arguments. But if we pass in a function using the optional key 
# argument, it returns the argument x that maximizes key(x) (aka the 'argmax').

def Mod(x):
    return x%5

print("The biggest num is ",max(100,51,19))
print("The hig remainder is ",max(100,51,9, key=Mod))  # this will perform the mod on each max arg and return the max num.

#<---------------------------------Round----------------------------------
help(round)
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return(round(num,2))

print(round_to_two_places(3.461))

# The help for round says that ndigits (the second argument) may be negative. What do you think will happen when it is? 
print("Negative rounding ndigit ",round(98762155.230,-1))
# what i can infer is that ndigits=-1 rounds to the nearest 10, ndigits=-2 rounds to the nearest 100 and so on. 
# Where might this be useful?

# Suppose we're dealing with large numbers:

# The area of Finland is 338,424 km²
# The area of Greenland is 2,166,086 km²

# We probably don't care whether it's really 338,424, or 338,425, or 338,177. All those digits of accuracy are just distracting. We can chop them off by calling round() with ndigits=-3:

# The area of Finland is 338,000 km²
# The area of Greenland is 2,166,000 km²
# </-----------------------------Round---------------------------

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % 3

# What if friends increase more than 3 ???? if not increase lets keep defaut value to 3

def to_smash(total_candies,friends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % friends

print(to_smash(91))     # here friends will take by default 3 as it is optional parameter and initialized to 3
print(to_smash(91),8)

