from ui.input_handler import (
    get_integer,
    get_float
)

from ui.menus import (
    show_account_menu
)

from services.account_report_service import (
    search_transactions,
    show_information,
    generate_monthly_statement
)

from services.scheduled_payment_service import (
    create_scheduled_payment,
    show_scheduled_payments,
    execute_payment,
    delete_scheduled_payment
)

from services.loan_service import (
    create_loan,
    show_loans,
    pay_loan
)





def account_session(
    bank,
    account,
    save_callback
):


    while True:


        show_account_menu()



        choice = get_integer(
            "\nChoose an option: "
        )



        if choice == 1:


            amount = get_float(
                "Enter deposit amount: "
            )



            if account.deposit(
                amount
            ):

                save_callback()





        elif choice == 2:


            amount = get_float(
                "Enter withdrawal amount: "
            )



            if account.withdraw(
                amount
            ):

                save_callback()





        elif choice == 3:


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


                    return





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



            account_types = {

                1: "Basic",

                2: "Savings",

                3: "Premium"

            }



            if account_choice in account_types:


                if bank.change_account_type(

                    account.account_number,

                    account_types[account_choice]

                ):

                    save_callback()





        elif choice == 12:


            generate_monthly_statement(
                account
            )





        elif choice == 13:


            account.show_notifications()





        elif choice == 14:


            if account.create_card():

                save_callback()





        elif choice == 15:


            account.show_card()





        elif choice == 16:


            if account.block_card():

                save_callback()





        elif choice == 17:


            if account.unblock_card():

                save_callback()





        elif choice == 18:


            print(
                "\n=== Create Scheduled Payment ==="
            )



            name = input(
                "Payment name: "
            ).strip()



            amount = get_float(
                "Payment amount: "
            )



            day = get_integer(
                "Payment day: "
            )



            if create_scheduled_payment(

                account,

                name,

                amount,

                day

            ):

                save_callback()





        elif choice == 19:


            show_scheduled_payments(
                account
            )





        elif choice == 20:


            show_scheduled_payments(
                account
            )



            payment_number = get_integer(
                "Choose payment number: "
            )



            if execute_payment(

                account,

                payment_number

            ):

                save_callback()





        elif choice == 21:


            show_scheduled_payments(
                account
            )



            payment_number = get_integer(
                "Choose payment number to delete: "
            )



            if delete_scheduled_payment(

                account,

                payment_number

            ):

                save_callback()


        elif choice == 22:


            print(
                "\n=== Request Loan ==="
            )


            print(
                "1. Personal"
            )

            print(
                "2. Business"
            )

            print(
                "3. Premium"
            )



            loan_choice = get_integer(
                "Choose loan type: "
            )



            loan_types = {

                1: "Personal",

                2: "Business",

                3: "Premium"

            }



            if loan_choice not in loan_types:


                print(
                    "Invalid loan type."
                )


            else:


                amount = get_float(
                    "Loan amount: "
                )



                if create_loan(

                    account,

                    loan_types[loan_choice],

                    amount

                ):

                    save_callback()





        elif choice == 23:


            show_loans(
                account
            )





        elif choice == 24:


            show_loans(
                account
            )



            loan_number = get_integer(
                "Choose loan number: "
            )



            amount = get_float(
                "Payment amount: "
            )



            if pay_loan(

                account,

                loan_number,

                amount

            ):

                save_callback()





        elif choice == 25:


            print(
                "Logged out."
            )


            break





        else:


            print(
                "Invalid option."
            )