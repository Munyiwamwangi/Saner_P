import psycopg2

from simple_salesforce import Salesforce
from Sanergy.settings import (SALESFORCE_USERNAME,
                              SALESFORCE_SECURITY_TOKEN,
                              SALESFORCE_PASSWORD,
                              SALESFORCE_DOMAIN)


def salesforcelogin():
    return Salesforce(
        username=SALESFORCE_USERNAME,
        password=SALESFORCE_PASSWORD,
        security_token=SALESFORCE_SECURITY_TOKEN,
        domain=SALESFORCE_DOMAIN
    )


def postgressConnection():
    connection = psycopg2.connect(
        user="intradmin",
        password="sanergy123",
        host="127.0.0.1",
        port="5432",
        database="intranetsarnergy"

    )

    return connection
