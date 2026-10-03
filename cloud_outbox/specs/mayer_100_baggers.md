# 100 Baggers: Stocks That Return 100-to-1 and How to Find Them — Christopher W. Mayer (Laissez Faire Books, 2015)

- **Source file:** Google Drive `100_Baggers_Stocks_That_Return_100_to_1_and_How_To_Find_Them_by.pdf` (file id `1X2VPkGe5wdn5Bc8HTmdzXzODYeLvv69H`, 2,756,241 bytes), 202 PDF pages with a text layer.
- **Text file used:** text/mayer_100_baggers.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF index). The book's printed page numbers run about 4–6 behind; never use them.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use the table of contents or running headers.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/mayer_100_baggers.md text/mayer_100_baggers.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Chapters 1–15 read sequentially, [[PAGE 1]] to [[PAGE 191]]. The Appendix, [[PAGE 192]]–[[PAGE 202]], is only a table of the 365 100-baggers (name, start date, total return, years to 100×) and contains no trading rules. Its format was checked on pp. 192–194 and 202, and its rows were not used as rules. Figure and table images are partly garbled in the text layer; only clearly legible numbers are used.

## 1. The method in brief

Mayer updates Thomas Phelps's *100 to 1 in the Stock Market* (1972). He studied 365 US stocks that returned ≥ 100× (dividends reinvested) between 1962 and 2014, starting from a market cap > $50M in today's dollars [p. 13, 15]:

- median starting sales ≈ $170M and market cap ≈ $500M [p. 50];
- average time to 100× of 26 years; only 20 did it within 10 years [p. 34, 51].

This is not a statistical model. The author warns of survivorship and hindsight bias [p. 15–16]. The essential recipe is:

1. **The core principle:** a high return on capital, with the ability to reinvest at that rate for many years [p. 171].
2. **The "twin engines":** large growth in sales and EPS, plus an expanding P/E [p. 40, 49, 179].
3. **Preferences:**
   - small companies (market cap < $1B) [p. 180];
   - owner-operators with large stakes [p. 86–95, 180–181];
   - a moat, evidenced by high and stable gross margins [p. 127–128];
   - lower multiples (PEG ≈ ≤ 1) [p. 176–178];
   - shrinking share counts (buybacks bought cheaply) [p. 116–119];
   - concentration on best ideas (half-Kelly) [p. 112–115].
4. **Holding:** "buy right and hold on", using a 10-year **coffee-can** commitment. Sell only for an investment reason (a mistake, or the thesis or criteria broken), never on price or a stop-loss [p. 9–12, 21–36, 188–191].

## 2. Strategies

### 2.1 "100-bagger" quality compounder screen with a coffee-can hold

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | long-horizon quality-growth / buy-and-hold | 171–191 |
| Timeframe & holding period | 10-year commitment (coffee can); 100× typically takes 20–25 years, the fastest about 5 | 22, 181 |
| Universe / eligibility filters | Market cap < $1B preferred (not required); established companies with long growth runways, not start-ups; avoid hot sectors, things you don't understand, and weak balance sheets; national or international markets | 36, 46, 141, 165, 180 |
| Core quality test | High return on capital (ROE about 20%) sustained, with the profits reinvested at that rate; low or no dividend preferred, since dividends reduce compounding | 85, 171, 179 |
| Growth | "Growth, growth and more growth": sales and EPS per share, not growth via dilution or price cuts. Revenue growth with little reported profit is acceptable if return on capital is high on an adjusted basis (Amazon R&D add-back, Comcast subscribers) | 56–58, 172–173 |
| Moat evidence | Gross margin high relative to competitors and stable (Berry: the single most important factor in long-run performance) | 127–128, 179 |
| People | Owner-operators with large stakes preferred (Sosnoff: management and board ≥ 10–20% of the stock); capital allocators who buy back stock below intrinsic value | 86, 99, 119, 180–181 |
| Valuation | Lower multiples preferred, avoiding "stupid prices" (e.g., 50× needs 100× earnings growth); PEG (P/E ÷ EPS growth) ≈ ≤ 1 is acceptable; don't dumpster-dive for deep value | 176–178 |
| Entry | No timing rule. Buy when the criteria are met; market crashes create the best prices (keep some cash) | 154–167, 186 |
| Position sizing | Concentrate on the best ideas (top 5–7 ≈ half the portfolio, as Akre and Donville do); half-Kelly preferred over full Kelly; a coffee can is only part of total wealth | 28, 84, 113, 172 |
| Exit | Reluctant seller: sell only when (a) you made a mistake (the facts are worse than believed), (b) the stock no longer meets the criteria, or (c) you are very sure of a better switch. Never for non-investment reasons (price "too high", tax loss, "not moving"). No stop-losses | 188–191 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Market cap at purchase | < $1B (preferred) | study median ≈ $500M; Martelli: 68% of 10-baggers < $300M at their low | 38, 50, 180 |
| ROE / return on capital | ~20% sustained | 15%+ "in most years" in many 100-baggers | 81, 85, 171 |
| Insider stake | ≥ 10–20% (Sosnoff) | — | 86 |
| PEG | ≤ 1 | P/E = growth rate "justified" | 178 |
| Holding commitment | 10 years | 20–25 years for 100× | 181 |
| Required CAGR for 100× | 20% for 25 years | 26% → 20 yrs, 36% → 15 yrs | 11, 48 |

**Key quotes**

- "the median sales figure for the 365 names at the start was about $170 million and the median market cap was about $500 million." [p. 50]
- "The average time was 26 years." [p. 51]
- "If management and the board have no meaningful stake in the company—at least 10 to 20% of the stock—throw away the proxy and look elsewhere." [p. 86]
- "high gross margins are the most important single factor of long run performance." [p. 127]
- "you need a business with a high return on capital with the ability to reinvest and earn that high return on capital for years and years." [p. 171]
- "If earnings grow 20%, for example, then a P/E of 20 is justified." [p. 178]
- "dividends are an expensive luxury for an investor seeking maximum growth" [p. 179]
- "As a general rule, I suggest focusing on companies with market caps of less than $1 billion." [p. 180]
- "What you put in it, you commit to holding for 10 years." [p. 181]
- "Never if you can help it take an investment action for a non-investment reason." [p. 189]
- "Stop losses are a substitute for thought." [p. 191]

**Pseudocode** (annual rebalance of candidates; positions held ≥ 10 years unless a criterion breaks)

```
universe: listed >= 3 yrs ; mcap < 1e9 (NSE ASSUMPTION: < Rs. 8,000 cr) ; exclude banks/NBFC? no (book includes financials) 
quality : median(ROE, last 5y) >= 20% and min(ROE, last 5y) >= 15%
          and NetDebt/Equity <= 0.5                                  # "not with leverage" (ASSUMPTION threshold)
          and payout_ratio <= 30%                                    # reinvestment preference (ASSUMPTION)
growth  : sales CAGR(5y) >= 12% and EPS CAGR(5y) >= 15% and shares_out CAGR(5y) <= 1%   # no dilution
moat    : gross_margin(5y avg) >= industry median + 10pp and stdev(gross_margin,5y) <= 3pp   # ASSUMPTION
owner   : promoter/insider holding >= 20% (NSE: promoter stake, exclude pledged > 10%)
value   : PEG = PE / EPS_CAGR(5y)*100 <= 1.0 (or PE <= 25)            # ASSUMPTION cap
rank by ROE*sales_growth / PE ; buy top 10-15 equal or conviction weight (max 12.5% each, ASSUMPTION from Donville)
hold: no price-based exit. Annual review -> sell only if: median ROE(3y) < 15% OR sales growth(3y) < 5% OR insider stake halves OR equity dilution > 10%
replace only with a candidate scoring materially higher (book: "very sure of his ground")
```

**Ambiguities & assumptions**

- None of the screen thresholds (beyond market cap < $1B, ROE ~20% and insider ≥ 10–20%) are given as hard rules. Mayer says there is "no magic formula" [p. 191]. Every other threshold above is an assumption.
- The 100-bagger list is survivorship-selected. Back-testing the screen is a fair test only if it is run point-in-time on all stocks, including delisted ones.

### 2.2 Donville high-ROE compounder rule set (sell when ROE drops below 20%)

| Field | Rule (as stated by Jason Donville, quoted by the author) | Page |
|---|---|---|
| Type | quality compounder | 79–85 |
| Screen | High ROE for 4–5 years in a row, earned from high margins, not leverage. "Through-the-cycle" average ROE is acceptable (e.g., 10% and 30% years = 20%); avoid businesses that lose money in a down cycle (most miners, many oil and gas) | 83–84 |
| Growth filter | Top-line growth ≥ 10% (buybacks with < 5% sales growth = stock goes nowhere) | 84 |
| Capital allocation | Judge how management reinvests the cash ("let's talk about your last five acquisitions") | 83 |
| Entry | Ideally buy cyclical high-ROE names in an off year | 83 |
| Position sizing | Up to 12.5% per stock (fund allows 20%); top 5 ≈ 50% | 84 |
| Exit | Hold while ROE ≥ 20%, unless the valuation "gets stupid" | 85 |
| Evidence cited | Home Capital: ROE 20.7–31.8% for 1998–2012; the stock was a 49-bagger in 16 years, ~28% annualised, close to its ROE | 79–80 |

**Key quotes**

- "If a company has a high ROE for four or five years in a row—and earned it not with leverage but from high profit margins—that’s a great place to start" [p. 83]
- "Jason is reluctant to buy a high-ROE company where the top line isn’t at least 10 percent." [p. 84]
- "The top five typically make up 50 percent of the fund." [p. 84]
- "If the ROE doesn’t fall below 20%, generally, I don’t sell" [p. 85]

**Pseudocode**

```
eligible: min(ROE over last 5 fiscal years) >= 15% and mean(ROE,5y) >= 20%      # "through-the-cycle" (ASSUMPTION blend)
          and (EBIT margin rank in industry top tercile) and Debt/Equity <= 0.5   # "not with leverage"
          and no loss year in last 10y ; sales CAGR(3y) >= 10%
buy: rank by mean ROE then lowest PE ; weights: 5 largest = 50% total (10% each), rest equal, cap 12.5%
annual exit: trailing ROE < 20% (on the fiscal-year print) -> sell ; or PE > 2 * own 10y median PE ("stupid valuation", ASSUMPTION)
```

## 3. Risk & money-management rules

- Concentrate. Half-Kelly roughly halves volatility for a ~25% lower return (Poundstone: 10% → 7.5%), and cuts the chance of halving before doubling from 1/3 to 1/9 [p. 113].
- Use only part of your money for the coffee can; a single position can go to zero [p. 31, 34].
- Avoid debt-financed investing (Graham's 1930 lesson, John Dix) and weak balance sheets, which are what fail to recover after crashes [p. 165–167].
- Keep some cash for crashes; buy after crashes. Avoid the overpriced, the permanently impaired, and the massively diluted [p. 155–156, 164–166].
- Expect deep drawdowns in winners (Apple −80% twice, Netflix −25% in a day four times, Monster −40% in three separate months) [p. 30, 190].

## 4. Non-codable guidance

- Ignore macro, the Fed and market forecasts; there were 187 100-baggers available to buy in the "dead" 1966–82 market [p. 135, 143–145, 186–187].
- Read conference-call transcripts across quarters for disappearing initiatives; avoid hot sectors and incomprehensible accounts [p. 138–141].
- Simplicity: Sosnoff's law (the thicker the research file, the worse the stock) [p. 146].
- In inflation, prefer asset-light businesses that can raise prices (See's vs "Gold-Oil Co.") [p. 151–153].
- Holding companies run by owner-operators bought below sum-of-parts (Todd Peters's list) [p. 108–111].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - 10+ years of annual fundamentals (ROE, ROCE, sales, EPS, gross margin, payout, share count, debt);
  - promoter holding and pledge data;
  - point-in-time market cap;
  - survivorship-free price history (delisted stocks included).
- **Testability with our data:** Testable only as a low-turnover annual-rebalance screen. Results need long histories (≥ 15 years) and point-in-time fundamentals to avoid look-ahead. Price data alone cannot test it.
- **Market-structure differences:**
  - Mayer cites Motilal Oswal's Indian 100× study (SQGLP: Size, Quality, Growth, Longevity, Price) [p. 41–43]. See specs for motilal_qglp when that resource is processed (it is in the to-do list).
  - Promoter holding is the natural owner-operator measure. Treat high promoter pledging as a red flag.
  - Market-cap threshold (ASSUMPTION): < Rs. 5,000–8,000 crore in place of $1B.
  - Dividend distribution tax history and buyback tax changes (2019–2024) affect payout comparisons.

## 6. Verdict

- **Codeability:** Partial. ROE, growth, market cap, insider stake, gross-margin stability, PEG and share-count rules can be coded. Moat judgement, management quality and the "reluctant seller" mistake test are discretionary. The book explicitly offers principles, not a formula.
- **Priority for backtesting:** Medium-Low as a trading strategy (very low turnover, multi-year horizon). It is valuable as a long-only quality-compounder screen and as a reference for the Motilal QGLP resource. The Donville ROE ≥ 20% hold/sell rule (2.2) is the most mechanical piece.
- **Top 3 things a coder is most likely to get wrong**
  1. Adding price stop-losses or trailing stops. The method explicitly rejects them; exits are fundamental only (mistake, criteria broken, much better switch) [p. 189–191].
  2. Back-testing on the published 100-bagger list (pure survivorship) instead of screening the full universe point-in-time [p. 15–16].
  3. Screening for cheap deep-value (low P/E, below book) instead of high, sustainable return on capital with reinvestment. Mayer says that is "hunting in the wrong fields"; lower multiples are preferred only among high-quality growers [p. 176].
