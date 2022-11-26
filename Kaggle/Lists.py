# Lists
# Lists and the things you can do with them. Includes indexing, slicing and mutating

# Lists
# Lists in Python represent ordered sequences of values. Here is an example of how to create them:

primes = [2, 3, 5, 7]

# We can put other types of things in lists:
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# We can even make a list of lists:

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

# A list can contain a mix of different types of variables:
my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

#<---------------------------- Indexing----------------------------------------->
# You can access individual list elements with square brackets.

# Which planet is closest to the sun? Python uses zero-based indexing, so the first element has index 0.

nearplanet =planets[0]
print(nearplanet)

# What's the next closest planet?
nearplanet = planets[1]
print(nearplanet)

# Which planet is furthest from the sun?

nearplanet = planets[len(planets)-1]
print(nearplanet)

# Elements at the end of the list can be accessed with negative numbers, starting from -1:
nearplanet = planets[-1]
print(nearplanet)
# i.e when we want to access element from end we can use -1,-2,-3......

#</---------------------------- Indexing----------------------------------------->

#<-------------------------------Slicing------------------------------------------>
# What are the first three planets? We can answer this question using slicing:

nearplanet = planets[0:3]
print("First Three:",nearplanet)
# i.e planets[0:3] is our way of asking for the elements of planets starting from index 0 and continuing up to but not 
# including index 3.

# The starting and ending indices are both optional. If I leave out the start index, it's assumed to be 0. So I could 
# rewrite the expression above as:
nearplanet = planets[:3]
print("First Three:",nearplanet)

# If I leave out the end index, it's assumed to be the length of the list.
nearplanet = planets[4:]
print("First Three:",nearplanet)
# i.e. the expression above means "give me all the planets from index 3 onward".


# We can also use negative indices when slicing:

# All the planets except the first and last
x = planets[1:-1]
print(x)

# The last 3 planets
x = planets[-3:]
print(x)

# Changing lists
# Lists are "mutable", meaning they can be modified "in place".

# One way to modify a list is to assign to an index or slice expression.

# For example, let's say we want to rename Mars:

planets[3] = "Malacandra"
print(planets)

# Hm, that's quite a mouthful. Let's compensate by shortening the names of the first 3 planets.
planets[:3] = ['Mer','Ven','Ear']
print(planets)

# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
print(planets)

#</-------------------------------Slicing------------------------------------------>

# List functions
# Python has several useful functions for working with lists.

# len gives the length of a list:

# How many planets are there?
x = len(planets)
print(x)

#sorted returns a sorted version of a list:
# The planets sorted in alphabetical order
x= sorted(planets)
print(x)
