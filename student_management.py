students = []


def add_student():
    try:
        student_id = int(input("Enter student ID: "))

        for student in students:
            if student["id"] == student_id:
                print("Student ID already exists.")
                return

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade
        }

        students.append(student)
        print("Student added successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("--------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grade:", student["grade"])


def search_student():
    try:
        student_id = int(input("Enter student ID to search: "))

        for student in students:
            if student["id"] == student_id:
                print("Student found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grade:", student["grade"])
                return

        print("Student not found.")

    except ValueError:
        print("Invalid student ID.")


def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))

        for student in students:
            if student["id"] == student_id:
                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))
                student["grade"] = input("Enter new grade: ")

                print("Student updated successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid student ID.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")

    except ValueError:
        print("Please enter a number from 1 to 6.")