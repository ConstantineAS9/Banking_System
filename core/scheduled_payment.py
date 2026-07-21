from datetime import datetime


class ScheduledPayment:

    def __init__(
        self,
        name,
        amount,
        day,
        active=True
    ):

        self.name = name

        self.amount = amount

        self.day = day

        self.active = active

        self.created_date = (
            datetime.now().strftime(
                "%Y-%m-%d"
            )
        )

        self.last_processed = None



    def process(
        self,
        account
    ):

        if not self.active:

            return False



        if self.amount <= 0:

            return False



        if account.balance < self.amount:

            return False



        account.balance -= self.amount



        account.add_transaction(

            "Scheduled Payment",

            f"{self.name}: {self.amount}"

        )



        account.add_notification(

            "Scheduled Payment",

            f"Payment '{self.name}' of {self.amount:.2f} completed."

        )



        self.last_processed = (
            datetime.now().strftime(
                "%Y-%m-%d"
            )
        )


        return True



    def cancel(self):

        self.active = False



    def activate(self):

        self.active = True



    def is_active(self):

        return self.active



    def to_dict(self):

        return {

            "name": self.name,

            "amount": self.amount,

            "day": self.day,

            "active": self.active,

            "created_date": self.created_date,

            "last_processed": self.last_processed

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



        payment = cls(

            name=data.get(
                "name",
                "Unknown"
            ),

            amount=data.get(
                "amount",
                0
            ),

            day=data.get(
                "day",
                1
            ),

            active=data.get(
                "active",
                True
            )

        )


        payment.created_date = data.get(
            "created_date",
            payment.created_date
        )


        payment.last_processed = data.get(
            "last_processed"
        )


        return payment