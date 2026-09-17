# ALL THE MAIN CALCULATOR FUNCTIONS. 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
     return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def getChoice(choice):
    while True:
        try:
            return float(input(choice))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# MAIN CLASS WHERE THE CALCULATOR PROGRAM IS EXECUTED.
class main:
    print("Welcome to the Calculator!")
    print("Choose an operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    try:    
        choice = int(input("Enter a choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    a = getChoice("Enter the first number: ")
    b = getChoice("Enter the second number: ")

    match choice:
        case 1:
            result = add(a, b)
        case 2:
            result = subtract(a, b)
        case 3:
            result = multiply(a, b)
        case 4:
            result = divide(a, b)

    print(f"The result is: {result}.")