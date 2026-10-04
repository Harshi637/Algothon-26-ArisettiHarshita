import numpy as np

def getMyPosition(prcSoFar):
    """
    3-Day Cross-Sectional Mean Reversion Strategy

    - Calculates each asset's 3-day return.
    - Buys the 10 assets with the worst recent performance.
    - Shorts the 10 assets with the best recent performance.
    - Uses the maximum allowed dollar position.
    - Leaves the remaining assets at zero.
    """

    num_assets, num_days = prcSoFar.shape

    positions = np.zeros(num_assets)

    # Need at least 3 days of history
    if num_days < 4:
        return positions

    # 3-day percentage return
    recent_return = (
        prcSoFar[:, -1] / prcSoFar[:, -4]
    ) - 1.0

    # Rank assets by recent performance
    ranked = np.argsort(recent_return)

    # Number of assets on each side
    n = 10

    # Buy the 10 worst performers
    long_assets = ranked[:n]

    # Short the 10 best performers
    short_assets = ranked[-n:]

    # Position limits in dollars
    dollar_limits = np.full(num_assets, 10000.0)
    dollar_limits[0] = 100000.0

    current_prices = prcSoFar[:, -1]

    # Long positions
    for i in long_assets:
        positions[i] = dollar_limits[i] / current_prices[i]

    # Short positions
    for i in short_assets:
        positions[i] = -dollar_limits[i] / current_prices[i]

    return positions