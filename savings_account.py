from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        # Inherits constructor from BankAccount parent class
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate  # Example: 0.05 is 5%

    def add_interest(self):
        interest_earned = self.current_balance * self.interest_rate
        self.current_balance += interest_earned
        print(f"Earned ${interest_earned:.2f} in interest. New balance: ${self.current_balance:.2f}")