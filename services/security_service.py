def validate_pin(pin):

    """
    Validates that a PIN contains exactly 4 digits.
    """

    if not isinstance(
        pin,
        str
    ):

        return False



    pin = pin.strip()



    if len(pin) != 4:

        return False



    if not pin.isdigit():

        return False



    return True





def validate_password(password):

    """
    Placeholder for future admin/user passwords.
    """

    if not isinstance(
        password,
        str
    ):

        return False



    password = password.strip()



    if len(password) < 6:

        return False



    return True





def mask_pin(pin):

    """
    Hides PIN for display purposes.
    Example:
    1234 -> ****
    """

    if not validate_pin(pin):

        return "****"



    return "****"





def check_login_attempts(account):

    """
    Checks whether an account should be locked.
    """

    if account.failed_attempts >= 3:

        account.locked = True

        return False



    return True





def reset_login_attempts(account):

    """
    Resets failed login counter after successful login.
    """

    account.failed_attempts = 0

    return True





def register_failed_attempt(account):

    """
    Adds a failed login attempt and locks account if needed.
    """

    account.failed_attempts += 1



    if account.failed_attempts >= 3:

        account.locked = True

        return True



    return False