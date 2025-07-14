 # Generator functions for recurring expenses
 
def rent_generator(amount):
    while True:
        yield {"category": "rent", "amount": amount}
