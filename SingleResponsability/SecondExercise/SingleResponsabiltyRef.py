class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"
        
    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
class PaymentProcessor:
    def pay(self, order: Order, payment_type: str, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

class CalculateProcesor:
    def total_price(self, order = Order):
        total = 0
        for quantity, price in zip(order.quantities, order.prices):
            total += quantity * price
        return total

   
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 2, 150)
order.add_item("USB cable", 2, 5)

#print(order.total_price())
payment_processor = PaymentProcessor()
payment_processor.pay(order, "debit", "0372846")
# Output:
# Processing debit payment type
# Verifying security code: 0372846  

total = CalculateProcesor()
print(total.total_price(order))
# Output: 400
# Explanation: 1*50 + 2*150 + 2*5 = 50 + 300 + 10 = 360