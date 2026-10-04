# ALGOTHON'26 Submission – Team ArisettiHarshita

## 📌 Project Overview

This project presents a quantitative trading strategy developed for **ALGOTHON'26**.

The objective is to design a trading strategy that generates strong **risk-adjusted returns** in a simulated market containing **51 assets**.

The final strategy uses short-term **cross-sectional mean reversion**. It identifies assets that have recently underperformed or overperformed relative to the rest of the market and takes long or short positions accordingly.

Through iterative backtesting and controlled experimentation, the strategy was optimized to achieve a final evaluator score of:

## 🏆 735.24

---

## 🎯 Problem Statement

Design a quantitative trading strategy that maximizes **risk-adjusted returns** in a simulated market of 51 assets.

The strategy is evaluated using portfolio-level daily P&L and a Sharpe-ratio-based scoring system.

---

## 💡 Strategy Approach

The strategy is based primarily on **2-day cross-sectional mean reversion**.

For each asset, the recent return is calculated using:

```text
Recent Return = Price(t) / Price(t-2) - 1
```

Assets are ranked according to their recent returns.

The strategy follows the basic idea:

```text
Recent underperformers → Long positions
Recent overperformers  → Short positions
```

---

## 📊 Trading Logic

The final strategy uses:

- **2-day return** as the primary signal
- **45 long candidates**
- **10 short candidates**
- An asymmetric threshold for long and short signals
- Asset-specific exclusion filters
- Position sizing based on the allowed dollar limits

### Long Signal

An asset is considered for a long position when:

```text
Recent Return < -0.15%
```

### Short Signal

An asset is considered for a short position when:

```text
Recent Return > +0.10%
```

The strategy first ranks assets and then applies the signal conditions and exclusion filters to the selected candidates.

---

## 🚫 Asset-Specific Filtering

During controlled backtesting, asset-specific filters were introduced to remove assets that reduced the risk-adjusted performance of the strategy.

### Long Exclusions

```text
35, 38, 14, 23, 28, 29, 2, 21, 43
```

### Short Exclusions

```text
10, 29, 39, 24, 35, 38,
43, 46, 49, 20, 41, 1,
2, 28, 8, 11, 9, 12,
3, 16, 6
```

---

## 💰 Position Sizing

The strategy follows the position limits provided by the evaluation framework.

```text
Standard asset limit: $10,000
Designated asset limit: $100,000
```

For each selected asset, the position size is calculated using the applicable dollar limit and the current asset price.

---

## 🔬 Optimization Process

The strategy was developed through iterative backtesting and controlled experimentation.

Different aspects of the strategy were tested, including:

- Lookback periods
- Number of long positions
- Number of short positions
- Long and short thresholds
- Position sizing
- Volatility-based signals
- Individual asset exclusions

Changes that improved the official evaluator score were retained, while unsuccessful experiments were reverted.

The final strategy prioritizes **risk-adjusted performance** rather than raw returns alone.

---

## 📈 Final Evaluation

The final verified evaluation produced:

| Metric | Result |
|---|---:|
| Mean Daily P&L | **803.00** |
| Daily Return | **0.438%** |
| P&L Standard Deviation | **3854.37** |
| Annualized Sharpe Ratio | **3.29** |
| Total Dollar Volume | **45,817,579** |
| Final Score | **735.24** |

### 🏆 Final Score

**735.24**

---

## 🛠️ Technologies Used

- Python
- NumPy
- Quantitative Trading
- Cross-Sectional Mean Reversion
- Statistical Analysis
- Backtesting
- Portfolio Construction
- Git
- GitHub
- ALGOTHON'26 Evaluation Framework

---

## 📂 Project Structure

```text
ALGOTHON'26/
│
├── ArisettiHarshita.py
├── eval.py
├── prices.txt
├── README.md
└── .gitignore
```

### File Description

| File | Description |
|---|---|
| `ArisettiHarshita.py` | Final quantitative trading strategy |
| `eval.py` | Evaluation framework |
| `prices.txt` | Historical price data |
| `README.md` | Project documentation |
| `.gitignore` | Git configuration |

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone <GITHUB_REPOSITORY_URL>
```

### 2. Enter the Project Directory

```bash
cd <REPOSITORY_FOLDER>
```

### 3. Make Sure the Required Files Are Present

```text
ArisettiHarshita.py
eval.py
prices.txt
```

### 4. Run the Evaluator

```bash
python eval.py
```

The evaluator will execute the strategy against the provided market data and display the portfolio performance and final score.

---

## 🎯 Design Goals

### Risk-Adjusted Performance

The primary goal is to maximize the final risk-adjusted score rather than simply maximizing raw P&L.

### Simple and Interpretable Strategy

The strategy uses a relatively simple mean-reversion signal that can be clearly explained and analyzed.

### Controlled Exposure

Position sizes follow the limits defined by the evaluation framework.

### Selective Trading

Return thresholds and asset filters reduce exposure to weaker signals.

### Backtest-Driven Optimization

Strategy modifications were evaluated individually, with successful changes retained and unsuccessful changes reverted.

---

## ⚠️ Limitations

- The strategy is optimized for the provided simulated market environment.
- Asset-specific exclusions are based on the available evaluation data.
- Mean reversion may perform poorly during strong persistent trends.
- The strategy does not use fundamental information.
- The strategy does not use external news data.
- Performance may differ in a different market environment.

---

## 🔮 Future Improvements

Possible future improvements include:

- Dynamic position sizing
- Volatility-aware allocation
- Transaction-cost optimization
- Market regime detection
- Adaptive lookback periods
- Dynamic signal thresholds
- Portfolio correlation management
- Drawdown-aware risk management
- Multiple-signal ensemble strategies
- Out-of-sample validation

---

## 👥 Team

**Team Name:** ArisettiHarshita

**Team Member:** Arisetti Harshita

**Other Team Members:** Add team member names and Discord IDs here.

---

## 🔗 Submission Links

### GitHub Repository

`<GITHUB_REPOSITORY_URL>`

### Prototype Demonstration Video

`<GOOGLE_DRIVE_VIDEO_LINK>`

### Live / Deployed Project

`<LIVE_PROJECT_LINK>`

### Project ID

`<PROJECT_ID>`

---

## 🔐 Demo Login Credentials

```text
N/A
```

---

## 📝 Additional Notes for Judges

The final strategy was developed through controlled experimentation and backtesting using the provided evaluation framework.

Multiple signal horizons, portfolio sizes, thresholds, position-sizing approaches, and asset-level filters were evaluated.

The final configuration uses:

```text
2-day cross-sectional mean reversion
45 long candidates
10 short candidates
-0.15% long threshold
+0.10% short threshold
Asset-specific long filters
Asset-specific short filters
Position sizing based on dollar limits
```

The final verified evaluator score achieved was:

## 🏆 735.24

The strategy focuses on **risk-adjusted performance and consistency** rather than simply maximizing raw returns.

---

## 🏆 Final Result

```text
ALGOTHON'26

Strategy:
2-Day Cross-Sectional Mean Reversion

Long Candidates:
45

Short Candidates:
10

Long Threshold:
-0.15%

Short Threshold:
+0.10%

Annualized Sharpe:
3.29

Final Score:
735.24
```

---

## 📜 Conclusion

The submitted strategy demonstrates how a relatively simple quantitative signal can be improved through systematic experimentation and backtesting.

The final approach combines:

```text
2-Day Mean Reversion
        +
Cross-Sectional Ranking
        +
Asymmetric Thresholds
        +
Asset-Specific Filtering
        +
Controlled Position Sizing
        ↓
Risk-Adjusted Trading Strategy
```

The final verified evaluator score is **735.24**.

---

# ALGOTHON'26

## Team ArisettiHarshita

### Final Score: 735.24
