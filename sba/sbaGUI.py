import tkinter as tk
from tkinter import messagebox

def calculate_monthly_payment(principal, interest_rate, periods):
    """
    Calculate the monthly payment for a loan.

    Args:
        principal (float): The loan amount (principal).
        interest_rate (float): The annual interest rate (in percentage).
        periods (int): The total number of payment periods.

    Returns:
        float: The monthly payment amount.
    """
    monthly_interest_rate = interest_rate / 100 / 12
    numerator = principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** periods)
    denominator = ((1 + monthly_interest_rate) ** periods) - 1
    monthly_payment = numerator / denominator
    return monthly_payment

def generate_amortization_schedule(principal, interest_rate, periods):
    """
    Generate an amortization schedule for a loan.

    Args:
        principal (float): The loan amount (principal).
        interest_rate (float): The annual interest rate (in percentage).
        periods (int): The total number of payment periods.

    Returns:
        list: A list of tuples representing each payment period with (Month, Interest, Principal, Remaining Balance).
    """
    monthly_payment = calculate_monthly_payment(principal, interest_rate, periods)
    monthly_interest_rate = interest_rate / 100 / 12
    remaining_balance = principal
    amortization_schedule = []

    for month in range(1, periods + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        amortization_schedule.append((month, interest_payment, principal_payment, remaining_balance))

    return amortization_schedule

def calculate():
    """Calculate the monthly payment and display the result."""
    try:
        principal = float(principal_entry.get())
        interest_rate = float(interest_rate_entry.get())
        periods = int(periods_entry.get())
        monthly_payment = calculate_monthly_payment(principal, interest_rate, periods)
        result_label.config(text="Monthly payment: ${:,.2f}".format(monthly_payment))

        # Generate and display amortization schedule
        amortization_schedule = generate_amortization_schedule(principal, interest_rate, periods)
        schedule_text.delete(1.0, tk.END)
        for item in amortization_schedule:
            schedule_text.insert(tk.END, f"{item}\n")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear():
    """Clear all input fields and result label."""
    principal_entry.delete(0, tk.END)
    interest_rate_entry.delete(0, tk.END)
    periods_entry.delete(0, tk.END)
    result_label.config(text="")
    schedule_text.delete(1.0, tk.END)

def exit_program():
    """Exit the program."""
    root.destroy()

# Create GUI
root = tk.Tk()
root.title("SBA Loan Calculator")

# Input fields
principal_label = tk.Label(root, text="Loan Amount (principal):")
principal_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=5, pady=5)

interest_rate_label = tk.Label(root, text="Annual Interest Rate (%):")
interest_rate_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
interest_rate_entry = tk.Entry(root)
interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)

periods_label = tk.Label(root, text="Number of Periods (months):")
periods_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
periods_entry = tk.Entry(root)
periods_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=3, column=1, padx=5, pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=3, column=2, padx=5, pady=5)

# Display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Amortization schedule text box
schedule_text = tk.Text(root, height=10, width=50)
schedule_text.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
