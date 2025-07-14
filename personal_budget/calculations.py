 # FP utilities: totals, filters, forecasts
import functools 
from collections import defaultdict


def total_expenses(budget):
    total_expenses = sum((map(lambda e: e["amount"], budget["expenses"])))
    return total_expenses

    
    
    

def remaining_balance(budget):
    return budget["income"] - total_expenses(budget)




def update_totals(totals, expense):
    category = expense["category"]
    amount = expense["amount"]

    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

    return totals




def expenses_by_category(budget):
    expenses = budget["expenses"]
    totals = functools.reduce(lambda totals, expense: update_totals(totals, expense), expenses, {} )
    
    return totals





def filter_expenses_by_catagory(budget, category):
    filtered_list = list(filter(lambda expense: expense["category"] == category, budget["expenses"]))
    return filtered_list



    

    

