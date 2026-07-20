from datetime import datetime

from services.credit_service import (
    increase_credit_score,
    decrease_credit_score
)



LOAN_TYPES = {

    "Personal": {
        "interest": 0.05,
        "max": 10000
    },

    "Business": {
        "interest": 0.08,
        "max": 50000
    },

    "Premium": {
        "interest": 0.03,
        "max": 100000
    }

}





def create_loan(
    account,
    loan_type,
    amount
):


    if loan_type not in LOAN_TYPES:

        print(
            "Invalid loan type."
        )

        return False
    
    if account.credit_score < 450:

        print(
            "Loan rejected. Credit score too low."
        )

        return False



    rules = LOAN_TYPES[loan_type]



    if amount <= 0:

        print(
            "Loan amount must be positive."
        )

        return False



    if amount > rules["max"]:

        print(
            "Loan exceeds maximum limit."
        )

        return False



    interest = amount * rules["interest"]



    total = amount + interest



    loan = {

        "type": loan_type,

        "amount": amount,

        "interest": interest,

        "remaining": total,

        "created": datetime.now().strftime(
            "%Y-%m-%d"
        )

    }



    account.loans.append(
        loan
    )


    account.balance += amount



    account.add_transaction(

        "Loan Received",

        f"{loan_type} loan {amount}"

    )


    increase_credit_score(
        account,
        5
    )



    print(
        "Loan approved."
    )


    return True





def show_loans(account):


    print(
        "\n=== LOANS ==="
    )



    if not account.loans:

        print(
            "No active loans."
        )

        return



    for index, loan in enumerate(

        account.loans,

        start=1

    ):


        print(

            f"{index}. "
            f"{loan['type']} | "
            f"Original: {loan['amount']:.2f} | "
            f"Remaining: {loan['remaining']:.2f}"

        )





def pay_loan(
    account,
    index,
    amount
):


    if index < 1 or index > len(account.loans):

        print(
            "Invalid loan."
        )

        return False



    loan = account.loans[index - 1]



    if amount <= 0:

        print(
            "Invalid payment."
        )

        return False



    if amount > account.balance:

        print(
            "Not enough money."
        )

        return False



    if amount > loan["remaining"]:

        amount = loan["remaining"]



    account.balance -= amount



    loan["remaining"] -= amount



    account.add_transaction(

        "Loan Payment",

        f"Paid loan {amount}"

    )


    increase_credit_score(
        account,
        2
    )



    if loan["remaining"] <= 0:

        account.loans.pop(
            index - 1
        )

        print(
            "Loan fully paid."
        )


    else:

        print(
            "Loan payment successful."
        )


    return True


def mark_late_payment(
    account,
    index
):


    if index < 1 or index > len(account.loans):

        print(
            "Invalid loan."
        )

        return False



    loan = account.loans[index - 1]


    decrease_credit_score(
        account,
        20
    )


    account.add_transaction(

        "Late Loan Payment",

        f"Late payment on {loan['type']} loan"

    )


    print(
        "Late payment recorded."
    )


    return True