from bank import withdraw
 
balance = 100 

try:
    print(f"the current available balance is : ${balance}")

    amount = 200 

    print(f"the amount to be withdrawed is : ${amount}")

    balance = withdraw(amount, balance)

    print(f"the new available balance is : ${balance}")

except ValueError as e:
    
    print(f"Error : {e}")