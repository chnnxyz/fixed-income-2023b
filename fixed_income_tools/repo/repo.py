def reverse_repo_trader_profit(p_now: float, 
                              p_maturity: float, 
                              repo_rate: float,
                              n_days: float) -> float:
    '''Calculates the profit for a repo trader

    Parameters
    ----------
    P_now: float
        Current Price
    P_maturity: float
        Price at maturity
    repo_rate: float
        Normalized repo rate (e.g. 0.06 means 6%)
    n_days: float
        Number of days for the repo trade.
    
    Returns
    -------
    profit: float
        Profit for the repo trader.
    '''
    r_i = n_days * repo_rate * p_now / 360
    profit = p_now + r_i - p_maturity
    return profit


def repo_trader_profit(p_now: float, 
                       p_maturity: float, 
                       repo_rate: float,
                       n_days: float,
                       hair_cut: float = 0.01) -> float:
    '''Calculates the profit for a repo trader

    Parameters
    ----------
    P_now: float
        Current Price
    P_maturity: float
        Price at maturity
    repo_rate: float
        Normalized repo rate (e.g. 0.06 means 6%)
    n_days: float
        Number of days for the repo trade.
    hair_cut: float, optional, default=0.01
        Hair cut percentange on a normalized scale.
    
    Returns
    -------
    profit: float
        Profit for the repo trader.
    '''
    r_i = n_days * repo_rate * p_now  * (1 - hair_cut) / 360
    profit = p_maturity - p_now - r_i
    return profit
