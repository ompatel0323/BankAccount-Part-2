class BankAccount:
    bank_title = "Software Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        self._accountNumber = account_number
        self.__routingNumber = routing_number


    def get_account_number(self):
        return self._accountNumber

    def get_routing_number(self):
        return self.__routingNumber

    def deposit(self, money):
        if money <= 0:
            return
        self.current_balance += money

    def withdraw(self, money):
        if money <= 0:
            print(f"You cannot withdraw ${money}.")
            return

        if self.current_balance - money < self.minimum_balance:
            print(f"You cannot withdraw ${money}.")
            return

        self.current_balance -= money


    def print_customer_information(self):
        print(f"\nBank Title: {self.bank_title}\n" 
              f"\tCustomer name: {self.customer_name}\n"
              f"\tCurrent balance: ${self.current_balance}\n" 
              f"\tMinimum balance: ${self.minimum_balance}")


    def withdraw(self, money):
            if money <= 0:
                print(f"You cannot withdraw ${money}.")
                return
    
            if self.current_balance - money < -self.overdraft_limit:
                print(f"You cannot withdraw ${money}.")
                return
    
            self.current_balance -= money


class savings_account(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.current_balance * (self.interest_rate / 100)
    
class checking_account(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, overdraft_limit, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.overdraft_limit = overdraft_limit

    

# b1 = BankAccount("Om Patel", 100, 50)

# b1.deposit(100)
# b1.withdraw(100)
# b1.print_customer_information()

# b2 = BankAccount("John Smith", 150, 70)

# b2.print_customer_information()
# b2.withdraw(140)