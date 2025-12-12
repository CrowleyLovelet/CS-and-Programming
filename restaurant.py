from abc import ABC, abstractmethod
from datetime import date

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_info(self):
        return f"{self.name} - ${self.price}"

class Menu:
    def __init__(self):
        self.items = []
    def add_item(self, item: MenuItem):
        self.items.append(item)
    def show_menu(self):
        print("\\\\\\Menu de Bibizianiks//////")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.get_info()}")
    def get_item(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

class Customer:
    def __init__(self, name, birthdate=None):
        self.name = name
        self.birthdate = birthdate

class Table:
    def __init__(self, number):
        self.number = number
        self.current_order = None
    def assign_order(self, order):
        self.current_order = order
        print(f"This order is for table {self.number}.")

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.waiters = []
        self.tables = []
    def add_waiter(self, waiter):
        self.waiters.append(waiter)
    def add_table(self, table):
        self.tables.append(table)
    def show_menu(self):
        self.menu.show_menu()

class Waiter:
    def __init__(self, name):
        self.name = name
    def take_order(self, customer: Customer, restaurant: Restaurant, table: Table):
        print(f"How do you do, {customer.name}! I am {self.name}. I will be your waiter today!")
        restaurant.show_menu()
        order = Order(customer)
        table.assign_order(order)
        while True:
            choice = input("Pick menu item from the list or type 'basta' to stop ordering: ")
            if choice.lower() == 'basta':
                break
            if not choice.isdigit():
                print("Do you know hom numbers look? Enter a number pls.")
                continue
            index = int(choice) - 1
            item = restaurant.menu.get_item(index)
            if item:
                order.add_item(item)
                print(f"{item.name} is in your order.")
            else:
                print("We dont have it here brother.")
        return order

class PricingThingy(ABC):
    @abstractmethod
    def calculate_total(self, order):
        pass

class StandardPricing(PricingThingy):
    def calculate_total(self, order):
        return sum(item.price for item in order.items)

class BirthdayBonusPricing(PricingThingy):
    def calculate_total(self, order):
        total = sum(item.price for item in order.items)
        customer = order.customer
        if customer.birthdate:
            today = date.today()
            if customer.birthdate.day == today.day and customer.birthdate.month == today.month:
                print("Happy birthday! 20% discount.")
                total *= 0.8
        return total

class Order:
    def __init__(self, customer: Customer, pricing_thingy: PricingThingy = None):
        self.customer = customer
        self.items = []
        self.pricing_thingy = pricing_thingy or StandardPricing()

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self):
        return self.pricing_thingy.calculate_total(self)

    def set_pricing_thingy(self, pricing_thingy: PricingThingy):
        self.pricing_thingy = pricing_thingy

class Payment:
    def __init__(self, order: Order):
        self.order = order

    def pay_cash(self):
        total = self.order.calculate_total()
        print(f"Wow you are rich!!! ${total:.2f} in cash.")

    def pay_card(self):
        total = self.order.calculate_total()
        print(f"Wow you have a card!!! ${total:.2f} by card.")

class Receipt:
    def __init__(self, order: Order, table: Table):
        self.order = order
        self.table = table

    def print_receipt(self):
        print(f" receipt for table {self.table.number}")
        print(f"receipt for customer: {self.order.customer.name}")
        for item in self.order.items:
            print(f"- {item.name}: ${item.price}")
        total = self.order.calculate_total()
        print(f"Total: ${total:.2f}")

# -----ahhhhhh---ohhhh---simulation------
restaurant = Restaurant("Bibizianiks")

restaurant.menu.add_item(MenuItem("Sushi", 20))

restaurant.menu.add_item(MenuItem("Donates", 5))

restaurant.menu.add_item(MenuItem("Coke", 5))

restaurant.menu.add_item(MenuItem("Lemonade", 10))

restaurant.add_table(Table(1))

restaurant.add_table(Table(2))

waiter = Waiter("Bobik")

restaurant.add_waiter(waiter)

customer = Customer("Zuchara", birthdate=date(1888, 8, 8))

table = restaurant.tables[0]

order = waiter.take_order(customer, restaurant, table)

bonus = input("Any chance it's your birthday today? (yes/no/y/n): ").strip().lower()

if bonus in ("yes", "y"):
    order.set_pricing_thingy(BirthdayBonusPricing())
    
payment_method = input("Would it be cash or card? : ").strip().lower()

payment = Payment(order)

if payment_method == "cash":
    payment.pay_cash()
else:
    payment.pay_card()

receipt = Receipt(order, table)

receipt.print_receipt()
