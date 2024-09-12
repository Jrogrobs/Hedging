import pandas as pd
import numpy as np


def Minimum_Variance_Hedge_Ratio(spot_price, futures_price, hedge_size, futures_size):
    """
    spot_price: spot prices
    futures_price: futures prices
    hedge_size: size of the spot position to be hedged
    futures_size: size of the futures position
    corr: correlation
    std: standard deviation
    h: Hedging ratio
    N: Optimal number of contracts to hege
    """

    corr = np.corrcoef(spot_price, futures_price)
    spot_price_std = np.std(spot_price)
    futures_price_std = np.std(futures_price)
    
    h = corr *(spot_price_std / futures_price_std)   
    
    N = (h*hedge_size) / futures_size
    return(h, N)
    
    
    
    
