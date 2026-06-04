import csv

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, amount])

        print("Expense saved successfully!")

    elif choice == "2":
        print("\n--- Expenses ---")

        try:
            with open("expenses.csv", "r") as file:
                reader = csv.reader(file)

                found = False
                for row in reader:
                    print(row[0], "-", row[1])
                    found = True

                if not found:
                    print("No expenses found!")

        except FileNotFoundError:
            print("No expenses found!")

    elif choice == "3":
        total = 0

        try:
            with open("expenses.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    total += float(row[1])

            print("Total Spending =", total)

        except FileNotFoundError:
            print("No expenses found!")

    elif choice == "4":
        expenses = []

        try:
            with open("expenses.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    expenses.append(row)

            if len(expenses) == 0:
                print("No expenses to delete!")
                continue

            print("\n--- Expenses ---")
            for i, expense in enumerate(expenses):
                print(f"{i + 1}. {expense[0]} - {expense[1]}")

            delete_index = int(input("Enter expense number to delete: ")) - 1

            if 0 <= delete_index < len(expenses):
                deleted = expenses.pop(delete_index)

                with open("expenses.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(expenses)

                print(f"{deleted[0]} deleted successfully!")
            else:
                print("Invalid expense number!")

        except FileNotFoundError:
            print("No expenses found!")

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")