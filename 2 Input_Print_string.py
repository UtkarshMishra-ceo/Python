#input function use to take input from user 
#input function always takes input in string
name=input("enter you name")
print(name)
#adding two numbers

num1=input("enter first number : ")
num2=input("enter second number : ")
total=num1+num2  
print(total)                   

'''if we give num1=2 and num2=2 it gives output 22 because input takes input in string
 so we have to convert it into integer and then add it'''
total=int(num1)+int(num2)                 #type casting
print(total) 
#or
num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
total=num1+num2
print(f"After Coverting into Integer total is  {total}")

# type casting
a=str(20)       #Convert value into string
b=int("20")     #covert value into integer
c=float(20)     #covert value into floating point number
print(f"Type casting a= {a} b= {b} c= {c}")

# String Concatenation => Adding two string
print("your name is " +name) 
first_name="utkarsh"
last_name="mishra"
full_name=first_name +" "+ last_name

print(full_name)                  #or
print(first_name +" "+ last_name) # " " helps to provide space
print(first_name*3)               #print utkarsh 3 times

#Raw string
print(r"Line A \n Line B") #it write \n as it is output = Line A \n Line B
# declare multivariable at once
name , age ="utkarsh",20
x=y=z=1                                                  # if value is same we write like this
print("hello "+name+" your age is " +str(age))           #ugly format

# String Formatting 
print("hellow {} your age is {}".format(name , age))     #python 3 string formatting
print("your age is {0:f}".format(age))                   # it convert int age into float 
print("your age is {0:.3f}".format(age))                 # .3f give output upto 3 decimal values use .
print("hellow {1} your age is {0}".format(name , age))   # with numbers here 0 means name and 1 means age

# python 3.6 string formatting (best to use)
print(f"hellow {name} your age is {age}")                #dont forget to put f before ""
print(f"hellow {name} your age is {age+2}")              #we can also add like this

'''we can't add number to a string we convert no. into string using str() function.
 print("hello "+name+" your age is " + age ) gives you error '''

# more than one input at once we can use splict() function
num1,num2,num3 =input("enter three number use comma").split(",")           #we use comma like 3,3,3

''' if we put , in split function we have to place comma before enter 2nd value
 otherwise we have to give space before enter value'''

num1,num2,num3 =input("enter three number give space").split()            #in this we use space like 3 3 3

avg=(int(num1)+int(num2)+int(num3))/3
print("average is"+str(avg)) #or

print("average of three no {}".format((int(num1)+int(num2)+int(num3))/3)) #python 3 string formatting

print(f"average of three no {(int(num1)+int(num2)+int(num3))/3}")         # python 3.6 string formatting
#here {} is known as place holder

#Raw string 
''' If we put r in print funtion before  "" in print function it treat all values as raw string'''
#example
print(r"Line A \n Line B") 
# it treat escape sequence as normal text
