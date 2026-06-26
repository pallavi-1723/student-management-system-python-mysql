from db import connect_db

# Add Student
def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    course = input("Enter Course: ")
    email = input("Enter Email: ")

    query = """
    INSERT INTO students(name, age, gender, course, email)
    VALUES(%s, %s, %s, %s, %s)
    """

    values = (name, age, gender, course, email)

    cursor.execute(query, values)
    conn.commit()

    print("Student Added Successfully!")

    conn.close()


# View Students
def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\n----- STUDENT RECORDS -----")

    for student in students:
        print(student)

    conn.close()


# Search Student
def search_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE student_id=%s",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print(student)
    else:
        print("Student Not Found")

    conn.close()


# Update Student
def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    new_course = input("Enter New Course: ")

    cursor.execute(
        """
        UPDATE students
        SET course=%s
        WHERE student_id=%s
        """,
        (new_course, student_id)
    )

    conn.commit()

    print("Student Updated Successfully!")

    conn.close()


# Delete Student
def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE student_id=%s",
        (student_id,)
    )

    conn.commit()

    print("Student Deleted Successfully!")

    conn.close()


# Menu
def menu():

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()