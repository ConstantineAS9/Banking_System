from core.account import BankAccount

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



def account_to_dict(account):

    return {

        "owner": account.owner,

        "balance": account.balance,

        "pin": account.pin,

        "account_number": account.account_number,

        "transactions": account.transactions,

        "failed_attempts": account.failed_attempts,

        "locked": account.locked,

        "created_date": account.created_date,

        "account_note": account.account_note,

        "account_type": account.account_type

    }





def dict_to_account(data):


    if not isinstance(data, dict):

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
            data.get("owner")
        ),

        validate_balance(
            data.get("balance")
        ),

        validate_pin(
            data.get("pin")
        ),

        account_number,

        validate_account_type(
            data.get("account_type")
        )

    )



    account.transactions = validate_transactions(
        data.get("transactions")
    )


    account.failed_attempts = validate_failed_attempts(
        data.get("failed_attempts")
    )


    account.locked = validate_locked(
        data.get("locked")
    )


    account.created_date = validate_string(
        data.get("created_date")
    )


    account.account_note = validate_string(
        data.get("account_note")
    )


    return account