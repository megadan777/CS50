#User can only input 25 cents, 10 cents, and 5 cents.
inserted_amount = int(input("Buy a Coke - Insert Coin: "))

#Coke is 50 cents
coke_price = 50

# Calculate change
change = inserted_amount - coke_price

# Print the initial change
print(f"Your change is {change} cents.")

# Loop to decrement change until it reaches zero
while change > 0:
    # Decrement by 1 cent in each iteration
    change -= 1
    print(f"Remaining change: {change} cents.")

print("Change has been fully dispensed.")