import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", c.fetchall())
try:
    c.execute("SELECT * FROM bookings")
    print("Bookings:", c.fetchall())
except Exception as e:
    print("Error:", e)
conn.close()