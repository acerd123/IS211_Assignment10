import sqlite3

# Connect to (or create) the pets.db database
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER,
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (pet_id) REFERENCES pet(id)
);
''')

# Commit and close connection
conn.commit()
conn.close()

print("pets.db has been created with the appropriate tables.")
