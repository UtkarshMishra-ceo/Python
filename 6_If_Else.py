#if is use to check condition 
#if condition is true the code in if block run otherwise code in else block run
print("If-Else")
a,b=6,5
if(a>b):
    print("byy")
else:
    print("hello") 


#spaces is require in python
# Q: Why spaces is important in python
''' in otherprogramming language we use curly braces {} so we don,t need to think about spaces 
but in python we dont use curly braces thats why space is important otherwise it gives indentation error'''

# pass statement
x=18
if x>18:
    pass
'''if we write nothing in in if block so it gives error thats why we use pass'''
'''pass simply pass control out of if statement'''

#"==" it is use to check the equality
#and , or operator --> to check two condition at same time

name='abc'
age=12
print("--> And operator")
if name=='abc' and age==19: #(when both conditions are true then it gives true otherwise false)
    print("condition true")

else:
    print("condition false")

print("--> Or operator")
if name=='abc' or age==20: #(if any one condition is true then it gives true  )
    print("condition true")

else:
    print("condition false")

# in keyword --> it check any word/character present in string,list,dictonary,set,tuple
print("-->In keyword")
name="utkarsh"
if 'a' in name:              #if present code of if block will run
    print("a is present")
else:                        #if not present code of else block will run
    print("not present")

#Check empty or not -> check string is empty or not
print("-->Empty or Not")
name="utkarsh"
if name:           #true, if string is not empty
    print("hello")
else:              #false, if string is empty
    print("empty")    

print("--> If - Elif -Else")
age=int(input("enter age :"))
if(age>18):
 print("yes")
elif(age==18):
 print("yes")
else:
 print("no")
