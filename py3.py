import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, description, category):
        expense = {
            'amount': amount,
            'description': description,
            'category': category,
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully.")

    def get_monthly_summary(self, month, year):
        monthly_expenses = [expense for expense in self.expenses if datetime.strptime(expense['date'], '%Y-%m-%d').month == month and datetime.strptime(expense['date'], '%Y-%m-%d').year == year]
        total = sum(expense['amount'] for expense in monthly_expenses)
        return total, monthly_expenses

    def get_category_summary(self, category):
        category_expenses = [expense for expense in self.expenses if expense['category'] == category]
        total = sum(expense['amount'] for expense in category_expenses)
        return total, category_expenses

    def run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Monthly Summary")
            print("3. View Category Summary")
            print("4. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                try:
                    amount = float(input("Enter amount: "))
                    description = input("Enter description: ")
                    category = input("Enter category: ")
                    self.add_expense(amount, description, category)
                except ValueError:
                    print("Invalid input. Please enter numeric value for amount.")
            elif choice == '2':
                try:
                    month = int(input("Enter month (1-12): "))
                    year = int(input("Enter year (e.g., 2023): "))
                    total, expenses = self.get_monthly_summary(month, year)
                    print(f"\nMonthly Summary for {month}/{year}")
                    print(f"Total Expenses: ${total:.2f}")
                    for expense in expenses:
                        print(expense)
                except ValueError:
                    print("Invalid input. Please enter numeric values for month and year.")
            elif choice == '3':
                category = input("Enter category: ")
                total, expenses = self.get_category_summary(category)
                print(f"\nCategory Summary for {category}")
                print(f"Total Expenses: ${total:.2f}")
                for expense in expenses:
                    print(expense)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
