from save_system import SaveSystem
from bank import Bank
from input_handler import get_integer, get_float
from menus import show_menu
from sessions import account_session, admin_session
from security import validate_pin


def main():

    bank = Bank()

    save_system = SaveSystem()


    def save_accounts():

        save_system.save_accounts(bank.accounts)


    bank.set_save_callback(save_accounts)

    loaded_accounts = save_system.load_accounts()

    bank.load_accounts(loaded_accounts)


    choice = 0


    while choice != 4:

        show_menu()

        choice = get_integer("\nChoose an option: ")


        if choice == 1:

            print("\n=== Create Account ===")

            name = input(
                "Enter owner name: "
            ).strip()


            if not name:

                print("Name cannot be empty.")

                continue


            balance = get_float(
                "Enter starting balance: "
            )


            if balance < 0:

                print("Starting balance cannot be negative.")

                continue


            pin = input(
                "Enter account PIN: "
            ).strip()


            if not validate_pin(pin):

                print(
                    "Invalid PIN. PIN must contain exactly 4 numbers."
                )

                continue


            print("\n=== Account Type ===")
            print("1. Basic")
            print("2. Savings")
            print("3. Premium")


            account_choice = get_integer(
                "Choose account type: "
            )


            account_types = {
                1: "Basic",
                2: "Savings",
                3: "Premium"
            }


            if account_choice not in account_types:

                print("Invalid account type.")

                continue


            account_type = account_types[account_choice]


            account = bank.create_account(
                name,
                balance,
                pin,
                account_type
            )


            if account:

                save_accounts()



        elif choice == 2:

            print("\n=== Login ===")


            account_number = get_integer(
                "Enter account number: "
            )


            pin = input(
                "Enter account PIN: "
            ).strip()


            logged_in_account = bank.login(
                account_number,
                pin,
            )


            if logged_in_account:

                account_session(
                    bank,
                    logged_in_account,
                    save_accounts
                )



        elif choice == 3:

            admin_session(bank)



        elif choice == 4:

            save_accounts()

            print(
                "Goodbye! Thank you for using the Banking System."
            )



        else:

            print("Invalid option.")



if __name__ == "__main__":

    main()