class Item:

    Brand = "apple"

    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.quntity = q

a = Item("Laptop", 100, 4)
print(a.name)
print(a.Brand)
print(Item.Brand)