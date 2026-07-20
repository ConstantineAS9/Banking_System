from ui.input_handler import get_integer

from ui.menus import show_admin_menu



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


            bank.search_accounts(
                keyword
            )



        elif choice == 3:


            bank.show_bank_statistics()



        elif choice == 4:


            bank.apply_interest_to_all_accounts()



        elif choice == 5:


            account_number = get_integer(
                "Enter account number: "
            )


            bank.unlock_account(
                account_number
            )



        elif choice == 6:


            account_number = get_integer(
                "Enter account number: "
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
                "Choose new type: "
            )



            types = {

                1: "Basic",

                2: "Savings",

                3: "Premium"

            }



            if account_choice in types:


                bank.change_account_type(

                    account_number,

                    types[account_choice]

                )



        elif choice == 7:


            print(
                "Returning to main menu."
            )



        else:


            print(
                "Invalid option."
            )