import requests

def get_exchange_rates(base_currency):
    """Fetch live exchange rates for the given base currency."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error fetching data from API")

    data = response.json()
    return data["rates"]

def convert_currency(amount, from_currency, to_currency):
    """Convert amount from one currency to another using live rates."""
    rates = get_exchange_rates(from_currency)
    if to_currency.upper() not in rates:
        raise ValueError("Invalid target currency code")

    converted_amount = amount * rates[to_currency.upper()]
    return converted_amount
