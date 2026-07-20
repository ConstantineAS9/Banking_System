from core.card import BankCard



def create_card(account):

    if hasattr(account, "card") and account.card:

        print(
            "Account already has a card."
        )

        return None



    account.card = BankCard(
        account.account_number
    )


    account.add_transaction(
        "Card Created",
        f"Card issued: {account.card.card_number}"
    )


    print(
        "Card created successfully."
    )


    return account.card





def show_card(account):

    if not hasattr(account, "card") or account.card is None:

        print(
            "No card assigned to this account."
        )

        return



    account.card.show_card()





def freeze_card(account):

    if not hasattr(account, "card") or account.card is None:

        print(
            "No card assigned."
        )

        return False



    account.card.freeze()


    account.add_transaction(
        "Card Frozen",
        "Bank card frozen"
    )


    print(
        "Card frozen successfully."
    )


    return True





def activate_card(account):

    if not hasattr(account, "card") or account.card is None:

        print(
            "No card assigned."
        )

        return False



    account.card.activate()


    account.add_transaction(
        "Card Activated",
        "Bank card activated"
    )


    print(
        "Card activated successfully."
    )


    return True