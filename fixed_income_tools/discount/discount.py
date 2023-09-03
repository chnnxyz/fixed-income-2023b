from typing import Union
from math import pow

def discount_factor(r: float, 
                    n_compounding: Union[int,float], 
                    t: float, 
                    T: float) -> float:
    '''Calculates the discount rate Z(t, T)

    Parameters
    ----------
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
    z: float
        Discount factor
    '''
    return pow((1 + r / n_compounding), -1 * n_compounding * (T - t))
