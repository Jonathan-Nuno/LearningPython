
### for index in range (start, end, # to incriment/dicrement)

### Activity 1 - Create a list of friends and loop through them and print them on the terminal

#friends = ["Alex", "Steve", "John", "Harry", "Jack", "Bryan", "Mary"]
### "len(friends)" give you the number in the array
#for index in range (0, len(friends), 2):
#    print(friends[index])

### Activity 2 - Print the array in reverse order
### by adding a -1 after "len(friends)" gives you the number in the array minus 1
#friends = ["Alex", "Steve", "John", "Harry", "Jack", "Bryan", "Mary"]

#for index in range (len(friends) -1, -1, -1):
#    print(friends[index])

#animals = []

### append items to the array using "X".append("Y")
#animals.append("cat")
#animals.append("dog")
#animals.append("bird")

#print(animals)

### remove item from the array using "X".remove("Y")
#animals.remove("cat")

### remove item from array using index "del x[#]"
#del animals[2]

### insert item at a specific location using x.inser(point in array, "Y")
#animals.insert(0,"fish")

### Activity 3 - Write a python app which will ask name of the user and then add the name to the array and pring out the array

#names = []
#for i in range(0,3):
#    name = input("Enter name: ")
    ### add name to the array
#    names.append(name)
### VarName.append(InputVarName)    
#print(names)


#While loop

while True:
    name = input("Enter name or press Q to quit: ")
    if name == "q" or name == "Q":
        break

