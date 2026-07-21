from datetime import datetime
import math

from services.transaction_service import add_transaction


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


        # Bank card object
        # Saved and restored through serializer

        self.card = None



        # Scheduled payments

        self.scheduled_payments = []



        # Loan system

        self.loans = []



        # Credit system

        self.credit_score = 600



        # Notification system

        self.notifications = []



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



    # =========================
    # TRANSACTIONS
    # =========================


    def add_transaction(
        self,
        category,
        message
    ):

        return add_transaction(

            self,

            category,

            message

        )



    # =========================
    # MONEY OPERATIONS
    # =========================


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


            self.add_notification(

                "Deposit",

                f"You deposited {amount:.2f}."

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


            self.add_notification(

                "Withdrawal",

                f"You withdrew {amount:.2f}."

            )



        return True
    

        # =========================
    # VALIDATION
    # =========================


    def validate_amount(
        self,
        amount
    ):

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



    # =========================
    # SECURITY
    # =========================


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



        self.add_notification(

            "Security",

            "Your account PIN was changed."

        )



        print(
            "PIN changed successfully."
        )



        return True



    # =========================
    # ACCOUNT TYPE
    # =========================


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



        self.add_notification(

            "Account Type",

            f"Account changed from {old_type} to {new_type}."

        )



        return True



    # =========================
    # INTEREST SYSTEM
    # =========================


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



        self.add_notification(

            "Interest",

            f"Interest payment of {interest:.2f} received."

        )



        return True



    # =========================
    # ACCOUNT NOTES
    # =========================


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



        self.add_notification(

            "Account",

            "Your account note was updated."

        )



        return True



    # =========================
    # NOTIFICATIONS
    # =========================


    def add_notification(
        self,
        title,
        message
    ):


        notification = {

            "title": title,

            "message": message,

            "date": datetime.now().strftime(

                "%Y-%m-%d %H:%M:%S"

            ),

            "read": False

        }



        self.notifications.append(

            notification

        )



        return True





    def show_notifications(self):


        print(
            "\n=== NOTIFICATIONS ==="
        )



        if not self.notifications:

            print(
                "No notifications."
            )

            return



        for notification in reversed(

            self.notifications

        ):


            status = (

                "READ"

                if notification.get("read")

                else "NEW"

            )



            print(

                f"[{status}] "

                f"{notification.get('date')} | "

                f"{notification.get('title')} | "

                f"{notification.get('message')}"

            )



            notification["read"] = True





    def unread_notifications(self):


        count = 0



        for notification in self.notifications:


            if not notification.get("read"):

                count += 1



        return count
    

        # =========================
    # CARD SYSTEM COMPATIBILITY
    # =========================


    def create_card(self):

        if self.card is not None:

            print(
                "Account already has a card."
            )

            return False



        from core.card import BankCard



        self.card = BankCard(

            self.account_number

        )



        self.add_transaction(

            "Card Created",

            "New bank card created"

        )



        self.add_notification(

            "Card",

            "A new bank card has been issued."

        )



        print(
            "Card created successfully."
        )



        return True





    def show_card(self):

        if self.card is None:

            print(
                "No card linked to this account."
            )

            return False



        self.card.show_card()



        return True





    def block_card(self):

        if self.card is None:

            print(
                "No card found."
            )

            return False



        self.card.freeze()



        self.add_transaction(

            "Card Blocked",

            "Bank card blocked"

        )



        self.add_notification(

            "Card",

            "Your bank card has been blocked."

        )



        print(
            "Card blocked."
        )



        return True





    def unblock_card(self):

        if self.card is None:

            print(
                "No card found."
            )

            return False



        self.card.activate()



        self.add_transaction(

            "Card Activated",

            "Bank card activated"

        )



        self.add_notification(

            "Card",

            "Your bank card has been activated."

        )



        print(
            "Card activated."
        )



        return True



    # =========================
    # SCHEDULED PAYMENTS
    # =========================


    def add_scheduled_payment(
        self,
        payment
    ):

        self.scheduled_payments.append(

            payment

        )


        return True





    def remove_scheduled_payment(
        self,
        payment
    ):


        if payment in self.scheduled_payments:

            self.scheduled_payments.remove(

                payment

            )

            return True



        return False



    # =========================
    # LOANS
    # =========================


    def add_loan(
        self,
        loan
    ):


        self.loans.append(

            loan

        )


        return True





    def remove_loan(
        self,
        loan
    ):


        if loan in self.loans:

            self.loans.remove(

                loan

            )

            return True



        return False



    # =========================
    # INFORMATION
    # =========================


    def get_account_summary(self):

        return {

            "owner": self.owner,

            "account_number": self.account_number,

            "account_type": self.account_type,

            "balance": self.balance,

            "locked": self.locked,

            "transactions": len(self.transactions),

            "credit_score": self.credit_score

        }