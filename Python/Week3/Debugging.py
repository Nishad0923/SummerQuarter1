# Prints the age of the user
def PrintName():
    age = 30
    print("Age:" + str(age))         

# Add 2 numbers together
def Add(num1, num2):
    return num1 + num2
     
# Ask the user their name and say hello to them
def SayHello():
    name = Input("What is your name?")
    print("Hello ", name)

PrintName()
print(Add(5,5)) 
SayHello()