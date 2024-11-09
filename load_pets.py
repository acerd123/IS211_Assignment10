import sqlite3

def load_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    # Insert data into tables
    cursor.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (1, 'James', 'Smith', 41)")
    cursor.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (2, 'Diana', 'Greene', 23)")
    cursor.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (3, 'Sara', 'White', 27)")
    cursor.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (4, 'William', 'Gibson', 23)")

    cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (1, 'Rusty', 'Dalmation', 4, 1)")
    cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (2, 'Bella', 'AlaskanMalamute', 3, 0)")
    cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (3, 'Max', 'CockerSpaniel', 1, 0)")
    cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (4, 'Rocky', 'Beagle', 7, 0)")
    cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (5, 'Rufus', 'CockerSpaniel', 1, 0)")
    cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (6, 'Spot', 'Bloodhound', 2, 1)")

    cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (1, 1)")
    cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (1, 2)")
    cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (2, 3)")
    cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (2, 4)")
    cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (3, 5)")
    cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (4, 6)")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Data loaded successfully into pets.db")

if __name__ == "__main__":
    print("Running load_pets.py")
    load_data()
