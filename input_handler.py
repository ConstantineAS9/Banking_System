import math


def get_integer(message):

    while True:

        try:

            value = int(input(message))

            return value

        except (ValueError, EOFError):

            print("Please enter a valid number.")



def get_float(message):

    while True:

        try:

            value = float(input(message))


            if math.isnan(value) or math.isinf(value):

                print("Enter a valid amount.")

                continue


            return value


        except (ValueError, EOFError):

            print("Enter a valid amount.")