import matplotlib.pyplot as plt

print("===== Expense Tracker =====")

total = 0

food_total = 0
travel_total = 0
shopping_total = 0


while True:

    print("\n1. Add Expense")
    print("2. View Total Expenses")
    print("3. Show Expense Chart")
    print("4. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":

        amount = int(input("Enter expense amount: "))

        category = input(
            "Enter category (Food/Travel/Shopping): "
        )

        total = total + amount
        
        if category.lower() == "food":
            food_total = food_total + amount
        elif category.lower() == "travel":
            travel_total = travel_total + amount
        elif category.lower() == "shopping":
            shopping_total = shopping_total + amount
        
        file = open("expenses.txt", "a")
        file.write(
            "Expense: " + str(amount) +
            " | Category: " + category + "\n"
        )
        file.close()
        print("Expense added successfully!")

    elif choice == "2":

        print("\nTotal Expenses:", total)

    elif choice == "3":

        categories = ["Food", "Travel", "Shopping"]

        amounts = [
            food_total,
            travel_total,
            shopping_total
        ]

        plt.bar(categories, amounts)
        plt.title("Expense Tracker")
        plt.xlabel("Categories")
        plt.ylabel("Amount Spent")
        plt.show()


    elif choice == "4":
        print("Exiting Expense Tracker...")
        break
    else:
        print("Invalid choice. Please try again.")