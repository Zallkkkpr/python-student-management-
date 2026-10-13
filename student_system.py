import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, name TEXT, course TEXT, marks INTEGER)''')

print("--- Zallkkkpr's Student Management System V2 ---")

while True:
    print("\n1. Add Student\n2. View All\n3. Search\n4. Update Marks\n5. Delete Student\n6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        id = int(input("ID: "))
        name = input("Name: ")
        course = input("Course: ")
        marks = int(input("Marks: "))
        cursor.execute("INSERT INTO students VALUES (?,?,?,?)", (id, name, course, marks))
        conn.commit()
        print("Added!")

    elif choice == '2':
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)

    elif choice == '3':
        s_id = int(input("ID to search: "))
        cursor.execute("SELECT * FROM students WHERE id=?", (s_id,))
        print(cursor.fetchone())

    elif choice == '4':
        s_id = int(input("ID to update: "))
        new_marks = int(input("New Marks: "))
        cursor.execute("UPDATE students SET marks=? WHERE id=?", (new_marks, s_id))
        conn.commit()
        print("Updated!")

    elif choice == '5':
        s_id = int(input("ID to delete: "))
        cursor.execute("DELETE FROM students WHERE id=?", (s_id,))
        conn.commit()
        print("Deleted!")

    elif choice == '6':
        print("Bye! Project by Zallkkkpr")
        break

conn.close()
