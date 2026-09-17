# BAD CODE: Violates KISS, DRY, and YAGNI

# 1. VIOLATES YAGNI: Including unnecessary functions that were never requested
def calculate_loan_interest(principal, rate, time):
    return principal * (rate / 100) * time

def fetch_weather_data(zipcode):
    return f"Weather for {zipcode}: Sunny"

# 2. VIOLATES KISS: Over-engineering simple math operations using classes and inheritance
class CalculatorBase:
    def execute(self, a, b):
        pass

class Addition(CalculatorBase):
    def execute(self, a, b):
        return a + b

class Subtraction(CalculatorBase):
    def execute(self, a, b):
        return a - b

class Multiplication(CalculatorBase):
    def execute(self, a, b):
        return a * b

class Division(CalculatorBase):
    def execute(self, a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return a / b

# MAIN CLASS WHERE THE BAD CALCULATOR PROGRAM IS EXECUTED
class main_bad:
    print("Welcome to the Complicated Calculator!")
    print("Choose an operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    
    choice = input("Enter a choice (1-4): ")

    # 3. VIOLATES CLEAN CODE & DRY: Using massive if-elif chains instead of match-case,
    # and copy-pasting the exact same input validation 4 separate times.
    if choice == '1':
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            calc = Addition()
            result = calc.execute(a, b)
            print(f"The result is: {result}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    elif choice == '2':
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            calc = Subtraction()
            result = calc.execute(a, b)
            print(f"The result is: {result}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    elif choice == '3':
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            calc = Multiplication()
            result = calc.execute(a, b)
            print(f"The result is: {result}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    elif choice == '4':
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            calc = Division()
            result = calc.execute(a, b)
            print(f"The result is: {result}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    else:
        print("Invalid choice.")
