from datetime import datetime



def add_transaction(
    account,
    category,
    message
):

    """
    Adds a transaction entry to an account.
    """

    if not isinstance(
        category,
        str
    ) or not category.strip():

        return False



    if not isinstance(
        message,
        str
    ) or not message.strip():

        return False



    transaction = {

        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "category": category.strip(),

        "message": message.strip()

    }



    if not hasattr(
        account,
        "transactions"
    ):

        account.transactions = []



    account.transactions.append(
        transaction
    )



    return True





def show_transactions(
    account
):

    """
    Displays transaction history.
    """

    print(
        "\n=== Transaction History ==="
    )



    if not account.transactions:

        print(
            "No transactions yet."
        )

        return





    for transaction in account.transactions:


        if isinstance(
            transaction,
            dict
        ):


            print(

                f"{transaction.get('timestamp', 'Unknown')} | "

                f"{transaction.get('category', 'Unknown')} | "

                f"{transaction.get('message', '')}"

            )


        else:

            print(
                transaction
            )





def get_transactions_by_category(
    account,
    category
):

    """
    Returns transactions matching a category.
    """

    if not isinstance(
        category,
        str
    ):

        return []



    category = category.lower().strip()



    results = []



    for transaction in account.transactions:


        if not isinstance(
            transaction,
            dict
        ):

            continue



        current_category = transaction.get(
            "category",
            ""
        ).lower()



        if current_category == category:

            results.append(
                transaction
            )



    return results





def count_transactions(
    account
):

    """
    Returns total transaction count.
    """

    if not hasattr(
        account,
        "transactions"
    ):

        return 0



    return len(
        account.transactions
    )