import copy
import csv

# Core state and pure functions


#Creates a new budget dict with given income
def initialize_budget(income=0):
    return {"income": income, "expenses": []}



def add_income(budget, amount):
    updated_budget = copy.deepcopy(budget)
    updated_budget["income"] += amount
    return updated_budget


def add_expense(budget, category, amount):
    new_expense = copy.deepcopy(budget)
    new_expense["expenses"].append({"category": category, "amount":amount})
    return new_expense

def export_expenses_to_csv(budget, filename="expenses.csv"):
    expenses = budget["expenses"]
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount"])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print(f"Expenses exported successfully to {filename}")
    
    

def import_budget_from_csv(filename):
    with open(filename, mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

        # Get income from the first row
        if rows[0][0].lower() == "income":
            income = float(rows[0][1])
            expense_rows = rows[2:]  # Skip income and header rows
        else:
            raise ValueError("CSV must start with income row.")

        # Build expenses list
        expenses = [{"category": row[0], "amount": float(row[1])} for row in expense_rows]

    return {"income": income, "expenses": expenses}



