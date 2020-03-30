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
        user='postgres',
        password='intranet2020',
        host='intranet-sandbox-db-instance-v1.cvudwjs0pws7.eu-west-2.rds.amazonaws.com',
        port="5432",
        database='intranet_sandbox_db',

    )

    return connection
