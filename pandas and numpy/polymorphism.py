#polymorphism in python
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
    def location(self):
        print(f"My address is {self.city}, {self.state}")


class homeTown:
    def __init__(self, city, state):
        self.city = city
        self.state = state
    def location(self):
        print(f"My hometown location is {self.city}, {self.state}")
a=Address("Bangalore", "Karnataka")
a.location()

b=homeTown("Mysore", "Karnataka")       
b.location()