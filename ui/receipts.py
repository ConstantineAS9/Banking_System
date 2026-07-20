def show_deposit_receipt(
    account,
    amount
):

    print(
        "\n==================================="
    )

    print(
        "        DEPOSIT RECEIPT"
    )

    print(
        "==================================="
    )


    print(
        f"Account : {account.account_number}"
    )

    print(
        f"Amount  : {amount:.2f}"
    )

    print(
        f"Balance : {account.balance:.2f}"
    )

    print(
        "Status  : SUCCESS"
    )


    print(
        "==================================="
    )





def show_withdrawal_receipt(
    account,
    amount
):

    print(
        "\n==================================="
    )

    print(
        "       WITHDRAWAL RECEIPT"
    )

    print(
        "==================================="
    )


    print(
        f"Account : {account.account_number}"
    )

    print(
        f"Amount  : {amount:.2f}"
    )

    print(
        f"Balance : {account.balance:.2f}"
    )


    print(
        "==================================="
    )





def show_interest_payment(
    account,
    interest
):

    print(
        "\n==================================="
    )

    print(
        "        INTEREST PAYMENT"
    )

    print(
        "==================================="
    )


    print(
        f"Account  : {account.account_number}"
    )

    print(
        f"Interest : {interest:.2f}"
    )

    print(
        f"Balance  : {account.balance:.2f}"
    )


    print(
        "==================================="
    )





def show_account_type_change(
    old_type,
    new_type
):

    print(
        "\n==================================="
    )

    print(
        "      ACCOUNT TYPE CHANGED"
    )

    print(
        "==================================="
    )


    print(
        f"Previous Type : {old_type}"
    )

    print(
        f"New Type      : {new_type}"
    )


    print(
        "==================================="
    )