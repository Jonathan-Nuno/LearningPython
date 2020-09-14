# Classes and objects

# creating Car class (car Blueprint)
class Car:
    # initializer also known as constructor
    def __init__(self): 
        self.make = ""
        self.model = ""
        self.color = ""

car = Car() #car is an object of Car class
car.make = "Honda"
car.model = "Accord"
car.color = "Blue"

another_car = Car()
another_car.make = "Toyota"
another_car.model = "Camry"
another_car.color = "Black"

class Table:
    def __init__(self):
        self.width = None
        self.height = None
        self. material = ""

table = Table()
table.width = 150
table.height = 100
table.material = "wood"

table2 = Table()
table2.width = 250
table2.height = 175
table2.material = "plastic"

class BankAcc:
    def __init__(self, accType, initial_balance, account_number):
        self.accNum = account_number
        self.accType = accType
        self.balance = initial_balance
        self.is_business_account = False

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def transfer(self, destination_account, amount):
        self.withdraw(amount)
        destination_account.deposit(amount)


account_checking = BankAcc("checking", 100, "45678")
account_checking.deposit(10)


account_saving = BankAcc("savings", 500, "12345")
account_saving.withdraw(100)

account_checking.transfer(account_saving, 50)
print(account_checking.balance)
print(account_saving.balance)

# def upgrade_to_manager(em):
#     em.is_manager = True

# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.is_manager = False

# employee = Employee("John Doe")
# employees.append(employee)
# employee.name = "Mary Doe"

# print(employees[0].name)


# print(employee.is_manager)
# upgrade_to_manager(employee)
# print(employee.is_manager)