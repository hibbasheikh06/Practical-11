def greet(name):
   print(f"Hello,{name}!")
greet("Hiba")

def my_function():
    global x
    x=10 #local variable

my_function() #output: 10
print(x)