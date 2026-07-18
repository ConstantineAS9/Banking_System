from input_handler import get_integer, get_float
from menus import show_account_menu, show_admin_menu


def admin_session(bank):

    choice = 0

    while choice != 4:

        show_admin_menu()

        choice = get_integer("\nChoose an option: ")


        if choice == 1:

            bank.show_accounts()


        elif choice == 2:

            account_number = get_integer(
                "Enter account number: "
            )

            account = bank.find_account(account_number)

            if account:

                account.show_information()

            else:

                print("\nNo account with that number was found.")


        elif choice == 3:

            bank.show_bank_statistics()


        elif choice == 4:

            print("\nReturning to the Main Menu...")


        else:

            print("Invalid option.")



def account_session(bank, account, save_callback):

    choice = 0


    while choice != 10:

        show_account_menu()

        choice = get_integer("\nChoose an option: ")


        if choice == 1:

            print("\n--- Deposit Money ---")

            amount = get_float(
                "Enter deposit amount: "
            )

            if account.deposit(amount):

                save_callback()



        elif choice == 2:

            print("\n--- Withdraw Money ---")

            amount = get_float(
                "Enter withdrawal amount: "
            )

            if account.withdraw(amount):

                save_callback()



        elif choice == 3:

            print("\n--- Transfer Money ---")

            receiver_number = get_integer(
                "Enter receiver's number: "
            )

            amount = get_float(
                "Enter transfer amount: "
            )


            if bank.transfer_money(
                account.account_number,
                receiver_number,
                amount
            ):

                save_callback()



        elif choice == 4:

            account.show_balance()



        elif choice == 5:

            account.show_transactions()


        elif choice == 6:

            print("\n--- Search Transactions ---")

            keyword = input(
                "Enter search keyword: "
            ).strip()

            account.search_transactions(keyword)



        elif choice == 7:

            print("\n--- Change PIN ---")

            old_pin = input(
                "Enter current PIN: "
            ).strip()


            new_pin = input(
                "Enter new PIN: "
            ).strip()


            confirm_pin = input(
                "Confirm new PIN: "
            ).strip()


            if account.change_pin(
                old_pin,
                new_pin,
                confirm_pin
            ):

                save_callback()



        elif choice == 8:

            account.show_information()



        elif choice == 9:

            print("\n--- Delete Account ---")

            pin = input(
                "Enter your PIN to delete account: "
            ).strip()


            confirmation = input(
                "WARNING!\n" 
                "Deleting an account is permanent\n" 
                "Type 'yes' to continue: "
            ).strip().lower()


            if confirmation == "yes":

                if bank.delete_account(
                    account.account_number,
                    pin
                ):

                    save_callback()

                    print(
                        "Account deleted. Returning to main menu."
                    )

                    break



        elif choice == 10:

            print("\nYou have been logged out successfully.")
            break



        else:

            print("\nInvalid option. Please try again.")