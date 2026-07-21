from datetime import datetime, timedelta
import random


class BankCard:

    def __init__(
        self,
        account_number,
        card_number=None,
        expiry_date=None,
        cvv=None,
        active=True
    ):

        self.account_number = account_number

        self.card_number = (
            card_number
            if card_number
            else self.generate_card_number()
        )

        self.expiry_date = (
            expiry_date
            if expiry_date
            else self.generate_expiry_date()
        )

        self.cvv = (
            cvv
            if cvv
            else self.generate_cvv()
        )

        self.active = active



    def generate_card_number(self):

        number = ""

        for _ in range(16):

            number += str(
                random.randint(0, 9)
            )

        return number



    def generate_cvv(self):

        return str(
            random.randint(
                100,
                999
            )
        )



    def generate_expiry_date(self):

        expiry = (
            datetime.now()
            + timedelta(days=365 * 5)
        )

        return expiry.strftime(
            "%m/%Y"
        )



    def freeze(self):

        self.active = False



    def activate(self):

        self.active = True



    def is_active(self):

        return self.active



    def show_card(self):

        print(
            "\n==================================="
        )

        print(
            "             BANK CARD"
        )

        print(
            "==================================="
        )

        print(
            f"Card Number : {self.card_number}"
        )

        print(
            f"Expiry Date : {self.expiry_date}"
        )

        print(
            f"CVV         : {self.cvv}"
        )

        print(
            f"Status      : {'Active' if self.active else 'Frozen'}"
        )

        print(
            "==================================="
        )



    def to_dict(self):

        return {

            "account_number": self.account_number,

            "card_number": self.card_number,

            "expiry_date": self.expiry_date,

            "cvv": self.cvv,

            "active": self.active

        }



    @classmethod
    def from_dict(
        cls,
        data
    ):

        if not isinstance(
            data,
            dict
        ):

            return None


        return cls(

            account_number=data.get(
                "account_number"
            ),

            card_number=data.get(
                "card_number"
            ),

            expiry_date=data.get(
                "expiry_date"
            ),

            cvv=data.get(
                "cvv"
            ),

            active=data.get(
                "active",
                True
            )

        )