# src/utils.py

def calculate_interest(amount, rate, time):
    """Рассчитывает простые проценты по формуле: interest = principal * rate * time"""
    return amount * rate * time / 100


def compound_interest(principal, rate, times_compounded, time):
    """Рассчитывает сложные проценты"""
    return principal * (1 + rate / times_compounded) ** (times_compounded * time) - principal