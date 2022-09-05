
## Tut 3 for control flows in Python My Notes and Codes

'''
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


# Loop statements:
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
'''
### Tut 5 Pythom Math/Number Methods
# Data scientist/data analytic like log normal distribution, finding exponent etc uses math/number methods

#1. abs()
#   abs(x) will return the absolute value of a number x which we pass in argument. The number x can be integer, float, complex,..

from math import ceil, floor
import math

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