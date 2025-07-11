# Core state and pure functions



def initialize_budget(income=0):
    categories = [
        {"category": "rent", "amount": 400},
        {"category": "groceries", "amount": 150},
        {"category": "utilities", "amount": 100},
        {"category": "transportation", "amount": 75},
        {"category": "insurance", "amount": 100},
        {"category": "entertainment", "amount": 50},
        {"category": "subscriptions", "amount": 50},
        {"category": "miscellaneous", "amount": 75}
    ]

    return {"income": income, "expenses": categories}





"""  FUTURE USE 

def initialize_budget(income=0):
    Creates a new budget dict with given income
    return {"income": income, "expenses": []} """



def add_income(budget, amount):
    updated_budget = budget.copy()
    updated_budget = initialize_budget(amount)
    return updated_budget 


def add_expense(budget, category, amount):
    new_expense = budget.copy()
    new_expense.update({"category": category, "amount":amount})
    return new_expense

    
    
    """Returns new budget state with added expense"""
    ...

print(add_expense(initialize_budget(1000),"cheese", 100))