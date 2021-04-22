""" simple connection module """

import pyodbc

local_trust_conn_options = [
    "DRIVER={ODBC Driver 17 for SQL Server}",
    "SERVER=localhost\\SQLExpress",
    "DATABASE=ratesapp",
    "Trusted_Connection=yes",
]

conn_string = ";".join(local_trust_conn_options)

def main() -> None:
    """ main """

    with pyodbc.connect(conn_string) as con:
        rates = con.execute("select * from rates")

        for rate in rates:
            print(rate)

if __name__ == "__main__":
    main()
    