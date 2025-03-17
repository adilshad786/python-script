import mysql.connector



cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")
print("Connected successfully to:", cursor.fetchone())

conn.close()
