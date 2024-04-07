# #order of execution
# # in python

print("Hello World")
# #stings are surrounded by quotes 
# #single or double quotes '' or ""
# #be consitent with the quotes you use
print("order of execution")

print("in python")
print("*"*20)

# #variables are used to store data
# #variables are created when you assign a value to it
# #variables are case sensitive
# price = 10 #integer variable
# name = "John" #string variable
# rating = 4.9 #float variable
# is_published = True #boolean variable
# #start all variables with a lower case letter or underscore
# #use underscores to separate words
# # use camel case if you want to start with a capital letter
# # on the next word
# playerBulls = "michael jordan"

# #Concatentation to join variables in a sentence
# print(name + " is a basketball player")
# print(name + "has a rating of " + str(rating))
# #use the str() function to convert a number to a string
# #the plus (+) sign is used to concatenate strings
# print("the price of the book is " + str(price))

# #getting input from the user
name = input("What is your name? ")
age = input("What is your age? ")
# age = 35
print("Hello " + name + " you are " + age + " years old")

#ask two questions from the user
#person's name and favorite color
#then print a message like "Moses likes blue"
#use your variables in the final message 
personName = input("What is your name? ")
favoriteColor = input("What is your favorite color? ")
print(personName + " likes " + favoriteColor)