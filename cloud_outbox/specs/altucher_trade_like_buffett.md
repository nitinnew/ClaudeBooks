# Trade Like Warren Buffett — James Altucher (John Wiley & Sons, Wiley Trading series, 2005)

- **Source file:** Google Drive `Trade Like Warren Buffett - James Altucher.pdf` (file id `1Pp8Rah-PaDeQmhzKZB0Iowv0C0Ace7wC`, 2,486,034 bytes), 259 PDF pages with a text layer (246 pages carry text).
- **Text file used:** text/altucher_trade_like_buffett.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index; printed page = PDF page − 13, e.g. printed 1 = [[PAGE 14]]). Always take N from the marker.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/altucher_trade_like_buffett.md text/altucher_trade_like_buffett.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 253]].
  - Pure-number table rows (Ch. 4 company financials, Exhibits 5.1–5.3, 12.2, 12.5, 13.11–13.16, 15.1, 17.1) were read through a filtered view. Their headings, dates and captions were read; the cell values were not transcribed.
  - Charts are not readable; their captions were read.
  - The Index, [[PAGE 254]] to [[PAGE 259]], was scanned only. It contains no rules.
  - Ch. 11 (two interviews), Ch. 14 (life settlements), Ch. 15 (fixed-income arbitrage), Ch. 16 (Bill Gates' Cascade) and Ch. 17 (Jealousy) were read in full. Their rules are captured where they exist; they are mostly descriptive.

## 1. The method in brief

The book argues that Buffett is not only a buy-and-hold investor. He has traded many "workout" strategies, each built around a **margin of safety**, which the book defines as having more than one exit if the first thesis fails [p. 92, 142, 153].

Altucher sorts the strategies into four families:

- **Deep value and liquidation (Graham-Dodd):** the "cash index" of stocks trading below net cash [p. 34–36]; the cigar-butt and control cases (Sanborn Map, Dempster) [p. 48–52]; Buffett's personal REIT liquidation plays [p. 162–168].
- **Arbitrage:** merger arbitrage with expected-value and annualised-return formulas [p. 96–100]; relative-value or "negative stub" arbitrage [p. 134–141]; closed-end fund discounts [p. 172–180]; fixed-income arbitrage [p. 236–241].
- **Senior-capital-structure deals:** PIPEs and convertible preferreds (Gillette, Salomon, Champion, Level 3, Williams) [p. 142–154]; distressed and junk bonds (WPPSS, RJR, Nextel, Amazon) [p. 156–161].
- **Market-level tests:** a P/E-band timing test [p. 204–206]; a Fed-model deviation system [p. 211–215]; mean-reversion "disaster" systems (10% pullback, extreme advance/decline) [p. 229–233].

**Evidence.** Altucher's own Wealth-Lab backtests (P/E band, Fed model, pullbacks, A/D); cited academic studies (Mitchell-Pulvino merger arbitrage 1963–1998; Mitchell-Pulvino-Stafford negative stubs 1985–2000; Fich-Stefanescu; Gasbarro et al.; Flynn); CSFB/Tremont index statistics; his Dec-2002 cash-index basket, which rose more than 100% within six months [p. 47].

## 2. Strategies

| # | Strategy | Timeframe | Entry rule (as stated) | Stop / exit (as stated) | Page |
|---|---|---|---|---|---|
| 2.1 | "Cash Index" — net-cash stock basket | Months (basket held ~6 months in the example) | Market cap < cash + short-term investments (excluding inventory and long-term investments); Debt/Equity < 0.20; Market cap + annual burn rate < cash; some revenue/earnings stability. Qualitative: irrational sell-off, favourable arbitrage analysis if a deal exists, insider buying, value-fund ownership | Graham: hold until trading above cash. Catalysts: MBO, turnaround, cash dividend, takeover, reverse merger. Diversify across names | 34–36, 47 |
| 2.2 | Graham book-value / net-net bargain | Until convergence | Buy at ⅔ of book (liquidation) value. Ashton variant: below net-net working capital, value mostly in cash, excluding heavy cash burners | Sell when price > book value (Graham); Ashton sells at fair value | 33, 52, 94, 189 |
| 2.3 | Quality at low price-to-free-cash-flow (Ashton/Centaur) | Multi-year; catalyst-driven | Small, high-quality, shareholder-oriented companies at single-digit P/FCF (paid ~7× up to 11× for Atrion); target ≥15% annualised return | Sell at fair value or the high end of fair value ("always sell too early") | 185, 187–189 |
| 2.4 | Merger (risk) arbitrage | Deal life | Announced deals only. Expected value V = P·(D − T)/T; annualised AV = V × 365/x. Take the deal if AV beats alternatives. Cash deal: long the target. Stock deal: long the target, short the acquirer at the ratio. Filters: S&P 500 bidder, target below book, no hostile deals, prefer multiple bidders, bullish on the target's fundamentals | Exit at close. Plan in advance what to do if the deal breaks (fourth question). No numeric stop | 92, 96–100, 109, 113–114 |
| 2.5 | Relative-value / negative-stub (parent–subsidiary) arbitrage | Until the spin-off / distribution | Parent's market cap < value of its stake in the listed subsidiary (negative stub). Buy the parent, short the subsidiary at the distribution ratio (e.g. 0.72 UBID per Creative share; 1.5 PALM per COMS) | Exit at the distribution. Study sizing: ≤20% of equity per deal; meet all margin calls | 134–141 |
| 2.6 | Closed-end fund discount with a catalyst | Until the discount narrows | Fund at a deep discount to NAV, holdings hard to value, AND a catalyst (management change, liquidation, activist/control) | Sell as the discount narrows. A blind long-discount/short-premium portfolio is NOT profitable (Flynn) | 173–178 |
| 2.7 | P/E-band market timing (Altucher's test; result negative) | Monthly, since 1900 | Buy the S&P 500 total-return index when P/E < 10 | Sell when P/E > 20. Underperformed buy-and-hold "by a factor of 6,000" | 204–206 |
| 2.8 | Fed-model deviation timing | Monthly bars (dates are 1st of month), 1982/83–2002 | Ratio = 10-yr bond yield ÷ S&P earnings yield (trailing 12-month core earnings). Buy when the ratio is 1.5 SD below its 10-period moving average | Sell when the ratio returns to its 10-period MA. 14 trades, 71% winners, +11% average | 211–215 |
| 2.9 | 10% one-day pullback (mean reversion) | Daily | Buy a stock that closes 10% below the prior day's close (S&P MidCap 400 universe, 1997–2002) | Sell at the end of the next day (variant 2: hold one month, Nasdaq-100 subset). 5% of equity per trade | 229–231 |
| 2.10 | Extreme advance/decline capitulation | Daily signal, 2-month hold | Buy MDY at the close when NYSE advances − declines < −300 | Sell after two months. 9 trades, 6 winners (1996–2002) | 233 |

**Parameters**

- **Cash index** [p. 35–36]
  - Market cap < cash.
  - D/E < 0.20.
  - Market cap + annual burn < cash.
  - The 11 names of 11 Dec 2002 are listed in Exhibits 2.3–2.13 [p. 37].
- **Graham margin of safety:** buy at ⅔ of liquidation value [p. 94]. Sell above book [p. 52].
- **Merger arbitrage** [p. 97]
  - V = P·(D − T)/T, where P is the completion probability, D the deal price and T the target price.
  - AV = V × 365/x, where x is the expected days to close.
  - Worked example: deal at $11, target at $10, P = 1, x = 365 → 10%.
- **Merger-arbitrage study constraints:** RAIM caps each position at 10% of the portfolio and uses only liquid deals [p. 109]. Leverage on workouts is acceptable; on "generals" it is dangerous [p. 107].
- **Negative stub study** [p. 140–141]
  - ≤20% of equity per deal.
  - Short rebate 3% a year.
  - 22% a year average, 1986–2000.
- **Michaelis ratio (Source Capital)** [p. 176]
  - Total return = Yield + Growth.
  - Yield = ROE × payout ÷ P/B.
  - Growth = ROE × (1 − payout).
- **Ashton sizing** [p. 190–191]
  - Standard position 5%; maximum ("double") 7.5%.
  - Net-net positions 1–2%.
  - 25–30 longs at a time.
  - Shorts are covered after a ~30% fall within 6–8 weeks [p. 193].
- **Pabrai** [p. 198, 203]
  - Accept a special situation only if the math gives 2:1 within 2–3 years.
  - At most 10% per position, across ~10 uncorrelated bets.
  - Buying at 50 cents on the dollar beats a ~20% buy-and-hold ceiling if convergence takes ≤4 years.
- **P/E band:** buy below 10, sell above 20. Variants (upper 25/30/35, lower 15) did not beat buy-and-hold [p. 204–206].
- **Fed model:** 1.5 SD band around a 10-period MA of bond yield ÷ earnings yield [p. 214].
- **10% pullback** [p. 229–230]
  - −10% versus the prior close; exit the next close.
  - $50k per trade on $1M.
  - ~8,200 trades, 60% winners, +1.4% average.
  - Maximum drawdown −3.5%, against −40% for buy-and-hold.
- **Extreme A/D:** A − D < −300; hold 2 months [p. 233].

**Key quotes**

- "1. Market cap < cash." [p. 35]
- "2. Debt/Equity < 0.20." [p. 35]
- "3. Market Cap + Annual Burn Rate < Cash." [p. 36]
- "I like to know that if the company continues to burn money at its current rate, then the company can still be liquidated a year later so I can ideally get my money back" [p. 36]
- "Within six months of writing that article, the basket of stocks I recommended was up over 100 percent" [p. 47]
- "you should always buy a stock when it trades at 2⁄3 book value and then sell when it trades higher than book value" [p. 52]
- "It is this double-edged margin of safety (more than one possible exit strategy from the trade) that is the hallmark of a Buffett trade." [p. 92]
- "buying a stock that is trading at two-thirds of its liquidation value" [p. 94]
- "V = the expected value of the deal if the deal works out" [p. 97]
- "AV = V × (365 / x)" [p. 97]
- "I definitely feel some borrowed money is warranted against a portfolio of workouts, but feel it is a very dangerous practice against generals." [p. 107]
- "only limiting each position to 10 percent of your portfolio and also restricting yourself to deals involving more liquid securities" [p. 109]
- "when an acquirer is in the S&P 500 Index the risk arbitrage portfolio returns are 85 percent higher than when the buyer is not in the Index" [p. 109]
- "I believe that overall we have averaged annual pre-tax returns of at least 25 percent from arbitrage." [p. 113]
- "Buy deals in which an S&P 500 company is the bidder." [p. 114]
- "Buy deals in which the targeted company is trading for less than book." [p. 114]
- "Don’t do a deal when it is a hostile takeover (it is less likely to be completed)." [p. 114]
- "Buy a deal in which there are multiple bidders." [p. 114]
- "The idea of the relative value arbitrage is to buy an asset when it is convertible into other assets that have more value than it does." [p. 134]
- "limit the initial investment in any one deal to 20 percent of total equity" [p. 140]
- "The strategy of playing the spread between a parent and subsidiary resulted in an average return of 22 percent per year between 1986 and 2000." [p. 141]
- "Always ask yourself what your recourse will be if your initial plan for a stock purchase or a trade of any sort does not work out." [p. 153]
- "All he wants to know is, Can the company generate enough cash to pay him back?" [p. 157]
- "blindly playing a portfolio of going long discounted funds and going short funds trading at a premium is not a successful strategy and often offers negative returns" [p. 174]
- "3. Look for a catalyst that would get the funds trading closer to the NAV." [p. 175]
- "Growth = Return on Equity × Reinvestment rate" [p. 176]
- "a margin of safety that will give us a 15 percent annualized return, which is generally our equity hurdle rate" [p. 185]
- "Typically we prefer that most of that value is in cash, not in accounts receivable or inventories" [p. 189]
- "We also screen out those that have burnt a significant amount of cash." [p. 189]
- "But usually our maximum position, which we call the double, is 7.5 percent." [p. 190]
- "My sense is that any special situation is fine as long as your math is giving you two-to-one returns in two or three years or less." [p. 203]
- "to buy the S&P 500 whenever the P/E ratio is lower than 10 and to sell when it is higher than 20" [p. 204]
- "this method underperformed the method of simply buying on January 1, 1900, and holding until now by a factor of 6,000" [p. 205]
- "Nothing beat the buy-and-hold method." [p. 206]
- "Then I divided the bond yield by the earnings yield and bought the stock market whenever the ratio hit 1.5 standard deviations below its 10-day moving average." [p. 214]
- "I’m then selling the market when the ratio gets back to its 10-day moving average." [p. 214]
- "The average gain per trade was 11 percent." [p. 214]
- "1. Buy a stock that is 10 percent lower than the prior day close." [p. 229]
- "2. Sell at the end of the day." [p. 229]
- "let’s assume we start off with $1 million and use $50,000 per trade (five percent of portfolio per trade)" [p. 230]
- "Use the same procedure as above, except instead of holding for one day, hold for one month." [p. 231]
- "2. Sell in two months." [p. 233]
- "Not a lot of trades are generated—only nine, six of which are profitable." [p. 233]

**Pseudocode**

```
# 2.1 Cash index (quarterly fundamentals, point-in-time)
cash_st      = cash + short_term_investments            # exclude inventory, LT investments (p.35)
burn_annual  = max(0, -(operating_cf + capex_sign))     # ASSUMPTION: burn = negative FCF, annualised
if mktcap < cash_st and debt/equity < 0.20 and mktcap + burn_annual < cash_st
   and revenue_yoy > -50%:                              # p.36 "not dropping 50% a year"
     add to basket (equal weight, ASSUMPTION)
exit name when mktcap > cash_st (Graham rule p.34) or catalyst realised; review after 6-12m (ASSUMPTION)

# 2.2 Graham book bargain (p.52, 94)
buy  if price <= (2/3) * book_value_per_share      (or price < NCAV = current_assets - total_liabilities)
sell if price > book_value_per_share

# 2.4 Merger arbitrage (p.97)
V  = P * (D - T) / T                 # P = subjective completion probability
AV = V * 365 / days_to_close
filters: acquirer in index (S&P500 / NIFTY500 for NSE), not hostile, target P/B < 1 preferred, multiple bidders preferred
if AV > hurdle (ASSUMPTION: risk-free + 4%): long target; if stock deal: short ratio*acquirer
position <= 10% of portfolio (RAIM constraint p.109)

# 2.5 Negative stub (p.137-141)
stub = parent_mktcap - stake_shares * sub_price - (other_liquid_net_assets ignored)
if stub < 0 and sub shortable: long 1 parent, short r sub (r = distribution ratio); <= 20% equity per deal
exit at distribution date

# 2.7 P/E band (monthly)
if pe < 10: long index ; if pe > 20: flat           # documented failure vs buy-and-hold (p.205-206)

# 2.8 Fed-model deviation (monthly)
ratio = y10 / (E_ttm / P)
m = SMA(ratio,10); s = STD(ratio,10)                 # ASSUMPTION: s over same 10-bar window
if ratio < m - 1.5*s: buy index
if ratio >= m: sell

# 2.9 10% pullback (daily)
if close <= 0.90 * close[-1]: buy at close (ASSUMPTION: entry at signal close) ; exit next close
size = 5% equity; variant: exit after ~21 trading days

# 2.10 Extreme A/D (daily)
if (adv - dec) < -300: buy MDY at close; exit after 2 months (~42 trading days)
```

**Ambiguities & assumptions**

- **2.8 frequency is unclear.** The text says "10-day moving average" on a chart described as monthly, and every trade date in Exhibit 12.5 is the 1st of a month [p. 211, 214]. The SD window is not stated. The text says data go "back to 1982", while the exhibit is titled "Trades Executed 1983–2002".
- **2.9 entry and exit.** The text says "Sell at the end of the day". It is unclear whether entry is at the close that triggered the signal or intraday at the −10% level [p. 229]. Variant 2's universe is only "11 Nasdaq 100 stocks", with $2,000 (0.2%) per trade [p. 231].
- **2.10 breadth source.** It is not stated whether the A − D count comes from the NYSE or another exchange. With a fixed −300 threshold, the result depends on the number of issues listed [p. 233].
- **2.1 burn rate** is not formally defined. The qualitative criteria 5–8 (irrational sell-off, arbitrage analysis, insider buying, value-fund ownership) are discretionary [p. 36].
- **2.4 completion probability P** is subjective. The book says that deciding P and the time to close requires "a fair amount of discretion" [p. 98–99].
- **2.3:** the 15% hurdle and P/FCF ranges come from one manager interview. They are not a tested rule [p. 185, 189].
- **2.7 results:** only the failing P/E-band result is reported, plus one parameter sweep that also failed [p. 206].

## 3. Risk & money-management rules

- **Two exits:** every trade needs a second exit ("back door") if the first thesis fails [p. 92, 142, 153].
- **Diversification as a margin of safety:** spread the cash-index names, because any one management may never return the cash [p. 47–48].
- **Leverage:** acceptable on a diversified book of workouts; dangerous on "generals" [p. 107]. Leverage on negative-stub and fixed-income arbitrage can be fatal (Eifuku −90% in 7 days; LTCM at up to 100:1) [p. 138, 238].
- **Position caps**
  - 10% per merger deal (RAIM) [p. 109].
  - 20% of equity per stub deal [p. 140].
  - 5% (standard) or 7.5% (maximum) per position, and 1–2% per net-net (Ashton) [p. 190].
  - 10% maximum (Pabrai) [p. 203].
  - 5% per trade in the pullback system [p. 230].
- **Merger arbitrage hedging**
  - If the acquirer cannot be borrowed, short a sector basket or ETF.
  - Lock up borrows with a prime broker for the deal's duration.
  - Use puts or collars around stock deals [p. 99–100, 123–126].
- **Junk bonds:** never buy newly issued junk. Buy only "a very few" misappraised issues, and compare the bond's yield with buying an operating business [p. 157–159].

## 4. Non-codable guidance

- **PIPE and convertible-preferred deals** (Gillette 8.75%, Salomon 9%, Champion 9.25%, Level 3 9%, Williams 9.875%): a "free ride" on equity upside while collecting a coupon [p. 146–153]. These are private deals, not available to most investors.
- **Control and activist value unlocking** (Sanborn Map, Dempster) [p. 48–52]. Personal REIT liquidation arbitrage (Laser Mortgage, MGI, Burnham Pacific, Tanger, JDN, HRPT) [p. 162–168].
- **Buying quality on a temporary setback:** good companies after an earnings miss or scandal (American Express Salad Oil, Costco −22%, HCA, Gap, Outback, Nike). Average down [p. 56–58, 66, 72, 76–79, 85–87].
- **Disaster-event studies:** the market recovered after 10 systemic shocks, from 1939 to 9/11 [p. 217–229].
- **Life settlements and fixed-income arbitrage** are described, not specified [p. 234–241].
- **Shorting (Ashton):** short "cash incinerators" with large floats, just after a PIPE or secondary offering [p. 191–193].

## 5. Adapting to NSE (Indian equities)

- **Data required**
  - Daily OHLCV and corporate fundamentals (cash, short-term investments, debt, FCF, book value) for NSE-listed stocks; NIFTY 50/500 and MidCap index levels.
  - The 10-year G-sec yield and index P/E (NSE publishes P/E, P/B and dividend yield for its indices).
  - NSE daily advances/declines.
  - A deal database for open offers, delistings and schemes of arrangement.
- **Testability with our data**
  - 2.7, 2.8, 2.9 and 2.10 are directly testable on NSE price, index P/E and G-sec data.
  - 2.1 and 2.2 are testable as fundamental screens; small-cap liquidity filters are essential.
  - 2.4 maps to SEBI open offers and delisting reverse book-building (cash deals; shorting the acquirer is mostly unavailable outside F&O names).
  - 2.5 maps to holding companies trading below the value of their listed subsidiary stakes. This is common in India, but persistent holdco discounts mean "negative stub" is rarer than "deep discount". Shorting the subsidiary needs F&O eligibility or SLB borrowing.
  - 2.6 has a tiny NSE universe (listed closed-end funds and InvITs/REITs are possible proxies).
- **Market-structure differences**
  - Price bands and circuit filters cap daily moves (2%/5%/10%/20% bands on many stocks), so −10% one-day moves cluster at circuit limits. Restrict 2.9 to F&O stocks (no price bands) or treat band hits as untradeable.
  - The A − D threshold of −300 must be rescaled to NSE breadth, e.g. as a percentile of (A − D)/(A + D).
  - Market-wide short selling outside F&O is limited (SLB only), so hedged arbitrage legs are often impractical.
  - STT and stamp duty add per-trade costs, which matter for the high-turnover 2.9 (~1.4% average gross per trade in the US test).

## 6. Verdict

- **Codeability:** Partial to high.
  - Fully mechanical as stated: 2.7, 2.8 (with frequency ambiguity), 2.9 and 2.10.
  - Codeable screens with discretionary overlays: 2.1, 2.2 and 2.4 (P is subjective).
  - PIPEs, distressed bonds and activism are not codeable for us.
- **Priority for backtesting:** Medium–High.
  - Run first on NSE: 2.9 (on F&O stocks) and 2.10 (rescaled breadth). Both are short-horizon mean-reversion tests with clear rules.
  - Next: 2.8 (G-sec ÷ earnings-yield deviation) and the 2.1/2.2 net-cash and book screens.
  - 2.7 is a useful negative control.
- **Top 3 things a coder is most likely to get wrong**
  1. Running the Fed-model system (2.8) on daily data. The stated "10-day" MA sits on monthly data; Exhibit 12.5 trades are dated the 1st of the month [p. 214].
  2. Computing the cash-index screen with total current assets. Cash must be cash plus short-term investments only, inventory and long-term investments excluded, and market cap + annual burn must still be below cash [p. 35–36].
  3. Treating merger arbitrage as "buy every announced deal" without the filters (S&P 500 bidder, no hostile deals, target below book, multiple bidders) and without annualising with AV = V × 365/x [p. 97, 114].
