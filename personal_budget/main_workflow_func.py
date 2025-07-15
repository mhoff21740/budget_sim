 

from personal_budget.budget_state import  add_income, add_expense, export_budget_to_csv
from personal_budget.reporting import *
 
 
 
def main_budget_workflow(budget):
    while True: 
        print("What you like to do?")
        try:
            selection = int(input(" 1.) View your budget summary?\n 2.) Add income?\n 3.) Add an expense?\n 4.) View Expenses by Category?\n 5.) View all expenses so far?\n 6.) View Remaining Balance?\n 7.) Export expenses?\n 8.) Exit Application?\n"))
        except ValueError:
            print("Invalid input, please select a number from one of the options.")
            continue
        if selection not in [1,2,3,4,5,6,7,8]:
            print("Invalid selection, please select a valid option")
            continue
        if selection == 1:
            print_budget_summary(budget)
        elif selection ==2:
            try:
                amount = int((input("How much would you like to add? ")))
            except ValueError:
                print("Invalid input, please enter a dollar amount.\n")
                continue
            print("Here is your new updated budget summary:")
            budget = add_income(budget, amount)
            print_budget_summary(budget)
        elif selection == 3:
            category= str(input("What is the expense category? "))
            normalized = category.lower()
            try:
                amount = int(float(input("What is the amount? ")))
            except ValueError:
                print("Invalid input, please enter a dollar amount.\n")
                continue
            budget = add_expense(budget, normalized, amount)
            reamaining = remaining_balance(budget)
            print(f"\nYou now have ${reamaining} left to spend.\n")
        elif selection == 4:
            category = str((input("Which expense category would you like to view?")))
            normalized_cat = category.lower()
            categories = [e["category"] for e in budget["expenses"]]
            if normalized_cat not in categories:
                print("This category is not valid or in your list\n")
                continue
            filtered_list = filter_expenses_by_catagory(budget, normalized_cat)
            print_filtered_expenses(filtered_list)
        
        elif selection == 5:
            view_all_expeneses(budget)
            
        elif selection == 6:
            reamaining = remaining_balance(budget)
            print(f"\nYou now have ${reamaining} left to spend.\n")
        
        elif selection ==7:
            filename = input("Please enter a name for your file: ")
            file = filename + ".csv"
            export_budget_to_csv(budget,file)
        
        elif selection == 8:
            print("Goodbye!")
            break

        else:
            print("Please select a valid option")
            continue