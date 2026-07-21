from datetime import datetime

from core.scheduled_payment import ScheduledPayment



def create_scheduled_payment(
    account,
    name,
    amount,
    day
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



    if not hasattr(
        account,
        "scheduled_payments"
    ):

        account.scheduled_payments = []



    payment = ScheduledPayment(

        name.strip(),

        amount,

        day

    )



    account.scheduled_payments.append(
        payment
    )



    account.add_transaction(

        "Scheduled Payment Created",

        f"{name}: {amount}"

    )



    account.add_notification(

        "Scheduled Payment",

        f"Scheduled payment '{name}' created."

    )



    print(
        "Scheduled payment created successfully."
    )



    return True





def show_scheduled_payments(
    account
):


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



        status = (

            "Active"

            if payment.active

            else "Cancelled"

        )



        print(

            f"{index}. "

            f"{payment.name} | "

            f"Amount: {payment.amount:.2f} | "

            f"Day: {payment.day} | "

            f"Status: {status}"

        )





def execute_payment(
    account,
    index
):


    if (

        index < 1

        or index > len(account.scheduled_payments)

    ):

        print(
            "Invalid payment."
        )

        return False





    payment = account.scheduled_payments[index - 1]



    if not payment.active:

        print(
            "Payment is cancelled."
        )

        return False





    if account.balance < payment.amount:

        print(
            "Insufficient funds."
        )

        return False





    account.balance -= payment.amount



    account.add_transaction(

        "Scheduled Payment",

        f"{payment.name}: {payment.amount}"

    )



    account.add_notification(

        "Payment Completed",

        f"Scheduled payment '{payment.name}' completed."

    )



    payment.last_processed = datetime.now().strftime(

        "%Y-%m-%d"

    )



    print(
        "Scheduled payment executed."
    )



    return True





def delete_scheduled_payment(
    account,
    index
):


    if (

        index < 1

        or index > len(account.scheduled_payments)

    ):

        print(
            "Invalid payment."
        )

        return False





    payment = account.scheduled_payments.pop(

        index - 1

    )



    account.add_transaction(

        "Scheduled Payment Deleted",

        payment.name

    )



    account.add_notification(

        "Scheduled Payment",

        f"Scheduled payment '{payment.name}' deleted."

    )



    print(
        "Scheduled payment deleted."
    )



    return True





def process_all_scheduled_payments(
    account
):


    if not hasattr(
        account,
        "scheduled_payments"
    ):

        return False



    processed = False



    for payment in account.scheduled_payments:


        if payment.process(account):

            processed = True





    return processed