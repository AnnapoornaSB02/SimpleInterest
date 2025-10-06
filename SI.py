def calculate_simple_interest(principal, rate, time):
    """
    principal: initial amount
    rate: annual interest rate in percent (e.g. 5 for 5%)
    time: time in years
    Returns: simple interest amount
    """
    return (principal * rate * time) / 100
def calculate_compound_interest(principal, rate, time, n=1):
    """
    principal: initial amount
    rate: annual interest rate in percent
    time: time in years
    n: number of times interest is compounded per year (default = 1, i.e. annually)
    
    Returns: (compound_interest, total_amount)
    """
    # Convert rate percent to decimal
    r = rate / 100
    # Formula: A = P * (1 + r/n)^(n * time)
    amount = principal * (1 + r / n) ** (n * time)
    ci = amount - principal
    return ci, amount

def main():
    print("Interest Calculator")
    print("1. Simple Interest")
    print("2. Compound Interest")
    choice = input("Choose option (1 or 2): ").strip()

    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter annual interest rate (in %): "))
        t = float(input("Enter time in years: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == "1":
        si = calculate_simple_interest(p, r, t)
        total = p + si
        print(f"Simple Interest = {si}
