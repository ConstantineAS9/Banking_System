from core.scheduled_payment import ScheduledPayment



def add_scheduled_payment(
    account,
    name,
    amount,
    day
):

    if not hasattr(
        account,
        "scheduled_payments"
    ):

        account.scheduled_payments = []



    payment = ScheduledPayment(

        name,

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


    print(
        "Scheduled payment added successfully."
    )


    return payment





def show_scheduled_payments(account):

    if not hasattr(
        account,
        "scheduled_payments"
    ) or not account.scheduled_payments:


        print(
            "No scheduled payments."
        )

        return



    print(
        "\n=== Scheduled Payments ==="
    )


    for index, payment in enumerate(
        account.scheduled_payments,
        start=1
    ):


        print(

            f"{index}. "
            f"{payment.name} | "
            f"{payment.amount:.2f} | "
            f"Day: {payment.day} | "
            f"Status: {'Active' if payment.active else 'Cancelled'}"

        )





def process_payments(account):

    if not hasattr(
        account,
        "scheduled_payments"
    ):

        return



    for payment in account.scheduled_payments:

        payment.process(
            account
        )





def cancel_payment(
    account,
    index
):

    if not hasattr(
        account,
        "scheduled_payments"
    ):

        return False



    if index < 0 or index >= len(
        account.scheduled_payments
    ):

        return False



    account.scheduled_payments[index].cancel()



    account.add_transaction(
        "Scheduled Payment Cancelled",
        "Payment cancelled"
    )


    return True