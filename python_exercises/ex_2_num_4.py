import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from typing import Union

from nelson_siegel_svensson import NelsonSiegelSvenssonCurve
from nelson_siegel_svensson.calibrate import calibrate_nss_ols




def price_from_ytm(N:float, c:float, T:Union[int, float], n: int, y: float):
    '''Calculates a bond price based on the yield to maturity
    
    Parameters
    ----------
    N: float
        Face value of the bond
    c: float
        Coupon rate in a scale where 0 is 0% and 1 is 100%.
    T: numeric
        Time to maturity, commonly in years, but unit-agnostic
    n: int
        Payment frequency
    y: float
        Yield to maturity

    Returns
    -------
    price: float
        Price of the bond
    '''
    # Get total payments
    tot_payments = n * T
    # Get coupon pay times to get discount factors
    coupon_pay_times = [i * T/tot_payments for i in range(1, tot_payments +1)]
    # Define a simple helper function for discount that inherits most of the
    # arguments from the function

    def _discount(t:float):
        '''Calculates discount factor Z(0,t)'''
        power = - n * T
        return math.pow(1 - y / n, power)
    
    # Get all discount factors.
    discounts = [_discount(coup) for coup in coupon_pay_times]
    tot_dct = sum(discounts)
    # Get coupon component
    coupon = c * tot_dct / n
    # Get zero coupon component
    # This may not work if the bond does not mature at a coupon payment.
    # For this exercise, this should do the trick.
    zero_coup = discounts[-1]

    # Return total price
    return N * (coupon + zero_coup)

def macaulay(P:float, N:float, c:float, T:Union[int, float], n: int, y: float):
    '''Gets the macauly duration of a security

    Parameters
    ----------
    P: float
        Price of the bond
    N: float
        Face value of the bond
    c: float
        Coupon rate in a scale where 0 is 0% and 1 is 100%.
    T: numeric
        Time to maturity, commonly in years, but unit-agnostic
    n: int
        Payment frequency
    y: float
        Yield to maturity

    Returns
    -------
    d_mc: float
        Macaulay duration of the bond
    '''
    tot_payments = n * T
    
    # Get all weights for all coupon payments except maturity
    weights = [(N * c / n)/(P * math.pow(1 + y/n, i)) 
               for i in range(1, tot_payments)]
    # Get weight for maturity and append to weights
    last_weight = (N * (1 + c / n))/(P * math.pow(1 + y/n, tot_payments))
    weights.append(last_weight)

    #Get T_j
    coupon_pay_times = [i * T/tot_payments for i in range(1, tot_payments +1)]

    #Do the linear combination
    

if __name__ == "__main__":
    data = pd.read_csv('data/usyields.csv')
    # Get maturities and yields to fit
    mats = data['maturity'].to_numpy()
    y = data['2020-02-24'].to_numpy
    calibrate_nss_ols()