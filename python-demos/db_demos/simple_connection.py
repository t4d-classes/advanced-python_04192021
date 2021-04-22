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
        rates = con.execute("select ClosingDate as closing_date from rates")
        for rate in rates:
            print(rate.closing_date)

if __name__ == "__main__":
    main()
