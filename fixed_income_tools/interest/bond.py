from typing import Iterable, Union

import numpy as np

from fixed_income_tools.discount import discount_factor

def zero_coupon_bond(N: float,
                     r: float, 
                     n_compounding: Union[int, float], 
                     t: float, 
                     T: float) -> float:
    '''Prices a Zero Coupon Bond
    
    Parameters
    ----------
    N: float
        Nominal
    r: float
        Interest rate
    n_compounding: numeric
        Number of compoundings
    t: float
        Current time
    T: float
        Maturity
    
    Returns
    -------
    price: float
        Price of zero coupon bond
    '''
    return N * discount_factor(r, n_compounding, t, T)

def coupon_bond(N, r, n_compounding, t, T, c, n):
    if not isinstance(r, Iterable):
        r = [r]
    if not isinstance(t, Iterable):
        t = [t]
    discounts = np.array([discount_factor(rate,
                                          n_compounding,
                                          time,
                                          T) for rate, time in zip(r, t)])
    last_discount = discounts[-1]
    return N * c * np.sum(discounts)/ n + last_discount * N
