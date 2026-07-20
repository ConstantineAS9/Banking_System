from core.account import BankAccount


class Bank:

    def __init__(self):

        self.accounts = []

        self.save_callback = None



    def set_save_callback(self, callback):

        self.save_callback = callback



    def save(self):

        if self.save_callback:

            self.save_callback()



    def create_account(
        self,
        owner,
        starting_balance,
        pin,
        account_type="Basic"
    ):

        if not isinstance(owner, str) or not owner.strip():

            print(
                "Owner name cannot be empty."
            )

            return None



        if starting_balance < 0:

            print(
                "Starting balance cannot be negative."
            )

            return None



        if starting_balance > BankAccount.MAX_STARTING_BALANCE:

            print(
                f"Maximum starting balance is {BankAccount.MAX_STARTING_BALANCE}."
            )

            return None



        account = BankAccount(

            owner.strip(),
            starting_balance,
            pin,
            account_type=account_type

        )


        self.accounts.append(
            account
        )


        print(
            f"Account created successfully. Account number: {account.account_number}"
        )


        self.save()


        return account





    def login(
        self,
        account_number,
        pin
    ):


        account = self.find_account(
            account_number
        )



        if account is None:

            print(
                "Account not found."
            )

            return None



        if account.locked:

            print(
                "Account is locked."
            )

            return None



        if account.pin != pin:


            account.failed_attempts += 1



            if account.failed_attempts >= 3:

                account.locked = True

                print(
                    "Too many failed attempts. Account locked."
                )


            else:

                print(
                    f"Wrong PIN. Attempt {account.failed_attempts}/3"
                )



            self.save()


            return None




        account.failed_attempts = 0


        self.save()


        print(
            "Login successful."
        )


        return account





    def find_account(
        self,
        account_number
    ):


        for account in self.accounts:

            if account.account_number == account_number:

                return account



        return None





    def load_accounts(
        self,
        accounts
    ):

        if isinstance(accounts, list):

            self.accounts = accounts

        else:

            self.accounts = []





    def show_accounts(self):

        print(
            "\n=== Bank Accounts ==="
        )



        if not self.accounts:

            print(
                "No accounts found."
            )

            return



        for account in self.accounts:

            print(

                f"Account #: {account.account_number} | "
                f"Owner: {account.owner} | "
                f"Type: {account.account_type} | "
                f"Balance: {account.balance:.2f} | "
                f"Status: {'Locked' if account.locked else 'Active'}"

            )





    def search_accounts(
        self,
        keyword
    ):


        if (
            not isinstance(keyword, str)
            or not keyword.strip()
        ):

            print(
                "Invalid search."
            )

            return



        keyword = keyword.lower().strip()


        found = False



        print(
            "\n=== SEARCH RESULTS ==="
        )



        for account in self.accounts:


            if (

                keyword in account.owner.lower()

                or keyword == str(account.account_number)

                or keyword in account.account_type.lower()

            ):


                print(

                    f"Account #: {account.account_number} | "
                    f"Owner: {account.owner} | "
                    f"Type: {account.account_type} | "
                    f"Balance: {account.balance:.2f}"

                )


                found = True




        if not found:

            print(
                "No accounts found."
            )





    def show_bank_statistics(self):

        total_balance = 0

        total_transactions = 0

        locked_accounts = 0

        highest_balance = 0

        lowest_balance = None



        for account in self.accounts:


            total_balance += account.balance


            total_transactions += len(
                account.transactions
            )



            if account.balance > highest_balance:

                highest_balance = account.balance



            if (

                lowest_balance is None

                or account.balance < lowest_balance

            ):

                lowest_balance = account.balance



            if account.locked:

                locked_accounts += 1




        total_accounts = len(
            self.accounts
        )



        average_balance = 0



        if total_accounts:

            average_balance = (

                total_balance / total_accounts

            )

        else:

            lowest_balance = 0




        print(
            "\n==================================="
        )

        print(
            "       BANK STATISTICS"
        )

        print(
            "==================================="
        )


        print(
            f"Total Accounts     : {total_accounts}"
        )

        print(
            f"Total Money        : {total_balance:.2f}"
        )

        print(
            f"Average Balance    : {average_balance:.2f}"
        )

        print(
            f"Highest Balance    : {highest_balance:.2f}"
        )

        print(
            f"Lowest Balance     : {lowest_balance:.2f}"
        )

        print(
            f"Locked Accounts    : {locked_accounts}"
        )

        print(
            f"Total Transactions : {total_transactions}"
        )





    def transfer_money(
        self,
        sender_number,
        receiver_number,
        amount
    ):


        sender = self.find_account(
            sender_number
        )


        receiver = self.find_account(
            receiver_number
        )



        if sender is None:

            print(
                "Sender account not found."
            )

            return False



        if receiver is None:

            print(
                "Receiver account not found."
            )

            return False



        if sender == receiver:

            print(
                "Cannot transfer to the same account."
            )

            return False



        if amount <= 0:

            print(
                "Transfer amount must be positive."
            )

            return False



        if amount > sender.balance:

            print(
                "Insufficient funds."
            )

            return False




        if not sender.withdraw(
            amount,
            False
        ):

            return False



        if not receiver.deposit(
            amount,
            False
        ):


            sender.deposit(
                amount,
                False
            )

            return False



        sender.add_transaction(
            "Transfer Sent",
            f"Transferred {amount} to account {receiver.account_number}"
        )


        receiver.add_transaction(
            "Transfer Received",
            f"Received {amount} from account {sender.account_number}"
        )



        self.save()


        print(
            "Transfer successful."
        )


        return True
    

    def apply_interest_to_all_accounts(self):

        print(
            "\n==================================="
        )

        print(
            "        INTEREST REPORT"
        )

        print(
            "==================================="
        )


        added = False


        for account in self.accounts:


            if account.apply_interest():

                added = True



        if not added:

            print(
                "No accounts received interest."
            )


        self.save()





    def change_account_type(
        self,
        account_number,
        new_type
    ):


        account = self.find_account(
            account_number
        )



        if account is None:

            print(
                "Account not found."
            )

            return False



        if account.change_account_type(
            new_type
        ):


            self.save()

            return True



        return False





    def unlock_account(
        self,
        account_number
    ):


        account = self.find_account(
            account_number
        )



        if account is None:

            print(
                "Account not found."
            )

            return False



        if not account.locked:

            print(
                "Account is already unlocked."
            )

            return False



        account.locked = False

        account.failed_attempts = 0



        account.add_transaction(
            "Admin Action",
            "Account unlocked by admin"
        )



        self.save()



        print(
            "Account unlocked successfully."
        )


        return True





    def delete_account(
        self,
        account_number,
        pin
    ):


        account = self.find_account(
            account_number
        )



        if account is None:

            print(
                "Account not found."
            )

            return False



        if account.pin != pin:

            print(
                "Incorrect PIN."
            )

            return False



        if account.balance != 0:

            print(
                "Account must have zero balance before deletion."
            )

            return False



        self.accounts.remove(
            account
        )



        self.save()



        print(
            "Account deleted successfully."
        )


        return True