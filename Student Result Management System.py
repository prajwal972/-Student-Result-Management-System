students = {}

def calculate_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 45:
        return "C"
    else:
        return "Fail"

while True:
    print("\n--- Student Result Management System ---")
    print("1. Add Student")
    print("2. View Student Result")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Student Name: ")
            m1 = int(input("Enter marks for Subject 1: "))
            m2 = int(input("Enter marks for Subject 2: "))
            m3 = int(input("Enter marks for Subject 3: "))

            total = m1 + m2 + m3
            percentage = total / 3
            grade = calculate_grade(percentage)

            students[roll] = {
                "name": name,
                "marks": [m1, m2, m3],
                "total": total,
                "percentage": percentage,
                "grade": grade
            }

            print("Student added successfully!")
    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            s = students[roll]
            print("\nName:", s["name"])
            print("Marks:", s["marks"])
            print("Total:", s["total"])
            print("Percentage:", s["percentage"])
            print("Grade:", s["grade"])
        else:
            print("Student not found!")
    elif choice == "3":
        roll = input("Enter Roll Number: ")

        if roll in students:
            m1 = int(input("Enter new marks for Subject 1: "))
            m2 = int(input("Enter new marks for Subject 2: "))
            m3 = int(input("Enter new marks for Subject 3: "))

            total = m1 + m2 + m3
            percentage = total / 3
            grade = calculate_grade(percentage)

            students[roll]["marks"] = [m1, m2, m3]
            students[roll]["total"] = total
            students[roll]["percentage"] = percentage
            students[roll]["grade"] = grade

            print("Marks updated successfully!")
        else:
            print("Student not found!")
    elif choice == "4":
        roll = input("Enter Roll Number: ")

        if roll in students:
            del students[roll]
            print("Student record deleted!")
        else:
            print("Student not found!")
    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Please try again.")
