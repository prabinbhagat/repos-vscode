from math import ceil, floor
import math

## Tut 3 for control flows in Python My Notes and Codes

''''''
#Adding two numbers
a = 5
b = 6
print("The sum of {0} and {1} is".format(a,b) ,a+b)


# if statement

val = input("enter a Num ")
chechval = int(val)
if (chechval % 2==0):
    print("even num")
else:
    print("odd")
    
# Age form nested if2

age = int(input("Please input your age: "))
if(age<18):
    print("You are minor")
    if(age<17):        
        print("You are in school")
    else:   
        print("you are in collage")

elif(age>=18 and age <= 35):
    print("Mid age")
elif(age>= 45 and age <=50):
    print("mid mid age")
else:
    print("Senior citizen")


# Loop statements :
# for loop, while loop

# finding sum of all numbers

lst = [1,2,3,4,5,6,7,8,9,10]
sumEven = 0
sumOdd = 0
for i in lst:
    print(i)
    if(i % 2 == 0):
        sumEven += i
    else:
        sumOdd += i

print("The sum of even no is {0} and sum of odd no is {1}".format(sumEven,sumOdd))
print("Sum of all number in lst ",sumEven+sumOdd)

#print 11 to 20 except 17 and 20

i = 11
while(i>=11 and i<=20 ):
    if(i == 17):
        i+=1
        continue    
    if(i==20):
        break
    print(i)
    i+=1



## TUT 4 Operators, logical,equality,comparasion,arithmetic,Bitwise

#Logical Operator AND-OR-NOT
True
print(type(True))
a = bool(1) #type casting
print(a)

x = True and False
print(x)

x= True or False
print(x)

x = not True
print (x)
        
#   Equality Operators:
#     Following operations are present in python for equlity check operation-

#     Operators	Meaning:

#     is	    a is b returns true if variable/identifiers a and b points to the same object
#     is not	a is not b returns true if variable/identifiers a and b points to the different object
#     ==	    a == b returns true if variable/identifiers a and b has same value
#     !=	    a != b returns true if variable/identifiers a and b has different value


c = "Prabin"
b = "rabin"
if (c == b):
    print(c==b)
else:
    print(c==b)
    
age = int(input("Enter the age: "))

if (age == 18):
    print("You are eligible to vote..")



name ="Prabin Bhagat"
print(id(name))
myName = "Prabin Bhagat"
print(id(myName))

a = name is myName
print(a)                            # Both pointing to same memory Location will return true

myList = ['a','b','c','d']
myAnotherList = ['a','b','c','d']

print(id(myList))
print(id(myAnotherList))
print(myList is myAnotherList)      # Collection are created in diffrent way though element are same they point to diff mem locatn
print(myList == myAnotherList)      # Will return true as '==' compares value, whreas "is" checks same mem location

print ("5 not equals to 4? ", (5 != 4))
print (myList is not myAnotherList) 

## comparison operators
# Operation 	Meaning
# <	            less than
# <=	        less than or equal to
# >	            greater than
# >=        	greater than or equal to

marks = float(input("Enter your marks for the subject: "))

if(marks<=35):
    print("You have failed")
else:
    print("You Have Passed.")
    if(marks >= 65 and marks < 70):
        print("Second division")
    elif(marks >= 70):
        print("First Division")

## Arithmetic Operators
# Operation	Meaning
# +	        addition
# -	        subtraction
# *	        multiplication
# /	        true division
# //	    integer division
# %	        the modulo operator

print("22 + 7 = ",22+7)
print("22 - 7 = ",22-7)
print("22 * 7 = ",22*7)
print("22 / 7 = ",22/7)
print("22 // 7 = ",22//7)
print("22 % 7 = ",22%7)

### Tut 5 Pythom Math/Number Methods
# Data scientist/data analytic like log normal distribution, finding exponent etc uses math/number methods

#1. abs()
#   abs(x) will return the absolute value of a number x which we pass in argument. The number x can be integer, float, complex,..

# from math import ceil, floor
# import math

print("Absolute value of 34.65: ",abs(34.65))
print("Absolute value of 34.30: ",abs(34.30))
print("Absolute value of -34.50: ",abs(-34.30))

#2. ceil()
#   ceil(x) will return the ceiling value of a number x which we pass in argument.The ceiling value of a number x will be the smallest integer not less than x
#   Note :- This function will not be accessible directly using ceil() method. Math module will be required to access this method

a = ceil(-3.14)
b = ceil(3.14)
print("The ceiling value of -3.14 is :" ,a)
print("The ceiling value of 3.14 is :" ,b)

#3. floor()
a = floor(3.14)
b = floor(3.90)
c = floor(-3.14)
print("The floor value of 3.14: " ,a)
print("The floor value of 3.90: " ,b)
print("The floor value of -3.14: " ,c)

#4. exp()
#   The math.exp() method returns E raised to the power of x (Ex).
#   'E' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it.

a = math.exp(2)
print("The exponential of 2 is ",a)

#5. fabs() method returns the absolute value of a number, as a float.
# Absolute denotes a non-negative number. This removes the negative sign of the value if it has any.
# Unlike Python abs(), this method always converts the value to a float value.

a = math.fabs(-3)
print("The fabs of -3 is ",a)

# 6. log() method returns the natural logarithm of a number, or the logarithm of number to base.
#    Syntax: math.log(x, base)
#            x: 	Required. Specifies the value to calculate the logarithm for. If the value is 0 or a negative number, it returns a ValueError. 
#                   If the value is not a number, it returns a TypeError
#            base:	Optional. The logarithmic base to use. Default is 'e'

# Return the natural logarithm of different numbers
print(math.log(2.8912))
print(math.log(2))
print(math.log(1))

#7. max() function returns the item with the highest value, or the item with the highest value in an iterable.
# If the values are strings, an alphabetically comparison is done. Syntax max(n1, n2, n3, ...) or max(iterable) ; iterable:An iterable, with one or more items to compare

x = max(9,5,8,7,2,3,5,8,9,6)
print("The max of is" ,x)

x = max("A","AA","AAA","B","BB","BBB","RAM","S")
print("The max of is" ,x)

#8. POW()
# Power of
a = pow(2,8)
b = pow(-2,-8)
x = pow(4, 3, 5)   # with modulus If a third parameter is present, it returns x to the power of y, modulus z.
print("Five to the power of 2 is ",a ,b)
print("x")

#9. sqrt()
#a = math.sqrt(-9)
b = math.sqrt(121)
print(b)

## Trignometric Functions

a = math.sin(45)
a = math.cos(90)
a= math.tan(45)
print(a)

## Hypotenaos function 

a = math.hypot(2,2)
print(a)

#10 modf()
# This method returns the fractional and integer parts of x in a two-item tuple. 
# Both the parts have the same sign as x. The integer part is returned as a float.
a= math.modf(5)
print("modf ",a)
print ("math.modf(100.12) : ", math.modf(100.12))
print ("math.modf(100.72) : ", math.modf(100.72))
print ("math.modf(119) : ", math.modf(119))
print ("math.modf(math.pi) : ", math.modf(math.pi))


########## FOR LOOPS ###########

#Print each concept in oops list list:
oops = ["abstraction", "polymorphism", "inheritence","Encapsulation"]
for x in oops:
  print(x)

#Looping Through a String
#Even strings are iterable objects, they contain a sequence of characters:

#Loop through the letters in the word "encapsulation":
for x in "encapsulation":
  print(x)

# The range() Function
# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a 
# parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
  print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by
# adding a third parameter: range(2, 30, 3):

################# FOR LOOP ENDS ##################


#Program to check prime numbers in a range

primeNumberCount = int(input("How many prime numbers would you like to see? "))

for i in range(2,primeNumberCount):
    if(i == 1 or i == 0):
        continue
    for j in range(2,primeNumberCount):
        if(i%j == 0):
            if(i != j):
                break
            else:
                print(i)

#Program to check max of 4 numbers

lstUser = []
for i in range (4): lstUser.append(int(input("Please input number:")))
    # x =int(input("Please input number:"))
    # lstUser.append(x)    
print("The max number is :",max(lstUser))


## Tut 6 Data Structures List,Dictionary,Sets etc.


# ******************************** 1.Lists ******************************


# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. 
# Each element or value that is inside of a list is called an item. Just as strings are defined as characters
# between quotes, lists are defined by having values between square brackets [ ]

# mutable vs immutable eg:

fName = "Prabin"
print(fName)

fName = "Bhagat"
print(fName)

x = fName[0]  # Get first element of string
print(x)

# Suppose I want to change firt item of Bhagat from B to V

#fName[0] = "V"         # this will result in error:'str' object does not support item assignment

# What I can infer is that you cannot change items/element of string OBJECT after its assignment so, we can say that
#   STRINGS ARE IMMUTABLE

# IN context to above list is mutable
## Lists
# List can be heterogeneous,Homogeneous

oopConcept = ["Abs","Poly","InHeri","Encap"]
print(oopConcept)

print(oopConcept[2])

oopConcept[2] = "Inheritance"   #Here we are changing element of the list
print(oopConcept[2],oopConcept)

myList = ["Ram","Rahi",'X','Y','Z',"123.25",123,"3.14",50,5+2,math.tan(45)]
print(myList,type(myList))

myOtherLst = list((1,2,3,4,'I',"love","list"))
print(len(myOtherLst))

for i in range(len(myOtherLst)-1):
    print(i)
    if(myOtherLst[i] == "I"):
        myOtherLst[i] = "We"

        print(myOtherLst)

otherList = [1,2,3,4,5,6]
print(max(otherList))
        
# Append is use to insert object to the end of the list

otherList.append("Prabin")
print(otherList)
otherList.append(["Rabin","Bhagat"])                       # This is nesting of list adding list into list
print(otherList)
#output: [1, 2, 3, 4, 5, 6, 'Prabin', ['Rabin', 'Bhagat']]

print(otherList[7])

# What if you wanted to acces the first element of nested list i.e., Rabin
print(otherList[7][0])

# I want to acces a range of element from a specific position
# we will use indexing technique with :  (index:last index) Note:last element i (n-1)
# printing all element from 3rd index
print("Indexing technique: ",otherList[3:])

print("Indexing technique: ",otherList[3:6])  # it will not go to 6 index it will gotill 5 index in list or in collection or range last element i n-1
print(otherList)

# Now unlike append i want to insert element at a specific index we use insert method
otherList.insert(2,"World")  # insert at index 2
print(otherList)

#Suppose i want to add two elemnts at once without creating nested list the key is Extend method

lst = [1,2,3,4,5,6,7,8]
lst.append([9,10])     # creates nested lst
lst.extend([9,10])     # extends lst by adding elemnts seperateley 
print(lst)

# Operation performed on list
#1 sum() - will add all the element
lst = [1,2,3,4,5,6,7,8]
a = sum(lst)
print(a)

print(lst*5) # it will append lst five times but if you want to divide each element with 5 use for loop

for i in lst:
    print(i*5)

#2 pop() will remove last element if index not specified and update the list 
lst.pop()
print(lst)
lst.pop(4)
print(lst)

#3 count() will calcualte total occurance of given element in list

print(lst.count(1))

# ******************************** 1.Lists Ends******************************

