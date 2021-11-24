  #function to add two numbers
def add_two(a,b): #here a,b is known as parameter
     return a+b

a=add_two(5,4)  #here 5,4 is called argument 
print(a)

#Lets take some more example
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
print(add_two(num1,num2))

# Return vs print
''' print function print the value  but return function return the value
 it is not necessary to use return but if we want value back so we use return'''

# Function Practice
print("LAST CHARACTER")
def Last_Char(x):
    return(Name[-1])

Name=input("Enter a name:")
LC=Last_Char(Name)
print(LC)


# [Note: we can't pass int value to a string function]
print("ODD AND EVEN")
def odd_even(x):
    if(num%2==0):
        print("No is even")
    else:
        print("No is odd")

num=int(input("Enter a number:"))
print(odd_even(num))  #or

''' def odd_even(num):
    if num%2==0
        return "even"
    return "odd"
    '''
#To check only even
def is_even(a):
    if a%2==0:
        return True
    return False

print(is_even(10))

#or
''' def is_even(num):
    return num%2==0

print(is_even(10)
'''