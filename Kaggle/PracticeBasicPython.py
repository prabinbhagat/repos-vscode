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







