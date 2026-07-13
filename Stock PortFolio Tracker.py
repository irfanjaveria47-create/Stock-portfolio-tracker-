# Stock Portfolio Tracker

prices = {
    "AAPL": 150,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 2800,
    "AMZN": 3400
}

portfolio = []
total_investment = 0

print("Welcome to Stock Portfolio Tracker")
print("-" * 40)
print("Available Stocks and Prices:")
for stock, price in prices.items():
    print(f"{stock}: ${price}")

print("-" * 40)

while True:
    stock_name = input("Enter stock symbol (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in prices:
        print("Invalid stock symbol. Please choose from the available list.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = prices[stock_name]
    value = price * quantity
    total_investment += value

    portfolio.append({
        "Stock": stock_name,
        "Price": price,
        "Quantity": quantity,
        "Value": value
    })

    print(f"Added {quantity} shares of {stock_name}. Value = ${value}")
    print("-" * 40)

print("Portfolio Summary")
print("-" * 40)

for item in portfolio:
    print(f"{item['Stock']}: Price = ${item['Price']}, Quantity = {item['Quantity']}, Value = ${item['Value']}")

print("-" * 40)
print(f"Total Investment: ${total_investment}")

with open("portfolio_report.txt", "w") as f:
    f.write("Stock Portfolio Tracker Report")
    f.write("=" * 40 + "")
    for item in portfolio:
        f.write(f"{item['Stock']}: Price = ${item['Price']}, Quantity = {item['Quantity']}, Value = ${item['Value']}")
    f.write("-" * 40 + "")
    f.write(f"Total Investment: ${total_investment}")

print("Report saved to portfolio_report.txt")