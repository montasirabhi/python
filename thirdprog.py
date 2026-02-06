# #============================ List & Tuple ===========================


# # List in Python 
# """
# A built-in data type that store set of values

# """

# mark1 = 95.5
# mark2 = 96.6
# mark3 = 69.5
# mark4 = 87.4
# mark5 = 42.3

# # We can short that by using list Like : 

# marks = [95.5, 96.6 , 69.5 , 87.4 , 42.3 ]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[2])


# # It can store elements of different types [integer , float , string etc. ] like : 

# student = ["Abhi" , 100 , "Pabna"]

# print(student)
# print(student[0])
# print(student[1])
# print(student[2])

# # string can not be changed , list can be changed 

# student[0] = "Montasir"

# print(student)

# # List slicing

# print(marks[1:3])


# #List Methods 

# list = [2,1,3]
# list2 = [2 , 1, 3]

# list.append(4) # To Add another element at the list 
# print(list) 

# list.sort() # To short in acending order like 1 , 2 , 3 , 4
# print(list)

# list.sort(reverse = True ) # To short in disacending order like 4 ,3 , 2 , 1
# print(list)

# list2.reverse() # The list in reverse 3 , 1 , 2
# print(list2)

# list.insert(1,5)  # Same as append but , it can insert the value in anywhere of the list ( 1 is the index , and 5 is the value )
# print(list)

# list.remove(5) # to remove the frist value of 5 (if there are multiple 5 in the list)
# print(list)

# list.pop(1) #to remove the value from index 1
# print(list)



# # ========================== Tuples =========================

# # Tuples can not be chaged like the list 

# tup = (100 , 90, 80, 70 , 60 , 80)  # list make with third braket , and tuple with frist bracket

# print(type(tup)) 

# # we can print the value of tuple 

# print(tup[0])

# # If you have only one value for tuple  list , you must add a comma after that , otherwise it will show as integer , string or float  . 
# tup1 = (1)
# print(tup1)
# print(type(tup1)) # Integer

# tup2 = (1,)
# print(tup2)
# print(type(tup2)) # Tuple

# # Tuple  Methods

# print(tup.index(90)) # To show , then the 90 come in the tuple for the frist time

# print(tup.count(80)) # To show how many time the 60 exsist on the tuple


# # Practice : 

# # Question 1 : Get movie names form user and store them in a list

# movie1 = input("First Movie Name")
# movie2 = input("Secound Movie Name")
# movie3 = input("Third Movie Name")

# list = [movie1 , movie2 , movie3]

# print(list)

# # Method 2 :


# movies = []
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# # Question 2 : Check the list is palindrome or not 

# list1 = [1,2,1]
# list2 = [1,2,3]
# list1_copy = list1.copy()
# list1_copy.reverse()

# list2_copy = list2.copy()
# list2_copy.reverse()

# if( list1 == list1_copy):
#     print("Yes")
# else:
#     print("No")

# if( list2 == list2_copy):
#     print("Yes")
# else:
#     print("No")



# Question 3: To Count in truple How much "A" on the truple

tup = ("a","d","f","a")

print(tup.count("a"))

# Question 4 : Sort A list from A To D 

list = ["C" , "B","A","D","C" , "B","A","D",]
list.sort()
print(list)