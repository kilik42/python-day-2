#while loops allow you to repeat code until a condition is met
#while loops are defined with the while keyword
#while loops are used when you don't know how many 
#times you need to repeat the code


from turtle import st


citlaliAge = 15
print("Citlali is", citlaliAge, "years old.")
praiseAge = 16
print("Praise is", praiseAge, "years old.")
aaronAge = 17
print("Aaron is", aaronAge, "years old.")
fionaAge = 18
print("Fiona is", fionaAge, "years old.")
xavierAge = 19
print("Xavier is", xavierAge, "years old.")

# studentList = ["Citlali", "Praise", "Aaron", "Fiona", "Xavier"]
# studentName = 0
# while studentName < len(studentList):
#     print(studentList[studentName])
#     studentName += 1

# fruitList = ["apple", "banana", "cherry", "date", "elderberry"]

# # for loop to print the fruitList
# # for loop is when you know how many times 
# # you need to repeat the code
# for fruit in fruitList:
#     print(fruit + " is a fruit.")

studentList = ["Citlali", "Praise", "Aaron", "Fiona", "Xavier"]

for student in studentList:
    ask  = input("What is your last name?")
    print(student + " " + ask)

