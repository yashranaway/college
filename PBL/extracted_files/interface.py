# Interface
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

    def refund_payment(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")


# Implement the interface
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of Rs {amount}")

    def refund_payment(self, amount):
        print(f"Refunding credit card payment of Rs {amount}")


class PhonePeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PhonePe payment of Rs {amount}")

    def refund_payment(self, amount):
        print(f"Refunding PhonePe payment of Rs {amount}")


# Class that uses the payment processor
class Order:
    def __init__(self, processor: PaymentProcessor, amount):
        self.processor = processor
        self.amount = amount

    def pay(self):
        self.processor.process_payment(self.amount)

    def refund(self):
        self.processor.refund_payment(self.amount)


# Using the classes
credit_card = CreditCardProcessor()
phonepe = PhonePeProcessor()

order1 = Order(credit_card, 1000)
order2 = Order(phonepe, 500)

order1.pay()
order2.pay()

order1.refund()
order2.refund()

# This will raise a NotImplementedError if we try to use it
# payment_processor = PaymentProcessor()
# payment_processor.process_payment(1000)
