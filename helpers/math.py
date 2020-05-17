

def cagr(start_value, end_value, num_periods):
    if num_periods < 2 or start_value == 0:
        return None
    return (end_value / start_value) ** (1 / (num_periods - 1)) - 1