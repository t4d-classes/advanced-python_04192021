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

        with con.cursor() as cur:
            cur.execute("select * from rates")

            print(cur.fetchone())     
            print(cur.fetchall())     

if __name__ == "__main__":
    main()

