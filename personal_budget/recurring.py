 # Generator functions for recurring expenses
 
def recurring_expense(category,amount):
    while True:
        yield {"category": category, "amount": amount}




