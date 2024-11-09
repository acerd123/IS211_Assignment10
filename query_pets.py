import sqlite3

def query_person_pets(person_id):
    
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cursor.fetchone()

    if person:
        first_name, last_name, age = person
        print(f"{first_name} {last_name}, {age} years old")

        
        cursor.execute("""
            SELECT pet.name, pet.breed, pet.age 
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        """, (person_id,))
        pets = cursor.fetchall()

        if pets:
            for pet in pets:
                pet_name, pet_breed, pet_age = pet
                print(f"{first_name} owned {pet_name}, a {pet_breed} that was {pet_age} years old")
        else:
            print(f"{first_name} has no pets.")
    else:
        print("Person not found.")

    
    conn.close()

def main():
    while True:
        person_id = int(input("Enter person ID (-1 to exit): "))
        if person_id == -1:
            break
        query_person_pets(person_id)

if __name__ == "__main__":
    print("Running query_pets.py")
    main()
