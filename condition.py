x = 3
print( x == 3 )
print(x < 3)
print(x > 3)


name = "mike" 
age = 13

#AND
"""if name == "mike" and age == 13:
      print("Your name is %s,%d year old", %(name,age))
	"""  
#OR
if name == "mike" or name == "rick":
   print("Your name is mike or rick")
   
   
final = 5 #vairiable declaration

if final == 4 :
     final = final+1 
     pass
elif final == 5 :
     final = final+5 
     pass
else :
     final = final-1
	
print(final)

#exercise
number = 17
second_number = 10
first_array = [4,5,6]
second_array = [1,2]

if number > 15:
    print("1")

if first_array: #doubt
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")
