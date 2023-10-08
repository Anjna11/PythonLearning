class Item:

    Brand = "apple"
    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.quntity = q

    def total_price(self):
        return self.price * self.quntity
    
    def fun(self):
        print("Name of Item: ", self.name)
        print("Price of Item: ", self.price)
        print("Price of Item: ", self.quntity)
    
i1 = Item("Phone", 100, 5)
i2 = Item("Laqptop", 1000, 4)
i1.fun()
i2.fun()