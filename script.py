import mysql.connector
import os

# GitHub Secrets से Environment Variables लोड करें
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

try:
    # MySQL Database से कनेक्ट करें
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=int(DB_PORT),
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    # Cursor बनाएँ
    cursor = conn.cursor()
    
    # Database का नाम प्रिंट करें
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    print(f"✅ Successfully connected to database: {db_name[0]}")
    
    # Connection Close करें
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

