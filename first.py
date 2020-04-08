print("this line will be printed.")

#integer declaration
intval = 7 
print(intval) 


#float (float declaration can be done in twoways)
floatval = 7.0
floatval = float(7)
print(floatval)


#String declaration either in sigle quote or double quote
mystring = 'hello' # here apostrophe cannot be typed
mystring = "hello World" 
print(mystring)



#int operations
val1 = 2 
val2 = 3
val3 = float(2.0)
tot = val1 + val2 + val3 
print(tot)



#String combine
str1 = "hello"
str2 = "world"
str = str1 + " " + str2 
print(str) 


#multiple declaration at the same line
a , b , c = 4 , 5 ,6 
print(a,b,c)


#mixing operation between number nd string cannot be done
str1 = "hello"
val1 = 2 
print(str1 + val1)


#exercise
finalstr = "hello"
finalfloat = float(7)
finalint = 5

if finalstr == "hello" :
   print("String: %s" %finalstr) 
   
if isinstance(finalfloat,float) and finalfloat == 7.0:
   print("Float: %f" %finalfloat)
   
if isinstance(finalint,int) and finalint == 5:
    print("Int: %d" %finalint)
