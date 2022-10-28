 
## Why Functions?
#1. To make code more readable.
#2. To make code more efficient.
#3.  To make code more maintainable.
#4. To make code more reusable.
#5.  To make code more extensible.


from ast import Return


print('Hello world welcome to black vamp tuts')
# What if i had same print statement multiple times
print('Hello world welcome to black vamp tuts')
print('Hello world welcome to black vamp tuts')
print('Hello world welcome to black vamp tuts')
print('Hello world welcome to black vamp tuts')

# Now i want to change the text black to Red , i will have to manually change it in all the lines.
# Which is hectic, So, for this FUNCTIONS comes to rescue. Lests create a function for the same

def Welcome():
    print('Hello world welcome to my function black vamp tuts')

Welcome()
Welcome()

# Now i want to return a string then

def WelcomeAgain():
    return "Welcome Again"

print(WelcomeAgain())

# Now lets add description and Return type for our funcition

def WelcomeOnce()->str:
    """
    Description: This function will print a welcome message.

    Return: This will return a string

    """
    return "Hello World"

print(WelcomeOnce())

# Lets parameterize our function

def SayHello(name:str)->str:
    return print( "Hello " + name)

SayHello('Prabin')

## Function to Add Even and ODD

def AddEvenOdd(list):
    evenSum =0
    oddSum = 0
    for i in list:
        if(i%2==0):
            evenSum += i
        else:
            oddSum += i
    return "Sum of Even " +str(evenSum) + " Sum of odd " + str(oddSum)

    #return evenSum,oddSum   this will also work smoothly

#sum1,sum2 = AddEvenOdd([1,2,3,4,5,6,7,8,9,10])

print(AddEvenOdd([1,2,3,4,5,6,7,8,9,10]))

## Positionl and Keyword argument:

def Hello(name,age):  
    print("Hello "+ name + " You are "+str(age) + " Years old.")

Hello("Prabin",32) #when we define a parameter and we call a function we specifically give value than it is Postitional argument

def HelloAgain(name,age = 32):  # it is keyword argument as we define default value, just like optional param in vb.net
    print("Hello "+ name + " You are "+str(age) + " Years old.")

HelloAgain("Robin")   
HelloAgain("Robin",36)  # Here we converted keyword args to positional args.


def hello(*args,**kwargs):   # *args = positinal  **kwargs = keyword, we can use anything instead of args,kwargs.
    print("args: ",args)
    print("kwargs: ",kwargs)

hello("Prabin","Bhagat",age = 31,Dob = 2000)

# now lets take the output of above which is tuple and dict and store it in lst and dict

lst = list(('Prabin', 'Bhagat'))
dic = {'age': 31, 'Dob': 2000}
hello(lst,dic)  # it will consider both lst and dic as postional argument(coz key value pair is missing) which is a problem,how will we seperate them as position and keyword?????
# ans : it is simple just use * and **
hello(*lst,**dic)