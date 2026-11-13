# HARMONYMUGZ BANK
**YOUR MONEY. YOUR WORLD. YOUR FUTURE.**

Starter repository for four connected areas:
- BANK: customer-facing app
- PARTNER: authorised partner-bank staff portal
- CONTROL: HARMONYMUGZ company administration
- Central website: public information and portal links

## Important safety notice
This is a development prototype, not a licensed bank. It does not connect to real accounts, payment networks or bank ledgers. Use fictional demo data only. Real-money services require an authorised banking/payment partner, regulatory approval, legal and compliance advice, and independent security testing. The partner bank must control balances, the ledger and settlement. Company administrators must never edit bank balances or approve transfers.

## Backend starter
This repository contains a basic Django REST Framework backend and placeholder portal routes. Frontend websites, Flutter mobile apps, authentication, role permissions and bank integrations are not implemented yet.

For a supported Python environment:
1. Install dependencies with `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and set a private random `DJANGO_SECRET_KEY`.
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`

Routes: `/api/health/`, `/api/bank/`, `/api/partner/`, `/api/control/`.

Never commit `.env`, passwords, API keys, private keys, customer information or real banking data.
