class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.greet()
person2.greet()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Deposited {amount} into account. New balance: {self.balance}")
        else:
            print("Account is not active")
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} from account. New balance: {self.balance}")
    def deactivate_account(self):
        self.is_active = False
        print("Account deactivated")
    def activate_account(self):
        self.is_active = True
        print("Account activated")

account1 = BankAccount("Alice", 100)
account1.deposit(50)
account1.withdraw(30)
account1.deactivate_account()
account1.activate_account()
