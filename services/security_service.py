def validate_pin(pin):

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