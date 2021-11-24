'''list is a ordered collection of item , it is a datastructure 
you can store  anything in list int, float ,string'''
#Methods in list
'''To insert data'''
#append() method -->it add value into a list
#extend() method -->it add another list into list
#insert() method -->it use to insert data into particular position 
#we can provide position into it if position not present add data in last 
'''To delete data'''
numbers=[1,5,6,10,9,6,'fruits']
#pop() method =it delete last item of list and return it
number.pop()
print(numbers)
#we can pass position of ant element in pop to delete particular element
numbers.pop(2) #it delete elemnt present at second position

#remove() method -->if we did't remember position of element 
# we simple write name in this method to delete it
number.remove("fruits") 
'''if data not present in list it create error'''

#del operator -->we can also use del operator to delete items
del number[1]
'''some more methods'''

# count() method --> it count how much time a particular character repeat in list

#sort() method --> it convert actual list into sorted order

#sorted function --> it print the list in sorted order but not change actual list
num=[5,10,2,6,8]
print(sorted(num))

#reverse() method --> to reverse the list

#clear() method --> to delete the list

#copy() method --> copy the list into other

#index() method --> if we want to find position of particular element
num.index(10) #it tells the position of 10
#len()function --> gives length of list
'''we can also use string slicing in list'''
'''is vs equals'''
#'==' check the values present in list is same or not
# 'is' check both the list present at same memory location or not

''' (+) operator is use to concate two list '''
'''in  keyword with list'''

'''Join And Split Method'''
#spli() Method --> convert string in list
#join() Method  --> convert list into string
