import decimal

def solve():
    # Set high precision to handle the potential growth of terms
    # However, the theoretical sequence shows that U_n = (2^n + 1) / (2^(n-1) + 1)
    # This is because the recurrence x_n = 2003*x_{n-1} - 6002*x_{n-2} + 4000*x_{n-3}
    # with x_n/x_{n-1} = U_n has characteristic roots 1, 2, and 2000.
    # Given U_1 = 3/2 and U_2 = 5/3, the coefficient for the root 2000 is exactly 0.
    # Thus, x_n = 1 + 2^n (or any scale thereof).
    # U_n = (2^n + 1) / (2^{n-1} + 1)

    decimal.getcontext().prec = 100

    # Calculate U_2000 using the derived formula
    # U_n = (2**n + 1) / (2**(n-1) + 1)
    # For n=2000, this is (2**2000 + 1) / (2**1999 + 1)

    two_pow_2000 = decimal.Decimal(2)**2000
    two_pow_1999 = decimal.Decimal(2)**1999

    u_2000 = (two_pow_2000 + 1) / (two_pow_1999 + 1)

    # Round to the nearest whole number
    return int(round(u_2000))

print(solve())
