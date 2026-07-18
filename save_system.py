import json
import math
from account import BankAccount


class SaveSystem:

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

            with open("accounts.json", "w", encoding="utf-8") as file:
                json.dump(account_data, file, indent=4)

        except IOError:
            print("Could not save accounts.")



    def load_accounts(self):

        try:

            with open("accounts.json", "r", encoding="utf-8") as file:
                account_data = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):

            account_data = []


        accounts = []
        seen_account_numbers = set()
        highest_account = 0


        for account in account_data:


            if not isinstance(account, dict):
                continue


            owner = account.get("owner", "Unknown")

            if not isinstance(owner, str) or not owner.strip():

                owner = "Unknown"

            else:

                owner = owner.strip()



            balance = account.get("balance", 0)


            if (
                not isinstance(balance, (int, float))
                or isinstance(balance, bool)
                or math.isnan(balance)
                or math.isinf(balance)
                or balance < 0
            ):

                balance = 0



            account_number = account.get("account_number")


            if not isinstance(account_number, int):

                continue


            if account_number in seen_account_numbers:

                continue


            seen_account_numbers.add(account_number)



            pin = account.get("pin", "0000")


            if not isinstance(pin, str) or len(pin) != 4 or not pin.isdigit():

                pin = "0000"



            transactions = account.get("transactions", [])


            if not isinstance(transactions, list):

                transactions = []



            failed_attempts = account.get("failed_attempts", 0)


            if not isinstance(failed_attempts, int) or failed_attempts < 0:

                failed_attempts = 0



            locked = account.get("locked", False)


            if not isinstance(locked, bool):

                locked = False



            created_date = account.get("created_date", "")


            if not isinstance(created_date, str):

                created_date = ""



            account_type = account.get(
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



            new_account.transactions = transactions
            new_account.failed_attempts = failed_attempts
            new_account.locked = locked
            new_account.created_date = created_date



            account_note = account.get(
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