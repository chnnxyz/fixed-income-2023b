from math import log

def continuous_compound_rate(r: float, n_compounding: int) -> float:
    '''Calculatrs a continuous compound rate

    Parameters
    ----------
    r: float
        Period interest rate
    n_compounding: int
        Number of compoundings in a year.

    Returns
    -------
    compound_rate: float
        Continuous compound rate.
    '''
    return n_compounding * log(1 + r/n_compounding)
