class student:
    def __init__(self,*args):
        self.data=args
    def user(self):
        print(self.data)
        print("Name:",self.data[0])
        
    def details(self):
        print("Address:",self.data[0])
        print("College:",self.data[1])

s1=student(["rohit","dheeraj","satyarth"],"delhi","dtu")
s1.user()
s1.details()
