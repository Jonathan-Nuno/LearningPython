#def greet():
   # print(f"Hello {my_name}!")

#greet("Mary")

#my_name = input("Enter your name: ")
#print(my_name)

#greet()

#adding two numbers
#first_number = input ("Enter first numer: ")
#second_number = input ("Enter second number: ")

#results = int(first_number) + int(second_number)
#print(results)

#Activity: ask user for 2 $ amounts, then add them and print them out on the screen
fda = input ("What is the Dollar amount? $ ")
sda = input ("What is the next Dollar amount? $ ")

total = float(fda) + float(sda)

print(f"Your total is ${total}")

def calculate_tip(total, percentage):
    return total * (percentage/100)

tip = calculate_tip(total, 15)

if tip >= 10:
    print("YOU ARE VERY GENEROUS")
elif tip < 10 and tip >= 5:
    print("THANK YOU")
else: 
    print("YOU ARE A BAD TIPPER!")

print(tip)

## Conditions
