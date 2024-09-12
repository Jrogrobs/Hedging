import numpy as np

def Equity_Hedge(p_spot, p_futures):
    """
    Function to implement an Equity Hedge using stock index futures
    p_spot: current value of the portfolio
    p_futures: curent value of futures contract
    N: Hedging Ratio
    """
    
    N = p_spot / p_futures
    return(N)



def Equity_Hedge_with_Beta(p_spot, p_futures,beta, beta_new):
    """
    Function to implement an Equity Hedge using stock index futures
    p_spot: current value of the portfolio
    p_futures: curent value of futures contract
    beta: current portfolio beta
    beta_new: new portfolio beta
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
    
