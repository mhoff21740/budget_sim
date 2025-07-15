


from personal_budget.budget_state import initialize_budget, add_income, add_expense, export_expenses_to_csv, import_budget_from_csv
from personal_budget.reporting import *

def main():
    
    print("Welcome to the Budget App!\n")
    print("What would you like to do?")
    choice = int(input("1.) Import and exisiting budget\n 2.) Start a new budget?"))
    if selection not in [1,2]:
        print("Invalid selection, please try again")     
    if selection == 1:
        pass
    income = round(float(input("Enter your monthly income(round to the nearest dollar): ")))
    budget = initialize_budget(income)
    print("Budget created successfully!\n")
    while True: 
        print("What you like to do?")
        selection = int(input(" 1.) View your budget summary?\n 2.) Add income?\n 3.) Add an expense?\n 4.) View Expenses by Category?\n 5.) View all expenses so far?\n 6.) View Remaining Balance?\n 7.) Export expenses?\n 8.) Exit Application?\n"))
        if selection not in [1,2,3,4,5,6,7,8]:
            print("Invalid selection, please select a valid option")
            continue
        if selection == 1:
            print_budget_summary(budget)
        elif selection ==2:
            amount = float((input("How much would you like to add? ")))
            print("Here is your new updated budget summary:")
            budget = add_income(budget, amount)
            print_budget_summary(budget)
        elif selection == 3:
            category= str(input("What is the expense category? "))
            normalized = category.lower()
            amount = int(float(input("What is the amount? ")))
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
            export_expenses_to_csv(budget,"test.csv")
        
        elif selection == 8:
            print("Goodbye!")
            break

        else:
            print("Please select a valid option")
            continue 
            
                           
            
## clean up main, move main loop to standalone function to allow for main loop to handle inports or a fresh budget. Otherwise I will need to create two while loops foir each scenario. 
    
    
    
    
    
if __name__ == "__main__":
    main()