''' Define a function which takes three numbers as a input and return geater of three'''
print("Greatest Of three No.")
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greatest(10,20,30))
     
     #or function in function
print("Function in function")
def new_greatest(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c)

def greater(a,b):   #function for greatest of two numbers
    if a>b:
        return a
    return b

print(new_greatest(50,60,70))

# #KISS - keep it simple stupid 

''' Define is_palindrome function that take one word in string as input and return true if it is 
palindrome else return false Palindrome- word that reads some backwards as forward
 is_palindrome("mada") ----> true
logic(algorithm)
Step 1: reverse the string
step 2: compare reversed string with original string
'''
print("Palindrome Of a String")
def is_palindrome(word):
    reversed_word=word[::-1]
    if word==reversed_word:
        return True
    return False

print(is_palindrome(input("Enter word:")))

'''Fibonacci Series
    0 1 1 2 3 5 8 13 21 34'''
print("Fibonacci Series")
def fibonacci_series(n):
    a=b=0
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")

fibonacci_series(10)
print("\n")
#default parameters
'''If we want to leave parameter empty we use default parameter'''
# Note: We only make last parameter as default
print("Default Parameter")
def user_info(first_name, last_name,age='unknown'):
    print(first_name)
    print(last_name)
    print(age)
    
user_info('Utkarsh','Mishra')

# This will give error
'''def user_info(first_name, last_name='unknown',age):
    print(first_name)
    print(last_name)
    print(age)
    
user_info('Utkarsh',,15)'''

# Scope variable
'''The scope of local variable is only in the function in which it defined
and we can use global variable in any function'''
print("Scope Variable")
def func():
    x=7             #Local variable         
    return x
print(func())
def func2():
    print(X)        #Here it not print the value of x because scope is over in 

x=5                 #Global variable
def func():
    x=7
    return x
print(func())      #it print the value of x in function
print(x)           #it print the value of globalvariable

def func2():
    global x       #use of global variable in function
    print(x)
func2()