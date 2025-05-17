def calculate_dca(total_investment, investment_period, frequency, initial_price):
    investment_intervals = investment_period * frequency
    investment_per_interval = total_investment / investment_intervals
    investment_amounts = []
    total_invested = []
    price_at_interval = []
    shares_purchased = []
    total_shares = []
    portfolio_value = []
    
    cumulative_investment = 0
    cumulative_shares = 0
    price_change = 0.02  # Example fixed price change for each interval

    for i in range(investment_intervals):
        investment_amounts.append(investment_per_interval)
        cumulative_investment += investment_per_interval
        total_invested.append(cumulative_investment)

        # Simulate price at interval with a deterministic change
        if i % 2 == 0:
            simulated_price = initial_price * (1 + price_change * (i // 2))
        else:
            simulated_price = initial_price * (1 - price_change * ((i // 2) + 1))
        price_at_interval.append(simulated_price)

        shares = investment_per_interval / simulated_price
        shares_purchased.append(shares)
        cumulative_shares += shares
        total_shares.append(cumulative_shares)

        value = cumulative_shares * simulated_price
        portfolio_value.append(value)

    # Display the results
    for i in range(investment_intervals):
        print(f"Interval {i+1}:")
        print(f"  Investment Amount: {investment_amounts[i]:.2f}")
        print(f"  Total Invested: {total_invested[i]:.2f}")
        print(f"  Price at Interval: {price_at_interval[i]:.2f}")
        print(f"  Shares Purchased: {shares_purchased[i]:.4f}")
        print(f"  Total Shares: {total_shares[i]:.4f}")
        print(f"  Portfolio Value: {portfolio_value[i]:.2f}")
        print()

# Get user input
total_investment = float(input("Enter the total investment amount: "))
investment_period = int(input("Enter the investment period in months: "))
frequency = int(input("Enter the number of investments per month: "))
initial_price = float(input("Enter the initial price of the stock: "))

calculate_dca(total_investment, investment_period, frequency, initial_price)
