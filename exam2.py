print("Welcome to the Pattern Genrate and Number Analyzer!")

option = None
while True:
    print("\nSelect an option:")
    print(" 1.Genrate a Pattern \n 2.Analyze a range of Numbers \n 3.Exit")
    option = int(input("Enter your Choice : "))
    print()
    match option:
     case 1:
         row= int(input("Enter the number of Rows for the pattern : "))
         print("\nPattern:")
         for i in range(1,row+1):
            for j in range(i):
                 print("*",end=" ")
            print()
     case 2:
         start = int(input("Enter the Start of the Range : "))   
         end = int(input("Enter the end of the Range  : "))
         total = 0
         for i in range(start,end+1):
             if i %2 == 0:
                 print(f"Number {i} is Even.")
             else:
                 print(f"Number {i} is Odd.")
             total += i
         print(f"Sum of all numbers from {start} to {end} is : {total}")
     case 3:
        print("Exit the Program.Goodbye! \n")
        break
