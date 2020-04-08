mylist = []
mylist.append(10)
mylist.append(20)
mylist.append(30)

print(mylist[0])

#for printing in loop
for x in mylist:
   print(x) 
   
#exercise
numbers = [] 
string = [] 
name = ["john","eric","jessi"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

string.append("hello")
string.append("world")

second_name = name[1] # index of second name is 1

for y in numbers:
   print(y)  # it displays one by one
print(numbers) # it displays value enclosed in bracket
print(string)
print("second name in name list is %s " %second_name)