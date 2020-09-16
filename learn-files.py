
# FILES
# File modes
# w - writing to a file
# r - reading from a file
# a - appending to an existing file
# w+ - opening writing and readting
# other + modes


# Option 1 - Manially close the file after writing
# file = open("todo.txt", "w") # open file for riting
# file.write("Task 1 name ")
# file.close() # always close the file so file resources can be released or else it can cause problems 

# writing file using with open approach
# with open("todo.txt", "w") as file_object:
#     file_object.write("Feed the dog")

# appending to and existing file
# with open("todo.txt", "a") as file_object:
#     file_object.write("Mow the lawn \n")
#     file_object.write("Feed the dog \n")

# Activity 1: Ask user for input for their favorite dish and write the name of the dish in the file

# def addTxt(txt):
#     with open ("todo.txt" , "a") as file_object:
#         file_object.write(txt + "\n")

# while True:
        
#     text_input = input("Please enter todo item or q to quit: ")
#     if text_input == "q":
#         print("todo list closed")
#         break

#     addTxt(text_input)


# by default if you don't pass the mode then the default mode is "r" (reading)
# file = open("todo.txt") # open returns an object of type File (class)


# READING FROM A FILE

#read all the contents of the file and return as a string
# with open("hello.txt") as file_object:
#     content = file_object.read()

# print(content)

# # read lines from a file and returning each line as an item in the array
# with open("todo.txt") as file_object:
#     lines = file_object.readlines()

# print(lines)

# Activity 2: You will read our favorite dishes file and display them on the screen

# with open("todo.txt") as file_object:
#     content = file_object.read()
#     print(content)

def remover(dupe):
    return list(dict.fromkeys(dupe))

with open("emails.txt") as file_object:
    content = file_object.read()

duplicate = content.split(",")
emails = []

for email in duplicate:
    email = email.strip() #to remove \n
    if email not in emails:
        emails.append(email)

a = ["a", "b", "c"]

result = ",".join(emails)

with open("duplicate_free_emails.txt", "w") as file_object:
    file_object.writelines(result)
