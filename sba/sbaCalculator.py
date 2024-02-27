def calculate_monthly_payment(principal, interest_rate, periods):
    """
    Calculate the monthly payment for a loan using the loan amortization formula.

    Args:
        principal (float): The loan amount (principal).
        interest_rate (float): The annual interest rate (in percentage).
        periods (int): The total number of payment periods (in months).

    Returns:
        float: The calculated monthly payment.
    """
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = interest_rate / 100 / 12
    
    # Calculate the numerator of the loan amortization formula
    numerator = principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** periods)
    
    # Calculate the denominator of the loan amortization formula
    denominator = ((1 + monthly_interest_rate) ** periods) - 1
    
    # Calculate the monthly payment using the loan amortization formula
    monthly_payment = numerator / denominator
    
    # Return the calculated monthly payment
    return monthly_payment

def generate_amortization_schedule(principal, interest_rate, periods):
    """
    Generate an amortization schedule for the loan.

    Args:
        principal (float): The loan amount (principal).
        interest_rate (float): The annual interest rate (in percentage).
        periods (int): The total number of payment periods (in months).

    Returns:
        list: A list of dictionaries representing the amortization schedule.
    """
    schedule = []
    remaining_balance = principal
    monthly_payment = calculate_monthly_payment(principal, interest_rate, periods)
    for month in range(1, periods + 1):
        interest = remaining_balance * (interest_rate / 100 / 12)
        principal_paid = monthly_payment - interest
        remaining_balance -= principal_paid
        schedule.append({
            "Month": month,
            "Interest": interest,
            "Principal": principal_paid,
            "Remaining Balance": remaining_balance
        })
    return schedule

def main():
    """
    Main function to prompt the user for input, calculate the monthly payment,
    and generate an amortization schedule.
    """
    # Prompt the user to enter the loan amount, interest rate, and number of periods
    principal = float(input("Enter the loan amount (principal): "))
    interest_rate = float(input("Enter the annual interest rate (%): "))
    periods = int(input("Enter the number of periods (months): "))

    # Calculate the monthly payment using the provided inputs
    monthly_payment = calculate_monthly_payment(principal, interest_rate, periods)
        
    # Print the monthly payment
    print("Monthly payment: ${:,.2f}".format(monthly_payment))

    

    res = input(str("Do you want me to print and amortization schedule?"))
    if res.upper() == 'Y':        
        # Generate the amortization schedule
        schedule = generate_amortization_schedule(principal, interest_rate, periods)

        # Print the amortization schedule
        print("\nAmortization Schedule:")
        print("{:<8} {:<15} {:<15} {:<20}".format("Month", "Interest", "Principal", "Remaining Balance"))
        for entry in schedule:
            print("{:<8} {:<15,.2f} {:<15,.2f} {:<20,.2f}".format(entry["Month"], entry["Interest"], entry["Principal"], entry["Remaining Balance"]))

if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
