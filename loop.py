#loops and functions

# For loops 
primes = [2,3,5,7]
for prime in primes:
  print(prime)
  
  
for x in range(5) :
  print(x)
  
for x in range(4,8) :
   print(x)

for y in range(1,9,2) :
   print(y)
   
#While loops
i = 0 
while i < 5:
     i=i+1
     print(i)

"""	 
#break and continue
for x in range(10):
     if x % 2 != 0:
	      continue
	 if x == 10:
	      break 
	 print(x)
	""" 
#functions

def func_noargs():
   print("Hi There!")
   
def func_withargs(name,greet):
   print("Hello !, %s, I Wish you happy %s" %(name,greet))
   
def func_returnval(a,b):
      return a + b 

func_noargs() 

func_withargs("folks","New year!")

x = func_returnval(3,2)
print(x)



















