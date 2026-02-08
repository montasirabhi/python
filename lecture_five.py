# #=========================== Loop ===========================

# # Loops are use to repeat instructions

# # While Loop 
# count = 1 

# while count <= 5 :
#     print("hello")
#     count += 1

# print(count)

# i = 1 

# while i <= 50 :
#     print("Abhi" , i)
#     i += 1

# print(i)

# # To Print numbers from 1 to 50 

# i = 1

# while i <= 50 :
#     print(i)
#     i+= 1

# print("Loop Ended")

# # To Print numbers from 50 to 1

# i = 50

# while i >= 1 :
#     print(i)
#     i-= 1

# print("Loop Ended")


# # Practices : 

# # Question 1 : Print Numbers form 1 to 100

# i = 1

# while i <= 100 : 
#     print(i)
#     i +=1



# # Question 2 : Print Numbers form 100 to 1

# i = 100

# while i >= 1 : 
#     print(i)
#     i -=1



# #Question 3 : Print the multiplication of a number n

# n = int(input("Enter A Number"))
# i = 1
# while i <= 10 :
#     print(n*i)
#     i +=1


# # Question 4 : Print The Elements of the following list using a loop : 

# # 1 ,4,9,16,25,36,49,64,81,100 

# i = 1

# while i<=10 :
#     print(i*i)
#     i += 1


# # ============ Or ============

# nums = [1 ,4,9,16,25,36,49,64,81,100 ]

# idx = 0

# while idx < len(nums) :
#     print(nums[idx])
#     idx += 1





# Question 5 : Search for a number X in this tuple using loop : 

# 1 ,4,9,16,25,36,49,64,81,100 

nums = (1 ,4,9,16,25,36,49,64,81,100)
x = 36
i = 0

while i < len(nums) :
    
    if(nums[i] == x) :
        print("Found At Index", i)
    else :
        print("Founding ....")
    i += 1