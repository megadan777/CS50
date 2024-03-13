def buy_coke():
    # Coke price in cents
    coke_price = 50
    amount_due = coke_price

    while amount_due > 0:
        # Prompt user to insert coins until amount_due is zero
        inserted_amount = int(input(f"Amount Due: {amount_due} cents - Insert Coin (25/10/5 cents): "))

        # Check if the inserted amount is valid
        if inserted_amount in [25, 10, 5]:
            amount_due -= inserted_amount
            if amount_due > 0:
                print(f"Your change is {amount_due} cents.")
            else:
                print("Change Owed: 0 cents.")
        else:
            print(f"Invalid amount. Please insert a valid coin.")

    print("Thank you for purchasing. Enjoy your Coke!")

# Call the function to start the Coke purchase process
buy_coke()