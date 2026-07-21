MIN_CREDIT_SCORE = 300

MAX_CREDIT_SCORE = 850





def increase_credit_score(
    account,
    amount
):

    if not isinstance(
        amount,
        int
    ):

        return False



    if amount <= 0:

        return False





    account.credit_score += amount





    if account.credit_score > MAX_CREDIT_SCORE:

        account.credit_score = MAX_CREDIT_SCORE





    return True







def decrease_credit_score(
    account,
    amount
):

    if not isinstance(
        amount,
        int
    ):

        return False



    if amount <= 0:

        return False





    account.credit_score -= amount





    if account.credit_score < MIN_CREDIT_SCORE:

        account.credit_score = MIN_CREDIT_SCORE





    return True







def set_credit_score(
    account,
    score
):

    if not isinstance(
        score,
        int
    ):

        return False





    if score < MIN_CREDIT_SCORE:

        score = MIN_CREDIT_SCORE



    if score > MAX_CREDIT_SCORE:

        score = MAX_CREDIT_SCORE





    account.credit_score = score



    return True







def get_credit_rating(
    score
):

    if score >= 750:

        return "Excellent"



    elif score >= 650:

        return "Good"



    elif score >= 550:

        return "Average"



    else:

        return "Poor"









def can_receive_loan(
    account
):

    return account.credit_score >= 450







def show_credit_score(
    account
):

    print(
        "\n==================================="
    )

    print(
        "          CREDIT SCORE"
    )

    print(
        "==================================="
    )



    print(
        f"Score  : {account.credit_score}"
    )



    print(
        f"Rating : {get_credit_rating(account.credit_score)}"
    )



    print(
        "==================================="
    )