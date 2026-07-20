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

        self.created_date = datetime.now().strftime(
            "%Y-%m-%d"
        )

        self.last_processed = None



    def process(self, account):

        if not self.active:

            return False



        if account.balance < self.amount:

            return False



        account.balance -= self.amount



        account.add_transaction(

            "Scheduled Payment",

            f"{self.name}: {self.amount}"

        )


        self.last_processed = datetime.now().strftime(
            "%Y-%m-%d"
        )


        return True



    def cancel(self):

        self.active = False