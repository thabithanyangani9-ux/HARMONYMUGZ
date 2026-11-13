# Architecture and security boundaries
- BANK: customer experience; display only bank-verified information.
- PARTNER: bank staff workflows; access controlled by the partner bank.
- CONTROL: company operations; cannot change bank-held balances or approve transfers.
- Website: public information, disclosures, support and portal links.

Before any real launch: implement role-based access, MFA, HTTPS, audit logs, secret management, backups, monitoring, incident response and independent security testing. Never store PINs, CVVs or full card numbers. Integrate only through an authorised partner-bank API.
