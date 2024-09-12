import numpy as np

def Minimum_Variance_Hedge_Ratio(delta_spot_price, delta_futures_price):
    """
    Simple function to calculate the Minimum Variance Hedge Ratio.
    """
    corr = np.corrcoef(delta_spot_price, delta_futures_price)
    spot_price_std = np.std(delta_spot_price)
    futures_price_std = np.std(delta_futures_price)
    h = corr *(spot_price_std / futures_price_std)
    
print(h)
