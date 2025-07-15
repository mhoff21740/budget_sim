
from calculations import total_expenses, remaining_balance, expenses_by_category, filter_expenses_by_catagory
from budget_state import initialize_budget



budget = {
    "income": 1500,
    "expenses": [
        {"category": "rent", "amount": 600},
        {"category": "groceries", "amount": 200},
        {"category": "utilities", "amount": 100},
        {"category": "entertainment", "amount": 150},
        {"category": "transportation", "amount": 100}
    ]
}



def print_budget_summary(budget):
    print("---------- Budget Summary ---------".center(70))
    print(f"Income: {budget['income']}".center(70))
    print(f"Total Expenses: {total_expenses(budget)}".center(70))
    print(f"Remaining Balance: {remaining_balance(budget)}".center(70))
    print("-----------------------------------".center(70))
    
      
    
def print_expenses_by_category(budget):
    print("---------- Expenses by Category ----------".center(70))
    expenses = expenses_by_category(budget)
    for category, amount in expenses.items():
        print(f"- {category.capitalize()}: ${amount}".center(70))
    print("------------------------------------------".center(70))


    
def print_filtered_expenses(expenses):
    print("---------- Filtered Expenses ----------".center(70))
    if not expenses:
        print("No expenses found".center(70))
    
    else:
        for expense in expenses:
            print(f"- {expense['category']}: ${expense['amount']}".center(70)) 
    print("---------------------------------------".center(70))
    
    




