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
    "depends": ["base", "account"],
    "data": [
        "views/partner.xml",
        "views/bank.xml",
        "data/account_chart.xml",
        "data/account.account.template.csv",
        "data/account_chart_template.xml",
        "data/account_tax_template.xml",
        "data/account_chart_template_data.xml",
    ],
}
