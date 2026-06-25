#inheritance
class Address:
    def __init__(self, city, state):
        self.city = city #attribute
        self.state = state #attribute
    def location(self):
        return f"My location is {self.city} in {self.state}"
    

a=Address("jaipur", "rajasthan")


class User(Address):
    def __init__(self,name,age,city,state):
        self.name=name
        self.age=age
        #self.city=city
        #self.state=state

    def userName(self):
        print(f"My name is {self.name} and I am {self.age} years old")
    def __userDetails(self):
        return f"My location is {self.city} in {self.state}"

u=User("khushbu",22,"jaipur","rajasthan")

u.userName()
u._User__userDetails()
u.location()
