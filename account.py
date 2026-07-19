from datetime import datetime
import math


class BankAccount:

    next_account_number = 1001


    ACCOUNT_RULES = {
        "Basic": {
            "deposit": 50000,
            "withdrawal": 10000
        },

        "Savings": {
            "deposit": 100000,
            "withdrawal": 25000
        },

        "Premium": {
            "deposit": 500000,
            "withdrawal": 100000
        }
    }


    INTEREST_RATES = {
        "Basic": 0,
        "Savings": 0.02,
        "Premium": 0.05
    }


    MAX_STARTING_BALANCE = 100000


    def __init__(
        self,
        owner,
        starting_balance,
        pin,
        account_number=None,
        account_type="Basic"
    ):

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


        if (
            not isinstance(pin, str)
            or len(pin) != 4
            or not pin.isdigit()
        ):
            pin = "0000"


        self.pin = pin


        self.failed_attempts = 0
        self.locked = False
        self.transactions = []
        self.account_note = ""


        self.account_type = self.validate_account_type(
            account_type
        )


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



    def validate_account_type(self, account_type):

        if account_type in self.ACCOUNT_RULES:

            return account_type

        return "Basic"



    def change_account_type(self, new_type):

        if new_type not in self.ACCOUNT_RULES:

            print("Invalid account type.")

            return False


        if new_type == self.account_type:

            print(
                "You already have this account type."
            )

            return False


        old_type = self.account_type

        self.account_type = new_type


        self.add_transaction(
            "Account Upgrade",
            f"Account changed: {old_type} -> {new_type}"
        )


        print("\n===================================")
        print("      ACCOUNT TYPE CHANGED")
        print("===================================")

        print(f"Previous Type : {old_type}")
        print(f"New Type      : {new_type}")

        print("===================================")


        return True



    def calculate_interest(self):

        interest_rate = self.INTEREST_RATES[
            self.account_type
        ]

        return self.balance * interest_rate



    def apply_interest(self):

        interest = self.calculate_interest()


        if interest <= 0:

            print(
                f"{self.account_type} account does not earn interest."
            )

            return False


        self.balance += interest


        self.add_transaction(
            "Interest",
            f"Interest Earned: {interest}"
        )


        print("\n===================================")
        print("        INTEREST PAYMENT")
        print("===================================")

        print(f"Account  : {self.account_number}")
        print(f"Interest : {interest:.2f}")
        print(f"Balance  : {self.balance:.2f}")

        print("===================================")


        return True
    

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

            print(
                "Deposit cannot be zero or negative."
            )

            return False



        max_deposit = self.ACCOUNT_RULES[
            self.account_type
        ]["deposit"]



        if amount > max_deposit:

            print(
                f"Maximum deposit for {self.account_type} account is {max_deposit}."
            )

            return False



        self.balance += amount



        if create_transaction:

            self.add_transaction(
                "Deposit",
                f"Deposited: {amount}"
            )



        print("\n===================================")
        print("        DEPOSIT RECEIPT")
        print("===================================")

        print(f"Account : {self.account_number}")
        print(f"Amount  : {amount:.2f}")
        print(f"Balance : {self.balance:.2f}")
        print("Status  : SUCCESS")

        print("===================================")


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

            print(
                "Withdrawal cannot be zero or negative."
            )

            return False



        max_withdrawal = self.ACCOUNT_RULES[
            self.account_type
        ]["withdrawal"]



        if amount > max_withdrawal:

            print(
                f"Maximum withdrawal for {self.account_type} account is {max_withdrawal}."
            )

            return False



        if amount > self.balance:

            print(
                "Insufficient funds."
            )

            return False



        self.balance -= amount



        if create_transaction:

            self.add_transaction(
                "Withdrawal",
                f"Withdrew: {amount}"
            )



        print("\n===================================")
        print("       WITHDRAWAL RECEIPT")
        print("===================================")

        print(f"Account : {self.account_number}")
        print(f"Amount  : {amount:.2f}")
        print(f"Balance : {self.balance:.2f}")

        print("===================================")


        return True





    def show_balance(self):

        print(
            f"{self.account_number} {self.owner}'s balance: {self.balance:.2f}"
        )





    def show_transactions(self):

        print("\n=== Transaction History ===")


        if not self.transactions:

            print(
                "No transactions yet."
            )

            return



        for transaction in self.transactions:


            if isinstance(transaction, dict):

                print(
                    f"{transaction.get('timestamp', 'Unknown')} | "
                    f"{transaction.get('category', 'Unknown')} | "
                    f"{transaction.get('message', '')}"
                )


            else:

                print(transaction)





    def generate_monthly_statement(self):

        current_month = datetime.now().strftime(
            "%Y-%m"
        )


        deposits = 0
        withdrawals = 0
        transfers_sent = 0
        transfers_received = 0
        interest = 0


        monthly_transactions = []



        for transaction in self.transactions:


            if not isinstance(transaction, dict):

                continue



            timestamp = transaction.get(
                "timestamp",
                ""
            )


            if not timestamp.startswith(current_month):

                continue



            category = transaction.get(
                "category",
                ""
            )


            message = transaction.get(
                "message",
                ""
            )


            monthly_transactions.append(
                transaction
            )



            amount = self.extract_amount(
                message
            )



            if category == "Deposit":

                deposits += amount


            elif category == "Withdrawal":

                withdrawals += amount


            elif category == "Transfer Sent":

                transfers_sent += amount


            elif category == "Transfer Received":

                transfers_received += amount


            elif category == "Interest":

                interest += amount


                print("\n===================================")
        print("        MONTHLY STATEMENT")
        print("===================================")


        print(f"Owner          : {self.owner}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Type   : {self.account_type}")

        print("-----------------------------------")

        print(
            f"Current Balance : {self.balance:.2f}"
        )

        print("-----------------------------------")

        print(
            f"Deposits              : {deposits:.2f}"
        )

        print(
            f"Withdrawals           : {withdrawals:.2f}"
        )

        print(
            f"Transfers Sent        : {transfers_sent:.2f}"
        )

        print(
            f"Transfers Received    : {transfers_received:.2f}"
        )

        print(
            f"Interest Earned       : {interest:.2f}"
        )


        print("-----------------------------------")
        print("Transactions:")
        print("-----------------------------------")


        if not monthly_transactions:

            print(
                "No transactions this month."
            )

        else:

            for transaction in monthly_transactions:

                print(
                    f"{transaction.get('timestamp')} | "
                    f"{transaction.get('category')} | "
                    f"{transaction.get('message')}"
                )


        print("===================================")





    def extract_amount(self, message):

        if not isinstance(message, str):

            return 0


        numbers = []


        for word in message.replace(",", "").split():

            try:

                numbers.append(
                    float(word)
                )

            except ValueError:

                continue



        if numbers:

            return numbers[0]


        return 0





    def search_transactions(self, keyword):

        if (
            not isinstance(keyword, str)
            or not keyword.strip()
        ):

            print(
                "Invalid search keyword."
            )

            return



        keyword = keyword.lower().strip()


        found = False


        print("\n=== Search Results ===")



        for transaction in self.transactions:


            if isinstance(transaction, dict):

                text = (
                    str(transaction.get("category", ""))
                    + " "
                    + str(transaction.get("message", ""))
                ).lower()


            else:

                text = str(transaction).lower()



            if keyword in text:

                print(transaction)

                found = True



        if not found:

            print(
                "No matching transactions found."
            )





    def show_transaction_statistics(self):

        deposits = 0
        withdrawals = 0
        transfers_sent = 0
        transfers_received = 0
        pin_changes = 0



        for transaction in self.transactions:


            if not isinstance(transaction, dict):

                continue



            category = transaction.get(
                "category",
                ""
            ).lower()



            if category == "deposit":

                deposits += 1


            elif category == "withdrawal":

                withdrawals += 1


            elif category == "transfer sent":

                transfers_sent += 1


            elif category == "transfer received":

                transfers_received += 1


            elif category == "pin change":

                pin_changes += 1





        print("\n=== Transaction Statistics ===")

        print(
            f"Deposits           : {deposits}"
        )

        print(
            f"Withdrawals        : {withdrawals}"
        )

        print(
            f"Transfers Sent     : {transfers_sent}"
        )

        print(
            f"Transfers Received : {transfers_received}"
        )

        print(
            f"PIN Changes        : {pin_changes}"
        )





    def change_pin(self, old_pin, new_pin, confirm_pin):

        if isinstance(old_pin, str):

            old_pin = old_pin.strip()


        if isinstance(new_pin, str):

            new_pin = new_pin.strip()


        if isinstance(confirm_pin, str):

            confirm_pin = confirm_pin.strip()



        if old_pin != self.pin:

            print(
                "Incorrect current PIN."
            )

            return False



        if new_pin != confirm_pin:

            print(
                "New PINs do not match."
            )

            return False



        if (
            not isinstance(new_pin, str)
            or len(new_pin) != 4
            or not new_pin.isdigit()
        ):

            print(
                "PIN must contain exactly 4 numbers."
            )

            return False



        self.pin = new_pin


        self.add_transaction(
            "PIN Change",
            "PIN changed"
        )


        print(
            "PIN changed successfully."
        )


        return True





    def show_information(self):

        print("\n=== Account Information ===")

        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance:.2f}")
        print(
            f"Account Status: {'Locked' if self.locked else 'Active'}"
        )

        print(
            f"Failed Login Attempts: {self.failed_attempts}"
        )

        print(
            f"Total Transactions: {len(self.transactions)}"
        )

        print(
            f"Created: {self.created_date}"
        )

        print(
            f"Account Note: {self.account_note if self.account_note else 'No note'}"
        )


        self.show_transaction_statistics()





    def change_account_note(self, note):

        if not isinstance(note, str):

            print(
                "Invalid note."
            )

            return False



        self.account_note = note.strip()


        self.add_transaction(
            "Account Note",
            "Account note updated"
        )


        print(
            "Account note updated successfully."
        )


        return True





    def add_transaction(self, category, message):

        if (
            not isinstance(category, str)
            or not category.strip()
        ):

            return False



        if (
            not isinstance(message, str)
            or not message.strip()
        ):

            return False



        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )



        self.transactions.append(
            {
                "timestamp": timestamp,
                "category": category.strip(),
                "message": message.strip()
            }
        )


        return True