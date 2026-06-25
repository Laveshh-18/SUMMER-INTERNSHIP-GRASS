#List comprehensions {expression for item in literable}
print([i for i in range(10) if i % 2 == 0])


l=[10,20,30,40,50,60]
print([l[i] for i in range(len(l))])


k=[10,20,30,[40,50,60]]
print([k[i] for i in range(len(k))])