""" simple connection module """

import pyodbc

local_trust_conn_options = [
    "DRIVER={ODBC Driver 17 for SQL Server}",
    "SERVER=localhost\\SQLExpress",
    "DATABASE=ratesapp",
    "Trusted_Connection=yes",
]

# local_docker_conn_options = [
#     "DRIVER={ODBC Driver 17 for SQL Server}",
#     "SERVER=localhost,11433",
#     "DATABASE=ratesapp",
#     "UID=sa",
#     "PWD=sqlDbp@ss!"
# ]

# local_azure_conn_options = [
#     "DRIVER={ODBC Driver 17 for SQL Server}",
#     "SERVER=ewgpythonclass.database.windows.net",
#     "DATABASE=rates",
#     "UID=dbuser",
#     "PWD=sqlDbp@ss!"
# ]

conn_string = ";".join(local_trust_conn_options)

def main() -> None:
    """ main """

    with pyodbc.connect(conn_string) as con:

        lots_of_rates = [
            ('2021-01-07', 'EUR', 0.9),
            ('2021-01-08', 'EUR', 0.8),
            ('2021-01-09', 'EUR', 0.7),
            ('2021-01-10', 'EUR', 0.9),
            ('2021-01-11', 'EUR', 0.85),
        ]

        sql = " ".join([
            "insert into rates (ClosingDate, CurrencySymbol, ExchangeRate)",
            "values (?, ?, ?)",
        ])

        # for rate in lots_of_rates:
        #     con.execute(sql, rate)

        with con.cursor() as cur:
            cur.executemany(sql, lots_of_rates)            

if __name__ == "__main__":
    main()
