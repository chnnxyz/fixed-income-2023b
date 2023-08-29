def reverse_repo_trader_profit(p_now: float, 
                              p_maturity: float, 
                              repo_rate: float,
                              n_days: int) -> float:
    '''Calculates the profit for a repo trader

    Parameters
    ----------
    P_now: float
        Current Price
    P_maturity: float
        Price at maturity
    repo_rate: float
        Normalized repo rate (e.g. 0.06 means 6%)
    n_days: int
        Number of days for the repo trade.
    
    Returns
    -------
    profit: float
        Profit for the repo trader.
    '''
    r_i = n_days * repo_rate * p_now / 360
    profit = p_now + r_i - p_maturity
    return profit
