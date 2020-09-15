
## Exceptions

#activity 1 - handle exception for the wrong input converting to int
try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    result = first_number/second_number

except ZeroDivisionError:
    print("Don't divide by Zero")
except ValueError:
    print("Invalid input, please only enter numbers")
except:
    print("Opps something bad happened")
#fired when no exception has happened
else: # this block is optional
    print("No exceptions were fired")
finally: # optional block: finally is fired when exceptions happens and also when it does not happen
    print("Finally block executed...")