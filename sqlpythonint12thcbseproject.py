import sqlite3

mydb = sqlite3.connect("Students_records.db")
cursor = mydb.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY, 
    name varchar(20), 
    grade varchar(20), 
    marks INTEGER
)''')

while True:
    print("\n1. Add Student 2. View Students 3. Exit")
    choice = int(input("Choice: "))
    if choice == 3:
        break
    elif choice == 1:
        roll_no = int(input("Roll No: "))
        cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
        if cursor.fetchone():
            print("Error: Roll No already exists!")
        else:
            name = input("Name: ")
            grade = input("Grade: ")
            marks = int(input("Marks: "))
            cursor.execute("INSERT INTO students (roll_no, name, grade, marks) VALUES (?, ?, ?, ?)", (roll_no, name, grade, marks))
            mydb.commit()
            print("Student added successfully.")
    elif choice == 2:
        cursor.execute("SELECT * FROM students")
        for r in cursor.fetchall():
            print("Roll No: " + str(r[0]) + ", Name: " + r[1] + ", Grade: " + r[2] + ", Marks: " + str(r[3]))
    else:
        print("Invalid choice!")

mydb.close()
