import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():

    conn = psycopg2.connect(
        
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return conn

if __name__ == "__main__":

    conn = get_connection()

    print("Connected Successfully")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name='billing';
    """)
    

    print(cursor.fetchall())

    conn.close()