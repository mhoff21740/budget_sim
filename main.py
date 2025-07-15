


from personal_budget.main_workflow_func import main_budget_workflow
from personal_budget.budget_state import initialize_budget, import_budget_from_csv

def main():
    
    print("Welcome to the Budget App!\n")
    print("What would you like to do?")
    while True:
        choice = int(input("1.) Import and exisiting budget\n2.) Start a new budget?\n3.) Exit "))
        if choice not in [1,2,3]:
            print("Invalid selection, please try again")     
        if choice == 1:
            filename = str(input("Please enter the name of the budget file: "))
            budget = import_budget_from_csv(filename)
            main_budget_workflow(budget)
        elif choice == 2:
            try:
                income = int(input("Enter your monthly income (round to the nearest dollar): "))
                if income < 0:
                    print("Income cannot be negative. Please enter a valid number.")
                    continue
                budget = initialize_budget(income)
                print("Budget created successfully!\n")
                main_budget_workflow(budget)
                break  
            except ValueError:
                print("Invalid input. Please enter a valid dollar amount.\n")
        elif choice == 3:
            print("Goodbye!")
            break
                
        

        
        
        

    
    
    
if __name__ == "__main__":
    main()