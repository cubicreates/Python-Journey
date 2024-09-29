# Lesson 1 : Revising Printing Statements, User Input, Datatypes, Operators and Operators Precedence and Associativity




# Printing Statements

print("Hello World!") #basic print statement

# Using Variables

variable = 52

print("Hello",variable) #Way no. 1
print(f"Hello {variable}") #Way no. 2 ; My personal preffered method called String formatting


# User Input

UserInput = input("What is your name?: ")
print(UserInput)

# Datatypes and Typecasting
# To see the type of data we use type() fuction and to externally type cast it we use their initials.

a_1='Hi' #-->String
a_2= 2 #--> Integer
a_3= 2.0 #-->Floating Point Number
a_4= ['',1,True] #-->List
a_5= ('',1,True) #-->Tuple
a_6= False #--> Boolean
a_7= {1,2,34,56} # --> Set
a_8= {1:"Hi", 2:"Hello", 3:"World"} #-->Dictionary

print(type(a_1))
print(type(a_2))
print(type(a_3))
print(type(a_4))
print(type(a_5))
print(type(a_6))
print(type(a_7))
print(type(a_8))

# External Typecasting
a_2=str(a_2)
print(type(a_2))
print(a_2)
a_2=float(a_2)
print(type(a_2))
print(a_2)
a_3=int(a_3)
print(type(a_3))
print(a_3)



# Operators and Operator Precedence

# Arimetic Operators: + - * / ........
# Increment Operators: += -= *= /= ........
# Comparision Operators: <= >= == != ........
# Logical Operators: and or not ........

# Operator Precedence:-

# Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR

# Associativity 
# Default of assciativity of a single operator is left to right, it varies for multiple operators

# 1

# ()	
# Parentheses

# Left to right

# 2

# x[index], x[index:index]	
# Subscription, slicing

# Left to right

# 3

# await x	
# Await expression

# N/A

# 4

# **	
# Exponentiation

# Right to left

# 5

# +x, -x, ~x	
# Positive, negative, bitwise NOT

# Right to left

# 6

# *, @, /, //, %	
# Multiplication, matrix, division, floor division, remainder

# Left to right

# 7

# +, –	
# Addition and subtraction

# Left to right

# 8

# <<, >>	
# Shifts

# Left to right

# 9

# &	
# Bitwise AND

# Left to right

# 10

# ^	
# Bitwise XOR

# Left to right

# 11

# |	
# Bitwise OR

# Left to right

# 12

# in, not in, is, is not, <, <=, >, >=, !=, ==	
# Comparisons, membership tests, identity tests

# Left to Right

# 13

# not x	
# Boolean NOT

# Right to left

# 14

# and	
# Boolean AND

# Left to right

# 15

# or	
# Boolean OR

# Left to right

# 16

# if-else	
# Conditional expression

# Right to left

# 17

# lambda	
# Lambda expression

# N/A

# 18

# :=	
# Assignment expression (walrus operator)

# Right to left

# Rest is learnt as we work