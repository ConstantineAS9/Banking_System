from datetime import datetime
import math


class BankAccount:

    next_account_number = 1001

    MAX_DEPOSIT = 50000
    MAX_WITHDRAWAL = 10000
    MAX_STARTING_BALANCE = 100000

    def __init__(self, owner, starting_balance, pin, account_number=None):

        if not isinstance(owner, str) or not owner.strip():
            owner = "Unknown"

        self.owner = owner.strip()

        if (
            not isinstance(starting_balance, (int, float))
            or isinstance(starting_balance, bool)
            or math.isnan(starting_balance)
            or math.isinf(starting_balance)
            or starting_balance < 0
        ):
            starting_balance = 0

        self.balance = starting_balance

        if not isinstance(pin, str) or len(pin) != 4 or not pin.isdigit():
            pin = "0000"

        self.pin = pin

        self.failed_attempts = 0
        self.locked = False
        self.transactions = []

        if account_number is None:

            self.created_date = datetime.now().strftime(
                "%Y-%m-%d"
            )

        else:

            self.created_date = ""

        if (
            isinstance(account_number, int)
            and not isinstance(account_number, bool)
            and account_number > 0
        ):

            self.account_number = account_number

        else:

            self.account_number = BankAccount.next_account_number
            BankAccount.next_account_number += 1


    def deposit(self, amount, create_transaction=True):

        if (
            not isinstance(amount, (int, float))
            or isinstance(amount, bool)
            or math.isnan(amount)
            or math.isinf(amount)
        ):
            print("Invalid amount.")
            return False

        if amount <= 0:
            print("Deposit cannot be zero or negative.")
            return False
        
        if amount > BankAccount.MAX_DEPOSIT:

            print(
                f"Maximum deposit is {BankAccount.MAX_DEPOSIT}."
            )

            return False

        self.balance += amount

        if create_transaction:

            self.add_transaction(
                f"Deposited: {amount}"
            )

        print(f"Deposit successful. New balance: {self.balance}")

        return True


    def withdraw(self, amount, create_transaction=True):

        if (
            not isinstance(amount, (int, float))
            or isinstance(amount, bool)
            or math.isnan(amount)
            or math.isinf(amount)
        ):
            print("Invalid amount.")
            return False

        if amount <= 0:
            print("Withdrawal cannot be zero or negative.")
            return False
        
        if amount > BankAccount.MAX_WITHDRAWAL:

            print(
                f"Maximum withdrawal is {BankAccount.MAX_WITHDRAWAL}."
            )

            return False

        if amount > self.balance:
            print("Insufficient funds.")
            return False

        self.balance -= amount

        if create_transaction:

            self.add_transaction(
                f"Withdrew: {amount}"
            )

        print(f"Withdrawal successful. New balance: {self.balance}")

        return True


    def show_balance(self):

        print(
            f"{self.account_number} {self.owner}'s balance: {self.balance:.2f}"
        )


    def show_transactions(self):

        print("\n=== Transaction History ===")

        if not self.transactions:
            print("No transactions yet.")
            return

        for transaction in self.transactions:
            print(transaction)


    def change_pin(self, old_pin, new_pin, confirm_pin):

        if isinstance(old_pin, str):
            old_pin = old_pin.strip()

        if isinstance(new_pin, str):
            new_pin = new_pin.strip()

        if isinstance(confirm_pin, str):
            confirm_pin = confirm_pin.strip()

        if not isinstance(new_pin, str):
            print("Invalid PIN.")
            return False

        if old_pin != self.pin:
            print("Incorrect current PIN.")
            return False

        if new_pin != confirm_pin:
            print("New PINs do not match.")
            return False

        if len(new_pin) != 4:
            print("PIN must contain exactly 4 numbers.")
            return False
        
        if not new_pin.isdigit():
            print("PIN must contain only numbers.")
            return False
        
        self.pin = new_pin

        self.add_transaction(
            "PIN changed"
        )

        print("PIN changed successfully.")

        return True


    def show_information(self):

        print("\n=== Account Information ===")

        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f}")
        print(f"Account Status: {'Locked' if self.locked else 'Active'}")
        print(f"Failed Login Attempts: {self.failed_attempts}")
        print(f"Total Transactions: {len(self.transactions)}")
        print(f"Created: {self.created_date}")


    def add_transaction(self, message):

        if not isinstance(message, str) or not message.strip():
            return False

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.transactions.append(
            f"{timestamp} - {message.strip()}"
        )

        return True