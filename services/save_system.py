import json
import os


from core.account import BankAccount


from services.account_serializer import (
    account_to_dict,
    dict_to_account
)





class SaveSystem:


    FILE_NAME = os.path.join(
        "data",
        "accounts.json"
    )





    def save_accounts(
        self,
        accounts
    ):


        if not isinstance(
            accounts,
            list
        ):

            return False





        account_data = []





        for account in accounts:


            try:


                account_data.append(

                    account_to_dict(
                        account
                    )

                )


            except Exception:


                print(
                    "Skipping invalid account during save."
                )





        try:


            os.makedirs(

                "data",

                exist_ok=True

            )





            with open(

                self.FILE_NAME,

                "w",

                encoding="utf-8"

            ) as file:


                json.dump(

                    account_data,

                    file,

                    indent=4

                )





            return True





        except IOError:


            print(
                "Could not save accounts."
            )


            return False







    def load_accounts(
        self
    ):


        if not os.path.exists(
            self.FILE_NAME
        ):


            return []





        try:


            with open(

                self.FILE_NAME,

                "r",

                encoding="utf-8"

            ) as file:


                account_data = json.load(
                    file
                )





        except (

            FileNotFoundError,

            json.JSONDecodeError

        ):


            print(
                "Save file corrupted. Starting fresh."
            )


            return []





        if not isinstance(
            account_data,
            list
        ):


            return []





        accounts = []

        seen_numbers = set()

        highest_account_number = 0





        for data in account_data:


            try:


                account = dict_to_account(
                    data
                )



            except Exception:


                account = None





            if account is None:

                continue





            if account.account_number in seen_numbers:

                continue





            seen_numbers.add(

                account.account_number

            )





            highest_account_number = max(

                highest_account_number,

                account.account_number

            )





            accounts.append(
                account
            )





        if highest_account_number > 0:


            BankAccount.next_account_number = (

                highest_account_number + 1

            )


        else:


            BankAccount.next_account_number = 1001





        return accounts