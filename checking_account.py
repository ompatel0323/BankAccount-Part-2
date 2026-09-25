from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        # Inherits constructor from BankAccount parent class
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, recipient):
        if amount > self.transfer_limit:
            print(f"Transfer failed! ${amount} exceeds maximum transfer limit of ${self.transfer_limit}.")
        elif self.current_balance - amount < self.minimum_balance:
            print("Transfer failed! Insufficient funds (minimum balance violation).")
        else:
            self.current_balance -= amount
            recipient.deposit(amount)
            print(f"Transferred ${amount} to {recipient.customer_name}.")