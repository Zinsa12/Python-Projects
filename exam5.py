import statistics

data = []


def input_data():
    print("Enter data for 1D array (separated by spaces or commas)")
    global data
    user_input = input()

    user_input = user_input.replace(",", " ")

    data = list(map(int, user_input.split()))
    return data

def data_summary():
    print("Data Summary:")
    print(f"- Total element: {len(data)}")
    print(f"- Average element: {round(sum(data) / len(data), 2)}")
    print(f"- Maximum value : {max(data)}")
    print(f"- Minimum value : {min(data)}")
    print(f"- Sum of all elements: {sum(data)}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def filter_data(th):
    return list(filter(lambda x: x >= th, data))

def sort_data(data):
    print("Choosing option : \n 1.Ascending\n 2.Descending ")
    option = int(input("Enter your choice : "))
    match option:
        case 1:
            sorted_data = sorted(data)
            print("\nSorted Data in Ascending Order:")
            print(sorted_data)

        case 2:
            sorted_data = sorted(data, reverse=True)
            print("\nSorted Data in Descending Order:")
            print(sorted_data)

        case _:
            print("Invalid option for Sorted Data")

def dataset_statistics():
    minimum = min(data)
    maximum = max(data)
    total = len(data)
    average = total / len(data)
    sum1 = sum(data)
    return minimum, maximum, total, average,sum1


def main():
    print("Welcome to the Data Analyser and Transformer Program")

    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = int(input("Please enter your choice: "))
        match choice:
            case 1:
                   input_data()
                   if data:
                       print("Data Added Successfully!")
                   if not data:
                       print("No Data Added")

            case 2:
                if data:
                    data_summary()
                else:
                    print("Dataset is empty. Please input data first.")

            case 3:
                n =  int(input("Enter factorial number : "))
                if n <= 0:
                    print("Factorial number must be greater than 0.")
                else:
                    fact = factorial(n)
                    print(f"Factorial of {n} is : {fact}")

            case 4:
                if data:
                    th = int(input("Enter threshold value : "))
                    if th:
                        if th >= 0:
                            filter_value = filter_data(th)
                            print(filter_value)
                        else :
                            print("Invalid threshold value")
                    else:
                        print("Enter Threshold value Properly!")

                else:
                    print("Dataset is empty. Please input data first.")

            case 5:
                if data:
                    sort_data(data)
                else:
                    print("Dataset is empty. Please input data first.")

            case 6:
                if data:
                    min1,max1,total,avg,sum1 = dataset_statistics()
                    print("Total element: ", total)
                    print("Average element: ", avg)
                    print("Maximum value : ", max1)
                    print("Minimum value : ", min1)
                    print("Sum of all elements: ", sum1)
                else:
                    print("Dataset is empty. Please input data first.")

            case 7:
                print("Thank you for using Data Analyser and Transformer Program! Goodbye!")
                break
            case _:
                print("Invalid option! Select Proper option again.")

main()