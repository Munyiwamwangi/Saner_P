import psycopg2

def postgressConnection():
    connection = psycopg2.connect(
        user="intradmin",
        password="sanergy123",
        host="127.0.0.1",
        port="5432",
        database="intranetsarnergy"

    )

    return connection