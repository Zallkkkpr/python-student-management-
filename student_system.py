import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, name TEXT, course TEXT, marks INTEGER)''')

print("--- Zallkkkpr's Student Management System ---")

while True:
    print("\n1. Add Student\n2. View All Students\n3. Search Student\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        id = int(input("ID: "))
        name = input("Name: ")
        course = input("Course (BCA etc): ")
        marks = int(input("Marks: "))
        cursor.execute("INSERT INTO students VALUES (?,?,?,?)", (id, name, course, marks))
        conn.commit()
        print("Student Added Successfully!")

    elif choice == '2':
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif choice == '3':
        s_id = int(input("Enter ID to search: "))
        cursor.execute("SELECT * FROM students WHERE id=?", (s_id,))
        print(cursor.fetchone())

    elif choice == '4':
        print("Thank you! Project by Zallkkkpr")
        break

conn.close()
