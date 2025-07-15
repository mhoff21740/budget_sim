# Category filters / categorization logic
def filter_by_category(expenses, category):
    return list(filter(lambda e: e["category"] == category, expenses))



def filter_above_amount(expenses, min_amount):
    return list(filter(lambda e: e["amount"] >= min_amount,expenses))

