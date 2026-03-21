# exam 4
print("Welcome to the student data organizer! \n")

student_details = []
tuple = []
stuid_set = set()
sub_set = []

while True:
    print("\nSelect an option:\n 1. Add Student \n 2. Display all student \n 3. Update Student information \n 4. Delete Student \n 5. Display Subject Offered \n 6. Exit ")
    option = int(input("enter choice :"))
    match option:
        case 1:
            student = int(input("How many students do you have? "))

            for i in range(student):
                print(f"-----Enter Student Details : {i + 1} -------")

                while True:
                    stuId = int(input("Student ID: "))
                    if stuId in stuid_set:
                        print("----This ID already exists! Enter a different ID.------")
                    else:
                        stuid_set.add(stuId)
                        break

                name = str(input("Enter name : "))
                Age = int(input("Enter age : "))
                Grade = str(input("Enter grade : "))
                BOD = str(input("Enter Date of Birth(YYYY-MM-DD): ) : "))
                Subject = str(input("Enter subject(comma separated) : "))
                Subject.split(",")
                sub_set.append(
                    {
                        "sub": Subject
                    }
                )
                student_details.append({
                    "id": stuId,
                    "name": name,
                    "age": Age,
                    "grade": Grade,
                    "BOD": BOD,
                    "subject": Subject,
                })
                tuple.append((stuId, BOD))


            continue
        case 2:
            if len(student_details) <= 0 :
                print("Not Found any Student Details!!!")
            else:
                print("-----Display All Student Details-----")
                for i in student_details:
                        print("*************************************************************************************")
                        print(f"Student ID : {i['id']} | Name : {i['name']} | Age : {i['age']} | Grade : {i['grade']} | BOD : {i['BOD']} | Subject : {i['subject']}")
                        print()
        case 3:
            print("---------------------------------------------------------------------------------------")
            if len(student_details) <= 0 :
                print("Not Found any Student Details!!!")
            else:
                print("-----Update student details------")
                id = int(input("Enter Student ID that you want to update: "))

                for stu in student_details or sub_set:
                    if stu["id"] == id:
                        print("1.Update Name\n2.Update Age\n3.Update Grade\n4.Update Subject\n")
                        choice = int(input("Enter choice for update   :"))
                        match choice:
                            case 1:
                                stu["name"] = str(input("\nEnter Student Name : "))
                                print("Name Update Successfully !\n")
                            case 2:
                                stu["age"] = int(input("\nEnter Student Age : "))
                                print("Age Update Successfully !\n")

                            case 3:
                                stu["grade"] = str(input("\nEnter Student Grade : "))
                                print("Grade Update Successfully !\n")

                            case 4:
                                stu["subject"] = str(input("\nEnter Student Subject : "))
                                sub = stu["subject"]
                                print("Subject Update Successfully !\n")
                                sub_set.append(sub)
                            case _:
                                print("Invalid Choice")
                        break
                    else:
                        print("NO Student Found ! Enter a correct Student ID")
                continue
        case 4:
            if len(student_details) <= 0 :
                print("Not Found any Student Details!!!")
            else:
                print("-----Delete student details-----")
                id = int(input("Enter Student ID that you want to delete : "))

                for stu in student_details:
                    if stu["id"] == id:
                        student_details.remove(stu)
                        print("Student Details Deleted Successfully !\n")
                    else :
                        print("Student ID not found")
        case 5:
            if len(student_details) <= 0 :
                print("Not Found any Student Details!!!")
            else:
                print("-----Subject Offered-----")
                subjects = set()

                for entry in sub_set:
                    # if entry is dict → get subject
                    if isinstance(entry, dict):
                        entry = entry["sub"]

                    # now entry is always a string
                    for s in entry.split(","):
                        subjects.add(s.strip())

                print(subjects)

        case 6:
                print("----Thank you Users for using  Student Data Organizer----")
                break
        case _:
                print("Enter valid choice")



