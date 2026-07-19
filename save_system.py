import json
import math
from account import BankAccount


class SaveSystem:

    FILE_NAME = "accounts.json"


    def save_accounts(self, accounts):

        account_data = []


        for account in accounts:

            account_dict = {
                "owner": account.owner,
                "balance": account.balance,
                "pin": account.pin,
                "account_number": account.account_number,
                "transactions": account.transactions,
                "failed_attempts": account.failed_attempts,
                "locked": account.locked,
                "created_date": account.created_date,
                "account_note": account.account_note,
                "account_type": account.account_type,
            }


            account_data.append(account_dict)



        try:

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

            print("Could not save accounts.")




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



        accounts = []

        seen_account_numbers = set()

        highest_account = 0



        if not isinstance(account_data, list):

            account_data = []




        for data in account_data:


            if not isinstance(data, dict):

                continue



            owner = data.get(
                "owner",
                "Unknown"
            )


            if not isinstance(owner, str) or not owner.strip():

                owner = "Unknown"

            else:

                owner = owner.strip()




            balance = data.get(
                "balance",
                0
            )



            if (
                not isinstance(balance, (int, float))
                or isinstance(balance, bool)
                or math.isnan(balance)
                or math.isinf(balance)
                or balance < 0
            ):

                balance = 0




            account_number = data.get(
                "account_number"
            )



            if (
                not isinstance(account_number, int)
                or isinstance(account_number, bool)
                or account_number <= 0
            ):

                continue



            if account_number in seen_account_numbers:

                continue



            seen_account_numbers.add(account_number)




            pin = data.get(
                "pin",
                "0000"
            )



            if (
                not isinstance(pin, str)
                or len(pin) != 4
                or not pin.isdigit()
            ):

                pin = "0000"




            account_type = data.get(
                "account_type",
                "Basic"
            )



            if account_type not in [
                "Basic",
                "Savings",
                "Premium"
            ]:

                account_type = "Basic"





            new_account = BankAccount(
                owner,
                balance,
                pin,
                account_number,
                account_type
            )



            transactions = data.get(
                "transactions",
                []
            )


            if not isinstance(transactions, list):

                transactions = []



            new_account.transactions = transactions




            failed_attempts = data.get(
                "failed_attempts",
                0
            )



            if (
                not isinstance(failed_attempts, int)
                or failed_attempts < 0
            ):

                failed_attempts = 0



            new_account.failed_attempts = failed_attempts




            locked = data.get(
                "locked",
                False
            )



            if not isinstance(locked, bool):

                locked = False



            new_account.locked = locked





            created_date = data.get(
                "created_date",
                ""
            )


            if not isinstance(created_date, str):

                created_date = ""



            new_account.created_date = created_date




            account_note = data.get(
                "account_note",
                ""
            )


            if not isinstance(account_note, str):

                account_note = ""



            new_account.account_note = account_note





            if new_account.account_number > highest_account:

                highest_account = new_account.account_number




            accounts.append(new_account)





        if highest_account == 0:

            BankAccount.next_account_number = 1001


        else:

            BankAccount.next_account_number = highest_account + 1




        return accounts