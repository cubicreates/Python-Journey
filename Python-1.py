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



# Operators