from datetime import datetime
import math

from services.transaction_service import (
    add_transaction,
    show_transactions
)

from ui.receipts import (
    show_deposit_receipt,
    show_withdrawal_receipt,
    show_interest_payment,
    show_account_type_change
)


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


        self.owner = (
            owner.strip()
            if isinstance(owner, str) and owner.strip()
            else "Unknown"
        )


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
            isinstance(pin, str)
            and len(pin) == 4
            and pin.isdigit()
        ):

            self.pin = pin

        else:

            self.pin = "0000"



        self.transactions = []

        self.failed_attempts = 0

        self.locked = False

        self.account_note = ""



        self.account_type = (
            account_type
            if account_type in self.ACCOUNT_RULES
            else "Basic"
        )



        if account_number:

            self.account_number = account_number


        else:

            self.account_number = (
                BankAccount.next_account_number
            )

            BankAccount.next_account_number += 1



        self.created_date = (
            datetime.now().strftime("%Y-%m-%d")
        )



    def add_transaction(
        self,
        category,
        message
    ):

        add_transaction(
            self,
            category,
            message
        )



    def deposit(
        self,
        amount,
        create_transaction=True
    ):


        if not self.validate_amount(amount):

            print(
                "Invalid amount."
            )

            return False



        if amount <= 0:

            print(
                "Deposit must be positive."
            )

            return False



        limit = self.ACCOUNT_RULES[
            self.account_type
        ]["deposit"]



        if amount > limit:

            print(
                f"Maximum deposit is {limit}."
            )

            return False



        self.balance += amount



        if create_transaction:

            self.add_transaction(
                "Deposit",
                f"Deposited: {amount}"
            )



        show_deposit_receipt(
            self,
            amount
        )


        return True



    def withdraw(
        self,
        amount,
        create_transaction=True
    ):


        if not self.validate_amount(amount):

            print(
                "Invalid amount."
            )

            return False



        if amount <= 0:

            print(
                "Withdrawal must be positive."
            )

            return False



        limit = self.ACCOUNT_RULES[
            self.account_type
        ]["withdrawal"]



        if amount > limit:

            print(
                f"Maximum withdrawal is {limit}."
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



        show_withdrawal_receipt(
            self,
            amount
        )


        return True



    def validate_amount(self, amount):

        return (

            isinstance(amount, (int, float))
            and not isinstance(amount, bool)
            and not math.isnan(amount)
            and not math.isinf(amount)

        )



    def show_balance(self):

        print(
            f"{self.owner}'s balance: {self.balance:.2f}"
        )



    def change_pin(
        self,
        old_pin,
        new_pin,
        confirm_pin
    ):


        if old_pin != self.pin:

            print(
                "Incorrect current PIN."
            )

            return False



        if new_pin != confirm_pin:

            print(
                "PINs do not match."
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



    def change_account_type(
        self,
        new_type
    ):


        if new_type not in self.ACCOUNT_RULES:

            print(
                "Invalid account type."
            )

            return False



        old_type = self.account_type


        if old_type == new_type:

            print(
                "Already using this account type."
            )

            return False



        self.account_type = new_type



        self.add_transaction(
            "Account Upgrade",
            f"{old_type} -> {new_type}"
        )


        show_account_type_change(
            old_type,
            new_type
        )


        return True



    def calculate_interest(self):

        rate = self.INTEREST_RATES[
            self.account_type
        ]

        return self.balance * rate



    def apply_interest(self):

        interest = self.calculate_interest()



        if interest <= 0:

            return False



        self.balance += interest



        self.add_transaction(
            "Interest",
            f"Interest Earned: {interest}"
        )



        show_interest_payment(
            self,
            interest
        )


        return True



    def change_account_note(
        self,
        note
    ):


        if not isinstance(note, str):

            return False



        self.account_note = note.strip()


        self.add_transaction(
            "Account Note",
            "Account note updated"
        )


        return True