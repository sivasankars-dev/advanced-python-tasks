# Task 1: Bank Account System (Encapsulation + Class Design)
# Requirements:
# Create a BankAccount class with:
# Private attributes: account_number, balance
# Methods: deposit(), withdraw(), get_balance()
# Ensure balance cannot go negative.
# Stretch Goal: Add a TransactionHistory class to store the last 5 transactions.
from collections import deque

class TransactionHistory:
    def __init__(self):
        self.transactions = deque(maxlen=5)
        
    def add(self, entry):
        self.transactions.append(entry)
    
    def showTransactions(self):
        if self.transactions:
            print()
            print("Transaction History: ")
            for i, txn in enumerate(self.transactions, 1):
                print(f"{i}. {txn}")
        else:
            print("No Tranasactions Avaiable")

class BankAccount(TransactionHistory):
    def __init__(self, acNum):
        super().__init__()
        self.__acNum = acNum
        self.__balance = 0
        self.__pin = 1234

    def deposit(self, amt):
        if amt <= 0:
            print(f"deposit amount must be possible")
            return
            
        self.__balance += amt
        res = f"{amt} credited to your account. You have remaining balance {self.__balance}"
        self.add(f"Credited {amt}")
        print(res)
    
    def withdraw(self, amt):
        if amt <= 0:
            print("Withdrawal amount must be positive")
            return;
            
        if self.__balance >= amt:
            self.__balance -= amt
            res = f"{amt} debited from your account. Your remaining balance is {self.__balance}"
            self.add(f"Debited {amt}")
            print(res)
        else:
            print("You don't have balance in your account")
            
    def getBalance(self, pinNo):
        if self.__pin == pinNo:
            print(f"Your Current balance is {self.__balance}")
        else:
            print(f"please enter the right pin number")
        
    def changeYourPin(self, existingPin, changePin):
        if len(str(existingPin)) == 4 and str(changePin).isdigit():
            if self.__pin == existingPin:
                self.__pin = int(changePin)
                print(f"Your pin changed successfully")
            else:
                print(f"{existingPin} incorrect pin")
        else:
            print(f"Check your pin number")
    
    def __str__(self):
        return f"Account Number: *****{str(self.__acNum)[-4:]}, balance: {self.__balance}"
        
siva = BankAccount(123456789)
siva.deposit(5000)
siva.deposit(3000)
siva.deposit(500)
siva.withdraw(1500)
siva.getBalance(1235)
siva.changeYourPin(1234, '7709')
siva.getBalance(7708)
siva.showTransactions()
siva.withdraw(150)
siva.deposit(300)
siva.showTransactions()

print(siva)
