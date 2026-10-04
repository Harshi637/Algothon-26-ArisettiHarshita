import numpy as np

# Track previous positions to reduce unnecessary trades
prev_positions = np.zeros(51)

def getMyPosition(prcSoFar):
    """
    Trading strategy: Moving Average Crossover
    - Uses 5-day vs 20-day averages
    - Positions clipped to asset limits
    - Trades only when signals flip (reduces commissions)
    
    Parameters:
        prcSoFar (np.ndarray): Price history (51 assets × numDays)
    
    Returns:
        np.ndarray: Positions for each asset
    """

    global prev_positions
    num_assets, num_days = prcSoFar.shape
    positions = np.copy(prev_positions)

    # Only trade after enough history
    if num_days >= 20:
        short_ma = np.mean(prcSoFar[:, -5:], axis=1)   # 5-day average
        long_ma = np.mean(prcSoFar[:, -20:], axis=1)   # 20-day average

        for i in range(num_assets):
            signal = 0
            if short_ma[i] > long_ma[i]:
                signal = 1   # Long
            elif short_ma[i] < long_ma[i]:
                signal = -1  # Short

            target_position = signal * (100000 if i == 0 else 10000)

            # Update only if signal changed (reduces churn/commissions)
            if target_position != prev_positions[i]:
                positions[i] = target_position

    # Clip positions to respect limits
    positions[0] = np.clip(positions[0], -100000, 100000)   # ALGO
    positions[1:] = np.clip(positions[1:], -10000, 10000)   # Other assets

    # Save for next call
    prev_positions = positions
    return positions
