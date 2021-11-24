#For Loop 
''' It is use  to repeat a line of code many times
Note : Syntax of for loop is different in python'''

#Program 1
print("--> Print -- Hello World 10 time")
for i in range(10): #loop will execute from i=0 to i<10
     print("hellow world")

#Break and Continue Keyword
#Break
print("-->Break Keyword")
for i in range(1,11):
     if i==5:
          break # if the value of i is 5 loop break and rest of code in llop not run
     print(i)

#Continue
print("-->Continue Keyword")
for i in range(1,11):
     if i==5:
          continue  # back to loop in this 5 will not print 
     print(i)     
# Program 2
print("Sum of n numbers Ex: 1+2+3+4+5----+n")
num=int(input("Enter the number: ")) #sum of n numbers 1+2+3+.....n
sum=0
for i in range(1,num+1):
     sum+=i
print(f"sum of {num}no is {sum}")

# Program 3
print("Sum of number Ex: 1234 -> 1+2+3+4")
num= input("Enter a number: ")  # input 1234 =>output 1+2+3+4 =10
sum=0
for i in range(len(num)):
   sum+=int(num[i]) 
print(f"sum of num is {sum}")

#Program 4
print("Characters Count in String")
name = input("enter your name : ") # program for character count in string
temp=""
for i in range(len(name)):
    if name[i] not in temp :
         print(f" {name[i]} : {name.count(name[i])}") 
    temp+=name[i]

#DRY --> don't repeat yourself
#range () function 
'''range funtion tell us from where value is start and where end '''
# syntax: range(Start argument , Stop argument , Step argument)

#Step Argument in range
print("--> Even Numbers")
for i in range(1,11,2): 
     print(i)  #output even Numbers: 
print("-->Odd Numbers")
for i in range(0,11,2):
     print(i)  #outpur odd Numbers :1,3,5,7,9
print("-->reverse Number 10 to 1")
for i in range(10,0,-1):
     print(i)  #outpur 10,9,8,7,6,5,4,3,2,1   

# For Loop and strings
name="utkarsh"
for i in name:
    print(i)   #or 

for i in utkarsh:
    print(i)
# [Note: string in python is iterable]
