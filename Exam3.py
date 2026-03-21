# exam 3
from pywin.mfc.dialog import PrintDialog

print("Welcome to student data Organizer!\n")
Student = []

while True :
    print("""
    Select an option:
    1.Add Student 
    2.Display All Students 
    3.Update Student Information
    4.Delete Student
    5.Display Subjects Offered
    6.Exits
    """)
    num = int(input("Enter your choice : "))
    match num:
            case 1:
                print("Enter student Details : ")
                SID = input("Enter Student ID : ")
                exist = False
                for s in Student:
                    if s['SID'] == SID:
                        exist = True
                        break
                    if exist:
                        print("Student ID already exists!" )
                        continue
                Name = input("Name : ")
                Age = input("Age : ")
                Grade = input("Grade : ")
                BOD = input("Date of Birth(YYYY-MM-DD) : ")
                Subject = set(input("Subject : ").split(","))


                Student_record = {
                    "SID":(SID,BOD),
                    "Name":Name,
                    "Age":Age,
                    "Grade":Grade,
                    "Subject":Subject,
                }
                Student.append(Student_record)
                print("\nStudent Added Sucessfully!\n")

            case 2:
                print("---Dispaly all Students ---")
                if not Student:
                    print("No Students found!\n")
                else:
                    for s in Student:
                        print(f"Student ID :{s['SID'][0]} | Name : {s['Name']} |  Age : {s['Age']} |  Grade : {s['Grade']} | Subject : {s['Subject']}")

            # case 3:
            #     print("---Update Student Information---")
            #     StuID = input("Enter Student ID : ")
            #     for s in Student:
            #         if s['SID'] == StuID:
            #             print("1.Update Age \n 2.Update Subject")
            #             choice = input("Enter your choice : ")
            #             match choice:
            #                 case 1:
            #                     s["Age"] = input("\nEnter new Age : ")
            #                 case 2:
            #                     s["subject"] = input("\nEnter new Subject : ").split(",")
            #             print("Student Updated Sucessfully!\n")
            #         else:
            #             print("Student not found!\n")
            #
            # case 4:
            #     print("---Delete Student---")
            #     StuId = input("Enter Student ID : ")
            #     for s in Student:
            #         if s['SID'] == StuId:
            #             Student.remove(s)
            #             print("Student Deleted Sucessfully!\n")
            #         else:
            #             print("Student not found!\n")
            #
            # case 5:
            #     All_Subject = set()
            #     for s in Student:
            #         All_Subject.update(s['Subject'])
            #         print("\nUnique Subjects Offered:")
            #         for sub in All_Subject:
            #             print("-", sub)
            #         print()
            # case 6:
            #     break