# 📝 Scenario:
# You're building a system where users can pay using different payment methods — such as Credit Card, UPI, or PayPal.
# Each payment type processes transactions differently, but all must follow the same interface.
# ✅ Requirements:
# Create an abstract class PaymentMethod with:
# An abstract method process_payment(amount: float)
# Implement three subclasses:
# CreditCardPayment
# UPIPayment
# PayPalPayment
# Each subclass should:
# Override process_payment()
# Print a message showing:
# Payment method name
# Amount
# A message like "Payment successful"
# Create a function make_payment(payment_method: PaymentMethod, amount: float)
# It should call process_payment() on the given method.

# Bonus Challenge (Optional):
# Add another abstract method in PaymentMethod:
# Subclasses should implement custom validation logic (e.g., card number check, UPI ID format).
# In make_payment(), call validate() before process_payment().

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass
    
    @abstractmethod
    def validate(self, validateSource):
        pass

    def validate_and_pay(self, pin, amt):
        valid = self.validate(pin)
        if valid:
            self.process_payment(amt)
        else:
            print("Not validate")

class UPIPayment(PaymentMethod):
    def validate(self, validateSource):
        # Should have bank source at end of the upi id(just for sake)
        if "@icici" in validateSource:
            return True
        else:
            return False
        
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount}... Payment Successful.")

class CreditCardPayment(PaymentMethod):
    def validate(self, validateSource):
        # Should have 12 digit card number from the credit card(just for sake)
        if len(validateSource) == 12:
            return True
        else: 
            return False
        
    def process_payment(self, amount):
        print(f"Processing Credit card payment of ${amount}... Payment Successful.")

class PaypalPayment(PaymentMethod):
    def validate(self, validateSource):
        # Should have 12 digit card number from the credit card(just for sake)
        if len(validateSource) == 12:
            return True
        else: 
            return False
    
    def process_payment(self, amount):
        print(f"Processing Paypal payment of ${amount}... Payment Successful.")

def make_payment(paymentMethod: PaymentMethod, pin, amt: float):
    paymentMethod.validate_and_pay(pin, amt)

make_payment(UPIPayment(), "siva@icici", 100.00)
make_payment(CreditCardPayment(), "873873783783", 300.00)
make_payment(PaypalPayment(), "38787383738", 500.50) # Not have 12 digits