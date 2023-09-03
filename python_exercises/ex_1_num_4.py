import numpy as np
import math

N = 100 # Nominal
c = 0.05 # Coupon Rate
T = 2 # 2 years till maturity
n = 2 # Payment Frequency is semi - annual, i.e. every six months
r = np.array([0.05,0.055, 0.06, 0.065]) # Term Structure

def rates_to_discount(r):
    # You need a list to store your discount factors
    z = []
    # Create a loop
    for i in range (4):
        aux = math.pow((1 + r[i] / n), -1 * n * (T - i/2))
        z.append(aux)
        print(f"rate: {r[i]}")
        print(f"discount factor: {aux}")
    return np.array(z)

def bond_price(N, c, n, z):
    price = 0
    # Tip: You can use the formula created on part 1
    # Separete the formula into to parts
    discount_sum = sum(z) *  c * N/ n
    last_discount = z[3] * N # Aux 2. Multiply this by a 100
    price = discount_sum + last_discount # Use aux1 and aux 2 to write the formula
    return price

def n_times_to_inf(r, n):
    return n * np.log(1 + r / n)

def inf_to_n_times(r, n):
    return n * (np.exp(r / n) - 1)

if __name__ == "__main__":
    z = rates_to_discount(r)
    price = bond_price(N= N, c= c, n= n, z= z)
    print(price)
    print(f"r_nc: {r}")
    print(f"r: {n_times_to_inf(r, n)}")
    print(f"Back to r_nc: {inf_to_n_times(n_times_to_inf(r,n), n)}")
