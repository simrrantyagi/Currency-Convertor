from converter import convert_currency

print("-----Welcome to the Python Currency Converter-----")

from_currency = input("Enter base currency (e.g. USD, INR, EUR): ").upper()
to_currency = input("Enter target currency (e.g. USD, INR, EUR): ").upper()
amount = float(input(f"Enter amount in {from_currency}: "))

try:
    result = convert_currency(amount, from_currency, to_currency)
    print(f"\n {amount:.2f} {from_currency} = {result:.2f} {to_currency}")
except Exception as e:
    print(" Error:", e)
