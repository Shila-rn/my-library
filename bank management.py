class Customer:
    def __init__(self, name, phone_number, code):
        self.name= name 
        self.phone_number= phone_number
        self.code= code
    
    def __str__(self):
        return f"customer {self.name} by {self.phone_number} and by national code {self.code}"

class Bank:
    def __init__(self):
        self.customers= []

    def registration (self, person):
        self.customers.append(person)
        print(f"{person} opened an account")

    def remove(self, name):
        for person in self.customers:
            if person.name== name:
                self.customers.remove(person)
                print(f"customer{customer.name} was removed")
    
    def display(self):
        if self.customers:
            print("our customers:")
            for person in self.customers:
                print(person)
        else:
            print("no customer")

class Account:
    def __init__(self, account_number, account_balance):
        self.account_number= account_number
        self.account_balance= account_balance
 
    def deposit(self, amount):
        self.account_balance += amount
        print(f"amount{amount} was deposited to your bank account. account balance: {self.account_balance}")

    def withdrawal(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"amount{amount} was deducted from your account. account balance: {self.account_balance}")
        else:
            print("not enough balance")

    def checking_balance(self):
        print(f"your account balance is: {self.account_balance}")

    def __str__(self):
        return f"account number: {self.account_number} , account balance: {self.account_balance}"


bank= Bank()
person1= Customer("Saba Moradpour", "09307300335","123456")
person2= Customer("Asal Khaleghi","091754263","123456")
person3=Customer("Alireza Ebadi","091355886","123456789")
person4=Customer("Nazanin Raoof","0974153335","123654")
person5=Customer("Alireza Porrangi","09451667554", "08846231")


bank.registration(person1)
bank.registration(person2)
bank.registration(person3)
bank.registration(person4)
bank.registration(person5) 
bank.display()
print("----------------------------------")
account= Account("13556332166", 123000000)
print(account)
print("----------------------------------")
account.deposit(50000)
account.checking_balance()
print("------------------------------")
account.withdrawal(200000000000000000)
account.checking_balance()
print("---------------------------------")
account.withdrawal(100000)
account.checking_balance()