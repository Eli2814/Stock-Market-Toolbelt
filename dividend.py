def get_dividend_input():
    try:
        stock_name = input("Enter the stock name: ")
        num_shares = float(input(f"Enter the number of shares for {stock_name}: "))
        dividend_per_share = float(input(f"Enter the dividend per share for {stock_name}: ")) / 100
        payout_frequency = input("Enter the payout frequency (monthly, quarterly, semi-annually, annually): ").strip().lower()
        
        if payout_frequency not in ['monthly', 'quarterly', 'semi-annually', 'annually']:
            print("Invalid payout frequency. Please enter one of the following: monthly, quarterly, semi-annually, annually.")
            return None
        
        return {
            'stock_name': stock_name,
            'num_shares': num_shares,
            'dividend_per_share': dividend_per_share,
            'payout_frequency': payout_frequency
        }
    except ValueError:
        print("Invalid input. Please enter numeric values for number of shares and dividend per share.")
        return None

def calculate_annual_dividend(stock_data):
    payout_multiplier = {
        'monthly': 12,
        'quarterly': 4,
        'semi-annually': 2,
        'annually': 1
    }
    
    annual_dividend = stock_data['num_shares'] * stock_data['dividend_per_share'] * payout_multiplier[stock_data['payout_frequency']]
    return annual_dividend

def main():
    print("Dividend Calculator")
    stock_data = get_dividend_input()
    
    if stock_data:
        annual_dividend = calculate_annual_dividend(stock_data)
        print(f"\nAnnual Dividend Income for {stock_data['stock_name']}: ${annual_dividend:.2f}")
        
        # Optional: Calculate reinvested dividend value (simple example assuming annual compounding)
        reinvest = input("Do you want to calculate potential reinvested value (yes/no)? ").strip().lower()
        if reinvest == 'yes':
            years = int(input("Enter the number of years for reinvestment: "))
            annual_growth_rate = float(input("Enter the annual growth rate (in %): "))
            
            future_value = annual_dividend * (((1 + annual_growth_rate / 100) ** years - 1) / (annual_growth_rate / 100))
            print(f"Potential value after {years} years if reinvested at {annual_growth_rate}% annual growth rate: ${future_value:.2f}")
        
        
if __name__ == "__main__":
    main()
