# #========================== Dictonary & Sets =============================

# # Dictonaries are used to store data values in key:value paris
# # They are unodered , mutable( changeable ) & don't allow duplicate keys


# info = {
#     "key" : "value",
#     "name" : "Montasir Rahman Abhi",
#     "learning" : "Python",
#     "age" : 22,
#     "is_audult" : True,
#     "marks" : 95.5
# }

# # Dictonaries Also can contains List and Tuples 

# dic  = {
#     "name" : "Montasir Rahman Abhi",
#     "subjects" : ["python","C","Java"],
#     "topics" : ("dictonaries","Sets"),
#     "age" : 24
    
# }
# print(dic)
# print(info)
# print(type(dic))


# # Access in dict

# print(info["name"]) 

# # Change Value 

# info["age"] = "22"

# print(info["age"]) 

# # Add Value
# info["date_of_birth"] = "26 August 2004"
# print(info)



# #We Can Create  A Empty Dictonary 

# null_dic = {}

# null_dic["name"] = "Name of Mine"

# print(null_dic)


# # Multiple Value in one key ( Nested Dictonary)

student = {
    "name" : "Montasir" ,
    "subjects" : {
        "physic" : 97,
        "chem" : 98, 
        "math" : 95
    }
}
# print(student)

# # To show one value from the nested dictonary 
# print(student["subjects"]["chem"])

# # To Add Key in Nested dictonary 

# student["subjects"]["date_of_birth"] = "26 August 2004"

# print(student["subjects"])


# # ========================= Dictonary Methods ===================

# # To show all the keys ( Not Nested )

# print(student.keys())

# # To Convert the dic to list

# print(list(student.keys()))
# print(len(student))  # Length 



# # To show all the values 

# print(student.values())
# print(list(student.values()))

# # To show all in tuples 

# print(student.items())

# # To convert in list 
# print(list(student.items()))


# # To return key according to the value 

# print(student.get("name"))

# # Insert the specified items to dictonary 

# student.update({"city" : "Pabna"})

# print(student)




# # ================== Set in Python =================

# #  Set is the collection of the unordered items
# # Each element in the set must be unique & immutable 

# collection = { 1,2,3,4,5,"hello","world"}

# print(collection)
# print(type(collection))

# # Set ignores the duplicate values . 

# collection = { 1,2,3,3,3,4,"hello","world","world"}

# print(collection)
# print(len(collection)) # length will also ingnore duplicate items

# # Empty Set 

# collection = set()

# print(type(collection))

# # ======== Methods in set ===========

# # To add an element ( Note : Sets are mutable but the elements are immutable )

# collection.add(10)
# collection.add(20)
# print(collection)

# # To remove 
# collection.remove(20)
# print(collection)


# # To clear the set 

# collection.clear()
# print(collection)

# # To print a random element from the set 


# collection1 = { 1,2,3,3,3,4,"hello","world","world"}
# print(collection1.pop())

# set1 = {1,2,3}
# set2 = {3,4,5}

# # Combine set values & returns new ( Union )

# print(set1.union(set2))

# # Intersection ( combine common values & returns new )

# print(set1.intersection(set2))



# Practice 

dic = {
    "table" : ["a piece of furniture" , "list of facts & figures"],
    "cat" : "a small animal"
}
print(dic)

# Q2 

set1 = {"python" , "java" , "C++", "python","javascript"}
set2 = {"java ", "python" ,"java" , "C++","C" }

set3 = set.union(set2)

print(len(set3))

#Q3

dictonary = {}

subject1 = input("Enter the mark of Sub1")
subject2 = input("Enter the mark of Sub2")
subject3 = input("Enter the mark of Sub3")

subject11 = input("Enter the name of Sub1 Name")
subject12 = input("Enter the name of Sub2 Name ")
subject13 = input("Enter the name of Sub3 Name ")

dictonary[subject11] = subject1
dictonary[subject12] = subject2
dictonary[subject13] = subject3


print(dictonary)

# Q4 
values = {
    ("float" , 9.0),
    ("int",9)
}
print(values)
