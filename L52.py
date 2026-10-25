#Abstract Class and Abstraction Method in Python
from abc import ABC, abstractclassmethod

class A(ABC):

    @abstractclassmethod
    def show(self):
        pass

# obj1 = A()
# obj1.show()

class PaymentGateway(ABC):
    @abstractclassmethod
    def pay(self):
        pass

class TeluskoPay(PaymentGateway):
    def pay(self):
        print("Paying using TeluskoPay")

class RazorPay(PaymentGateway):
    def pay(self):
        print("Paying using RazorPay")

class Purchase:

    def __init__(self, gateway ):
        self.gateway = gateway

    def checkout(self):
        print("checking out..")

        self.gateway.pay()

gateway1 = RazorPay()
gateway2 = TeluskoPay()
purchase = Purchase(gateway2)

purchase.checkout()

print("Homework")
# HomeWork
class PaymentGateway(ABC):
    @abstractclassmethod
    def pay(self):
        pass

class CardPay(PaymentGateway):
    def pay(self):
        print("Paid using Card")

class UpiPay(PaymentGateway):
    def pay(self):
        print("Paid using UPI")

class Purchase:
    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("Checkout Started")
        self.gateway.pay()

p1 = Purchase(CardPay())
p2 = Purchase(UpiPay())

p1.checkout()
p2.checkout()