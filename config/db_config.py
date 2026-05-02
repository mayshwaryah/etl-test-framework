# config/db_config.py

from config.env_config import ENV
import mysql.connector

def get_connection():
    if ENV == "DEV":
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Krishna@22",
            database="source_db"
        )

    elif ENV == "QA":
        return mysql.connector.connect(
            host="qa-server",
            user="qa_user",
            password="qa_password",
            database="qa_db"
        )

    elif ENV == "PROD":
        return mysql.connector.connect(
            host="prod-server",
            user="prod_user",
            password="prod_password",
            database="prod_db"
        )

    else:
        raise Exception(f"Invalid ENV: {ENV}")