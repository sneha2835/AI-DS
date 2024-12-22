K0 = float(input("Enter the initial balance (K0): "))
interest_rate = float(input("Enter the interest rate (in %): "))
K1 = K0 * (1 + interest_rate / 100)
print(f"Capital after 1 year (K1): {K1:.2f}")
n = int(input("Enter the number of years: "))
year = 1
Kn = K0
while year <= n:
    Kn = Kn * (1 + interest_rate / 100)
    print(f"Capital after year {year}: {Kn:.2f}")
    year += 1
