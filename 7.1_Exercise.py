# Exercise-1 --> Check character count in string

'''Ask user for name 
Example- Utkarsh Mishra
print count of each word
output:
U : 1
t : 1
k : 1
a : 2
r : 2
s : 2
h : 2
  : 1  #space
M : 1
i : 1    '''

print("Character count in a string")
print("-->Count character")
name=input("enter any name :")
i=0
temp_var=""
while i < len(name) :
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1


