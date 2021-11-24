#String Methods

name="utkarsh mishra"
#len() function -> use to find length of string it also count space b/w string
print("Length Function")
print(len(name)) #output-14 

#lower() method ->it convert string into lower case
print("Lower Method")
print(name.lower()) #output - utkarsh mishra

#upper() method ->it convert string into upper case
print("Upper Method")
print(name.upper()) #output - UTKARSH MISHRA

#title() method -> capatalise first letter in string
print("Tittle Method")
print(name.title()) #output - Utkarsh Mishra

#count() method -> it count how much time a particular character repeat in string
print("Count Method")
print(name.count("a")) #output - 2 |because a repeat 2 times in Utkarsh Mishra 

#Find And replace method
string="she is beautiful and she is good dancer"

#find() method -> it find the position of word and character
print("Find Method")
print(string.find("is")) #output - 4 |because it starts from 4th position
print(string.find("is",5)) #output - 25 |it start searching from 5th index

''' Syntax Variable_name.find("word/character" ,start ,end)
if we give starting and ending point to a straing it searh in between them'''
is_pos1=string.find("is") #we can also save position 
print(is_pos1)

'''if we want to search next is in string '''
print(string.find("is",is_pos1+1))

#replace() method -> it is use to replace any word/character from string
'''syntax : string,replace("item to replace" , "replace with")'''

print(string.replace("is","was"))

string="she is beautiful and she is good dancer"
print(string.replace("is","was",1)) # it replace only first is. we can tell how much word can replace

#center method --> it use to write the string in center
print("Center Method")
name="utkarsh"
#we want output **utkarsh**
''' Syntax : Variable_name(lengthof string+ no.of symbol ,"symbol")'''

print(name.center(11,"*")) # 7 length of string + 4 stars 2-left 2-right 
#we can print anything in place of star and also use len() function to count length

print(name.center(len(name)+4,"@"))
print(name.center(len(name)+4," ")) #It print space to left and right side

#swapcase() method --> it convert lower case into upper case and vise versa
a="heLLo"
print(a.swapcase()) #output : HEllO

#Strip() method --> it use to remove/manage spaces in string
''' two type
-> lstrip() -- remove spaces from left
-> rstrip() -- remove spaces from right'''
name="     Utkarsh     "
dots="....."
print(name+dots)         #output:      Utkarsh     .....
print(name.rstrip()+dots) #output:      Utkarsh..... | it remove space from right
print(dots+name)         #output: .....     Utkarsh      |print space
print(dots+name.lstrip())#output: .....Utkarsh     |it remove space from left

''' If we have lots of space in between string we can us replace method to remove'''
full_name="utkarsh     mishra"
print(name.replace(" ","")) #it replace space with no space

#Exercise 1
print("Exercise to print 4 stars Left & Right of a string")
name=input("Enter your name:")
print(name.center(len(name)+8,"*")) #here 8 means 4 star to left and 4 to right

# Exercise 2
'''Take two comma separated inputs from user
->user's name
->a single character
output
->user's name length
->count the character that user inputed
use:case insensitive count'''
name,char=input("Enter your name and character to search:(comma separated)").split(",")
print(f"length of name is {len(name)} : and character count is {name.count(char)}")

#dont use "" in count section ex:count is {"name.count(char)"}
#  because the entered value is already in string

#don,t put space if you use comma separated
# otherwise it take space and character as a string'

''' Enter your name and character to count: Utkarsh, h'''
#here space after comma gives count zero 
#correct method is Utkarsh,h no space

print(f"length of name is {len(name)} : and character count is {name.lower().count(char.lower())}")
#in upper print function it only count lower case or upper case values
#but this count upper case and lower case both 

print(f"length of name is {len(name)} : and character count is {name.strip().lower().count(char.strip().lower())}")
#name.strip().lower().count() remove spaces from name and convert it into lowercase and count(character)
#char.strip().lower() remove space from char and convert it into lowercase
'''due to this we don't need to worry about spaces'''