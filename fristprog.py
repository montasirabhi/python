# Print Is A Function , it's use for printing Something On The Screen
#Hello World is an text what we wanted to Show on hour Screen . And Cotations Are Use For Print String 

print("Hello World")
print("I Am MD MONTASIR RAHMAN ABHI")
print("My Age Is 22")
print("Frist Sentence .","Secound Sentence")
print(23)
print(23+32)

#Variables
# A Variable is a name given to a memory location in a program.

name = "Abhi" #string
age = 22 # Intiger
price = 25.50 # Floating
age2 = age

# The name , age and price is the variables and Abhi , 23 , 25.50 are values
# A variable can store another variable what have a value

print(name)
print(age)
print(price)

print ("Hello World ! My Name is ", name ,". And My Age is", age , ". Todays Patato Rate is", price)
print(age2)
# The Comma Is Very Important to add tow thing in one line.


#Rules Of Identifiers
# 1) Identifires can be combination of uppercase and lowercase latters , digit or underscore(_)
# So my_Variable , variable_1, variable_for_print all are valid python identifires.
# An Identifires can not start with digit . So while variable1 is valid and 1variable is invalid.
# We can't use special symbols like !,#,@,%,$ etc in our identifier.
# Identifier can ve of any length.


# ==============================================


#Primary Data Types
# Integers (+ve , -ve like : 25 , -25)
# String ("Abhi", " Hello" , " Anything")
# Float (1.5 , 3.50 )
# Boolean ( True , False) Note : T and F will be capital letter
# None  ( a= None)
print(type(name))
print(type(age))
print(type(price))


Boll = 23
old = False
a = None

print(type(Boll))
print(type(old))
print(type(a))


# ==================================================

# Keywords : ( Reserved Words In Python)
# and ,as, assert , break , class , continue , def , del , elif 
# else , except , finally , False , for , from , global , if , import
# in , is, lambda, nonlocal , None , not , or , pass , raise
# return , True , try , with , while , yield


# Keywords Can not be used for variables 

# Python Is A Case Sensative Language . (A != a )
# In Python Name is not equal name . 

# ==================================


# Print Sum : 

a = 150
b = 250

sum = a + b
diff = a - b 
print(sum , diff)


# ===========================

# Comments . 
# We Can use comments as # or Triple cotation . 
"""
In The Triple Cottation 
We Can write multi line comments
"""

# Comment Shortcut :  Select the whole lines and  press : " Ctrl + / "




# =================Types of Operators========================

# Arithmetic Operators 

a = 5 
b = 2 

print(a + b) # Sum
print(a + b) # Different
print(a * b) # Multiply
print(a / b) # Devided
print(a % b) # Remainder ( % = Modiule )
print(a **  b) # a^b || a to the power b


# Relational / Comparison Operators 

a = 50 
b = 20

print(a == b) # False
print(a != b) # True
print(a <= b) # False
print(a >= b) # True
print(a < b) # False
print(a > b) # True


# Assignment Operators 

a = 50 # = is assign 50 to a
num = 10

num = num + 10 
print(num) # Answer will be 20

# in short =>

num += 10 
print(num) # Answer will be 20 + 10 = 30 

num -= 25
print(num) # Answer will be  30 - 25 = 5

num *= 5
print(num) # Answer will be  5 * 5 = 25

num /= 5
print(num) # Answer will be  25/5  = 5

num %= 3
print(num) # Answer will be  5/3  = 1 Reminder ( 2 ) 

num **= 2
print(num) # Answer will be  2^2  = 4





# Logical Operators (not , and , or)

print(not False) # Answer will be True 
print(not True) # Answer will be False

print(not (a>b)) # Answer will be False

value1 = True
value2 = True

print("ans operator :", value1 and value2)



# In this Way : 

value1 = True
value2 = True

print("ans operator :", value1 or  value2) # if anyone is true , than true  

