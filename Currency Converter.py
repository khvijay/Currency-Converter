# Define exchange rates dictionary
exchange_rates = {
    "USD": {"EUR": 0.92, "INR": 78.20, "CAD": 1.28},
    "EUR": {"USD": 1.09, "INR": 145.80, "CAD": 1.40},
    "INR": {"USD": 0.0074, "EUR": 0.0068, "CAD": 0.0093},
    "CAD": {"USD": 0.78, "EUR": 0.71, "INR": 78.50},
}

# Get user input for currencies and amount
from_currency = input("Enter the currency you want to convert from (e.g. USD, EUR): ")
to_currency = input("Enter the currency you want to convert to (e.g. INR, CAD): ")
amount = float(input("Enter the amount to convert: "))

# Check if currencies are valid
if from_currency not in exchange_rates or to_currency not in exchange_rates:
    print("Invalid currency code. Please try again.")
    exit()

# Get the conversion rate (assuming rates are stored for source currency)
rate = exchange_rates[from_currency][to_currency]

# Convert the amount
converted_amount = amount * rate

# Print the result
print(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
