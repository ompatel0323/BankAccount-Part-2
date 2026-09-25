class BankAccount:
    bank_title = "Charlotte National Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number      # Protected member (1 underscore)
        self.__routing_number = routing_number    # Private member (2 underscores)

    # Getter method to safely access the private routing number
    def get_routing_number(self):
        return self.__routing_number

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposited ${amount}. New balance: ${self.current_balance}")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(f"Cannot withdraw. Balance can't drop below minimum of ${self.minimum_balance}")
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.current_balance}")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer: {self.customer_name}")
        print(f"Account #: {self._account_number}")
        print(f"Balance: ${self.current_balance}")