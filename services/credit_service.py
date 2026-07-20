def increase_credit_score(
    account,
    amount
):


    account.credit_score += amount



    if account.credit_score > 850:

        account.credit_score = 850





def decrease_credit_score(
    account,
    amount
):


    account.credit_score -= amount



    if account.credit_score < 300:

        account.credit_score = 300





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





def show_credit_score(
    account
):


    print(
        "\n=== CREDIT SCORE ==="
    )


    print(
        f"Score: {account.credit_score}"
    )


    print(
        f"Rating: {get_credit_rating(account.credit_score)}"
    )