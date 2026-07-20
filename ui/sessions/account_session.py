from ui.input_handler import get_integer, get_float

from ui.menus import show_account_menu

from services.account_report_service import (
    search_transactions,
    show_information,
    generate_monthly_statement
)



def account_session(
    bank,
    account,
    save_callback
):

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
                "Enter receiver account number: "
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


            from services.transaction_service import show_transactions


            show_transactions(
                account
            )



        elif choice == 6:


            keyword = input(
                "Enter search keyword: "
            ).strip()



            search_transactions(

                account,

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


            show_information(
                account
            )



        elif choice == 9:


            note = input(
                "Enter account note: "
            )



            if account.change_account_note(
                note
            ):

                save_callback()



        elif choice == 10:


            pin = input(
                "Enter PIN to delete account: "
            ).strip()



            confirmation = input(

                "This action is permanent.\n"

                "Type YES to continue: "

            ).strip().lower()



            if confirmation == "yes":


                if bank.delete_account(

                    account.account_number,

                    pin

                ):


                    save_callback()



                    print(
                        "Account deleted."
                    )


                    break



        elif choice == 11:


            print(
                "\n1. Basic"
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



            types = {

                1: "Basic",

                2: "Savings",

                3: "Premium"

            }



            if account_choice in types:


                if bank.change_account_type(

                    account.account_number,

                    types[account_choice]

                ):

                    save_callback()



        elif choice == 12:


            generate_monthly_statement(
                account
            )



        elif choice == 13:


            print(
                "Logged out."
            )



        else:


            print(
                "Invalid option."
            )