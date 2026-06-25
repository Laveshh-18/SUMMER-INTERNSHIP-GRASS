#Operators


print(10+20) #add two numbers
print(10-20) #subtract two numbers
print(10*20) #multiply two numbers
print(10/20) #divide two numbers
print(10%20) #modulus operator gives the remainder of the division
print(10//20) #floor division gives the quotient of the division without the decimal part
print(10**20)       #exponentiation operator gives the result of the first number raised to the power of the second number

#unary operatprs
print(-10) #negation operator gives the negative of the number
print(+10) #positive operator gives the positive of the number
print(--10) #double negation gives the original number
print(+-10)  #combination of positive and negative operators gives the negative of the number
print(-+10) #combination of negative and positive operators gives the positive of the number
print(++10) #combination of positive and positive operators gives the positive of the number
print(10++10) #invalid syntax
print(10--10) #invalid syntax


#arithmatic operators
#+,-,*,/,%,//,**
num_1=100
num_2=20
print(num_1+num_2)
print(num_1-num_2)
print(num_1*num_2)
print(num_1/num_2)


#relational operators
#==,!=,>,<,>=,<=
#relational operators are used to compare two values and return a boolean value (True or False)
#output will be True or False
print(num_1==num_2) #equal to operator returns True if both operands are equal
print(num_1!=num_2) #not equal to operator returns True if both operands are not equal
print(num_1>num_2) #greater than operator returns True if the left operand is greater than the right operand
print(num_1<num_2) #less than operator returns True if the left operand is less than the right operand
print(num_1>=num_2) #greater than or equal to operator returns True if the left operand is greater than or equal to the right operand
print(num_1<=num_2) #less than or equal to operator returns True if the left operand is less than or equal to the right operand 


#assignment operators
#=,+=,-=,*=,/=,%=,//=,**=
num_1=100
num_1+=20 #num_1=num_1+20
print(num_1)
num_1-=20 #num_1=num_1-20
print(num_1)
num_1*=20 #num_1=num_1*20
print(num_1)
num_1/=20 #num_1=num_1/20
print(num_1)
num_1%=20 #num_1=num_1%20
print(num_1)
num_1//=20 #num_1=num_1//20
print(num_1)
num_1**=20 #num_1=num_1**20
print(num_1)

#logical operators
#and,or,not
print(num_1 and num_2)#and operator returns the first operand if both operands are true, otherwise it returns the second operand
print(num_1 or num_2)#or operator returns the first operand if at least one of the operands is true, otherwise it returns the second operand
print(not num_1)#not operator returns the opposite of the boolean value of the operand
print(not num_2)#not operator returns the opposite of the boolean value of the operand


str="hello"
str1="_"
print(str and str1) #and operator returns the first operand if both operands are true, otherwise it returns the second operand
print(str or str1) #or operator returns the first operand if at least one of the operands is true, otherwise it returns the second operand
print(not str) #not operator returns the opposite of the boolean value of the operand
