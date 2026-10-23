all_students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # CREATE
    if choice == "1":
        student_id = input("Enter Student ID: ")

        if student_id in all_students:
            print("Student ID already exists!")
        else:
            name = input("Enter Student Name: ")
            district = input("Enter District: ")
            dept = input("Enter Department: ")

            all_students[student_id] = {
                "Name": name,
                "District": district,
                "Dept": dept
            }

            print("Student added successfully!")

    # READ ALL
    elif choice == "2":
        if not all_students:
            print("No student records found.")
        else:
            for student_id, student in all_students.items():
                print("\nStudent ID:", student_id)
                print("Name:", student["Name"])
                print("District:", student["District"])
                print("Department:", student["Dept"])

    # SEARCH
    elif choice == "3":
        student_id = input("Enter Student ID: ")
        student = all_students.get(student_id)

        if student is not None:
            print("Name:", student["Name"])
            print("District:", student["District"])
            print("Department:", student["Dept"])
        else:
            print("Student not found!")

    # UPDATE
    elif choice == "4":
        student_id = input("Enter Student ID to update: ")

        if student_id in all_students:
            name = input("Enter new name: ")
            district = input("Enter new district: ")
            dept = input("Enter new department: ")

            all_students[student_id]["Name"] = name
            all_students[student_id]["District"] = district
            all_students[student_id]["Dept"] = dept

            print("Student updated successfully!")
        else:
            print("Student not found!")

    # DELETE
    elif choice == "5":
        student_id = input("Enter Student ID to delete: ")

        if student_id in all_students:
            del all_students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # EXIT
    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Try again.")