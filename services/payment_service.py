from core.scheduled_payment import ScheduledPayment





def add_scheduled_payment(
    account,
    name,
    amount,
    day
):


    if not isinstance(
        name,
        str
    ) or not name.strip():

        print(
            "Payment name cannot be empty."
        )

        return None





    if not isinstance(
        amount,
        (int, float)
    ):

        print(
            "Invalid payment amount."
        )

        return None





    if amount <= 0:

        print(
            "Payment amount must be positive."
        )

        return None





    if not isinstance(
        day,
        int
    ):

        print(
            "Invalid payment day."
        )

        return None





    if day < 1 or day > 31:

        print(
            "Payment day must be between 1 and 31."
        )

        return None





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
        "Scheduled payment added successfully."
    )



    return payment







def show_scheduled_payments(
    account
):


    if not hasattr(
        account,
        "scheduled_payments"
    ) or not account.scheduled_payments:


        print(
            "No scheduled payments."
        )

        return





    print(
        "\n==================================="
    )

    print(
        "       SCHEDULED PAYMENTS"
    )

    print(
        "==================================="
    )





    for index, payment in enumerate(

        account.scheduled_payments,

        start=1

    ):


        if isinstance(
            payment,
            ScheduledPayment
        ):


            print(

                f"{index}. "

                f"{payment.name} | "

                f"{payment.amount:.2f} | "

                f"Day: {payment.day} | "

                f"Status: {'Active' if payment.active else 'Cancelled'}"

            )



        else:


            print(
                f"{index}. Invalid payment data"
            )







def process_payments(
    account
):


    if not hasattr(
        account,
        "scheduled_payments"
    ):

        return





    for payment in account.scheduled_payments:


        if isinstance(
            payment,
            ScheduledPayment
        ):

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





    if index < 1 or index > len(
        account.scheduled_payments
    ):

        print(
            "Invalid payment."
        )

        return False





    payment = account.scheduled_payments[
        index - 1
    ]





    if not isinstance(
        payment,
        ScheduledPayment
    ):

        return False





    payment.cancel()





    account.add_transaction(

        "Scheduled Payment Cancelled",

        payment.name

    )





    account.add_notification(

        "Scheduled Payment",

        f"Scheduled payment '{payment.name}' cancelled."

    )





    print(
        "Scheduled payment cancelled."
    )



    return True







def activate_payment(
    account,
    index
):


    if not hasattr(
        account,
        "scheduled_payments"
    ):

        return False





    if index < 1 or index > len(
        account.scheduled_payments
    ):

        return False





    payment = account.scheduled_payments[
        index - 1
    ]





    if not isinstance(
        payment,
        ScheduledPayment
    ):

        return False





    payment.activate()





    return True