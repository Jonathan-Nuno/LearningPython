
#def create_pizza(size, *toppings):
#    print(f"The pizza {size}")
#    
#    for topping in toppings:
#        print(topping)

#size = input("Enter size for pizza: ")
#toppings = input("Enter toppings: ")

  # for index in range(o. len(toppings)):
    #   print(toppings[index])
 
 # array as toppings
 #create_pizza(16, ["Mushroom", "Onion", "Chicken"])

#create_pizza(16, "Mushroom", "Onion", "Chicken")
#create_pizza(14, "Mushroom", "Pineapple", "Hot Peppers", "Onion")

### Activity 1 - Creting a Dictionary

#first_name = input("Enter first name: ")
#last_name = input("Enter last name: ")

#names = {"firstName": first_name, "lastName": last_name}

#print(f'My name is {names["firstName"]} {names["lastName"]}')

### Deleting from a dictionary
#car = {"model": "Accord", "make": "Honda", "Electric": False}

#del car["Electric"]
#print(car)

### Creating nested dictionaries

#customer = {"firstName" : "John", "lastName" : "Doe"}
#address = {"street" : "1200 Richmond", "state" : "TX", "zipcode" : "44567"}

#customer["address"] = address

#print(customer)

### Activity 2 - Nested Dictionaries - multiple addresses

user = {"firstName" : "John", "lastName" : "Doe"}
address1 = {"street" : "1200 Richmond", "state" : "TX", "city" : "Houston"}
address2 = {"street" : "123 Darwin", "state" : "TX", "city" : "Houston"}

user["addresses"] = [address1, address2]

print(user)

#creating a person object and assigning the addresses at the same time
#person = {"firstName" : "John", "lastName": #"Doe", "address" : [
#    {"street" : "1200 Richmond"},
#    {"street" : "123 Darwin"},
#] } 
#print(person)


# Twitter
# Username
# Tweet date
# Profile_pic
# like
# rts
# noOfComments

#tweet = {"username" : "Johndoe", "tweet_date" : "09/11/2020", "profile_pic" : "someurl.png", "likes" : 10, "rts" : 2, "no_of_comments" : 10}

#tweet2 = {"username" : "Johndoe", "tweet_date" : "09/11/2020", "profile_pic" : "someurl.png", "likes" : 10, "rts" : 2, "no_of_comments" : 10}

#tweet3 = {"username" : "Johndoe", "tweet_date" : "09/11/2020", "profile_pic" : "someurl.png", "likes" : 10, "rts" : 2, "no_of_comments" : 10}

#tweets = [tweet, tweet2, tweet3]