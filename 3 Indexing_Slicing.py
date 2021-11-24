#String Indexing
language="python" 

''' Here position of p starts with 0 , y -> 1 , t -> 2 ,h -> 3 , o -> 4 ,n -> 5 '''
print(language[3]) #we use square brackets to write index & output is h

''' negative indexing start from last character in string with -1 
position of n -> -1 ,o -> -2 , h -> -3 , t -> -4 , y -> -5 and p -> -6'''
print(language[-1]) #output - n
# print(language[-7]) #it gives error because it is out of range of string

#String Slicing

lang="Python"
#if we want more character print at a time ex: py
print(lang[0:2]) #output - py

''' Syntax: variablename[start argument : stop argument-1] '''

print(lang[2:4]) #output - th

# We can also use negative indexing
print(lang[-4:-1]) #output - tho

print(lang[1:]) #output - ython 
print(lang[:3]) #output - Pyt

''' if we leave starting point blank it starts with 0th position
And if leave Ending point blank it Ends at last position'''

# Step_Argument_slicing
''' syntax - [start argu. : Stop argu. :step argument]'''

lang="Python"
print(lang[0:6:1]) #here one is step argument output - Python
''' step argument tell how much step it take '''

print('utkarsh'[0:5:1]) #we can also write this Output - utkar
print("utkarsh"[0:5:2]) #output - ukr |it print value at 0th ,2nd, 4th position
print("utkarsh"[0::3])  #output - uah |it print value at 0th ,3rd, 6th positon
print("utkarsh"[6::-1]) #it print reverse of string Output - hsraktu

# Exercise -2 
print("Exercise 2 | reverse of name")
''' Ask user name and print it into reverse order in two lines'''
name=input("Enter your name:")
print(name[::-1]) #or
print(f"reverse of your name is {name[::-1]}")

#Strings Are immutable
'''if we create string we unable to change its values on a particular index number
thats why it is called immutable'''

name="utkarsh"
print(name[1]) #output - t

# but it we want to change t from T 
# string[1]='T'
# it gives error 

''' If we want to replace '''
print(name.replace('t','T')) #Output - uTkarsh 
#but it not change original string it create new string

name1=print(name.replace('t','T'))
print('name') #output - utkarsh | no effect on original string
print('name1') #output - uTkarsh
