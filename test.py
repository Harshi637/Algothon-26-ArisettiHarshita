import numpy as np
from ArisettiHarshita import getMyPosition

# Fake price data: 51 assets, 30 days
prcSoFar = np.random.rand(51, 30) * 100  

positions = getMyPosition(prcSoFar)
print("Positions:", positions)
