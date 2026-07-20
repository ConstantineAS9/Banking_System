from datetime import datetime



def generate_monthly_statement(account):

    current_month = datetime.now().strftime(
        "%Y-%m"
    )


    deposits = 0
    withdrawals = 0
    transfers_sent = 0
    transfers_received = 0
    interest = 0


    monthly_transactions = []



    for transaction in account.transactions:


        if not isinstance(transaction, dict):

            continue



        timestamp = transaction.get(
            "timestamp",
            ""
        )



        if not timestamp.startswith(current_month):

            continue



        category = transaction.get(
            "category",
            ""
        )


        message = transaction.get(
            "message",
            ""
        )



        monthly_transactions.append(
            transaction
        )


        amount = extract_amount(
            message
        )



        if category == "Deposit":

            deposits += amount


        elif category == "Withdrawal":

            withdrawals += amount


        elif category == "Transfer Sent":

            transfers_sent += amount


        elif category == "Transfer Received":

            transfers_received += amount


        elif category == "Interest":

            interest += amount




    print("\n===================================")
    print("        MONTHLY STATEMENT")
    print("===================================")


    print(
        f"Owner          : {account.owner}"
    )

    print(
        f"Account Number : {account.account_number}"
    )

    print(
        f"Account Type   : {account.account_type}"
    )


    print("-----------------------------------")


    print(
        f"Current Balance : {account.balance:.2f}"
    )


    print("-----------------------------------")


    print(
        f"Deposits           : {deposits:.2f}"
    )

    print(
        f"Withdrawals        : {withdrawals:.2f}"
    )

    print(
        f"Transfers Sent     : {transfers_sent:.2f}"
    )

    print(
        f"Transfers Received : {transfers_received:.2f}"
    )

    print(
        f"Interest Earned    : {interest:.2f}"
    )


    print("-----------------------------------")
    print("Transactions:")
    print("-----------------------------------")



    if not monthly_transactions:

        print(
            "No transactions this month."
        )


    else:

        for transaction in monthly_transactions:

            print(

                f"{transaction.get('timestamp')} | "
                f"{transaction.get('category')} | "
                f"{transaction.get('message')}"

            )


    print("===================================")





def extract_amount(message):

    if not isinstance(message, str):

        return 0



    for word in message.replace(",", "").split():

        try:

            return float(word)

        except ValueError:

            continue



    return 0





def search_transactions(account, keyword):

    if (
        not isinstance(keyword, str)
        or not keyword.strip()
    ):

        print(
            "Invalid search keyword."
        )

        return



    keyword = keyword.lower().strip()



    found = False



    print(
        "\n=== Search Results ==="
    )



    for transaction in account.transactions:


        if isinstance(transaction, dict):

            text = (

                str(transaction.get("category", ""))
                + " "
                + str(transaction.get("message", ""))

            ).lower()


        else:

            text = str(transaction).lower()



        if keyword in text:

            print(
                transaction
            )

            found = True



    if not found:

        print(
            "No matching transactions found."
        )





def show_transaction_statistics(account):

    deposits = 0
    withdrawals = 0
    transfers_sent = 0
    transfers_received = 0
    pin_changes = 0



    for transaction in account.transactions:


        if not isinstance(transaction, dict):

            continue



        category = transaction.get(
            "category",
            ""
        ).lower()



        if category == "deposit":

            deposits += 1


        elif category == "withdrawal":

            withdrawals += 1


        elif category == "transfer sent":

            transfers_sent += 1


        elif category == "transfer received":

            transfers_received += 1


        elif category == "pin change":

            pin_changes += 1




    print(
        "\n=== Transaction Statistics ==="
    )


    print(
        f"Deposits           : {deposits}"
    )

    print(
        f"Withdrawals        : {withdrawals}"
    )

    print(
        f"Transfers Sent     : {transfers_sent}"
    )

    print(
        f"Transfers Received : {transfers_received}"
    )

    print(
        f"PIN Changes        : {pin_changes}"
    )





def show_information(account):

    print(
        "\n=== Account Information ==="
    )


    print(
        f"Owner: {account.owner}"
    )

    print(
        f"Account Number: {account.account_number}"
    )

    print(
        f"Account Type: {account.account_type}"
    )

    print(
        f"Balance: {account.balance:.2f}"
    )

    print(
        f"Account Status: {'Locked' if account.locked else 'Active'}"
    )

    print(
        f"Failed Login Attempts: {account.failed_attempts}"
    )

    print(
        f"Total Transactions: {len(account.transactions)}"
    )

    print(
        f"Created: {account.created_date}"
    )

    print(
        f"Account Note: {account.account_note if account.account_note else 'No note'}"
    )


    show_transaction_statistics(
        account
    )