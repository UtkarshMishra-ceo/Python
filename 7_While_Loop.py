#While Loop
'''If we want to repeat a line of code many times
their are two types of loops in python
syntax of while loop in every programming language is same but Syntax of 
for loop is different in python'''

print("-->Print -- hello World 10 times")
i=1
while(i<10):
    print("hellow World")
    i+=1

# Program-1 --> sum of n natural number
print("-->Sum of n natural number")
num=int(input("Enter Natural number:"))
sum,i=0,1
while i<=num:
    sum=sum+i
    i+=1
print(f"sum of n natural number is {sum}")

# Program-2 --> sum of number number Ex:1234=1+2+3+4   
print("-->Sum of Numbers 1234=1+2+3+4")
num=input("enter a number :")
sum=i=0
while i < len(num):
    sum= sum+int(num[i])
    i+=1
print(sum)
    
'''infinite loop -- loop which never stop'''
# use ctrl + C to stop
# i,j=0,10
# while i<=j:
#     print("hello")
    #infinite loop i+=1 is needed

# while true:
#     print("hello") 
#     infinite loop condition always true
'''Boolean datatype has two values True and False'''