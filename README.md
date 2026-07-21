# Banking System v1.5 Final

A modular console-based banking simulation written in Python.

## Overview

Banking System is a multi-file Python project that simulates a simplified real-world banking environment.

The project focuses on:

- Modular architecture
- Object-oriented programming
- Data persistence
- Security systems
- Financial management systems
- Expandable design

The project uses only Python standard libraries.

---

# Features

## Account Management

Users can:

- Create accounts
- Login with PIN authentication
- Change PIN
- Delete accounts
- Add account notes
- View account information
- Receive notifications

---

# Banking Operations

Supported operations:

- Deposit money
- Withdraw money
- Transfer money between accounts
- View transaction history
- Search transactions
- Generate monthly statements
- View receipts

---

# Account Types

The system supports:

## Basic Account

- Standard limits
- No interest

## Savings Account

- Higher limits
- Interest rewards

## Premium Account

- Highest limits
- Increased interest rewards

Each account type has:

- Deposit limits
- Withdrawal limits
- Interest rates

---

# Security System

Implemented security features:

- PIN validation
- Failed login tracking
- Account locking
- Admin account unlocking

Accounts are automatically locked after multiple failed login attempts.

---

# Bank Card System

Users can:

- Create bank cards
- View card information
- Freeze cards
- Activate cards

---

# Scheduled Payments

Users can:

- Create scheduled payments
- View scheduled payments
- Execute payments
- Delete payments

---

# Loan System

Users can:

- Request loans
- View active loans
- Make loan repayments

Supported loan types:

- Personal
- Business
- Premium

Loan decisions are affected by credit score.

---

# Credit Score System

The system includes:

- Credit score tracking
- Credit rating calculation
- Score improvements from good payments
- Score reduction from late payments

Credit ratings:

- Excellent
- Good
- Average
- Poor

---

# Admin Panel

Administrators can:

- View all accounts
- Search accounts
- View bank statistics
- Apply account interest
- Unlock accounts
- Change account types

---

# Data Storage

The project uses JSON storage.

Accounts are stored in:

The save system automatically:

- Saves account changes
- Loads existing accounts
- Restores account numbers

---

# Project Structure
BankingSystem/
│
├── core/
│ ├── account.py
│ ├── bank.py
│ ├── card.py
│ └── scheduled_payment.py
│
├── services/
│ ├── save_system.py
│ ├── account_serializer.py
│ ├── account_validator.py
│ ├── transaction_service.py
│ ├── security_service.py
│ ├── card_service.py
│ ├── credit_service.py
│ ├── loan_service.py
│ ├── payment_service.py
│ ├── scheduled_payment_service.py
│ └── account_report_service.py
│
├── ui/
│ ├── menus.py
│ ├── input_handler.py
│ ├── receipts.py
│ └── sessions/
│ ├── account_session.py
│ └── admin_session.py
│
├── data/
│ └── accounts.json
│
├── application.py
├── main.py
├── requirements.txt
└── README.md

---

# Requirements

Python: Python 3.10+

External libraries: None
The project uses only the Python standard library.

---

# Running The Program

Open the project folder and run:


python main.py



---

# Version History

## v1.5 Final - Cleanup & Stability Update

Added:

- Code cleanup
- Improved input handling
- Improved UI organization
- Admin save improvements
- Service cleanup
- Better project structure

Fixed:

- Duplicate systems
- Repeated code
- Persistence issues
- UI inconsistencies

---

## v1.4 - Financial Expansion Update

Added:

- Bank card system
- Scheduled payments
- Loan system
- Credit score system
- Notifications

---

## v1.3 - Banking Improvement Update

Added:

- Admin panel
- Account reports
- Account types
- Interest system
- Transaction search

---

## v1.0 - Initial Release

Added:

- Account creation
- Deposits
- Withdrawals
- Transfers
- Login system
- JSON saving

---

# Future Ideas

Possible future expansions:

- Multiple users
- Admin authentication
- Bank branches
- Investment system
- Currency exchange
- International transfers
- Database support
- GUI version

---

# Project Status

Current version: Banking System v1.5 Final

Status: Stable Release