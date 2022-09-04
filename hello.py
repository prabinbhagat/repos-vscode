
# Tutorial for control flows in Python My Notes and Codes

a = 5
b = 6
print(a+b)

# if statement

val = input("enter a Num ")
chechval = int(val)
if (chechval % 2==0):
    print("even num")
else:
    print("odd")
    
# Age form nested if

age = int(input("Please input your age: "))
if(age<18):
    if(age<17):
        print("You are minor")
        print("You are in school")
    else:
        print("you are in collage")

elif(age>=18 and age <= 35):
    print("Mid age")
elif(age>= 45 and age <=50):
    print("mid mid age")
else:
    print("Senior citizen")


## Loop statements
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
    

