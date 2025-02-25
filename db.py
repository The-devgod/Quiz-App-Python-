import sqlite3

conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Create a new table without the 'Country' column
cursor.execute('''
    CREATE TABLE IF NOT EXISTS new_userSignUp (
        FULLNAME TEXT,
        USERNAME TEXT,
        PASSWORD TEXT
    )
''')


conn.commit()
conn.close()

print("Database Created successfully!")
