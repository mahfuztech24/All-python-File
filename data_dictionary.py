first_dictionary={
    "Student":"Mahfuz",
    "Age":"32",
    "Grade":"5"
}

print(first_dictionary)
print(first_dictionary["Student"])
print(first_dictionary.get("Age"))
print(first_dictionary.fromkeys(first_dictionary,10))


student={
    "Name":"Mahfuz","E-mail":"mahfuz.tech24@gmail.com"
}
if student.get("E-mail") is None:
    print("E-mail is not Providen")
else:
    print(student.get("E-mail"))

    all_students={
        "3000":{"Name":"Mahfuzur Rahman","District":"Mymensing","Dept":"CST"},
        "3001":{"Name":"Nadim Mohammad Nasim","District":"Mymensing","Dept":"EEE"}
    }
    student_id=input("Enter Student ID:")
    students=all_students.get(student_id)

    if students is not None:
        print("Student Name",students.get("Name","Name not Found"))
        print("Department",students.get("Dept","Name not Found"))
    else:
        print("Student not Found")
        