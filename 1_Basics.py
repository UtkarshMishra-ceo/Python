#COMMENTS
# single line comment starts with (#)
# multiline comment starts with ''' and ends with '''
# Example of multiline comments :
''' some escape sequences characters are 
 \t for tab space .\n for new line , \\ for backslash , \' for ', \" for ",\b for backspace '''
 
# **************** print this lines ******************
'''
#  this is \\ double backslash 
# these are /\/\/\/\/\ mountains
# he is     awesome (use escape sequence instead of manual space)
# \" \n \' (print this as an output)
# print escape sequence using raw string
# print emoji having unicode (U+1F603 , U+1F618)
'''
a,b=10,5
c = a + b
d = a - b
e = a / b
f = a * b
#Assignment operators
''' 
=  -> It assign value    Ex:- A=1
+= -> It add value       Ex:- A+=1 means A=A+1
*= -> It Multiply value  Ex:- A*=1 means A=A*1
/= -> It Divide value    Ex:- A/=1 means A=A/1
-= -> It Substract value Ex:- A-=1 means A=A-1
'''

# Multi-line Print
print(f"""
1. Add is {c}
2. Sub is {d}
3. Div is {e}
4. Mul is {f}
""")

# Solution1
print('this is \\\\ double backslash')
# solution2
print('these are /\\/\\/\\/\\/\\ mountains')
# solution3
print('he is\tawesome')
#solution4
print('\\\" \\n \\\'')
# \' = '
# \\ = \
# so \\\' =\'
#solution5
print(r"this is \\ double backslash")
#solution6
print('\U0001F603') # add a backslash \ in starting and 000 in place of +
print('\U0001F618') 

#Variables
num=1       
print(num)
name="utkarsh" # Put string in single quote or in double quotes
print("name")
''' here num and name is a variable name it is name given to a memory location to store a value '''

#Rules for defining a variable name
''' 
=> A variable name can contain alphabets , digits and underscore.
=> A variable name can only start with an alphabet and underscore.
=> A variable name can't start with a digit.
=> No special symbol allowe in variable name.
=> No white space is allowed to be used inside a variable name. 
'''
num=2   #Noerror
_num=1  #Noerror
num_1=5 #Noerror
'''
1num=2  #error  =>can't start with a digit
num$=2  #error  => special character not allowed
Num 1=2 #error => white space not allowed
'''
#type() function
''' it tells us datatype of a variable'''
no=1
name='utkarsh'
num=12.5
List=[1,2,5,4,6]
tup=(1,2,3,4,5)
dic={'name':'utkarsh','age':20}
sets={1,5,6,4}
print(type(no))     #output: int
print(type(name))   #output: str
print(type(num))    #output: float
print(type(List))   #output: list
print(type(tup))    #output: tuple
print(type(dic))    #output: dict
print(type(sets))   #output: set
#Conventions
'''
=> it is a way/styleto choose sensible names for Python objects such as 
variables, functions, modules and so on.

=> PEP 8, is a document that provides guidelines 
and best practices on how to write Python code. It was written in 2001 by 
Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 
is to improve the readability and consistency of Python code.

=> PEP stands for Python Enhancement Proposal, and there are several of them. 
A PEP is a document that describes new features proposed for Python and
 documents aspects of Python, like design and style, for the community.
'''
#Example 
my_name_is="utkarsh" #snake case writing mainly used in python
myNameIs="utkarsh"   #camel case writing mainly used in java

''' it is not necessary but it create good impression and improve redability of code 
client understand in which language code written in by the way of writing  '''

# Write functions , variable, method, module in lowercase and separate with underscore
# Example:- my_code ,num_1 
# Write class name each word stard from uppercase and do not separate with underscore
# Example:- MyCode ,HelloWorld
# Write  constant in uppercase and separate with underscore
# Example:- MY_CODE ,HELLOW_WORLD
# Write Package in lowercase and do not separate with underscore
# Example:- mycode, hellowworld
# Use proper spaces in between codes and lines to improve redability of code

''' it is not necessary if you write code for yourself '''
