from input_handler import get_integer, get_float
from menus import show_account_menu, show_admin_menu



def admin_session(bank):

    choice = 0


    while choice != 7:

        show_admin_menu()


        choice = get_integer(
            "\nChoose an option: "
        )



        if choice == 1:

            bank.show_accounts()



        elif choice == 2:

            keyword = input(
                "Search owner/account/type: "
            ).strip()


            bank.search_accounts(keyword)



        elif choice == 3:

            bank.show_bank_statistics()



        elif choice == 4:

            print(
                "\n--- Applying Interest ---"
            )


            bank.apply_interest_to_all_accounts()



        elif choice == 5:

            print(
                "\n--- Unlock Account ---"
            )


            account_number = get_integer(
                "Enter account number: "
            )


            bank.unlock_account(
                account_number
            )



        elif choice == 6:

            print(
                "\n--- Change Account Type ---"
            )


            account_number = get_integer(
                "Enter account number: "
            )



            print("\n1. Basic")
            print("2. Savings")
            print("3. Premium")



            account_choice = get_integer(
                "Choose new account type: "
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

                continue



            bank.change_account_type(
                account_number,
                account_types[account_choice]
            )



        elif choice == 7:

            print(
                "\nReturning to the Main Menu..."
            )



        else:

            print(
                "Invalid option."
            )





def account_session(bank, account, save_callback):

    choice = 0



    while choice != 13:

        show_account_menu()


        choice = get_integer(
            "\nChoose an option: "
        )



        if choice == 1:

            print(
                "\n--- Deposit Money ---"
            )


            amount = get_float(
                "Enter deposit amount: "
            )


            if account.deposit(amount):

                save_callback()



        elif choice == 2:

            print(
                "\n--- Withdraw Money ---"
            )


            amount = get_float(
                "Enter withdrawal amount: "
            )


            if account.withdraw(amount):

                save_callback()



        elif choice == 3:

            print(
                "\n--- Transfer Money ---"
            )


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

            keyword = input(
                "Enter search keyword: "
            ).strip()


            account.search_transactions(
                keyword
            )



        elif choice == 7:

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

            note = input(
                "Enter new account note: "
            )


            if account.change_account_note(note):

                save_callback()



        elif choice == 10:

            pin = input(
                "Enter your PIN to delete account: "
            ).strip()



            confirmation = input(
                "WARNING!\n"
                "Deleting an account is permanent.\n"
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



        elif choice == 11:

            print(
                "\n--- Change Account Type ---"
            )


            print("1. Basic")
            print("2. Savings")
            print("3. Premium")



            account_choice = get_integer(
                "Choose new account type: "
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

                continue



            if bank.change_account_type(
                account.account_number,
                account_types[account_choice]
            ):

                print(
                    "Account type updated successfully."
                )



        elif choice == 12:

            account.generate_monthly_statement()



        elif choice == 13:

            print(
                "\nYou have been logged out successfully."
            )



        else:

            print(
                "\nInvalid option. Please try again."
            )