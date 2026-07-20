import math



def validate_owner(owner):

    if not isinstance(owner, str):

        return "Unknown"


    owner = owner.strip()


    if not owner:

        return "Unknown"


    return owner





def validate_balance(balance):

    if (

        not isinstance(balance, (int, float))

        or isinstance(balance, bool)

        or math.isnan(balance)

        or math.isinf(balance)

        or balance < 0

    ):

        return 0



    return balance





def validate_account_number(account_number):

    return (

        isinstance(account_number, int)

        and not isinstance(account_number, bool)

        and account_number > 0

    )





def validate_pin(pin):

    if (

        not isinstance(pin, str)

        or len(pin) != 4

        or not pin.isdigit()

    ):

        return "0000"



    return pin





def validate_account_type(account_type):

    valid_types = [

        "Basic",

        "Savings",

        "Premium"

    ]


    if account_type not in valid_types:

        return "Basic"



    return account_type





def validate_transactions(transactions):

    if not isinstance(transactions, list):

        return []


    return transactions





def validate_failed_attempts(value):

    if (

        not isinstance(value, int)

        or isinstance(value, bool)

        or value < 0

    ):

        return 0



    return value





def validate_locked(value):

    if not isinstance(value, bool):

        return False



    return value





def validate_string(value):

    if not isinstance(value, str):

        return ""


    return value