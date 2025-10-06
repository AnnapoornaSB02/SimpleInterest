def calculate_simple_interest(principal, rate, time):
    """
    principal: initial amount
    rate: annual interest rate in percent (e.g. 5 for 5%)
    time: time in years
    Returns: simple interest amount
    """
    return (principal * rate * time) / 100
