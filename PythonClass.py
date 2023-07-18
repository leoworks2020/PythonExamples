class Product:

    def __init__(self, name, price, quantity):
        # instance variable
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def increaseQuantity(self, amount):
        self.quantity += amount

    def decreaseQuantity(self, amount):
        if (self.quantity < amount):
            print("Not enough " + self.name + " in stock")
        else:
            self.quantity -= amount

    def toString(self):
        return self.name + ": $" + str(self.price) + " (" + str(self.quantity) + ")"

bread = Product("Bread", 2.99, 10)
milk = Product("Milk", 3.99, 5)

# display initial state of the products
print("Initial state of the products:")
print(bread.toString())
print(milk.toString())

# sell some bread and milk
bread.decreaseQuantity(3)
milk.decreaseQuantity(2)

# display updated state of the products
print("State of the products after selling some:")
print(bread.toString())
print(milk.toString())

# add more bread and milk to the inventory
bread.increaseQuantity(5)
milk.increaseQuantity(3)

# display final state of the products
print("Final state of the products:")
print(bread.toString())
print(milk.toString())