# -*- coding: utf-8 -*-
{
    "name": "russian_requisites",
    "summary": """
        Adds russian respecific requisites for juridical and physical persons""",
    "description": """Adds next requisites:\n
        - Passport series and number,\n
        - Passport issue date,\n
        - Department issued the passport,\n
        - IEC - Industrial Enterprises Classifier,\n
        - PSRN - Primary State Registration Number,\n
        - OKPO - All-Russian Classifier of Enterprises and Organizations,\n
        - Bank corresponding account.
    """,
    "author": "RYDLAB",
    "website": "https://rydlab.ru",
    "category": "Localization",
    "version": "1.0",
    "depends": ["base"],
    "data": [
        "views/partner.xml",
        "views/bank.xml",
    ],
}
