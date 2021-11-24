# Exercise-1 (Number Guessing Game)
''' Make a variable ,like winning_number & assign any number to it.
ask user to guess a number. If it correct print "you win!!!!"
If user guessed lower than actual then print "To Lowwww"
If user guessed higher than actual number then print "To Highh'''
print("-->Number Guessing Game")
winning_number=10
print("guess the number")
num=int(input("guess the number:"))
if(num==winning_number): #we use ()==) to check equality
    print("you win!!!!")
else:
    if(num>winning_number):
        print("To highhh")
    else:
        print("To Lowww")    

#Exercise-2 (Watch Coco)
'''Ask user's name & age. If user's name start with('a' or 'A') and 
age is above 10 then print "you can watch coco movie"
 else print "sorry, you can't"'''

print("-->Watch Coco movie")
name=input("Enter your name:")
age=int(input("Enter your age:"))
if name[0].lower()=="a" and age>10: #or simple method--> name[0]=='a' or name[0]=='A' and age>10
     print("you can watch coco movie")
else:
     print("you can't")    
# Check multiple condition using if elif else
#Exercise-3 (Show Ticket Pricing)
'''Ask user to Enter age and check following conditions
if age in between 1 to 3 print free
if age in between 4 to 10 print 150
if age in between 11 to 60 print 250
if age is above 60 print 200'''

print("-->Ticket Pricing")
age=int(input("enter your age:"))
if 0<age<=3:
    print("Price = Free")
elif 3<age<=10:
    print("Price = 150")
elif 11<age<=60:
    print("Print = 250")
else:
    print("Price = 200")    