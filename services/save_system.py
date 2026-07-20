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


        account_data = []



        for account in accounts:

            account_data.append(
                account_to_dict(account)
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



        except IOError:


            print(
                "Could not save accounts."
            )





    def load_accounts(self):


        try:


            with open(

                self.FILE_NAME,

                "r",

                encoding="utf-8"

            ) as file:


                account_data = json.load(file)



        except (

            FileNotFoundError,

            json.JSONDecodeError

        ):


            account_data = []



        if not isinstance(
            account_data,
            list
        ):

            account_data = []



        accounts = []

        seen_numbers = set()

        highest_account_number = 0



        for data in account_data:


            account = dict_to_account(
                data
            )



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



        if highest_account_number:

            BankAccount.next_account_number = (

                highest_account_number + 1

            )

        else:

            BankAccount.next_account_number = 1001



        return accounts