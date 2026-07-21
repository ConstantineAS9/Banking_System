import math





def get_integer(
    message
):

    """
    Gets a valid integer from the user.
    """

    while True:

        try:

            value = input(
                message
            ).strip()



            if not value:

                print(
                    "Input cannot be empty."
                )

                continue



            return int(
                value
            )



        except ValueError:

            print(
                "Please enter a valid number."
            )



        except EOFError:

            print(
                "\nInput interrupted."
            )





def get_float(
    message
):

    """
    Gets a valid decimal number from the user.
    """

    while True:

        try:

            value = input(
                message
            ).strip()



            if not value:

                print(
                    "Input cannot be empty."
                )

                continue



            number = float(
                value
            )



            if math.isnan(number) or math.isinf(number):

                print(
                    "Enter a valid amount."
                )

                continue



            return number



        except ValueError:

            print(
                "Enter a valid amount."
            )



        except EOFError:

            print(
                "\nInput interrupted."
            )





def get_positive_float(
    message
):

    """
    Gets a positive amount.
    Used for money operations.
    """

    while True:

        amount = get_float(
            message
        )



        if amount <= 0:

            print(
                "Amount must be positive."
            )

            continue



        return amount





def get_choice(
    message,
    minimum,
    maximum
):

    """
    Gets a menu choice inside a range.
    """

    while True:

        choice = get_integer(
            message
        )



        if choice < minimum or choice > maximum:

            print(
                f"Choose a number between {minimum} and {maximum}."
            )

            continue



        return choice