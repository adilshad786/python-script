import mysql.connector

conn = mysql.connector.connect(
    host="65.19.154.90",  # अपने सर्वर का सही IP डालें
    port=3306,            # MySQL का सही पोर्ट दें
    user="dilshadhost_786",
    password="M#BZ.J5QSqMvh9w",  # अपने डेटाबेस का सही पासवर्ड डालें
    database="dilshadhost_786"
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")
print("Connected successfully to:", cursor.fetchone())

conn.close()
