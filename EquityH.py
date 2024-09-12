import numpy as np

def Equity_Hedge(p_spot, p_futures):
    """
    Function to implement an Equity Hedge using stock index futures
    p_spot: Current value of the portfolio
    p_futures: current value of the futures contract
    N: Hedging Ratio
    """
    
    N = p_spot / p_futures
    return(N)



def Equity_Hedge_with_Beta(p_spot, p_futures,beta, beta_new):
    """
    Function to implement an Equity Hedge using stock index futures
    p_spot: Current value of the portfolio
    p_futures: Current value of the futures contract
    beta: Current portfolio beta
    beta_new: New portfolio beta
    N: Hedging Ratio
    """
    if beta > beta_new:
        N_short = (beta - beta_new) *(p_spot / p_futures)
        return(N_short)
    elif beta < beta_new:
        N_long = (beta_new - beta) *(p_spot / p_futures)
        return(N_long)
    else:
        return("Error")
    
