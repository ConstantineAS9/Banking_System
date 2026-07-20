# Banking System v1.4

A modular console-based banking simulation written in Python.

## Overview

Banking System is a multi-file Python project that simulates the core functionality of a real banking environment.

The project focuses on modular design, data persistence, security, and expandable banking features.

## Features

### Account Management

* Create bank accounts
* Login with PIN authentication
* Account locking after failed attempts
* Delete accounts
* Change PIN
* Account notes
* Account information display

### Banking Operations

* Deposit money
* Withdraw money
* Transfer money between accounts
* Transaction history
* Transaction search
* Monthly statements
* Receipts

### Account Types

The system supports:

* Basic Account
* Savings Account
* Premium Account

Each account type has different:

* Deposit limits
* Withdrawal limits
* Interest rates

### Security System

* PIN validation
* Failed login tracking
* Account locking
* Admin account unlocking

### Card System

Added in v1.4:

* Create bank cards
* View card information
* Block cards
* Unblock cards

### Scheduled Payments

Added in v1.4:

* Scheduled payment support
* Automated payment system foundation

### Loan System

Added in v1.4:

* Loan management
* Loan tracking
* Repayment system foundation

### Credit Score System

Added in v1.4:

* Customer financial reputation
* Credit evaluation foundation
* Loan decision support

### Admin Panel

Administrators can:

* View all accounts
* Search accounts
* View bank statistics
* Apply interest
* Unlock accounts
* Change account types

## Data Storage

The project uses JSON-based storage.

Account data is stored in:

```
data/accounts.json
```

The save system automatically stores and loads account information.

## Project Structure

```
BankingSystem/

│
├── core/
│   ├── account.py
│   └── bank.py
│
├── services/
│   ├── save_system.py
│   ├── account_serializer.py
│   ├── account_validator.py
│   ├── transaction_service.py
│   ├── security_service.py
│   └── account_report_service.py
│
├── ui/
│   ├── menus.py
│   ├── input_handler.py
│   ├── receipts.py
│   └── sessions/
│       ├── account_session.py
│       └── admin_session.py
│
├── data/
│   └── accounts.json
│
├── application.py
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.10+

No external libraries are required.

## Running The Program

Run:

```
python main.py
```

## Version History

## v1.4 - Financial Expansion Update

Added:

* Bank card system
* Scheduled payments
* Loan system
* Credit score system

## v1.3 - Banking Improvement Update

Added:

* Admin panel
* Reports
* Account types
* Interest system
* Transaction search

## v1.0 - Initial Release

Added:

* Account creation
* Deposits
* Withdrawals
* Transfers
* Login system
* JSON saving
