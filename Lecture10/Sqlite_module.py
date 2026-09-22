import sqlite3

DB_FILE = 'mydatabase.db'

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

# Recreate the table so the script works even if the database was created earlier
# with a different schema.
cur.execute('DROP TABLE IF EXISTS users')
cur.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL
    )
''')

cur.execute("INSERT INTO users (name, age, city) VALUES (?, ?, ?)", ('Alice', 25, 'New York'))
cur.execute("INSERT INTO users (name, age, city) VALUES (?, ?, ?)", ('Bob', 30, 'Los Angeles'))
cur.execute("INSERT INTO users (name, age, city) VALUES (?, ?, ?)", ('Charlie', 35, 'Chicago'))

conn.commit()
cur.execute("SELECT * FROM users WHERE age > 28")
rows = cur.fetchall()

print("Users older than 28:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, City: {row[3]}")

conn.close()