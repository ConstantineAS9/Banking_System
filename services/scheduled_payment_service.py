from datetime import datetime


def create_scheduled_payment(
    account,
    name,
    amount,
    receiver
):

    if not isinstance(name, str) or not name.strip():

        print(
            "Payment name cannot be empty."
        )

        return False



    if not isinstance(amount, (int, float)):

        print(
            "Invalid amount."
        )

        return False



    if amount <= 0:

        print(
            "Amount must be positive."
        )

        return False



    payment = {

        "name": name.strip(),

        "amount": amount,

        "receiver": receiver.strip(),

        "created": datetime.now().strftime(
            "%Y-%m-%d"
        )

    }



    account.scheduled_payments.append(
        payment
    )



    account.add_transaction(

        "Scheduled Payment Created",

        f"{name} - {amount}"

    )



    print(
        "Scheduled payment created."
    )


    return True





def show_scheduled_payments(account):


    print(
        "\n=== Scheduled Payments ==="
    )



    if not account.scheduled_payments:

        print(
            "No scheduled payments."
        )

        return



    for index, payment in enumerate(
        account.scheduled_payments,
        start=1
    ):


        print(

            f"{index}. "
            f"{payment['name']} | "
            f"{payment['amount']:.2f} | "
            f"To: {payment['receiver']}"

        )





def execute_payment(
    account,
    index
):


    if index < 1 or index > len(account.scheduled_payments):

        print(
            "Invalid payment."
        )

        return False



    payment = account.scheduled_payments[index - 1]



    amount = payment["amount"]



    if amount > account.balance:

        print(
            "Insufficient funds."
        )

        return False



    account.balance -= amount



    account.add_transaction(

        "Scheduled Payment",

        f"Paid {payment['name']} amount {amount}"

    )



    print(
        "Payment completed."
    )



    account.scheduled_payments.pop(index - 1)



    return True





def delete_scheduled_payment(
    account,
    index
):


    if index < 1 or index > len(account.scheduled_payments):

        print(
            "Invalid payment."
        )

        return False



    payment = account.scheduled_payments.pop(
        index - 1
    )


    account.add_transaction(

        "Scheduled Payment Deleted",

        payment["name"]

    )



    print(
        "Scheduled payment deleted."
    )


    return True