expenses = []

def add_expense(category, amount):
    # Add a new expense with category & amount
    expense = {
        "category": category,
        "amount": amount
    }        
    expenses.append(expense)
    print(f"\n✅ Added: {category.capitalize()} - ${amount:.2f}\n")

def total_expense():
    # Return total spent amount
    if not expenses:
        print("Empty list...")
    else:
        total = sum(exp["amount"] for exp in expenses)
        print(f"💰 Total Spent Amount: ${total:.2f}\n")

def show_category():
    # Display all added expenses
    if not expenses:
        print("Sorry! No records found :(")
    else:    
        print("\n== Added Expenses ==\n")
        for i, exp in enumerate(expenses, start=1):
            print(f"Item {i}: {exp['category']} - ${exp['amount']:.2f}\n")

def high_exp():
    # Return highest spent amount expense
    if not expenses:
        return None
    else:
        return max(expenses, key=lambda x: x["amount"])

def main():
    while True:
        print("\n\t*** Personal Expense Tracker ***")
        print("\nChoose any of the following options:\n")
        print("1. Add Expense")
        print("2. Total Spent")
        print("3. View All Expenses")
        print("4. Highest Expense")
        print("5. Exit\n")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Please enter a valid number (1–5).")
            continue

        if choice == 1:
            category = input("Enter Expense (food/travel): ").strip().capitalize()
            try:
                amount = float(input("Enter Amount: "))
                add_expense(category, amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == 2:
            total_expense()

        elif choice == 3:
            show_category()

        elif choice == 4:
            high = high_exp()
            if high:
                print(f"\n🏆 Highest expense: {high['category']} - ${high['amount']:.2f}")
            else:
                print("No expenses recorded yet...")

        elif choice == 5:
            print("👋 Exiting... Have a great day!")
            break

        else:
            print("❌ Invalid choice, please select from 1–5.")

if __name__ == '__main__':
    main()
