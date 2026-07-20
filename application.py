from services.save_system import SaveSystem
from core.bank import Bank

from ui.input_handler import (
    get_integer,
    get_float
)

from ui.menus import show_menu

from ui.sessions.account_session import (
    account_session
)

from ui.sessions.admin_session import (
    admin_session
)

from services.security_service import validate_pin


class Application:

    def __init__(self):

        self.bank = Bank()

        self.save_system = SaveSystem()


        self.bank.set_save_callback(
            self.save_accounts
        )


        loaded_accounts = (
            self.save_system.load_accounts()
        )


        self.bank.load_accounts(
            loaded_accounts
        )



    def save_accounts(self):

        self.save_system.save_accounts(
            self.bank.accounts
        )



    def run(self):

        while True:

            show_menu()


            choice = get_integer(
                "\nChoose an option: "
            )


            if choice == 1:

                self.create_account()



            elif choice == 2:

                self.login()



            elif choice == 3:

                admin_session(
                    self.bank
                )



            elif choice == 4:

                self.save_accounts()

                print(
                    "\nGoodbye! Thank you for using the Banking System."
                )

                break



            else:

                print(
                    "Invalid option."
                )



    def create_account(self):

        print(
            "\n=== Create Account ==="
        )


        name = input(
            "Enter owner name: "
        ).strip()


        if not name:

            print(
                "Name cannot be empty."
            )

            return



        balance = get_float(
            "Enter starting balance: "
        )


        pin = input(
            "Enter account PIN: "
        ).strip()



        if not validate_pin(pin):

            print(
                "Invalid PIN. PIN must contain exactly 4 numbers."
            )

            return



        print(
            "\n=== Account Type ==="
        )

        print(
            "1. Basic"
        )

        print(
            "2. Savings"
        )

        print(
            "3. Premium"
        )



        account_choice = get_integer(
            "Choose account type: "
        )



        account_types = {

            1: "Basic",
            2: "Savings",
            3: "Premium"

        }



        if account_choice not in account_types:

            print(
                "Invalid account type."
            )

            return



        account = self.bank.create_account(

            name,
            balance,
            pin,
            account_types[account_choice]

        )



        if account:

            self.save_accounts()



    def login(self):

        print(
            "\n=== Login ==="
        )


        account_number = get_integer(
            "Enter account number: "
        )


        pin = input(
            "Enter account PIN: "
        ).strip()



        account = self.bank.login(

            account_number,
            pin

        )



        if account:

            account_session(

                self.bank,
                account,
                self.save_accounts

            )