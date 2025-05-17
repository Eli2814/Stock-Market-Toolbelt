def apply_fibonacci_retracement(high, low):
    difference = high - low
    levels = {
        '23.6%': high - 0.236 * difference,
        '38.2%': high - 0.382 * difference,
        '50%': high - 0.5 * difference,
        '61.8%': high - 0.618 * difference,
        '78.6%': high - 0.764 * difference
    }
    return levels