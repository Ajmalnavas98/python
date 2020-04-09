class MyClass:
    variable = "blah"

    def func(self): # python doesnt use @ syntax to refer to instance attribute 
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)
myobjectx.func() 