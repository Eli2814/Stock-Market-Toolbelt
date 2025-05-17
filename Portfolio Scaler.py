def get_portfolio():
    portfolio = []
    while True:
        ticker = input("Enter ticker symbol (or 'done' to finish): ")
        if ticker.lower() == 'done':
            break
        shares = float(input(f"Enter number of shares for {ticker}: "))
        price_per_share = float(input(f"Enter current price per share for {ticker}: "))
        portfolio.append({'ticker': ticker, 'shares': shares, 'price_per_share': price_per_share})
    return portfolio

def calculate_portfolio_value(portfolio):
    total_value = sum(stock['shares'] * stock['price_per_share'] for stock in portfolio)
    return total_value

def scale_portfolio(original_portfolio, original_value, target_value):
    scale_factor = target_value / original_value
    scaled_portfolio = []
    for stock in original_portfolio:
        scaled_shares = stock['shares'] * scale_factor
        scaled_portfolio.append({
            'ticker': stock['ticker'],
            'original_shares': stock['shares'],
            'scaled_shares': scaled_shares,
            'price_per_share': stock['price_per_share'],
            'total_value': scaled_shares * stock['price_per_share']
        })
    return scaled_portfolio

def main():
    print("Enter your original portfolio details:")
    original_portfolio = get_portfolio()
    original_value = calculate_portfolio_value(original_portfolio)

    target_value = float(input("Enter the target portfolio value: "))

    scaled_portfolio = scale_portfolio(original_portfolio, original_value, target_value)

    print("\nScaled Portfolio:")
    for stock in scaled_portfolio:
        print(f"{stock['ticker']}: {stock['scaled_shares']} shares at ${stock['price_per_share']} per share (Total: ${stock['total_value']:.2f})")

    total_scaled_value = sum(stock['total_value'] for stock in scaled_portfolio)
    remainder = target_value - total_scaled_value
    print(f"\nTotal Scaled Portfolio Value: ${total_scaled_value:.2f}")
    print(f"Remainder: ${remainder:.2f}")

if __name__ == "__main__":
    main()
