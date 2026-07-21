def print_receipt_header(
    title
):

    print(
        "\n" + "=" * 40
    )

    print(
        title.center(40)
    )

    print(
        "=" * 40
    )





def print_receipt_footer():

    print(
        "=" * 40
    )





def show_deposit_receipt(
    account,
    amount
):

    print_receipt_header(
        "DEPOSIT RECEIPT"
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


    print_receipt_footer()





def show_withdrawal_receipt(
    account,
    amount
):

    print_receipt_header(
        "WITHDRAWAL RECEIPT"
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


    print_receipt_footer()





def show_interest_payment(
    account,
    interest
):

    print_receipt_header(
        "INTEREST PAYMENT"
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
        "Status   : SUCCESS"
    )


    print_receipt_footer()





def show_account_type_change(
    old_type,
    new_type
):

    print_receipt_header(
        "ACCOUNT TYPE CHANGED"
    )


    print(
        f"Previous Type : {old_type}"
    )

    print(
        f"New Type      : {new_type}"
    )

    print(
        "Status        : SUCCESS"
    )


    print_receipt_footer()