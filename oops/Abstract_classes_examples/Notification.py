# Scenario:
# You’re building a notification system that can send different types of messages: Email, SMS, and Push.
# ✅ Requirements:
# Create an abstract class Notifier with an abstract method send(message).
# Implement three subclasses:
# EmailNotifier
# SMSNotifier
# PushNotifier
# Each should print how it sends the message (e.g., "Sending Email: Your OTP is 1234").

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, data):
        pass
    
class EmailNotifier(Notifier):
    def send(self, data):
        print(f"Email Notification: Your OTP is {data}")
    
class SMSNotifier(Notifier):
    def send(self, data):
        print(f"SMS Notification: Your OTP is {data}")
        
class PushNotifier(Notifier):
    def send(self, data):
        print(f"Push Notification: Your OTP is {data}")
        
email = EmailNotifier()
sms = SMSNotifier()
push = PushNotifier()

email.send('1234')
sms.send('1234')
push.send('1234')