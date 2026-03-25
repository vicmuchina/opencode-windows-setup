---
name: nse-stock-analyzer
description: Institutional-grade stock analysis for Nairobi Securities Exchange (NSE) Kenya. Use this skill when conducting comprehensive stock research, valuation analysis, identifying undervalued opportunities, or generating investment reports for all 62 NSE listed companies. Triggers on tasks involving NSE stocks, Kenya market analysis, value investing, or African equities research.
license: MIT
metadata:
  author: zidiitrader
  version: "1.0.0"
  organization: Ziidi Trader
  date: February 2026
  markets: ["NSE Kenya", "East Africa"]
  companies: 62
  sectors: 11
  abstract: Comprehensive NSE stock analysis framework with institutional-grade methodology. Covers all 62 listed companies across 11 sectors with primary data sources, valuation models (Graham, DCF, Net-Net), goldmine screening criteria, and automated PDF report generation. Includes proven strategies for identifying undervalued opportunities in frontier markets.
---

# NSE Stock Analyzer - Institutional-Grade Analysis Framework

Comprehensive stock analysis framework for the Nairobi Securities Exchange (NSE), designed to identify undervalued opportunities using institutional-grade methodology. Covers all 62 listed companies across 11 sectors with proven strategies for generating alpha in frontier markets.

## When to Apply

Activate this skill when:
- Analyzing NSE Kenya listed stocks
- Conducting value investing research
- Identifying undervalued opportunities
- Generating investment reports
- Researching East African equities
- Performing DCF, Graham, or Net-Net valuations
- Building investment portfolios for frontier markets
- Researching banking, insurance, or energy sectors in Kenya

## Quick Navigation

| Section | Purpose |
|---------|---------|
| [Company Universe](#company-universe) | All 62 NSE listed companies |
| [Data Sources](#data-sources) | Primary and secondary data providers |
| [Valuation Methods](#valuation-methodology) | Graham, DCF, Net-Net, Composite Scores |
| [Goldmine Screening](#goldmine-screening-criteria) | 6-criteria opportunity filter |
| [Sector Analysis](#sector-analysis) | Deep-dives by industry |
| [PDF Generation](#pdf-report-generation) | Automated report creation |
| [Alpha Strategies](#alpha-generation-strategies) | Proven market-beating techniques |

---

## Company Universe (62 Stocks)

### Banking & Financial Services (12)

| Ticker | Company | Market Cap (KES) | Sector Role |
|--------|---------|------------------|-------------|
| SCOM | Safaricom PLC | 1.29 Trillion | Telecom/Mobile Money |
| EQTY | Equity Group Holdings | 283 Billion | Regional Banking |
| KCB | KCB Group PLC | 241 Billion | Pan-African Banking |
| NCBA | NCBA Group PLC | 146 Billion | Digital Banking |
| COOP | Co-operative Bank | 174 Billion | Cooperative Banking |
| ABSA | Absa Bank Kenya | 163 Billion | Corporate Banking |
| SCBK | Standard Chartered Bank | 127 Billion | International Banking |
| SBIC | Stanbic Holdings | 101 Billion | Regional Banking |
| IMH | I&M Group PLC | 83 Billion | Regional Banking |
| DTK | Diamond Trust Bank | 45 Billion | Regional Banking |
| BKG | BK Group PLC (Rwanda) | 43 Billion | Regional Banking |
| HFCK | HF Group Limited | 20 Billion | Mortgage Banking |

### Insurance (6)

| Ticker | Company | Market Cap (KES) | Notes |
|--------|---------|------------------|-------|
| JUB | Jubilee Holdings | 25.5 Billion | Regional Leader |
| BRIT | Britam Holdings | 32.9 Billion | Diversified |
| KNRE | Kenya Reinsurance | 22.3 Billion | **DEEP VALUE** |
| LBTY | Liberty Kenya | 5.0 Billion | Niche Player |
| SLAM | Sanlam Kenya | 1.3 Billion | Underfollowed |
| CIC | CIC Insurance Group | 17.2 Billion | Cooperative |

### Energy & Utilities (4)

| Ticker | Company | Market Cap (KES) | Notes |
|--------|---------|------------------|-------|
| KEGN | KenGen PLC | 62.9 Billion | Dividend Play |
| KPLC | Kenya Power | 35.9 Billion | Monopoly Utility |
| UMME | Umeme Limited (Uganda) | 14.3 Billion | Regional Utility |
| TOTL | TotalEnergies Marketing | 27.2 Billion | Energy Distribution |

### Manufacturing & Allied (9)

| Ticker | Company | Market Cap (KES) | Notes |
|--------|---------|------------------|-------|
| EABL | East African Breweries | 196.7 Billion | Consumer Leader |
| BAT | British American Tobacco | 49.5 Billion | Defensive |
| BAMB | Bamburi Cement | 19.6 Billion | Infrastructure Play |
| PORT | E.A. Portland Cement | 7.7 Billion | Turnaround |
| CARB | Carbacid Investments | 8.2 Billion | Industrial Gas |
| CRWN | Crown Paints Kenya | 8.4 Billion | Consumer |
| UNGA | Unga Group | 2.0 Billion | Food Processing |
| BOC | BOC Kenya | 1.5 Billion | Industrial Gas |
| MSC | Mumias Sugar | SUSPENDED | AVOID |

### Agriculture (5)

| Ticker | Company | Market Cap (KES) |
|--------|---------|------------------|
| KUKZ | Kakuzi PLC | 8.6 Billion |
| SASN | Sasini PLC | 7.1 Billion |
| LIMT | Limuru Tea | 1.2 Billion |
| KAPC | Kapchorua Tea | 1.0 Billion |
| WTK | Williamson Tea | 1.0 Billion |

### Commercial & Services (8)

| Ticker | Company | Market Cap (KES) |
|--------|---------|------------------|
| KQ | Kenya Airways | 30.9 Billion |
| NMG | Nation Media Group | 3.0 Billion |
| SGL | Standard Group | 0.5 Billion |
| TPSE | TPS Eastern Africa | 2.0 Billion |
| SCAN | WPP Scangroup | 1.1 Billion |
| UCHM | Uchumi Supermarkets | 0.5 Billion |
| LKL | Longhorn Publishers | 0.9 Billion |
| XPRS | Express Kenya | 0.3 Billion |

### Investment Companies (5)

| Ticker | Company | Market Cap (KES) |
|--------|---------|------------------|
| CTUM | Centum Investment | 9.3 Billion |
| TCL | TransCentury | 1.3 Billion |
| OCH | Olympia Capital | 0.5 Billion |
| HAFR | Home Afrika | 0.6 Billion |
| KURV | Kurwitu Ventures | 0.5 Billion |

### Other Listed Companies (9)

| Ticker | Company | Sector |
|--------|---------|--------|
| CGEN | Car & General | Automotive |
| FTGH | Flame Tree Group | Manufacturing |
| EVRD | Eveready East Africa | Consumer |
| EGAD | Eaagads Limited | Agriculture |
| SMER | Sameer Africa | Manufacturing |
| SKL | Shri Krishana Overseas | Trading |
| NBV | Nairobi Business Ventures | Trading |
| NSE | NSE PLC (Self-listed) | Financial |
| HBE | Homeboyz Entertainment | Media |

### REITs & ETFs (4)

| Ticker | Name | Type |
|--------|------|------|
| GLD | Absa NewGold ETF | Commodity (Gold) |
| SMWF | Satrix MSCI World Feeder | Global ETF |
| LAPR | Laptrust Imara Income-REIT | Real Estate |
| ACORN | Acorn D-REIT/I-REIT | Real Estate |

---

## Data Sources

### Primary Sources (MUST USE)

| Source | URL | Data Type | Access Method |
|--------|-----|-----------|---------------|
| **NSE Official** | nse.co.ke | Live prices, corporate actions, announcements | webfetch, tavily_search |
| **African Financials** | africanfinancials.com | Annual reports, interim reports, presentations | webfetch, tavily_extract |
| **Kwayisi AFX** | afx.kwayisi.org/nse | Real-time prices, historical data, market stats | webfetch |
| **StockAnalysis** | stockanalysis.com | Market cap, P/E, revenue, historical | webfetch, tavily_search |
| **Company IR Pages** | [Company Websites] | Full financial statements, fact sheets | webfetch |

### Secondary Sources (SUPPORTING)

| Source | Data Type |
|--------|-----------|
| Cytonn Research Reports | Market analysis, sector deep-dives, outlook |
| Central Bank of Kenya | Interest rates, forex, monetary policy |
| Kenya National Bureau of Statistics | Economic indicators, inflation, GDP |
| SIB Research Reports | Banking sector analysis |
| NCBA Investment Bank Reports | Stock picks, valuations |
| Kenyan Wall Street | Market news, corporate actions |

### Data Collection Commands

```bash
# NSE Official
webfetch("https://www.nse.co.ke", format="markdown")
webfetch("https://www.nse.co.ke/listed-companies/", format="markdown")

# Kwayisi AFX (Real-time prices)
webfetch("https://afx.kwayisi.org/nse/", format="markdown")

# African Financials (Company reports)
webfetch("https://africanfinancials.com/company/ke-{ticker}/", format="markdown")

# StockAnalysis
webfetch("https://stockanalysis.com/quote/nase/{ticker}/market-cap/", format="markdown")

# Tavily Search for news/analysis
tavily_tavily_search(query="{company} {ticker} NSE Kenya stock price valuation 2026", max_results=5, search_depth="advanced")
```

---

## Valuation Methodology

### Method 1: Graham's Intrinsic Value

**Formula:**
```
Intrinsic Value = sqrt(22.5 x EPS x Book Value Per Share)
```

**Interpretation:**
- Buy Signal: Price < 0.67 x Graham IV (33% margin of safety)
- Strong Buy: Price < 0.50 x Graham IV (50% margin of safety)

**Example (KCB Group):**
```
EPS = KES 19.5
BVPS = KES 93.0
Graham IV = sqrt(22.5 x 19.5 x 93.0) = sqrt(40,826) = KES 202
Current Price = KES 74.75
Margin of Safety = 63%
Rating: STRONG BUY
```

### Method 2: Price-to-Book Value

**Signals:**
- P/B < 0.5: Deep Value (Strong Buy)
- P/B < 1.0: Below Book Value (Buy)
- P/B 1.0-1.5: Fair Value (Hold)
- P/B > 2.0: Expensive (Avoid)

**Sector Benchmarks:**
| Sector | Average P/B | Value Threshold |
|--------|-------------|-----------------|
| Banking | 1.2x | < 0.8x |
| Insurance | 1.3x | < 0.7x |
| Energy | 1.5x | < 1.0x |
| Manufacturing | 1.8x | < 1.2x |

### Method 3: Discounted Cash Flow (DCF)

**Parameters for NSE:**
```
Risk-Free Rate: 14.5% (Kenya 10Y Bond Yield)
Equity Risk Premium: 6.5%
Cost of Equity: 21%
Terminal Growth Rate: 3% (Kenya GDP growth)
FCF Projection: 5 years
```

**DCF Formula:**
```
Fair Value = Sum(FCF_t / (1+r)^t) + Terminal Value / (1+r)^5

Terminal Value = FCF_5 x (1+g) / (r - g)
```

### Method 4: Net-Net Value (Deep Value)

**Formula:**
```
NCAV = Current Assets - Total Liabilities
NCAV Per Share = NCAV / Shares Outstanding
Buy Signal: Price < 0.67 x NCAV Per Share
```

**Application:**
- Best for: Insurance companies, investment holding companies
- Example: KNRE trading at 0.58x NCAV

### Method 5: Composite Value Score (0-100)

| Score | Rating | Action |
|-------|--------|--------|
| 90-100 | Exceptional Value | STRONG BUY |
| 75-89 | Good Value | BUY |
| 60-74 | Fair Value | HOLD |
| 40-59 | Expensive | AVOID |
| <40 | Significantly Overvalued | SELL/AVOID |

**Scoring Components:**
- Price-Based Signals (50%): P/E vs sector, P/B, EV/EBITDA
- Quality Signals (30%): ROE, ROA, Operating Margin, FCF
- Financial Safety (20%): Debt/Equity, Current Ratio, Interest Coverage

---

## Goldmine Screening Criteria

A stock qualifies as a **Goldmine Opportunity** if it passes **4 of 6** criteria:

| # | Criterion | Threshold | Weight | Rationale |
|---|-----------|-----------|--------|-----------|
| 1 | P/E vs Sector | < 0.7x sector average | 15% | Significant discount to peers |
| 2 | P/B Ratio | < 1.0 (or < 0.8x sector) | 15% | Trading below book value |
| 3 | ROE | > 15% | 12% | Excellent profitability |
| 4 | Dividend Yield | > 5% | 10% | Attractive income |
| 5 | DCF Upside | > 25% above current price | 15% | Significant undervaluation |
| 6 | Debt/Equity | < 1.0 | 8% | Financial safety |

### Bonus Criteria (Alpha Generators)

| Criterion | Threshold | Signal |
|-----------|-----------|--------|
| FCF Yield | > 10% | Strong cash generation |
| PEG Ratio | < 1.0 | Growth at reasonable price |
| Insider Buying | Net purchases | Management confidence |
| Earnings Surprise | > +15% | Beating expectations |
| Dividend Growth Streak | 3+ years | Reliable income |
| NPL Ratio (Banks) | < Industry avg | Credit quality |

### Current Goldmine Stocks (Feb 2026)

| Stock | Criteria Passed | Status |
|-------|-----------------|--------|
| KCB Group | 6/6 | GOLDMINE |
| Equity Group | 6/6 | GOLDMINE |
| Co-operative Bank | 6/6 | GOLDMINE |
| Absa Bank Kenya | 6/6 | GOLDMINE |
| NCBA Group | 5/6 | POTENTIAL |
| KenGen | 5/6 | POTENTIAL |
| Kenya Re | 4/6 | DEEP VALUE |

---

## Sector Analysis

### Banking Sector - OVERWEIGHT

**Key Metrics:**
- Sector P/E: 5.5x (vs market 7.8x)
- Sector P/B: 0.9x
- Sector ROE: 19.2%
- Sector Dividend Yield: 6.8%
- Combined H1 2025 PAT: KES 135 Billion

**Investment Thesis:**
1. Central Bank rate cuts supporting lending growth
2. Risk-based credit pricing improving margins
3. Digital transformation reducing operating costs
4. Regional expansion providing diversification

**Top Picks:** KCB, Equity Group, NCBA

**Watch Points:**
- NPL trends (industry avg 16.4%)
- Loan growth momentum
- Net interest margins

### Insurance Sector - SELECTIVE BUY

**Key Metrics:**
- Sector P/B: 1.3x
- Average P/E: ~8x

**Investment Thesis:**
1. Digital distribution growth
2. Bancassurance expansion (10% market share)
3. Regulatory capital requirements driving consolidation

**Deep Value Opportunity:** Kenya Re (KNRE) at 0.40x P/B

### Energy & Utilities - HOLD

**Key Metrics:**
- KenGen YTD: +4.6%
- Kenya Power YTD: +36.4%

**Investment Thesis:**
1. Operational turnaround potential
2. Strong dividend yields
3. Government backing

**Watch Points:**
- Tariff adjustments
- System loss reduction
- Forex exposure

---

## Alpha Generation Strategies

### Strategy 1: P/E Normalization Trade

**Concept:** Buy quality banks at P/E < 5x, sell at P/E > 7x

**Historical Performance:**
- KCB: Bought at P/E 3.8x, potential 80% upside to 7x
- Equity: Bought at P/E 4.7x, potential 50% upside to 7x

**Execution:**
1. Screen for banks with P/E < 5x AND ROE > 15%
2. Hold until P/E reaches sector average (6.3x)
3. Take profits at P/E > 7x

### Strategy 2: Deep Value Net-Net

**Concept:** Buy at < 0.67x NCAV, sell at book value

**Current Candidates:**
- KNRE: Price 0.58x NCAV, 72% upside to book value
- TCL: Price 0.47x NCAV
- HAFR: Price 0.69x NCAV

**Execution:**
1. Calculate NCAV quarterly
2. Enter at < 0.67x NCAV
3. Exit at > 0.9x book value

### Strategy 3: Dividend Capture

**Concept:** Buy high-yield stocks before ex-dividend

**Current High Yielders:**
| Stock | Dividend Yield | Ex-Date |
|-------|---------------|---------|
| SCBK | 15.1% | Q1 |
| KCB | 8.47% | Q2 |
| KEGN | 9.4% | Feb |
| EQTY | 5.67% | Q2 |

**Execution:**
1. Track ex-dividend calendar
2. Buy 2-4 weeks before ex-date
3. Sell after ex-date or hold for yield

### Strategy 4: Special Situations Arbitrage

**Current Opportunity: NCBA - Nedbank Acquisition**
- Offer Price: KES 99-105
- Current Price: KES 88.25
- Upside: 12-19%
- Timeline: Q3 2026

**Execution:**
1. Monitor regulatory approvals
2. Enter if spread > 10%
3. Hold until transaction closes

### Strategy 5: Insider Signal Tracking

**What to Watch:**
- Director share purchases (Form 2 filings)
- Substantial shareholder changes
- Management compensation alignment

**Action Triggers:**
- CEO/CFO buying > KES 1M: STRONG BUY signal
- Director selling > 50% holdings: SELL signal

### Strategy 6: Earnings Momentum

**Concept:** Buy stocks beating earnings expectations

**Recent Earnings Surprises (H2 2025):**
- KCB: +65% PAT growth
- HF Group: +134% PAT growth
- I&M: +38% PAT growth

**Execution:**
1. Track quarterly results vs expectations
2. Buy on +15% earnings surprise
3. Ride momentum for 1-2 quarters

### Strategy 7: Sector Rotation

**Recommended Allocation by Market Phase:**

| Phase | Banking | Insurance | Energy | Consumer | Cash |
|-------|---------|-----------|--------|----------|------|
| Recovery | 40% | 10% | 15% | 20% | 15% |
| Expansion | 30% | 15% | 10% | 30% | 15% |
| Peak | 20% | 10% | 10% | 20% | 40% |
| Contraction | 25% | 5% | 20% | 10% | 40% |

**Current Phase (Feb 2026): Recovery**
- Banking overweight (35%)
- Cash for opportunities (10%)

---

## Macro Indicators Dashboard

### Key Indicators to Monitor

| Indicator | Current | Signal | Action Trigger |
|-----------|---------|--------|----------------|
| CBK Rate | 8.75% | Falling | Buy rate-sensitive |
| Inflation | 4.4% | Stable | No action |
| USD/KES | 129.02 | Stable | No action |
| GDP Growth | 5.0% | Growing | Risk-on |
| Forex Reserves | USD 12.5B | Strong | Confidence |
| Market P/E | 7.8x | Cheap | Buy |

### Interest Rate Sensitivity

| Sector | Rate Sensitivity | Impact of Rate Cuts |
|--------|------------------|---------------------|
| Banking | Medium | Margin compression offset by volume |
| Insurance | Low | Positive (investment returns) |
| Real Estate | High | Positive (lower financing costs) |
| Energy | Low | Neutral |

---

## PDF Report Generation

### Automated Report Script

The skill includes a Python script for generating comprehensive PDF reports:

```bash
python scripts/generate_nse_report.py --output report.pdf
```

### Report Structure (18+ Pages)

1. **Cover Page** - Title, date, scope
2. **Executive Summary** - Key findings, top recommendations
3. **Market Analysis** - Index performance, macro indicators
4. **Company Profiles** - All 62 companies with metrics
5. **Valuation Analysis** - Graham IV, DCF, Net-Net
6. **Goldmine Screening** - Criteria results
7. **Sector Deep-Dives** - Banking, Insurance, Energy
8. **Risk Analysis** - Macro, market, sector risks
9. **Portfolio Recommendations** - Allocation, timeframes
10. **Data Sources** - Methodology, quality assessment
11. **Appendix** - Glossary, ticker list, disclaimer

### Using the Report Generator

```python
# In the skill's scripts directory
from generate_nse_report import generate_report

# Generate with custom data
generate_report(
    output_path="NSE_Report_February_2026.pdf",
    include_all_companies=True,
    valuation_methods=["graham", "dcf", "netnet"],
    screening_criteria="goldmine"
)
```

---

## Value Discovery Protocol

### When Agent Discovers Valuable Insights

**Definition of "Valuable":**
1. New stock passing 5+ goldmine criteria
2. P/E < 3x with ROE > 20% (extreme value)
3. P/B < 0.5x (deep value)
4. Special situation with > 20% arbitrage spread
5. Insider purchases > KES 5M by CEO/CFO
6. Earnings surprise > +25%
7. New dividend stock with yield > 10%
8. Corporate action with significant value unlock
9. Sector rotation signal
10. Macro indicator reversal

### Notification Protocol

When discovering valuable insights, the agent MUST:

1. **STOP** and compile the finding
2. **FORMAT** the discovery as:

```markdown
## VALUE DISCOVERY ALERT

**Discovery Type:** [Type from list above]
**Stock:** [Ticker] - [Company Name]
**Current Price:** KES [X]
**Fair Value Estimate:** KES [X]
**Potential Upside:** [X]%
**Confidence Level:** [High/Medium/Low]
**Catalyst:** [What will unlock value]
**Timeframe:** [Expected realization]
**Risk Factors:** [Key risks]

**Supporting Data:**
- [Metric 1]: [Value]
- [Metric 2]: [Value]
- [Metric 3]: [Value]

**Recommendation:** [ACTION]

**Source:** [Data source]
**Discovery Date:** [Date]
```

3. **ASK USER** for permission to update skill:

```
I've discovered a potentially valuable investment opportunity. Would you like me to:
1. Add this to the skill's known opportunities?
2. Generate a detailed research report?
3. Update the goldmine screening results?
4. Add to the watchlist?

Please confirm which actions to take.
```

---

## Risk Management

### Position Sizing Rules

| Market Cap | Max Position | Rationale |
|------------|--------------|-----------|
| > KES 200B | 15% | Large, liquid |
| KES 50-200B | 10% | Mid-cap |
| KES 10-50B | 5% | Small-cap |
| < KES 10B | 2% | Micro-cap, illiquid |

### Stop-Loss Guidelines

| Stock Type | Stop-Loss | Rationale |
|------------|-----------|-----------|
| Quality Value | -25% | Allow volatility |
| Deep Value | -35% | Higher uncertainty |
| Special Situation | Deal break | Event-driven |
| Momentum | -15% | Trend following |

### Exit Criteria

**Sell Signals:**
1. P/E reaches sector average (6.3x for banks)
2. P/B exceeds 1.5x for value stocks
3. ROE drops below 15% for quality stocks
4. Dividend cut announced
5. NPL ratio increases > 5% q/q
6. Management departure (CEO/CFO)
7. Fraud or governance issues
8. Better opportunity emerges

---

## References

### Skill Files

```
references/
├── company-universe.md      # All 62 companies detail
├── valuation-formulas.md    # DCF, Graham, Net-Net math
├── screening-criteria.md    # Goldmine methodology
├── sector-analysis.md       # Sector deep-dives
├── alpha-strategies.md      # Proven strategies
├── risk-management.md       # Position sizing, stops
└── data-sources.md          # Primary/secondary sources

scripts/
├── generate_nse_report.py   # PDF report generator
├── fetch_prices.py          # Real-time price fetcher
└── calculate_valuations.py  # Valuation calculator

templates/
├── report_template.md       # Report structure
├── discovery_alert.md       # Value discovery format
└── watchlist_template.md    # Tracking template
```

### External Resources

- NSE Official: https://www.nse.co.ke
- African Financials: https://africanfinancials.com
- Kwayisi AFX: https://afx.kwayisi.org/nse
- Central Bank of Kenya: https://www.centralbank.go.ke
- Cytonn Research: https://cytonnreport.com
- NCBA Investment Bank: https://investment-bank.ncbagroup.com

---

## Quick Start Checklist

When starting NSE analysis, follow this sequence:

1. [ ] Fetch current prices from Kwayisi AFX
2. [ ] Gather financial data from African Financials
3. [ ] Check macro indicators (CBK rate, inflation)
4. [ ] Run goldmine screening on all stocks
5. [ ] Calculate Graham IV for value candidates
6. [ ] Perform DCF on top 20 candidates
7. [ ] Identify deep value (Net-Net) opportunities
8. [ ] Check for special situations (M&A, restructuring)
9. [ ] Review sector trends and catalysts
10. [ ] Generate PDF report with recommendations
11. [ ] Alert user if VALUE DISCOVERY found

---

**Document Version:** 1.0.0
**Last Updated:** February 20, 2026
**Author:** Ziidi Trader Research Team
**Project:** NSE Institutional-Grade Stock Analysis