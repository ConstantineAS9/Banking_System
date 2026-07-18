from account import BankAccount


class Bank:

    def __init__(self):
        self.accounts = []
        self.save_callback = None

    def set_save_callback(self, callback):
        self.save_callback = callback

    def create_account(self, owner, starting_balance, pin):

        if not owner.strip():
            print("Owner name cannot be empty.")
            return False

        if starting_balance < 0:
            print("Starting balance cannot be negative.")
            return False

        if starting_balance > BankAccount.MAX_STARTING_BALANCE:
            print(
                f"Maximum starting balance is {BankAccount.MAX_STARTING_BALANCE}."
            )
            return False

        account = BankAccount(
            owner,
            starting_balance,
            pin
        )

        self.accounts.append(account)

        print(
            f"Account created for {owner}"
        )

        return account

    def login(self, account_number, pin):

        print("\n=== Login ===")

        account = self.find_account(account_number)

        if account is None:
            print("Account not found.")
            return

        if account.locked:
            print("Account is locked.")
            return

        if pin != account.pin:

            account.failed_attempts += 1

            if account.failed_attempts >= 3:
                account.locked = True
                print("Too many failed attempts. Account locked.")
            else:
                print(
                    f"Wrong PIN. Attempt {account.failed_attempts}/3"
                )

            if self.save_callback:
                self.save_callback()

            return

        print("Login successful.")

        account.failed_attempts = 0

        if self.save_callback:
            self.save_callback()

        return account

    def show_accounts(self):

        print("\n=== Bank Accounts ===")

        if not self.accounts:
            print("No accounts found.")
            return

        for account in self.accounts:
            print(
                f"Account #: {account.account_number} | Owner: {account.owner} | Balance: {account.balance:.2f}"
            )

    def show_bank_statistics(self):

        total_balance = 0
        total_accounts = len(self.accounts)
        locked_accounts = 0
        highest_balance = 0
        lowest_balance = None
        total_transactions = 0
        avrage_balance = 0

        for account in self.accounts:

            total_balance += account.balance

            total_transactions += len(account.transactions)

            if account.balance > highest_balance:
                highest_balance = account.balance

            if lowest_balance is None or account.balance < lowest_balance:
                lowest_balance = account.balance

            if account.locked:
                locked_accounts += 1

        if total_accounts > 0:
            avrage_balance = total_balance / total_accounts
        
        else:
            lowest_balance = 0

        print("\n===================================")
        print("       BANK STATISTICS")
        print("===================================")

        print(f"Total Accounts     : {total_accounts}")
        print(f"Total Money        : {total_balance:.2f}")
        print(f"Avrage Balance     : {avrage_balance:.2f}")
        print(f"Highest Balance    : {highest_balance:.2f}")
        print(f"Lowest Balance     : {lowest_balance:.2f}")
        print(f"Locked Accounts    : {locked_accounts}")
        print(f"Total Transactions : {total_transactions}")

    def find_account(self, account_number):

        for account in self.accounts:

            if account.account_number == account_number:
                return account

        return None

    def load_accounts(self, accounts):
        self.accounts = accounts

    def deposit_money(self, account_number, amount):

        account = self.find_account(account_number)

        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_money(self, account_number, amount):

        account = self.find_account(account_number)

        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer_money(self, sender_number, receiver_number, amount):

        sender = self.find_account(sender_number)
        receiver = self.find_account(receiver_number)

        if sender is None:
            print("Sender account not found.")
            return False

        if receiver is None:
            print("Receiver account not found.")
            return False

        if sender == receiver:
            print("You cannot transfer money to the same account.")
            return False

        if amount <= 0:
            print("Transfer amount must be positive.")
            return False

        if amount > sender.balance:
            print("Insufficient funds.")
            return False

        if amount > BankAccount.MAX_DEPOSIT:
            print("Receiver cannot accept this amount.")
            return False

        if receiver.deposit(amount, False) is False:
            return False

        if sender.withdraw(amount, False) is False:
            return False

        sender.add_transaction(
            f"Transferred {amount} to account {receiver.account_number}"
        )

        receiver.add_transaction(
            f"Received {amount} from account {sender.account_number}"
        )

        print("Transfer successful.")

        if self.save_callback:
            self.save_callback()

        return True

    def show_balance(self, account_number):

        account = self.find_account(account_number)

        if account:
            account.show_balance()
        else:
            print("Account not found.")

    def show_transactions(self, account_number):

        account = self.find_account(account_number)

        if account:
            account.show_transactions()
        else:
            print("Account not found.")

    def delete_account(self, account_number, pin):

        account = self.find_account(account_number)

        if account is None:
            print("Account not found.")
            return False

        if account.pin != pin:
            print("Incorrect PIN.")
            return False

        if account.balance != 0:
            print("Account must have zero balance before deletion.")
            return False

        self.accounts.remove(account)

        if self.save_callback:
            self.save_callback()

        print("Account deleted successfully.")

        return True