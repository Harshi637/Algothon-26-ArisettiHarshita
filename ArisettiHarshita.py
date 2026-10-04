import numpy as np

def getMyPosition(prcSoFar):
    num_assets, num_days = prcSoFar.shape
    positions = np.zeros(num_assets)

    if num_days < 3:
        return positions

    # 2-day mean reversion signal
    recent_return = (prcSoFar[:, -1] / prcSoFar[:, -3]) - 1.0

    # Rank from worst to best
    ranked = np.argsort(recent_return)

    # Asymmetric portfolio
    n_long = 45
    n_short = 10

    # Don't long assets 35 and 38
    long_assets = [
    i for i in ranked[:n_long]
    if i not in {35, 38, 14, 23, 28}
    ]
    
    # Don't short assets 10 and 29
    short_assets = ranked[-n_short:]
    short_assets = [
    i for i in short_assets
    if i not in {10, 29, 39, 24, 35, 38, 43, 46, 49, 20, 41}
    ]

    # Position limits
    dollar_limits = np.full(num_assets, 10000.0)
    dollar_limits[0] = 100000.0

    prices = prcSoFar[:, -1]

    # Long positions
    for i in long_assets:
        positions[i] = dollar_limits[i] / prices[i]

    # Short positions
    for i in short_assets:
        positions[i] = -dollar_limits[i] / prices[i]

    return positions