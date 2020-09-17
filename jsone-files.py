
import json


users = []

#READ THE FILE
# with open("users.json") as file_object:
#     users = json.load(file_object)

# print(users)

while True:
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    user = {"name" : name, "age" : age}
    users.append(user)
# Create a simple dictionary to represent a user
# user_dictionary = {"name" : "John Doe", "age" : 45}

# write the dictionary to json file
    with open("users.json", "w") as file_object:
        #json.dump(DataYouWantToWriteToJson, FileObjecToUse)
        json.dump(users, file_object)

    choice = input("Any key to continue or q to quit: ")
    if choice == "q":
        break