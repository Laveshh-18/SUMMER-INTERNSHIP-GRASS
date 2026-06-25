#list:- what is list in python
#list is a collection of items which are ordered and changeable. it allows duplicate members.
#list is defined by using square brackets [] and items are separated by commas.
mylist = ["apple","banana","cherry"]
print(mylist)
mylist1 = [1,2,3,4,5]   
print(mylist1)
mylist2 = [1,"hello",3.14,True]
print(mylist2)      
print(len(mylist))
print(len(mylist1))
print(len(mylist2))
inserted_list = mylist + mylist1
print(inserted_list)
#append() method is used to add an item to the end of the list.
mylist.append("orange")
print(mylist)
mylist1.append(6)
print(mylist1)

l=[10,20,30,40,50,6,"hello","True"]
print(l)
l.append("for arya mains")
print(l)
print(l[-1])


ll=[True,False,10,20]
ll.insert(1,100)
print(ll)


#question:-
l1=[10,20,30,{"name":"khushbu","address":["jaipur","kukas","bassi","chomu"]}]
print(l1)
for i in l1:
    print(i)
print(l1[3])
print(l1[3]["name"])
print(l1[3]["address"])
for i in l1[3]["address"]:
    print(i)






#question:-
a=[10,20,30,[40,50,[60,70,80]]]
for i in a:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    print(k)
            else:
                print(j)
    else:
        print(i)
#print(a)
#print(a[3])
#print(a[3][2])
#print(a[3][2][1])
#print(a[3][2][0])
#print(a[0])
#print(a[1])
#print(a[2])
#print(a[3][0])
#print(a[3][1])
#print(a[3][2][0])
#print(a[3][2][1])
#print(a[3][2][2])

