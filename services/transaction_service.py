from datetime import datetime



def add_transaction(
    account,
    category,
    message
):


    if (

        not isinstance(category, str)

        or not category.strip()

    ):

        return False



    if (

        not isinstance(message, str)

        or not message.strip()

    ):

        return False



    transaction = {

        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "category": category.strip(),

        "message": message.strip()

    }



    account.transactions.append(
        transaction
    )



    return True





def show_transactions(account):


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