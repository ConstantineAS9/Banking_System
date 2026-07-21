from core.account import BankAccount

from core.card import BankCard

from core.scheduled_payment import ScheduledPayment


from services.account_validator import (
    validate_owner,
    validate_balance,
    validate_account_number,
    validate_pin,
    validate_account_type,
    validate_transactions,
    validate_failed_attempts,
    validate_locked,
    validate_string
)





def account_to_dict(
    account
):

    card_data = None


    if account.card:


        if isinstance(
            account.card,
            BankCard
        ):

            card_data = account.card.to_dict()


        else:

            card_data = account.card





    scheduled_payments = []



    for payment in account.scheduled_payments:


        if isinstance(
            payment,
            ScheduledPayment
        ):

            scheduled_payments.append(
                payment.to_dict()
            )


        else:

            scheduled_payments.append(
                payment
            )





    return {

        "owner": account.owner,

        "balance": account.balance,

        "pin": account.pin,

        "account_number": account.account_number,

        "account_type": account.account_type,

        "transactions": account.transactions,

        "failed_attempts": account.failed_attempts,

        "locked": account.locked,

        "created_date": account.created_date,

        "account_note": account.account_note,

        "card": card_data,

        "scheduled_payments": scheduled_payments,

        "loans": account.loans,

        "credit_score": account.credit_score,

        "notifications": account.notifications

    }





def dict_to_account(
    data
):


    if not isinstance(
        data,
        dict
    ):

        return None





    account_number = data.get(
        "account_number"
    )



    if not validate_account_number(
        account_number
    ):

        return None





    account = BankAccount(

        validate_owner(
            data.get(
                "owner"
            )
        ),

        validate_balance(
            data.get(
                "balance"
            )
        ),

        validate_pin(
            data.get(
                "pin"
            )
        ),

        account_number,

        validate_account_type(
            data.get(
                "account_type"
            )
        )

    )





    account.transactions = validate_transactions(

        data.get(
            "transactions"
        )

    )





    account.failed_attempts = validate_failed_attempts(

        data.get(
            "failed_attempts"
        )

    )





    account.locked = validate_locked(

        data.get(
            "locked"
        )

    )





    account.created_date = validate_string(

        data.get(
            "created_date"
        )

    )





    account.account_note = validate_string(

        data.get(
            "account_note"
        )

    )







    card_data = data.get(
        "card"
    )



    if isinstance(
        card_data,
        dict
    ):


        account.card = BankCard.from_dict(
            card_data
        )


    else:


        account.card = None





    account.scheduled_payments = []



    payments = data.get(
        "scheduled_payments",
        []
    )



    if isinstance(
        payments,
        list
    ):


        for payment_data in payments:



            if isinstance(
                payment_data,
                dict
            ):


                payment = ScheduledPayment.from_dict(
                    payment_data
                )


                if payment:


                    account.scheduled_payments.append(
                        payment
                    )



            else:


                account.scheduled_payments.append(
                    payment_data
                )







    account.loans = data.get(

        "loans",

        []

    )



    if not isinstance(
        account.loans,
        list
    ):

        account.loans = []





    account.credit_score = data.get(

        "credit_score",

        600

    )



    if not isinstance(
        account.credit_score,
        int
    ):

        account.credit_score = 600





    account.notifications = data.get(

        "notifications",

        []

    )



    if not isinstance(
        account.notifications,
        list
    ):

        account.notifications = []





    return account