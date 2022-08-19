import math,os,threading, time, sys

a = int(input("Enter first number: "))
b = int(input("Enter power: "))
#get the power value
c = int(pow(a, b))
print(a,"**",b, "=",c)
#print logarithm using math function
print(math.log(a,a))
