import copy

# Core state and pure functions


#Creates a new budget dict with given income
def initialize_budget(income=0):
    categories = []
    return {"income": income, "expenses": categories}



def add_income(budget, amount):
    updated_budget = copy.deepcopy(budget)
    updated_budget["income"] = amount
    return updated_budget


def add_expense(budget, category, amount):
    new_expense = copy.deepcopy(budget)
    new_expense["expenses"].append({"category": category, "amount":amount})
    return new_expense

    

