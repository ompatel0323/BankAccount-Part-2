from savings_account import SavingsAccount
from checking_account import CheckingAccount

def main():
    print("=== TESTING SAVINGS ACCOUNTS ===")
    # 2 separate instances of SavingsAccount
    sav1 = SavingsAccount("Alice Johnson", 1000, 100, "SA-101", "053000219", 0.05)
    sav2 = SavingsAccount("Brian Smith", 2000, 200, "SA-102", "053000219", 0.03)

    sav1.deposit(1500)
    sav1.print_customer_information()
    sav1.add_interest()
    print()


    sav2.withdraw(3000)
    
    print("=== TESTING CHECKING ACCOUNTS ===")
    # 2 separate instances of CheckingAccount
    chk1 = CheckingAccount("Charlie Brown", 500, 50, "CA-201", "053000219", 200)
    chk2 = CheckingAccount("Diana Prince", 1500, 100, "CA-202", "053000219", 500)

    chk1.print_customer_information()

    chk1.withdraw(600) # Wtihdrawing more than current balance but within limit
    chk1.deposit(200)

    print("\n1. Attempting transfer above limit ($300 vs $200 limit):")
    chk1.transfer(300, chk2)

    print("\n2. Attempting valid transfer ($150):")
    chk1.transfer(150, chk2)

if __name__ == "__main__":
    main()