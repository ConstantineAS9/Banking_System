from core.card import BankCard





def create_card(
    account
):

    if account.card is not None:

        print(
            "Account already has a card."
        )

        return None





    account.card = BankCard(

        account.account_number

    )





    account.add_transaction(

        "Card Created",

        f"New card issued: {account.card.card_number}"

    )





    account.add_notification(

        "Card",

        "A new bank card has been issued."

    )





    print(
        "Card created successfully."
    )



    return account.card







def show_card(
    account
):

    if account.card is None:

        print(
            "No card assigned to this account."
        )

        return False





    account.card.show_card()



    return True







def freeze_card(
    account
):

    if account.card is None:

        print(
            "No card assigned."
        )

        return False





    if not account.card.active:

        print(
            "Card is already frozen."
        )

        return False





    account.card.freeze()





    account.add_transaction(

        "Card Frozen",

        "Bank card frozen"

    )





    account.add_notification(

        "Card",

        "Your bank card has been frozen."

    )





    print(
        "Card frozen successfully."
    )



    return True







def activate_card(
    account
):

    if account.card is None:

        print(
            "No card assigned."
        )

        return False





    if account.card.active:

        print(
            "Card is already active."
        )

        return False





    account.card.activate()





    account.add_transaction(

        "Card Activated",

        "Bank card activated"

    )





    account.add_notification(

        "Card",

        "Your bank card has been activated."

    )





    print(
        "Card activated successfully."
    )



    return True







def get_card_status(
    account
):

    if account.card is None:

        return "No Card"



    if account.card.active:

        return "Active"



    return "Frozen"