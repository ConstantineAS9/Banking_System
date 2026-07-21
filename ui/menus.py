def print_header(
    title
):

    print(
        "\n" + "=" * 40
    )

    print(
        title.center(40)
    )

    print(
        "=" * 40
    )





def show_menu():

    print_header(
        "BANKING SYSTEM"
    )


    print(
        "1. Create Account"
    )

    print(
        "2. Login"
    )

    print(
        "3. Admin Panel"
    )

    print(
        "4. Exit"
    )





def show_account_menu():

    print_header(
        "ACCOUNT MENU"
    )


    print(
        "--- Banking Operations ---"
    )

    print(
        "1. Deposit Money"
    )

    print(
        "2. Withdraw Money"
    )

    print(
        "3. Transfer Money"
    )

    print(
        "4. Check Balance"
    )

    print(
        "5. Transaction History"
    )

    print(
        "6. Search Transactions"
    )



    print(
        "\n--- Account Management ---"
    )

    print(
        "7. Change PIN"
    )

    print(
        "8. Account Information"
    )

    print(
        "9. Account Note"
    )

    print(
        "10. Delete Account"
    )

    print(
        "11. Change Account Type"
    )



    print(
        "\n--- Reports & Security ---"
    )

    print(
        "12. Monthly Statement"
    )

    print(
        "13. Notifications"
    )



    print(
        "\n--- Card System ---"
    )

    print(
        "14. Create Bank Card"
    )

    print(
        "15. Show Card"
    )

    print(
        "16. Block Card"
    )

    print(
        "17. Unblock Card"
    )



    print(
        "\n--- Scheduled Payments ---"
    )

    print(
        "18. Create Scheduled Payment"
    )

    print(
        "19. Show Scheduled Payments"
    )

    print(
        "20. Execute Scheduled Payment"
    )

    print(
        "21. Delete Scheduled Payment"
    )



    print(
        "\n--- Loan System ---"
    )

    print(
        "22. Request Loan"
    )

    print(
        "23. Show Loans"
    )

    print(
        "24. Pay Loan"
    )



    print(
        "\n25. Logout"
    )





def show_admin_menu():

    print_header(
        "ADMIN PANEL"
    )


    print(
        "1. Show All Accounts"
    )

    print(
        "2. Search Accounts"
    )

    print(
        "3. Bank Statistics"
    )

    print(
        "4. Apply Interest"
    )

    print(
        "5. Unlock Account"
    )

    print(
        "6. Change Account Type"
    )

    print(
        "7. Back"
    )