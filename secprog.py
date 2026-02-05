# # str1 = " This is A String"
# # str2 = ' MONTASIR RAHMAN ABHI'
# # str3 = """This Is Also A String"""

# # str = input("Enter Any Text")


# # #Retrun true if string ends with substr
# # print(str.endswith("hi"))

# # # Capitalize First Charecter ( Not Change The Main String) [ If it is capital , than it will make it small ]
# # print(str.capitalize())

# # # if we need to change the Main String  : 
# # str = str.capitalize()  

# # print(str)

# # # Replace 


# # # Test with user input

# # old = input("Enter The Old Value")
# # new = input("Enter The New Value")


# # print(str.replace(old,new))

# #find

# # find_new = input("Enter The Search ")
# str = "My Name Is Abhi Name will print twice(2) in count"
# print(str.find("A"))


# #Count 
# print(str.count("Name"))

# #slice

# print(str[1:5])
# print(str[1:])
# print(str[:5])


# # Practise

# # Question : Input user's first name and print the length

# # Answer :

# username = input(" Enter Your First Name ")

# print(len(username))

# # Question : Find "$" how many times 
# Text = "the sign of $ is here and $"

# print(Text.count("$"))
# print(Text.find("$"))



# # Conditional Statements : 

# light = input("Light Color")

# if(light == "Red"):
#     print("You Can Not Go . Stop Here")
# elif(light == "Yellow"):
#     print("Wait A Moment")
# elif(light == "Green"):
#     print("You Can Go")
# else:
#      print("Light Is Broken")
    

# # Marks Entry ( Save Mark )

# marks = 69

# if(marks >= 90):
#     print("You Have Got 'A' Grade .")
# elif(marks <90 and marks >= 80):
#     print("You Have Got 'B' Grade .")
# elif(marks <80 and marks >= 70):
#     print("You Have Got 'C' Grade .")
# elif(marks < 70 and marks >= 60):
#     print("You Have Got 'D' Grade .")
# else:
#     print("You Have Got 'E' Grade .")


# # Manual Mark 

# marks = int(input("Enter Student Mark"))

# if(marks >= 90):
#     print("You Have Got 'A' Grade .")
# elif(marks <90 and marks >= 80):
#     print("You Have Got 'B' Grade .")
# elif(marks <80 and marks >= 70):
#     print("You Have Got 'C' Grade .")
# elif(marks < 70 and marks >= 60):
#     print("You Have Got 'D' Grade .")
# else:
#     print("You Have Got 'E' Grade .")


# # Nesting : ( if statement in if statement )
# # Suppose Drive Age

# age = 82

# if(age >= 18):
#     if(age >=80):
#         print("You Can Not Drive")
#     print("You Can Drive")
# else:
#     print(" Can Not Drive")



# Practice : 
# Question 1 : check the number what the user input is Odd or Even

number = int(input("Enter A Number"))

if(number%2 == 0 ):
    type1 = "Even"
else:
    type1 = "Odd"

print("The Number is ", type1)

# Question 2 : Find the Hightest Number , entered by the user

a = int(input("Enter A Number"))
b = int(input("Enter B Number"))
c = int(input("Enter C Number"))

if(a > b and a > c ):
        big = a 
elif( b > a and b > c):
    big = b
else:
    big = c

print("The Highest Number is ", big)

# Question 3: If the number user input is multiply by 7

number1 = int(input("Enter The Number"))

if(number%7 == 0 ):
    type1 = "Yes"
else:
    type1 = "No"

print("The Number is ", type1)