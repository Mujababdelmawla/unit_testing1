def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficeint Funds...!!")
    return balance - amount 