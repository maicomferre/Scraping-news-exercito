import mysql.connector as mysql
import dotenv
import os

dotenv.load_dotenv()


def db_update_news(title, category, link, text)-> None:

    myl = mysql.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DB"),
    )

    cursor = myl.cursor()
