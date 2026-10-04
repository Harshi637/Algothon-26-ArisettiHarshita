import numpy as np

def getMyPosition(prcSoFar):
    num_assets, num_days = prcSoFar.shape

    positions = np.zeros(num_assets)

    if num_days < 3:
        return positions

    # 2-day return
    recent_return = (
        prcSoFar[:, -1] / prcSoFar[:, -3]
    ) - 1.0

    # Rank from worst to best
    ranked = np.argsort(recent_return)

    # Asymmetric portfolio
    n_long = 40
    n_short = 10

    long_assets = ranked[:n_long]
    short_assets = ranked[-n_short:]

    # Position limits
    dollar_limits = np.full(num_assets, 10000.0)
    dollar_limits[0] = 100000.0

    prices = prcSoFar[:, -1]

    # Long worst performers
    for i in long_assets:
        positions[i] = dollar_limits[i] / prices[i]

    # Short best performers
    for i in short_assets:
        positions[i] = -dollar_limits[i] / prices[i]

    return positions