''' LETS PERFORM VARIOUS CALCULATIONS IN PYTHON  '''
a=3 
b=2
print(a+b)   #addition
print(a-b)   #substraction
print(a*b)   #multiplication
print(a/b)   #float division (it gives output in point ans=1.5 )
print(a//b)  #integer division (it gives output in integer ans=1)
print(a%b)   #modulo (it gives reminder)
print(a**b)  #exponent (it gives power 3^2=9)

# Precedence Rule
'''
   OPERATORS          |   PRECEDENCE AND ASSOCIATIVITY RULE
   Parantheses ()     ---  Highest
   Exponent **        ---  Right to Left
   * , /, //, %       ---  Left to Right
   + , -              ---  Left to Right 
'''
# Example
print((2+3)*2)
'''   => 5*2 
      => 10    '''

print((2+3)*5/2%6)         
'''   => 5*5/2%6  here associativityrule apply for *,/,% 
      => 25/2%6   Associativity Left to Right
      => 12.5%6
      => 0.5  '''

# For Exponent
print(2**3**2) 
''' => 2**9   Associativity Right to left
    => 512  '''
                 
