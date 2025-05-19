def main():
    print("=== Stock Allocation Calculator ===\n")
    # Gather user inputs
    stock_a_symbol = input("Enter the symbol for Stock A: ").upper()
    price_stock_a = float(input(f"Enter the price of {stock_a_symbol}: $"))
    stock_b_symbol = input("Enter the symbol for Stock B: ").upper()
    price_stock_b = float(input(f"Enter the price of {stock_b_symbol}: $"))
    total_capital = float(input("Enter the total capital to allocate: $"))

    # Desired allocation
    allocation_choice = input("\nDo you want to allocate capital equally between the two stocks? (yes/no): ").strip().lower()

    if allocation_choice == 'yes':
        allocation_a = total_capital / 2
        allocation_b = total_capital / 2
    else:
        ratio_a = float(input(f"Enter the percentage of capital to allocate to {stock_a_symbol} (e.g., 60 for 60%): ")) / 100
        ratio_b = 1 - ratio_a
        allocation_a = total_capital * ratio_a
        allocation_b = total_capital * ratio_b

    # Calculate number of shares
    shares_a = int(allocation_a // price_stock_a)
    shares_b = int(allocation_b // price_stock_b)

    # Recalculate actual allocations
    actual_investment_a = shares_a * price_stock_a
    actual_investment_b = shares_b * price_stock_b
    total_invested = actual_investment_a + actual_investment_b
    remaining_capital = total_capital - total_invested

    # Display the results
    print("\n=== Investment Plan ===")
    print(f"\n{stock_a_symbol}:")
    print(f"  Price per share: ${price_stock_a:.2f}")
    print(f"  Shares to buy: {shares_a}")
    print(f"  Total investment: ${actual_investment_a:.2f}")

    print(f"\n{stock_b_symbol}:")
    print(f"  Price per share: ${price_stock_b:.2f}")
    print(f"  Shares to buy: {shares_b}")
    print(f"  Total investment: ${actual_investment_b:.2f}")

    print(f"\nTotal capital invested: ${total_invested:.2f}")
    print(f"Remaining capital: ${remaining_capital:.2f}")

    # Suggest adjustments if significant remaining capital
    min_price = min(price_stock_a, price_stock_b)
    if remaining_capital >= min_price:
        print("\nYou have enough remaining capital to purchase additional shares.")
        adjust_choice = input("Would you like to adjust allocations to invest remaining capital? (yes/no): ").strip().lower()
        if adjust_choice == 'yes':
            adjust_allocations(price_stock_a, price_stock_b, shares_a, shares_b, remaining_capital, stock_a_symbol, stock_b_symbol)

def adjust_allocations(price_a, price_b, shares_a, shares_b, remaining, symbol_a, symbol_b):
    # Decide where to allocate remaining capital
    print("\nAdjusting allocations...")
    options = []
    if remaining >= price_a:
        options.append(symbol_a)
    if remaining >= price_b:
        options.append(symbol_b)

    if len(options) == 1:
        choice = options[0]
    else:
        print(f"Options to allocate remaining capital: {', '.join(options)}")
        choice = input(f"Which stock would you like to buy more shares of? ({'/'.join(options)}): ").strip().upper()

    if choice == symbol_a:
        additional_shares = int(remaining // price_a)
        shares_a += additional_shares
        remaining -= additional_shares * price_a
    elif choice == symbol_b:
        additional_shares = int(remaining // price_b)
        shares_b += additional_shares
        remaining -= additional_shares * price_b
    else:
        print("Invalid choice. Remaining capital will not be invested.")
        return

    # Recalculate investments
    actual_investment_a = shares_a * price_a
    actual_investment_b = shares_b * price_b
    total_invested = actual_investment_a + actual_investment_b

    # Display updated results
    print("\n=== Updated Investment Plan ===")
    print(f"\n{symbol_a}:")
    print(f"  Shares to buy: {shares_a}")
    print(f"  Total investment: ${actual_investment_a:.2f}")

    print(f"\n{symbol_b}:")
    print(f"  Shares to buy: {shares_b}")
    print(f"  Total investment: ${actual_investment_b:.2f}")

    print(f"\nTotal capital invested: ${total_invested:.2f}")
    print(f"Remaining capital: ${remaining:.2f}")

if __name__ == "__main__":
    main()
