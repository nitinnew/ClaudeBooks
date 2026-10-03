# Security Analysis, 6th ed. — Benjamin Graham & David L. Dodd (McGraw-Hill, 2009; text of the 1940 2nd edition)

- **Source file:** Google Drive `Security-Analysis-Sixth-Edition Benjamin-Graham_-David-Dodd_Sixth edition.pdf` (file id `1t71MDRN08ql2UfvuYWMH00g-afiBycc9`, 3,371,444 bytes), 819 PDF pages with a text layer. Several chapters (9, 11–14, 20, 25, 30, 35–36, 46, Appendix) are "on accompanying CD" and are not in the PDF [p. 15–17].
- **Text file used:** text/graham_security_analysis_6th.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number; printed ≈ PDF − 53 in the Graham–Dodd chapters)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/graham_security_analysis_6th.md text/graham_security_analysis_6th.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage (partial; stated honestly):**
  - Read sequentially, the chapters that contain common-stock selection rules:
    - Contents [p. 13–17];
    - Ch. 27–29, common-stock theory and dividends [p. 401–445];
    - Ch. 37–39, earnings record and P/E [p. 525–560];
    - Ch. 42–43, book value and current-asset value [p. 601–627];
    - Ch. 50 and the start of Ch. 51, price–value discrepancies [p. 722–742].
  - Skimmed by keyword: Ch. 44 (stockholder–management) and Ch. 52 (market analysis vs. security analysis; critique of chart reading) [p. 750–756].
  - Not read: Parts I–III on bonds and preferreds and senior securities; Ch. 31–34 and 40–41 (income-account adjustments, capitalization structure); Ch. 45 and 47–49; Part VIII; the modern introductory essays.
  - These are analytical technique, not trading rules, but a fuller pass may add fixed-income screens.

## 1. The method in brief

Graham and Dodd's common-stock method values a business from demonstrated performance:

- **Earning power** is average earnings over 5–10 years, not current or trend-projected earnings [p. 529, 551].
- **Dividends** count, because a paid-out dollar is worth more to holders than a retained one [p. 437].
- **Balance-sheet values:** book, current-asset and cash-asset value [p. 606].

A purchase is an "investment" only if it is a bargain on these quantitative tests and the qualitative outlook is "not unsatisfactory" [p. 552, 556]. Three mechanical approaches emerge:

1. **Net-current-asset bargains:** buy below liquidating value [p. 615–624, 727–728].
2. **Investment-grade common stocks:** pay at most ~20× (typically 12–12.5×) average earnings, with stable earnings and strong working capital [p. 551–556].
3. **Market-level valuation timing:** buy a diversified list at about ⅔ of normal value and sell about ⅓ above it [p. 724].

Evidence:
- 1930s case histories: White Motor, Mohawk Mining, Otis, Standard Oil of Nebraska [p. 613–621].
- Census figures: more than 40% of NYSE industrials traded below net current assets in 1932, and 20.5% in early 1938 [p. 615].
- The authors' own experience favouring diversified "bargain issues" [p. 729].

No statistical back-test is given.

## 2. Strategies

### 2.1 Net-current-asset ("subliquidating value") bargains

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | deep value / asset-based | 612–624 |
| Timeframe & holding period | Until the discount closes via earnings recovery, sale/merger, or partial or complete liquidation; examples took 1–4 years | 617–621 |
| Universe / eligibility filters | Listed common stocks (industrials); prefer those with a prospect of a favourable development, or other attractive features (satisfactory current earnings and dividends, or high past earning power) | 621–622 |
| Market / regime filter | Works best when the general market is neither extremely high nor extremely low; avoid buying "cheap stocks" when the market as a whole is too high (1929, early 1937) | 624, 729 |
| Setup conditions | Price below current-asset value = current assets − all liabilities and claims ahead of the common (preferred at effective par). Variants: Group A, price < 7× last year's earnings and < NCAV; Group B, price ≤ ⅔ NCAV and < 12× last year's or average earnings | 606, 727–728 |
| Exclusion | Avoid issues "losing their current assets at a rapid rate" (compare NCAV now vs. ~3 years ago; Hupp Motors lost > 60%) | 622 |
| Entry trigger & order type | Purchase when the conditions hold; build a diversified group of such issues | 729 |
| Initial stop-loss | None stated | — |
| Exits: profit-taking | Not specified numerically; the examples exit on a re-rating to NCAV or on liquidation payouts (e.g. Mohawk paid out exactly its current-asset value) | 620 |
| Position sizing | Diversified group ("a diversified group of 'bargain issues'") | 729 |
| Portfolio limits | Not stated | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Value measure | Net current assets per share (current assets − all prior liabilities and preferred) | cash-asset value; liquidating value (rough averages: cash 100%, receivables 80% (range 75–90), inventory 66⅔% (50–75), fixed & misc. ~15% (1–50) of book) | 606, 613 |
| Price threshold | < NCAV | ≤ ⅔ NCAV (Group B) | 727–728 |
| Earnings cap | < 7× last year (Group A) | < 12× last year's or average earnings (Group B) | 727–728 |
| Asset-dissipation check | NCAV not falling rapidly | — | 622 |

**Key quotes**

- "The current-asset value of a stock consists of the current assets alone, minus all liabilities and claims ahead of the issue." [p. 606]
- "the liabilities are real but the value of the assets must be questioned." [p. 613]
- "When a common stock sells persistently below its liquidating value, then either the price is too low or the company should be liquidated." [p. 616]
- "Common stocks that (1) are selling below their liquid-asset value, (2) are apparently in no danger of dissipating these assets, and (3) have formerly shown a large earning power on the market price, may be said truthfully to constitute a class of investment bargains." [p. 623]
- "Strangely enough, this is a type of operation that fares best, relatively speaking, when price levels are neither extremely high nor extremely low." [p. 624]
- "over 40% of all the industrial companies listed on the New York Stock Exchange were quoted at some time in 1932 at less than their net current assets." [p. 615]

**Pseudocode** (annual or quarterly rebalance)

```
NCAV_ps = (CurrentAssets - TotalLiabilities - PreferredAtEffectivePar) / Shares
eligible if:
    Price <= 0.667 * NCAV_ps  and  Price < 12 * max(EPS_last, EPS_avg_5to10y)      # Group B
    or Price < NCAV_ps and Price < 7 * EPS_last                                     # Group A
    and NCAV_ps >= 0.6 * NCAV_ps_3y_ago                                            # ASSUMPTION for "not dissipating"
    and (avg EPS 5-10y > 0 or dividend paid)                                        # "formerly shown earning power"
market filter: skip new buys when market P/E (10y avg earnings) is in its top decile  # ASSUMPTION for "too high"
hold equal-weight >= 20 names; sell when Price >= NCAV_ps (or >= book value) or after 2-3 years   # ASSUMPTION
```

**Ambiguities & assumptions**

- The book gives no exit rule. ASSUMPTION: sell at NCAV (the re-rating target implied by the examples) or after a 2–3-year time stop.
- "Persistently" below liquidating value and "rapid" asset loss are undefined. ASSUMPTION: thresholds as in the pseudocode.

### 2.2 Investment-grade common stock (average-earnings multiple cap)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | value / quality | 550–556 |
| Timeframe & holding period | Long-term investment | 551 |
| Universe / eligibility filters | Satisfactory financial set-up and management, prospects not unsatisfactory | 552 |
| Setup conditions | (1) Earnings reasonably stable over 10 years; (2) average earnings bear a satisfactory ratio to price; (3) conservative financial set-up and strong working capital; not at a huge premium to tangible assets | 556 |
| Valuation | Earning power = average of 5–10 years (the most recent year only if conditions were not abnormally good, the trend is up and the industry outlook is confident). Maximum price ≈ 20× average earnings; typical neutral-prospects price ≈ 12–12.5× | 551–552 |
| Entry trigger | Price at or below the multiple cap (substantially below 20×) | 552 |
| Exits | Not stated | — |

**Key quotes**

- "But in most instances he will derive the investment value of a common stock from the average earnings of a period between five and ten years." [p. 551]
- "We would suggest that about 20 times average earnings is as high a price as can be paid in an investment purchase of a common stock." [p. 551]
- "This suggests that about 12 or 121/2 times average earnings may be suitable for the typical case of a company with neutral prospects." [p. 552]
- "The earnings have been reasonably stable, allowing for the tremendous fluctuations in business conditions during the ten-year period." [p. 556]

**Pseudocode**

```
E_avg = mean(EPS, last 7-10 fiscal years)  ; stable if no loss years and CV(EPS) < 0.5   # ASSUMPTION
buy if Price <= 12.5 * E_avg (max 20 * E_avg) and current ratio >= 2 and Debt/Equity <= 0.5 (ASSUMPTION for "conservative")
       and Price/TangibleBook <= 2.5 (ASSUMPTION for "not a huge premium")
```

### 2.3 Market-level valuation timing (Babson scheme)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | contrarian market-cycle allocation | 426, 723–724 |
| Universe | A diversified list of leading common stocks, e.g. the Dow Jones Industrial Average | 723 |
| Setup conditions | Normal value = average earnings (7–10 years) capitalised at about twice the yield on the highest-grade industrial bonds | 724 |
| Entry trigger | Buy the list at ≈ ⅔ of normal value, or scale in starting at 80% of normal value | 724 |
| Exits | Sell at ≈ ⅓ above normal value, or scale out 20–50% above normal | 724 |
| Caveats | Worked before 1925; would have required staying out of the 1927–1929 boom; needs fortitude; outright ownership only, not on margin | 724–725 |

**Key quotes**

- "The multiplier might be equivalent to capitalizing the earnings at, say, twice the current interest rate on highest grade industrial bonds." [p. 724]
- "Make composite purchases of the list when the shares can be bought at a substantial discount from normal value, say, at 2/3 such value." [p. 724]
- "Sell out such purchases when a price is reached substantially above normal value, say, 1/3 higher" [p. 724]

**Pseudocode** (monthly, index level)

```
E_norm = mean(index EPS, 10y) ; y_AAA = high-grade corporate yield
Normal = E_norm / (2 * y_AAA)
if Index <= 0.80 * Normal: start buying, fully invested by 0.667 * Normal
if Index >= 1.20 * Normal: start selling, fully out by 1.333 * Normal (or 1.5)
```

## 3. Risk & money-management rules

- Margin of safety: rely on demonstrated, average performance, not on projected trends [p. 531–532, 551].
- Diversify: common-stock investment is "a group operation" [p. 419].
- Don't trade on margin; the outright owner can afford to buy and sell too soon [p. 724].
- Adjust per-share earnings and asset values for dilution (convertibles, warrants) before applying the tests [p. 557–559].
- Value preferred stock at its effective par (dividend ÷ 5% or market/par, whichever is higher) when computing common-stock book value or NCAV [p. 603–604].

## 4. Non-codable guidance

- Qualitative survey must support the quantitative data: industry permanence, competitive position [p. 527].
- Current earnings should not be the primary basis of appraisal; the market over-reacts to them [p. 529].
- Trends cannot be projected indefinitely; trend-based valuations "obey no arithmetical rules" [p. 530–531].
- Dividends: a dollar paid out is worth more than a dollar retained. Price a low-payout stock between its dividend-yield and earnings-yield values, nearer the lower one [p. 437–439].
- Growth stocks: buy only at prices a prudent private buyer would pay. A marketability premium of no more than about 20% [p. 424–425].
- Litigation, receivership and seasoned-vs-unseasoned senior-security mispricings are mainly bond opportunities [p. 734–742].
- Chart reading "cannot possibly be a science" and cannot be continuously successful [p. 752–755].

## 5. Adapting to NSE (Indian equities)

- **Data required:** annual or quarterly balance sheets (current assets, total liabilities, preferred), 5–10 years of EPS, dividends, shares outstanding, and prices. For 2.3, NIFTY 10-year average EPS and AAA corporate bond yields.
- **Testability with our data:** 2.1 and 2.2 need point-in-time fundamentals; avoid look-ahead by lagging results by the filing delay (about 2–3 months after the quarter). 2.3 is testable on index EPS series.
- **Market-structure differences:**
  - NCAV stocks in India are mostly micro-caps and illiquid; apply a liquidity floor (ASSUMPTION: 20-day median traded value ≥ Rs. 50 lakh).
  - Promoter-controlled firms rarely liquidate, so the re-rating catalysts (sale, liquidation) are rarer. Graham himself flags stockholder apathy [p. 628].
  - Cash-rich holding companies may appear in the screen; a holding-company discount is common.

## 6. Verdict

- **Codeability:** Yes for the screens (2.1, 2.2, 2.3); the qualitative overlay and the exits are discretionary.
- **Priority for backtesting:** Medium. The NCAV screen (2.1) and the earnings-multiple cap (2.2) are classic, cleanly specified fundamental screens worth running on NSE once point-in-time fundamentals are available. With price data only, just 2.3 is feasible, and only if index EPS and bond yields are available.
- **Top 3 things a coder is most likely to get wrong**
  1. NCAV = current assets minus ALL liabilities (and preferred at effective par), not current assets minus current liabilities (that is working capital) [p. 606].
  2. Using current or trailing-twelve-month earnings for the multiple, instead of the 5–10-year average earning power [p. 551].
  3. Using fundamentals before they were published (look-ahead), and ignoring the asset-dissipation exclusion [p. 622].
