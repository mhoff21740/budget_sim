
from personal_budget.calculations import total_expenses, remaining_balance, expenses_by_category, filter_expenses_by_catagory
from personal_budget.budget_state import initialize_budget






def print_budget_summary(budget):
    print("\n")
    print("---------- Budget Summary ---------".center(70))
    print(f"Income: {budget['income']}".center(70))
    print(f"Total Expenses: {total_expenses(budget)}".center(70))
    print(f"Remaining Balance: {remaining_balance(budget)}".center(70))
    print("-----------------------------------".center(70))
    print("\n")
    
      
    
def print_expenses_by_category(budget):
    print("\n")
    print("---------- Expenses by Category ----------".center(70))
    expenses = expenses_by_category(budget)
    for category, amount in expenses.items():
        print(f"- {category.capitalize()}: ${amount}".center(70))
    print("------------------------------------------".center(70))
    print("\n")


    
def print_filtered_expenses(expenses):
    print("\n")
    print("---------- Filtered Expenses ----------".center(70))
    if not expenses:
        print("No expenses found".center(70))
    
    else:
        for expense in expenses:
            print(f"- {expense['category']}: ${expense['amount']}".center(70)) 
    print("---------------------------------------".center(70))
    print("\n")
    
    

def view_all_expeneses(budget):
    print("\n")
    print("---------- All Expenses ----------".center(70))
    expenses = budget["expenses"]
    if not expenses:
        print("You have no expenses.".center(70))
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        print(f"- {category}: ${amount}".center(70))
    print("---------------------------------------".center(70))
    print("\n")    
    


