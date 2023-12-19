from MySQLdb.cursors import DictCursor
import MySQLdb
import os
from dotenv import load_dotenv
load_dotenv()


def get_database_connection():
    return MySQLdb.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        passwd=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        autocommit=True,
        ssl_mode="VERIFY_IDENTITY",
        cursorclass=DictCursor,
        ssl={
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    )


def load_jobs_from_db(id=-1):
    connection = get_database_connection()
    cursor = connection.cursor()

    if id == -1:
        cursor.execute("SELECT * FROM jobs")
    else:
        cursor.execute("SELECT * FROM jobs WHERE id = %s", (id,))

    # Fetch the results if needed
    results = cursor.fetchall()

    # for row in results:
    # print(row) # Do something with the retrieved data

    # Close the cursor and connection when done
    cursor.close()
    connection.close()

    return results
