def calculate_limit_sell_price(average_cost, profit_percentage):
    """
    Calculate the limit sell price.
    
    :param average_cost: The average cost of the stock
    :param profit_percentage: The desired profit percentage (e.g., 0.02 for 2%)
    :return: The limit sell price
    """
    return average_cost * (1 + profit_percentage)

def calculate_stop_loss_price(average_cost, stop_loss_percentage):
    """
    Calculate the stop-loss price.
    
    :param average_cost: The average cost of the stock
    :param stop_loss_percentage: The stop-loss percentage (e.g., 0.01 for 1%)
    :return: The stop-loss price
    """
    return average_cost * (1 - stop_loss_percentage)

def main():
    print("Stop-Loss and Limit Order Calculator")
    
    # Get user input for average cost, desired profit percentage, and stop-loss percentage
    average_cost = float(input("What's Your Average Cost? "))
    profit_percentage = float(input("How Much Do You Wanna Make? (e.g., 0.02 for 2%) "))
    stop_loss_percentage = float(input("How Much Are You Willing To Lose? (e.g., 0.01 for 1%) "))
    
    # Calculate limit sell and stop-loss prices
    limit_sell_price = calculate_limit_sell_price(average_cost, profit_percentage)
    stop_loss_price = calculate_stop_loss_price(average_cost, stop_loss_percentage)
    
    # Display the results
    print(f"\nLimit Sell Price: {limit_sell_price:.2f}")
    print(f"Stop-Loss Price: {stop_loss_price:.2f}")

if __name__ == "__main__":
    main()

