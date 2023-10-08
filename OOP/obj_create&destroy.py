class demo:
    def __init__(self):
        print("Object Gets Created!")

    def __del__(self):
        print("Object Gets Destroyed!")

a = demo()
del a