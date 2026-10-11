# How to Make Money Trading with Candlestick Charts — Balkrishna M. Sadekar

- **Source file:** Google Drive: How to make money trading with candlestick charts.pdf
- **Text file used:** text/sadekar_candlestick_charts.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/<key>.md text/<key>.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read lines 1-5461 (the entire text file) in sequential chunks; last `[[PAGE N]]` reached = 399 (the final page, the Appendix ready reckoner, ends at line 5461). Pages with no text at all: 1, 10, 169, 246, 379 (verified by script: nothing between their marker and the next marker). No chapters skipped; every chapter was read, including chart captions, the stop-loss section, the tips section and the appendix. Charts/figures are images and are not in the text, so chart-specific details (exact pattern geometry, trendline positions) are known only from the captions and the author's commentary. The book's Index (listed in the contents, p. 18) is not present in the text file. Reading done by a Sonnet sub-agent (notes log covers lines 1-5461 in 7 chunks). The coordinator re-ran the verifier and an exact-page check and spot-checked 10 unquoted table citations (sizing p. 352, trend rule pp. 344-345, ABB p. 218, Tata Steel p. 235, weekly charts p. 357, 0.1% buffer p. 295, among others).

## 1. The method in brief

Sadekar teaches Japanese candlestick reversal signals as a swing-trading / weekly-investing method built on a fear-and-greed view of the market: buying into others' fears and selling into others' greed [p. 39]. He lists 13 patterns: Doji, Hammer, Hanging Man, Inverted Hammer, Shooting Star, Bullish and Bearish Engulfing, Piercing, Dark Cloud Cover, Bullish and Bearish Harami, Morning Star and Evening Star [p. 70], plus Bullish/Bearish Kicker in the appendix only [p. 388, 398]. Each pattern needs a definite prior trend, a defined candle geometry, and, above all, confirmation on the next candle before any trade is taken [p. 93, 105, 340, 341]. Overbought/oversold stochastics (N=12, 3-day smoothing) and volume spikes make a signal more probable but are explicitly "secondary" to the candle signal [p. 62, 65, 66, 67, 342]. Part II combines the signals with support/resistance trendlines and simple moving averages (20/30/50) [p. 250, 251, 271], and gives a pattern-specific stop-loss rule: exit where the signal is negated, not at an arbitrary percentage [p. 284, 285, 288]. Profits are taken on a confirmed opposite signal, with price targets (previous highs/lows, trendlines, Fibonacci, MAs) and a minimum reward-risk of 2 (author prefers 3) as filters only [p. 326, 346, 347]. The method is claimed to work on any market and any timeframe (stocks, indices, futures, commodities, currencies; daily, weekly, monthly) [p. 23, 357, 376, 377].

Evidence: the book offers no statistics, win rates or track record. The only support is the "four centuries" of Japanese use [p. 37, 281] and about 40 annotated example charts, almost all hand-picked winners plus a few deliberately shown failures (Jaiprakash Associates, Grasim, Syndicate Bank, Hindustan Petroleum) [p. 309, 312, 314, 319]. The author admits signals fail and says this is not a get-rich-quick scheme [p. 30, 281].

Market: the book is explicitly written for Indian traders and every chart is of an NSE or BSE company (Nifty index, Pfizer, Syndicate Bank, Hindalco, BHEL, Tata Steel, Infosys etc., prices in rupees, Rs 10 lakh portfolio example) [p. 23, 29, 351]. Charts are mostly 2005-2007 daily and weekly charts [p. 192, 233, 312]. The author also trades options and advocates trading both long and short [p. 280, 377].

## 2. Strategies

Every pattern below is a separate, separately testable setup. All long setups share the same entry/exit framework; the bearish setups are listed separately because the book gives them their own criteria and stops, but in the NSE cash market they can only be used as exits for long positions (see Section 5).

### 2.0 Shared definitions used in every pseudocode block (not a strategy)

- Candle fields: O, H, L, C per day; "white" = close above open, "dark" = close below open; each candle is independent of the previous close [p. 40, 41, 54, 55].
- "Definite trend": judged visually on the chart [p. 92, 105]; no numeric rule. See each Ambiguities block for the assumed numeric default.
- Confirmation: the day after the signal must show "continued buying" (buys) or "continued selling and a lower close" (sells) [p. 92, 105]. Only act on confirmation [p. 340, 341]. An unconfirmed signal is ignored [p. 126, 134, 137, 210, 243].
- Stochastics: %K = (C - L) / (H - L) * 100 over N days; N = 12; %K smoothed over 3 days; %D is a moving average of the smoothed %K [p. 63, 64, 66, 67]. Above 80 overbought, below 20 oversold [p. 65].
- Data requirements (all strategies): daily Open, High, Low, Close, Volume per stock; NIFTYBEES or equal-weight index for index-level confirmation (optional).


### 2.1 Doji (reversal / breakout of indecision)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick reversal / indecision signal; three uses: long at bottom, sell/short at top, trend-start after sideways market | 77, 78, 79, 80 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Open and close almost at the same price; upper and/or lower shadow allowed. Variants: Gravestone (no lower shadow, best at top of trend), Dragonfly (no upper shadow, best near bottom), Spinning Top (small body). Meaning depends on position: after uptrend in overbought state = sell warning; after downtrend in oversold state = buy watch; in a sideways market = wait for gap. Enhancers: stochastics oversold/overbought, heavy volume on Doji day, long upper and lower shadows, gap next day. | 74, 75, 76, 77, 78, 79, 80, 81 |
| Entry trigger & order type | Long: after Doji in downtrend/oversold, buy only on next-day strength (e.g. gap-up bullish candle). Sell/short: after Doji at top, act on next-day confirmation (dark candle / lower open). Sideways market: enter in the direction of the next day's gap up or gap down. Order type not stated. | 80, 81, 83, 85, 88, 89 |
| Initial stop-loss | Not found in this book for the Doji specifically. Book's general rule: exit where the signal is negated. | 285, 288 |
| Exits: profit-taking | No fixed target. Target is only a guide (previous high/resistance, trend line, Fibonacci level, major MA); take profit when a confirmed opposite (sell) candlestick signal appears even before target is reached. Reward-risk of at least 2 (author prefers 3+) required before entry. | 325, 326, 346, 347 |
| Exits: trailing / time / signal | Exit a Doji-based long when a spinning top/Doji at the top is confirmed by a dark candle the day after; or on a string-of-Doji sell confirmed by a bullish candle when short. | 88, 89, 372, 373 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Doji body tolerance | 'almost' same open and close | no number given | 74 |
| Enhancer: gap next day | gap up/down desired | - | 80, 81 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "The open and the close of the stock must be almost at the same price level." [p. 74]
- "What you want to see now is a gap up or gap down scenario the next day." [p. 80]
- "(yes, I wait for confirmation even after a Doji at the top)" [p. 85]
- "Doji at the top warrants immediate selling" [p. 83]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
def doji(t): return abs(C[t]-O[t]) <= 0.05*(H[t]-L[t]) and H[t]>L[t]          # ASSUMPTION tolerance
# long: Doji ends a downtrend
if doji(t0) and is_downtrend(t0-1) and K(t0)<20 and bull_confirm(t0) and True:
    ENTER_LONG at open(t0+2); stop = L[t0] * (1-0.001)    # ASSUMPTION stop
# exit of a long (cash market): Doji after uptrend then bearish confirmation
if doji(t0) and is_uptrend(t0-1) and K(t0)>80 and bear_confirm(t0):
    EXIT_LONG at open(t0+2)    # (or SHORT where allowed)
# sideways: Doji in range, trade the gap on next day
if doji(t0) and in_sideways_range(t0) and O[t0+1]>H[t0]: ENTER_LONG ; elif O[t0+1]<L[t0]: SELL/SHORT
```

**Ambiguities & assumptions**

- Contradiction on top Dojis: 'a Doji at the top warrants immediate selling' [p. 83] versus 'I wait for confirmation even after a Doji at the top' [p. 85] and the Hindalco example in which unconfirmed Dojis at the top were rightly ignored [p. 86, 87]. ASSUMPTION: require confirmation for both directions (the author's own practice, p. 85).
- Sideways market: no definition of 'sideways' or of the size of the gap. ASSUMPTION: range = price within a 15-day high/low band narrower than 10% of price; gap = open beyond the Doji day's high/low.
- No stop-loss specified. ASSUMPTION: long stop just below Doji low (0.1% buffer by analogy with the Piercing stop, p. 295).
- No numeric Doji tolerance; ASSUMPTION |C-O| <= 5% of the day's range.

### 2.2 Hammer (bullish)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bullish reversal, one-day signal plus confirmation | 90, 91 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite downtrend; small body; lower shadow at least twice the body; no or very small upper shadow; body colour irrelevant (white more positive). Enhancers: gap down on Hammer day, volume spike on Hammer day, stochastics oversold, longer lower shadow. The Hammer is also valid when stochastics are not oversold (Biocon) and a small upper shadow is acceptable. | 91, 92, 93, 94, 96, 97 |
| Entry trigger & order type | Enter only after confirmation: the following day must trade higher / show continued buying; an unconfirmed Hammer is not bought. Order type not stated; Punjab National Bank example bought 'around' Rs 430 after confirmation. | 92, 93, 96, 126 |
| Initial stop-loss | Below the low of the Hammer: if the price drops below the Hammer's low the signal is negated. | 289 |
| Exits: profit-taking | No fixed target. Target is only a guide (previous high/resistance, trend line, Fibonacci level, major MA); take profit when a confirmed opposite (sell) candlestick signal appears even before target is reached. Reward-risk of at least 2 (author prefers 3+) required before entry. | 325, 326, 346, 347 |
| Exits: trailing / time / signal | Signal exit: sell when bears take control (confirmed bearish signal, e.g. lower close after bearish pattern; gap down after a bearish pattern is strong evidence). Unconfirmed bearish signals are ignored. Being overbought alone is not a sell reason. No time stop given. Exit before earnings released. | 235, 334, 335, 342, 347 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lower shadow / body | >= 2 | 'the longer the lower shadow, the better' | 92, 94 |
| Upper shadow | none or very small | small upper shadow acceptable relative to the lower shadow | 92, 96 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "The lower shadow must be at least twice the size of the body." [p. 92]
- "The day after the Hammer is formed, one should witness continued buying." [p. 92]
- "the stock needs to trade higher the next day to confirm that the bulls have actually reversed the trend" [p. 93]
- "if the price drops below the low of the Hammer, the signal is negated" [p. 289]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
def hammer(t): return body>0 and lo_sh>=2*body and up_sh<=0.25*lo_sh(or <=0.1*rng) [ASSUMPTION]
if hammer(t0) and is_downtrend(t0-1) and bull_confirm(t0):
    score = (O[t0]<C[t0-1]) + (V[t0]>1.5*SMA(V,20)[t0]) + (K(t0)<20)    # optional enhancers, not mandatory
    ENTER_LONG at open(t0+2); stop = L[t0]*(1-0.001); target = prior swing high; require (target-entry)/(entry-stop)>=2
exit: stop hit (low < stop), or bearish pattern with bear_confirm, or target reached
```

**Ambiguities & assumptions**

- 'Definite downtrend' is visual only [p. 92]. ASSUMPTION: is_downtrend as in the helper (C below falling SMA20 and down >= 5% in 10 days).
- Confirmation not defined numerically: 'continued buying' / 'trade higher the next day' [p. 92, 93]. ASSUMPTION: next day white and closes above the Hammer day's close; entry at the open of the day after confirmation (book's phrase 'buy strength' [p. 122] supports buying even after a gap up).
- Book gives no number for 'very small' upper shadow. ASSUMPTION: upper shadow <= 25% of lower shadow.
- Whether the stop is triggered intraday or on a close is not stated for the Hammer; ASSUMPTION: intraday touch of the stop (low < Hammer low); test the close-basis variant.
- Entry at open vs close of the confirmation day: not stated. ASSUMPTION: open of the day following the confirmation candle.

### 2.3 Hanging Man (bearish)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bearish reversal, one-day signal plus confirmation; sell existing longs or short | 90, 108 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite uptrend; same shape as the Hammer (lower shadow at least twice the body, no or very small upper shadow); colour irrelevant (black stronger). Enhancers: volume spike on signal day, gap up on signal day, stochastics overbought, longer lower shadow; also stronger at a previous resistance. | 103, 105, 107, 109, 110 |
| Entry trigger & order type | Only after confirmation: next day shows continued selling and a lower close. Then short, or at least sell existing position and lock in profit. | 105, 106, 108, 112 |
| Initial stop-loss | For a short: the top of the Hanging Man is resistance; if the bulls take the price above the body of the Hanging Man the signal is failed. | 300 |
| Exits: profit-taking | Target is a guide only (previous low, trend line, Fibonacci level, major MA); cover when a confirmed bullish (buy) signal appears, e.g. Morning Star at old resistance-turned-support. Reward-risk of at least 2 (author prefers 3+). | 326, 346, 347, 370 |
| Exits: trailing / time / signal | Signal exit: cover when a confirmed buy signal appears or price breaks the stop level; no time stop given. Exit before earnings released. | 334, 335, 347, 370 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lower shadow / body | >= 2 | longer is better | 105, 107 |
| Upper shadow | none or very small | - | 105 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "The day after the Hanging Man signal should witness continued selling and a lower close." [p. 105]
- "Those who are averse to shorting stocks can at least sell their existing position and lock-in profits." [p. 108]
- "If the bulls can take the price above the body of the Hanging Man, the signal is considered failed." [p. 300]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
def hanging_man(t): same shape test as hammer(t)
if hanging_man(t0) and is_uptrend(t0-1) and bear_confirm(t0):
    if holding(stock): EXIT_LONG at open(t0+2)                          # NSE cash: exit only
    else (where shorting allowed): SHORT at open(t0+2); stop = H[t0]*(1+0.001)   # ASSUMPTION
    optional enhancers: gap up on t0, V spike, K>80
```

**Ambiguities & assumptions**

- The stop wording is inconsistent: 'top of the Hanging Man' is resistance, but failure is 'above the body' [p. 300]. ASSUMPTION: stop = high of the Hanging Man day (+0.1%), triggered on a close above the body top as the stricter alternative.
- Confirmation = lower close [p. 105]; no numeric lower-close definition. ASSUMPTION: close below the Hanging Man day's close and a dark candle.
- Short selling is not available in the NSE cash market; test only as an exit/avoid-entry filter for long positions.

### 2.4 Inverted Hammer (bullish)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bullish reversal, one-day signal plus confirmation | 114, 115 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite downtrend; upper shadow at least twice the body; no or very small lower shadow; colour irrelevant (white better). Enhancers: gap down on signal day, volume spike, stochastics oversold, longer upper shadow. 'Almost' formations (e.g. upper shadow less than twice the body, stochastics not oversold) should not be chased. | 116, 117, 118, 119, 124 |
| Entry trigger & order type | Wait for confirmation: the following day must show continued buying (closes higher). Buy even if the confirmation day is followed by a gap up ('buy strength and sell weakness'). A Hammer followed by an Inverted Hammer then a Doji and a gap up was bought on the gap up. | 116, 117, 118, 122, 123, 126 |
| Initial stop-loss | Below the bottom of the body of the Inverted Hammer (strong support area); declining below it means the bulls failed to hold support. | 291, 292 |
| Exits: profit-taking | No fixed target. Target is only a guide (previous high/resistance, trend line, Fibonacci level, major MA); take profit when a confirmed opposite (sell) candlestick signal appears even before target is reached. Reward-risk of at least 2 (author prefers 3+) required before entry. | 325, 326, 346, 347 |
| Exits: trailing / time / signal | Signal exit: sell when bears take control (confirmed bearish signal, e.g. lower close after bearish pattern; gap down after a bearish pattern is strong evidence). Unconfirmed bearish signals are ignored. Being overbought alone is not a sell reason. No time stop given. Exit before earnings released. | 235, 334, 335, 342, 347 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Upper shadow / body | >= 2 | longer is better | 116, 119 |
| Lower shadow | none or very small | - | 116 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "The upper shadow must be at least twice the size of the length of the body." [p. 116]
- "If the bulls manage to close the price higher the next day, the downtrend is considered broken." [p. 117]
- "The bottom of the body of the Inverted Hammer (Figure 11.2) is considered a strong support area." [p. 291]
- "would be well advised not to chase these" [p. 124]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
def inv_hammer(t): return body>0 and up_sh>=2*body and lo_sh<=0.25*up_sh [ASSUMPTION ratio]
if inv_hammer(t0) and is_downtrend(t0-1) and bull_confirm(t0):
    ENTER_LONG at open(t0+2); stop = min(O[t0],C[t0])*(1-0.001)
    require reward-risk >= 2 vs prior swing high
exit as in shared long exits
```

**Ambiguities & assumptions**

- Pattern requires 'upper shadow >= 2x body' strictly; 'almost' patterns are explicitly to be skipped [p. 124]. ASSUMPTION: strict >= 2.0.
- Stop: 'bottom of the body' [p. 291] is taken literally (body low = min(O,C)); the 0.1% buffer is only stated for the Piercing signal [p. 295]. ASSUMPTION: apply 0.1% buffer here too; test without.
- Trend, confirmation and entry-time ambiguities as in 2.2.

### 2.5 Shooting Star (bearish)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bearish reversal, one-day signal plus confirmation | 114, 128 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite uptrend; upper shadow at least twice the body; no or very small lower shadow; colour irrelevant (black stronger). Enhancers: volume spike, gap up on the signal day, stochastics overbought, longer upper shadow. A tiny lower shadow is acceptable relative to the upper shadow. | 130, 131, 132, 136 |
| Entry trigger & order type | After confirmation: the next day continues selling with a lower close, shown in the Tata Teleservices example as a close below the low of the Shooting Star. A Doji/Spinning Top the next day is not confirmation; wait for a bearish candle. | 130, 134, 136, 137 |
| Initial stop-loss | For a short: get out immediately if the bulls trade the stock above the high of the Shooting Star. | 301, 302 |
| Exits: profit-taking | Target is a guide only (previous low, trend line, Fibonacci level, major MA); cover when a confirmed bullish (buy) signal appears, e.g. Morning Star at old resistance-turned-support. Reward-risk of at least 2 (author prefers 3+). | 326, 346, 347, 370 |
| Exits: trailing / time / signal | Signal exit: cover when a confirmed buy signal appears or price breaks the stop level; no time stop given. Exit before earnings released. | 334, 335, 347, 370 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Upper shadow / body | >= 2 | longer is better | 130, 132 |
| Lower shadow | none or very small | - | 130 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "The day after the Shooting Star signal should witness continued selling and a lower close." [p. 130]
- "by closing the price below the low of the Shooting Star" [p. 134]
- "get out immediately if the bulls manage to trade the stock above the high" [p. 301]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
def shooting_star(t): body>0 and up_sh>=2*body and lo_sh<=0.25*up_sh
if shooting_star(t0) and is_uptrend(t0-1) and bear_confirm(t0):
    if holding: EXIT_LONG at open(t0+2)
    else (shorting allowed): SHORT at open(t0+2); stop = H[t0] (intraday touch)
```

**Ambiguities & assumptions**

- Confirmation definition differs: 'a lower close' [p. 130] versus 'closing the price below the low of the Shooting Star' [p. 134]. ASSUMPTION: default lower close than day-0 close; test strict close < day-0 low.
- Shorting is not possible in NSE cash; use as an exit for longs.

### 2.6 Bullish Engulfing

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bullish reversal, two-day signal plus confirmation | 138, 139 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite downtrend; day 2 white and its body completely engulfs day 1's black body (first day may be a Doji). Appendix form: day 2 white, opens below the previous Close and closes above the previous Open. Enhancers: very long first dark body, volume spike on either day, first dark candle gapped down, stochastics oversold, white body engulfs more than one black candle. Even a small engulfing candle qualifies. | 141, 143, 144, 149, 383, 384 |
| Entry trigger & order type | Buy on confirmation the following day (more buying; check that residual selling is not heavy). Order type not stated. | 147, 148 |
| Initial stop-loss | The bottom of the bullish (engulfing) candle is the support; after confirmation prices should not get back through this point. | 293, 294 |
| Exits: profit-taking | No fixed target. Target is only a guide (previous high/resistance, trend line, Fibonacci level, major MA); take profit when a confirmed opposite (sell) candlestick signal appears even before target is reached. Reward-risk of at least 2 (author prefers 3+) required before entry. | 325, 326, 346, 347 |
| Exits: trailing / time / signal | Signal exit: sell when bears take control (confirmed bearish signal, e.g. lower close after bearish pattern; gap down after a bearish pattern is strong evidence). Unconfirmed bearish signals are ignored. Being overbought alone is not a sell reason. No time stop given. Exit before earnings released. | 235, 334, 335, 342, 347 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Engulfing test | day-2 body completely covers day-1 body | appendix: open below prior Close, close above prior Open | 141, 383, 384 |
| First-day Doji allowed | yes | - | 141 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "the body should completely engulf" [p. 141]
- "Even if the first day is a Doji (described in Chapter 3), it is still a bullish engulfing signal." [p. 141]
- "the bottom of the bullish candle is logically analyzed to be a strong support" [p. 293]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
if is_downtrend(t0-1) and dark(t0-1) and white(t0) and O[t0]<=C[t0-1] and C[t0]>=O[t0-1] [ASSUMPTION <=,>=; doji day-1 also ok]:
    if bull_confirm(t0): ENTER_LONG at open(t0+2); stop = O[t0]*(1-0.001)   # body bottom of the white candle; require RR>=2
# exception: if K(t0)>80 (overbought) treat as bearish last-gasp signal (see 2.15)
```

**Ambiguities & assumptions**

- 'Bottom of the bullish candle' [p. 293] could be the low or the open of the white candle. ASSUMPTION: body bottom (open) minus 0.1%; test low-based stop.
- Strict inequality vs equality in the engulf test: the Nifty Harami example accepts an open equal to the prior close [p. 212] and the appendix says 'opening below the Close' [p. 384]. ASSUMPTION: allow equality.
- Confirmation day definition as in 2.2.

### 2.7 Bearish Engulfing

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bearish reversal, two-day signal plus confirmation | 138, 151 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite uptrend; day 2 black and its body completely engulfs the previous white body (first day may be a Doji). Appendix form: opens above previous Close, closes below previous Open. Enhancers: long white first day, volume spike, first white gapped up, stochastics overbought, black body engulfs more than one white candle. Works on indices (Nifty example) and index weakness supports single-stock sells. | 152, 154, 155, 162, 163, 393, 394 |
| Entry trigger & order type | After completion of the pattern the trader should see more selling; sell (or short) after confirmation. Not every unconfirmed Bearish Engulfing should be shorted (Jaiprakash weekly example). | 159, 160, 161, 364, 365 |
| Initial stop-loss | Bulls are back in charge if they close prices above the body of the dark candle. | 303 |
| Exits: profit-taking | Target is a guide only (previous low, trend line, Fibonacci level, major MA); cover when a confirmed bullish (buy) signal appears, e.g. Morning Star at old resistance-turned-support. Reward-risk of at least 2 (author prefers 3+). | 326, 346, 347, 370 |
| Exits: trailing / time / signal | Signal exit: cover when a confirmed buy signal appears or price breaks the stop level; no time stop given. Exit before earnings released. | 334, 335, 347, 370 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Engulfing test | day-2 body completely covers day-1 body | appendix: open above prior Close, close below prior Open | 152, 393, 394 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "black and the body should completely engulf" [p. 152]
- "The bulls would be considered in charge of the stock again, if they can manage to close prices above the body of the dark candle" [p. 303]
- "Candlestick signals are universal. They can be applied to indexes as well." [p. 163]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
if is_uptrend(t0-1) and white(t0-1) and dark(t0) and O[t0]>=C[t0-1] and C[t0]<=O[t0-1] and bear_confirm(t0):
    if holding: EXIT_LONG at open(t0+2)
    else (shorting allowed): SHORT at open(t0+2); stop: any close above max(O[t0],C[t0]) of dark candle
# index filter (optional): if NIFTY shows bearish engulfing, weight stock sell signals more
```

**Ambiguities & assumptions**

- Stop is on a closing basis here [p. 303] but intraday for the Shooting Star [p. 301]; both kept as the book states them.
- Cash market: exit signal for longs only.

### 2.8 Piercing Signal (bullish)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bullish reversal, two-day signal plus confirmation | 170, 171 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite downtrend; day 2 white candle opens below the previous day's trading range and closes at least half way into the previous dark body. Enhancers: very long first dark body, volume spike on either day, first dark candle gapped down, stochastics oversold, day-2 white opens far below the previous range. Valid even when stochastics are not oversold (Mahindra example): signal primary, oscillator secondary. | 171, 173, 175, 179, 180, 385 |
| Entry trigger & order type | Buy after confirmation on the next day (the book states this as a general rule for all signals; no Piercing-specific confirmation text). Order type not stated. | 340, 341 |
| Initial stop-loss | Just below (typically 0.1% below) the bottom of the bullish candle; signal negated if price comes back down through that point. | 295, 296 |
| Exits: profit-taking | No fixed target. Target is only a guide (previous high/resistance, trend line, Fibonacci level, major MA); take profit when a confirmed opposite (sell) candlestick signal appears even before target is reached. Reward-risk of at least 2 (author prefers 3+) required before entry. | 325, 326, 346, 347 |
| Exits: trailing / time / signal | Signal exit: sell when bears take control (confirmed bearish signal, e.g. lower close after bearish pattern; gap down after a bearish pattern is strong evidence). Unconfirmed bearish signals are ignored. Being overbought alone is not a sell reason. No time stop given. Exit before earnings released. | 235, 334, 335, 342, 347 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Day-2 open | below previous day's trading range (low) | - | 171, 173 |
| Penetration | close above 50% of day-1 body | deeper is better | 171, 173, 174 |
| Stop buffer | 0.1% below bottom of bullish candle | 'typically' | 295 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "closes above the half-way point of that dark body" [p. 171]
- "just below (typically 0.1% below) this price" [p. 295]
- "the candlestick signal is the primary factor. The oscillators are secondary factors." [p. 179]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
if is_downtrend(t0-1) and dark(t0-1) and white(t0) and O[t0]<L[t0-1] and C[t0]>=(O[t0-1]+C[t0-1])/2 and C[t0]<O[t0-1]:
    if bull_confirm(t0): ENTER_LONG at open(t0+2); stop = bottom(white candle)*(0.999)
```

**Ambiguities & assumptions**

- 'Bottom of the bullish candle' not defined as low or open; the white candle opens below the prior low so open ~ bottom of body, and the low may be lower. ASSUMPTION: use the low of the white candle minus 0.1%; test body bottom.
- 'opens below the low of the previous day' [p. 171]; the earlier chapter text sometimes says 'below the trading range' - same meaning. ASSUMPTION: strict O[t0] < L[t0-1].
- Whether close must be strictly below the previous open (otherwise it would be engulfing): not stated; ASSUMPTION: C < O[t0-1].

### 2.9 Dark Cloud Cover (bearish)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bearish reversal, two-day signal plus confirmation | 170, 183 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite uptrend; day 2 dark candle opens above the previous day's trading range and closes more than half way into the white body. Enhancers: very long first white body, volume spike on either day, first white gapped up, stochastics overbought, day-2 dark opens far above the previous range; also stronger at previous resistance. | 183, 185, 186, 187, 191, 394, 395 |
| Entry trigger & order type | Sell/short after confirmation selling the next day. Example: unconfirmed Dark Cloud signals in an uptrend were not acted on (Tata Steel). | 185, 234, 235 |
| Initial stop-loss | Just above the open of the dark candle of the Dark Cloud Cover; prices trading above that point negate the signal. | 304 |
| Exits: profit-taking | Target is a guide only (previous low, trend line, Fibonacci level, major MA); cover when a confirmed bullish (buy) signal appears, e.g. Morning Star at old resistance-turned-support. Reward-risk of at least 2 (author prefers 3+). | 326, 346, 347, 370 |
| Exits: trailing / time / signal | Signal exit: cover when a confirmed buy signal appears or price breaks the stop level; no time stop given. Exit before earnings released. | 334, 335, 347, 370 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Day-2 open | above previous day's trading range (high) | - | 183, 185 |
| Penetration | close more than half way into white body | deeper is better | 183, 186 |
| Stop buffer | 'just above' open of dark candle | no number | 304 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "closes more than half way into the white coloured body" [p. 183]
- "It is recommended to set your stop loss just above the open of the dark candle" [p. 304]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
if is_uptrend(t0-1) and white(t0-1) and dark(t0) and O[t0]>H[t0-1] and C[t0]<(O[t0-1]+C[t0-1])/2 and C[t0]>O[t0-1]:
    if bear_confirm(t0): EXIT_LONG at open(t0+2)   # or SHORT, stop=O[t0]*1.001 [ASSUMPTION buffer]
```

**Ambiguities & assumptions**

- Stop buffer unspecified; ASSUMPTION 0.1% by analogy with the Piercing stop [p. 295].
- Cash market: exit signal only.

### 2.10 Bullish Harami

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bullish reversal, two-day signal plus confirmation | 194, 196 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite downtrend; day 1 black body, day 2 white body completely engulfed by the black body (tails need not be engulfed; open equal to previous close acceptable). Enhancers: longer candles, heavy volume on either day, stochastics oversold, white closes higher into the black body, second Harami at the same support level, gap up next day. Day 2 may be Hammer/Inverted Hammer/Doji. A Harami with stochastics still falling and a gap down the next day should not be bought. | 196, 198, 200, 206, 210, 212, 216 |
| Entry trigger & order type | Wait for confirmation the next day (gap-up or higher close); buy as soon as prices open higher the next day after the second Harami. Entering without confirmation avoided. | 194, 195, 207, 210, 216 |
| Initial stop-loss | Just below the bottom of the bullish candle. In examples: exit as soon as the bears push price below the open of the white Harami candle, or when the stock breached and closed lower than the open of the Harami day / closed below the bottom of the Harami. | 297, 309, 313, 315 |
| Exits: profit-taking | No fixed target. Target is only a guide (previous high/resistance, trend line, Fibonacci level, major MA); take profit when a confirmed opposite (sell) candlestick signal appears even before target is reached. Reward-risk of at least 2 (author prefers 3+) required before entry. | 325, 326, 346, 347 |
| Exits: trailing / time / signal | Signal exit: sell when bears take control (confirmed bearish signal, e.g. lower close after bearish pattern; gap down after a bearish pattern is strong evidence). Unconfirmed bearish signals are ignored. Being overbought alone is not a sell reason. No time stop given. Exit before earnings released. | 235, 334, 335, 342, 347 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Harami test | day-2 white body inside day-1 black body | shadows may poke out; equality of open and prior close accepted | 196, 198, 212 |
| Stop level | below open/bottom of the white Harami candle | close basis (p. 313, 315) vs intraday (p. 309) | 297, 309, 313, 315 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "the body should be completely engulfed" [p. 198]
- "It is not necessary for the tails of the smaller candle to be engulfed by the previous candle." [p. 196]
- "the logical point to set the stop loss is just below the bottom of the bullish candle" [p. 297]
- "Because there was no confirmation buying the day after the signal was formed." [p. 210]
- "sold out as soon as the stock breached and closed lower than the open of the Harami" [p. 313]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
if is_downtrend(t0-1) and dark(t0-1) and white(t0) and O[t0]>=C[t0-1] and C[t0]<=O[t0-1]:
    # day-2 body inside day-1 body
    if bull_confirm(t0)   # prefer O[t0+1]>C[t0]: ENTER_LONG at open(t0+2)
    stop = O[t0]*(1-0.001) ; exit if close < O[t0]   # close-basis variant
    # failed trade may be re-entered on the next valid buy signal (p.310)
```

**Ambiguities & assumptions**

- Stop timing contradiction: intraday ('as soon as the bears drove the prices below the open', p. 309) vs closing basis ('breached and closed lower', p. 313; 'closed below the bottom of the Harami', p. 315). ASSUMPTION: close-basis (fewer whipsaws); test both.
- 'Bottom of the bullish candle' [p. 297] vs 'open of the white Harami candle' [p. 309]: ASSUMPTION: min(O,C) of day 2.
- Harami criterion text calls for 'completely engulfed' body but allows equality at the open [p. 212]; ASSUMPTION: >= / <= comparisons.

### 2.11 Bearish Harami

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bearish reversal, two-day signal plus confirmation | 194, 201 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite uptrend; day 1 white body, day 2 black body completely engulfed by the white body (tails need not be engulfed). Enhancers: longer candles, heavy volume on either day, stochastics overbought, black closes deep into the white body; day 2 may be a Hanging Man, Shooting Star or Doji. Colour order matters: a pattern with the wrong colours is not a Bearish Harami. | 201, 203, 205, 206, 234 |
| Entry trigger & order type | Sell after the Bearish Harami is confirmed; ABB example sold as soon as confirmed. A gap down after the Harami is strong confirmation (Tata Steel). | 194, 218, 235 |
| Initial stop-loss | Open of the dark candle is resistance; place a stop just above this level (bulls in control if price trades above). | 306 |
| Exits: profit-taking | Target is a guide only (previous low, trend line, Fibonacci level, major MA); cover when a confirmed bullish (buy) signal appears, e.g. Morning Star at old resistance-turned-support. Reward-risk of at least 2 (author prefers 3+). | 326, 346, 347, 370 |
| Exits: trailing / time / signal | Signal exit: cover when a confirmed buy signal appears or price breaks the stop level; no time stop given. Exit before earnings released. | 334, 335, 347, 370 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Harami test | day-2 black body inside day-1 white body | - | 203 |
| Stop buffer | 'just above' open of dark candle | no number | 306 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "the open of the dark candle is resistance. It is recommended to place a stop just above this level." [p. 306]
- "The correct point would have been to sell as soon as the Bearish Harami got confirmed." [p. 218]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
if is_uptrend(t0-1) and white(t0-1) and dark(t0) and body inside body and bear_confirm(t0):
    if holding: EXIT_LONG at open(t0+2)    # gap down next day = strong confirmation
    else (shorting allowed): SHORT ; stop = O[t0]*1.001
```

**Ambiguities & assumptions**

- ASSUMPTION: bearish exit trigger = lower close on the confirmation day; gap down (open below day-0 low) treated as stronger.

### 2.12 Morning Star (bullish, incl. Abandoned Baby)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bullish reversal, three-day signal | 219, 220 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite downtrend; day 1 long dark body; day 2 indecision (Doji/spinning top/small body, may gap); day 3 long white candle closing at least half way into day 1's dark body (a third day not reaching halfway is not a Morning Star). Abandoned Baby variant: gap below day 1 low and gap above day 2 high for day 3. Enhancers: long first body, volume spike on indecision day, stochastics oversold, middle day is itself a one-day reversal signal (Hammer), gap up after indecision day. | 222, 224, 225, 226, 228, 229, 230, 387, 388 |
| Entry trigger & order type | Pattern includes its own bullish third day; the general rule is to act on confirmation. For weekly charts, buy in the week after the Morning Star week. Order type not stated. | 340, 341, 360 |
| Initial stop-loss | Exit if price trades below the low of the signal formation (bulls then no longer in control); the book says the signal rarely fails. | 298, 299 |
| Exits: profit-taking | No fixed target. Target is only a guide (previous high/resistance, trend line, Fibonacci level, major MA); take profit when a confirmed opposite (sell) candlestick signal appears even before target is reached. Reward-risk of at least 2 (author prefers 3+) required before entry. | 325, 326, 346, 347 |
| Exits: trailing / time / signal | Tata Steel example: ignore unconfirmed Dark Cloud signals, ignore a mis-coloured 'Bearish Harami', exit when a Bearish Harami in overbought conditions is followed by a gap down. | 234, 235 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Day-3 penetration | close at least half way into day-1 body | deeper is better | 222, 228 |
| Middle day | 'day of indecision' | Doji or small body | 222, 231 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "The third day should be a long white candle reaching at least half" [p. 222]
- "There is a gap between the low of the first day and the high of the second day." [p. 225]
- "As long as the price does not trade below the low of the signal formation, the bulls are still in control." [p. 298]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
long_dark(t)=dark(t) and body>=1.5*avg_body(20) [ASSUMPTION]; indecision(t)= body<=0.3*avg_body or doji
if is_downtrend(t0-2) and long_dark(t0-2) and indecision(t0-1) and white(t0) and long_white(t0) and C[t0]>=(O[t0-2]+C[t0-2])/2:
    ENTER_LONG at open(t0+1) (pattern completes on t0; book's strict confirmation rule suggests t0+1 bull_confirm, entry t0+2)
    stop = min(L[t0-2],L[t0-1],L[t0])*(1-0.001)
```

**Ambiguities & assumptions**

- Whether to wait for next-day confirmation after the third day is not stated explicitly for the Morning Star; general rule 'buy only on confirmation' [p. 340, 341]. ASSUMPTION: enter at the open after day 3 (default) and test the extra confirmation day variant.
- 'Long' bodies and 'indecision' are not quantified. ASSUMPTION: long body >= 1.5 x 20-day average body; indecision body <= 30% of average body.
- Stop: 'low of the signal formation' [p. 298]; ASSUMPTION: lowest low of the three days minus 0.1%.

### 2.13 Evening Star (bearish)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick bearish reversal, three-day signal | 219, 236 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | 'Trade only in the direction of the trend' (up-trending stock: take buy signals and sell on sell signals, do not short; down-trending stock: short on sell signals, buy back on buy signals, do not buy long). Index sell signal adds weight to stock sell signals. Conflicts with the reversal premise: see Ambiguities. | 163, 344, 345 |
| Setup conditions | Definite uptrend; day 1 long white body; day 2 indecision; day 3 long dark candle reaching down at least half way into day 1's white body. Abandoned-baby style gaps add weight. Enhancers: very long first white body, volume spike on indecision day, stochastics overbought, middle day is a one-day reversal signal (Bearish Harami/Hanging Man/Shooting Star inside it). | 238, 239, 240, 241, 242, 397, 398 |
| Entry trigger & order type | Traders should cash out longs or go short; long-term traders short as soon as the signal is confirmed. Signals clustered near an unconfirmed Hanging Man or Shooting Star raise confidence. | 240, 243, 244, 361 |
| Initial stop-loss | The high of the Evening Star is the resistance; stop just above this point. | 307 |
| Exits: profit-taking | Target is a guide only (previous low, trend line, Fibonacci level, major MA); cover when a confirmed bullish (buy) signal appears, e.g. Morning Star at old resistance-turned-support. Reward-risk of at least 2 (author prefers 3+). | 326, 346, 347, 370 |
| Exits: trailing / time / signal | Signal exit: cover when a confirmed buy signal appears or price breaks the stop level; no time stop given. Exit before earnings released. | 334, 335, 347, 370 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Day-3 penetration | close at least half way into day-1 body | - | 238 |
| Stop buffer | 'just above' the high | no number | 307 |
| Definition of 'definite' prior trend | not defined numerically; judged visually | see Ambiguities | 92 |
| Confirmation | next candle continues in signal direction (higher close for buys, lower close for sells) | gap in signal direction is stronger | 93, 105, 122, 235 |
| Stochastics %K period N | 12 (author's usual) | 14 used by some; 5 for rapid signals; pick by trial and error against past reversals | 65, 66 |
| %K smoothing | 3 days | other numbers may be tried; %D smoothing length not stated | 66, 67 |
| Oversold / overbought levels | <20 oversold, >80 overbought | indicator is secondary to the candle signal; RSI/MACD acceptable | 65, 67, 250 |
| Minimum reward-risk | at least 2 | author personally likes 3 or higher | 326 |
| Capital per trade | 10% of capital (Rs 1 lakh of Rs 10 lakh) | an example; reader decides | 351, 352 |

**Key quotes**

- "The third day should be a long dark candle reaching down at least half way" [p. 238]
- "Traders should immediately cash out their positions, or go short." [p. 240]
- "Placing a stop loss just above this point would allow the candlestick trader to get out with only a small loss." [p. 307]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
if is_uptrend(t0-2) and long_white(t0-2) and indecision(t0-1) and long_dark(t0) and C[t0]<=(O[t0-2]+C[t0-2])/2:
    if holding: EXIT_LONG at open(t0+1)
    else (shorting allowed): SHORT at open(t0+1); stop = max(H[t0-2..t0])*1.001
```

**Ambiguities & assumptions**

- As with the Morning Star, extra confirmation day is not explicit; see 2.12 assumption.
- Cash market: exit signal for longs only.

### 2.14 Weekly-chart (longer term) version

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Same candlestick reversal signals applied to weekly (or monthly) candles for longer-term investing | 355, 357 |
| Timeframe & holding period | Weekly (or monthly) candles; positions for weeks or months (Bank of India example: at least 2 months). Monitor charts at least once a week. | 356, 358, 360, 373 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | Same support/resistance logic: a bullish weekly signal directly under a downtrend resistance line is not a good buy; wait for the breakout. Index (Nifty) weekly signals used as well. | 362, 363, 369, 370 |
| Setup conditions | Any of the signals in 2.1-2.13 on weekly candles; weekly candle open = first trading day open, close = last trading day close, high/low = extremes of the week. Example: Morning Star with oversold stochastics (Bank of India), Evening Star short (Syndicate Bank), Bearish Harami confirmed with close below up-trend support line and volume surge (MTNL). | 357, 358, 359, 360, 361, 371, 372 |
| Entry trigger & order type | Enter in the week after the signal week once confirmed (e.g. perfect time to buy is the week after the Morning Star week). A Bearish Engulfing that was not confirmed was not shorted; short the confirmed Bearish Harami. | 360, 364, 365, 366 |
| Initial stop-loss | Same pattern-specific stops as Section 2.2-2.13, evaluated on weekly candles; a failed signal only shows at the end of the week and thus costs more. | 358, 289, 297 |
| Exits: profit-taking | Confirmed opposite weekly signal (Evening Star confirmation = get out); for shorts a Morning Star at old resistance-turned-support prompts profit-taking. | 369, 370 |
| Exits: trailing / time / signal | Exit a short after a string of Doji is confirmed with a bullish candle (MTNL). | 372, 373 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Candle timeframe | weekly | monthly also; daily default; even 15-minute noted as same psychology | 357, 368 |
| Monitoring frequency | at least weekly | - | 356, 373 |
| Stochastics settings | not restated for weekly | - | 66 |

**Key quotes**

- "candlestick signals work just the same way on a weekly chart or on a monthly chart" [p. 357]
- "if a signal faults out, you will not know of it until the end of the week when the candle closes" [p. 358]
- "The perfect time to buy would have been in the week after the week of the Morning Star signal." [p. 360]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
resample daily bars to weekly: O=first open, H=max high, L=min low, C=last close, V=sum
run pattern scans 2.1-2.13 on weekly bars; confirmation = next weekly bar; entry = open of following week
stop checked on weekly closes (or weekly low) using the same pattern-specific level
```

**Ambiguities & assumptions**

- Stochastic period and trend definitions on weekly bars not restated. ASSUMPTION: N=12 weekly bars, 3-bar smoothing.
- Whether the weekly stop is checked intraday or on the weekly close is not stated. ASSUMPTION: weekly close (the book says a failed signal is only known at week's end, p. 358).
- No performance data for weekly vs daily beyond the claim 'Your gains will be much higher' [p. 358].

### 2.15 Context filters: engulfing exceptions, support/resistance, moving averages, reward-risk

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Context filters/overlays on the signals: engulfing exceptions in extreme zones, support/resistance trend lines, moving-average support, reward-risk filter | 163, 164, 167, 251 |
| Timeframe & holding period | Daily candles (book's default); signal day plus confirmation day; swing hold of a few days to a few weeks. Same rules work on weekly/monthly candles (see 2.14). | 66, 357 |
| Universe / eligibility filters | Liquid, high-volume stocks only; skip low-volume stocks and charts that are hard to read or have no history of clean past signals. Stocks and indices both allowed. Avoid holding through earnings or other binary news. | 163, 331, 332, 333, 334, 335 |
| Market / regime filter | A trendline broken on a closing basis flips role (support becomes resistance and vice versa). A tall white candle breaching resistance negates a short expectation. A trending stock may never get oversold, so signals are valid outside extreme stochastics. | 258, 259, 267, 180, 343 |
| Setup conditions | (a) Exception: a bullish engulfing in an overbought condition has bearish implications (last-gasp buying); a bearish engulfing in an oversold condition is bullish. (b) Candle signal forming on a horizontal/sloping trendline or on the 20/30/50-day SMA (stock bounces) raises probability; two signals at the same level add more weight. (c) Target = old support/resistance line extension, MA, previous high or low, Fibonacci level; trade only if reward-risk >= 2 (3 preferred). | 164, 167, 262, 263, 272, 273, 275, 278, 279, 322, 325, 326, 346 |
| Entry trigger & order type | Same confirmation-based entry as the underlying pattern; in HPCL the trade should have waited until new resistance was breached to the upside because reward-risk did not warrant it. | 320, 321, 322 |
| Initial stop-loss | Pattern-specific stop (2.2-2.13); trendline/MA break on a close is a further failure sign. | 258, 285, 288 |
| Exits: profit-taking | At the target (trendline, MA, previous high) if signals agree; otherwise on a confirmed opposite signal; targets are only targets. | 272, 346, 347 |
| Exits: trailing / time / signal | Candlestick sell signal overrides target; being overbought alone is not a reason to sell; in a strong trend the trader may hold until the up-trending channel breaks (personal choice). | 342, 343, 347 |
| Position sizing | Equal capital per trade: capital divided into 10 parts (Rs 1 lakh each on Rs 10 lakh); shares = allocation / price. Do not size up for a 'perfect' signal; treat every trade as the same probability. | 352, 353 |
| Adding to / pyramiding | Not found in this book as a method. Averaging down / adding to a losing trade is rejected explicitly. | 329, 330 |
| Portfolio limits (max positions, correlation, heat) | Example: 10 positions of 10% each (10 different stocks with signals). Book calls this an example only, not a rule; no correlation or heat limit given. | 351, 352 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| SMA lengths | 20 or 30 for trading; 50 / 200 used by money managers; 50 and 20 in examples | choose the MA from which the stock bounces most | 271, 272, 273 |
| Minimum reward-risk | 2 | 3 or higher preferred by author | 326 |
| Trend-line break | closing basis | - | 258 |
| Trend-line touches | more tests = stronger | no number | 258 |

**Key quotes**

- "Once a support trend line is broken, not intraday, but on a closing basis" [p. 258]
- "If a bullish engulfing signal occurs when the stock is in an overbought condition, then the signal has bearish implications." [p. 164]
- "Traders normally like to have at least a reward-risk ratio of 2, or higher." [p. 326]
- "Pull up a chart and put various moving averages on it." [p. 271]

**Pseudocode**

```
# helpers (data: daily O,H,L,C,V per stock)
# body=abs(C-O); rng=H-L; up_sh=H-max(O,C); lo_sh=min(O,C)-L; white=C>O; dark=C<O
# is_downtrend(t) [ASSUMPTION]: C[t]<SMA(C,20)[t] and SMA(C,20)[t]<SMA(C,20)[t-5] and C[t]/C[t-10]-1<=-0.05
# is_uptrend(t)   [ASSUMPTION]: mirror image
# K(t)=SMA(3)( 100*(C-LL12)/(HH12-LL12) ); OS: K<20 ; OB: K>80
# bull_confirm(t0): white(t0+1) and C[t0+1]>C[t0]      (optional strong form: O[t0+1]>C[t0], gap up)
# bear_confirm(t0): dark(t0+1)  and C[t0+1]<C[t0]      (optional strict form: C[t0+1]<L[t0])
rr = (target - entry) / (entry - stop)       # target = nearest prior swing high (or MA/trendline) above entry
take_trade only if rr >= 2
location_bonus = candle signal low within 1% of SMA(C,20|50) or within 1% of prior swing low/high [ASSUMPTION]
exception: bullish_engulfing and K>80 -> treat as bearish signal (needs next-day lower close); bearish_engulfing and K<20 -> bullish
```

**Ambiguities & assumptions**

- Trendlines are 'subjective'; 'whichever trend line the signal is formed at is the correct trend line' [p. 262, 263]. ASSUMPTION: algorithmic swing highs/lows within 1% as support/resistance zones.
- Which MA to use is empirical per stock [p. 271, 272]; ASSUMPTION: test fixed 20 and 50 SMA across the universe.
- No numeric definition of target; ASSUMPTION: nearest prior swing high (10-day fractal) above entry for longs.

### 2.16 Pattern definitions with no trade rules (non-codable as stand-alone strategies)

- Candle anatomy: White/Black/Opening/Closing Marubozu, Doji [p. 45, 47, 49, 51, 53]; each candle independent of the previous close [p. 54, 55]. The names are said to be irrelevant, the analysis matters [p. 44, 76, 77].
- Spinning Top = Doji with a small body [p. 76]; used as indecision candle in Morning/Evening Star [p. 231].
- Abandoned Baby (Morning/Evening Star with gaps on both sides) described as a very powerful signal [p. 225, 240]. No separate stop or entry given beyond the star rules.
- Bullish Kicker: day 1 long black body; day 2 long white candle opening above the previous day's open; ideal kicker has a gap between the two candles [p. 388, 389]. Bearish Kicker: mirror image, day 2 long dark candle opening below the previous open [p. 398, 399]. These appear only in the appendix: no trend condition, confirmation, stop or exit given. Not found in this book beyond the definitions.
- Multi-signal clusters add confidence (e.g. Hammer, Inverted Hammer, Doji, gap up in Tata Power) [p. 126, 127, 278, 279]; no scoring system is given.

## 3. Risk & money-management rules

| Rule | Detail | Page |
|---|---|---|
| Stop-loss comes from the signal | The stop is the point at which the candlestick signal is negated, not an arbitrary percent (2%, 5%, 7%, 10% rejected as 'not meaning much'). | 284, 285, 286, 288 |
| Pattern stops | Hammer: below its low; Inverted Hammer: below body bottom; Bullish Engulfing: bottom of bullish candle; Piercing: ~0.1% below bottom of bullish candle; Bullish Harami: just below bottom of bullish candle; Morning Star: below the signal's low; Hanging Man: above the body/top; Shooting Star: above the high; Bearish Engulfing: close above the dark body; Dark Cloud/Bearish Harami: just above the dark candle's open; Evening Star: just above the high. | 289, 291, 293, 295, 297, 298, 300, 301, 303, 304, 306, 307 |
| Cut losses short, let profits run | Take the small loss, wait for the next signal; may re-enter on another valid signal. | 284, 310, 311 |
| Never turn a losing trade into an investment | No holding past the stop, no averaging down, no hope-based break-even exit. | 328, 329, 330 |
| Reward-risk filter | Calculate entry, stop and target before every trade; at least 2, author prefers 3+; 'lose Rs 10 for a gain of Rs 15' is not worth it. | 325, 326 |
| Position size | Divide capital into 10 equal parts (Rs 1 lakh each of Rs 10 lakh) and take ten trades; shares = allocation / price; do not enlarge a 'perfect' trade. | 351, 352, 353 |
| Diversification | Never put all capital in one company. | 351 |
| Event risk | Do not hold a position through earnings, drug approvals, contracts, takeover news; exit before the release. | 334, 335 |
| Liquidity | Avoid low-volume stocks. | 331 |
| Daily review | Check every open position daily to see whether price action follows the expected path. | 308 |
| Practice/size | Start with a small real position, grow size with profits; paper trade 5-10 extra trades alongside real ones. | 375, 376 |
| Both sides | Learn long and short; risk of shorting equals long with proper stops. | 377, 378 |
| No drawdown or portfolio-heat rule | Not found in this book. | n/a |

## 4. Non-codable guidance

- Trading is mostly psychology (85-95%); fear and greed drive supply and demand; you cannot master them, you follow a system [p. 32, 36].
- Visual recognition and judging a 'definite' trend by eye; the author wants charts analysed within a minute and wants signals recognised instantly [p. 61, 92, 375].
- Imagine what smart money and novice traders are doing behind each candle ('trade fear and greed, not stocks') [p. 100, 258].
- Trendlines are subjective; the market decides which line is right [p. 262, 263].
- Skip charts that are hard to read; choose only clean charts with good past signals [p. 332, 333, 375].
- Do not buy exact bottoms or sell exact tops; capture the middle chunk [p. 218, 280, 340].
- Do not be trigger-shy; do not make excuses; trade confidently [p. 337, 338, 339].
- Keep charts simple: avoid analysis paralysis; one oscillator, a couple of MAs and trend lines [p. 348, 349, 350].
- Do not fret if price climbs after you sold on a signal [p. 347].
- Targets are only targets; the signal over-rides [p. 347].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily Open, High, Low, Close, Volume (adjusted) per stock; weekly bars resampled from daily. Optional: NIFTYBEES (or equal-weight index) for index-level signals; delivery % is not used by the book. No fundamentals needed (author says price discounts fundamentals and tells traders to avoid earnings days) [p. 38, 334]. Earnings/news calendar needed for the pre-earnings exit rule: not available in our data.
- **Testability with our data:** All patterns (2.1-2.14), stochastics, volume spike, SMA and swing-based support/resistance are fully backtestable on 2005-2026 daily OHLCV including delisted stocks. Index-level signals are testable via NIFTYBEES or a stock-panel equal-weight index (Nifty history only from 2024). The earnings-avoidance rule cannot be tested (no results calendar). Short trades cannot be tested as real NSE cash trades but the bearish signals can be backtested as hypothetical shorts or as exits for longs. Subjective items (trendlines by eye, 'definite trend', 'clean chart') need algorithmic proxies.
- **Market-structure differences:** The book is written for Indian traders and every chart is NSE/BSE, mostly 2005-2007, a strong bull market; one chart is the Nifty [p. 29, 162]. Concrete adaptations (all ASSUMPTION):
  - ASSUMPTION: No overnight shorting in the cash market, so bearish patterns (2.3, 2.5, 2.7, 2.9, 2.11, 2.13) are used as exits from longs (book allows this: 'sell their existing position', p. 108) and as data points for a hypothetical short-side study.
  - ASSUMPTION: Entry at next open after the confirmation candle; account for circuit limits (a gap to the upper/lower circuit may make entry or stop impossible) and skip trades if the open is at the circuit.
  - ASSUMPTION: Costs: STT, brokerage, and 0.1% slippage each way; the 0.1% stop buffer in the book is comparable to slippage, so stops may need a wider buffer.
  - ASSUMPTION: Liquidity filter for 'avoid low-volume stocks' [p. 331]: median 20-day traded value above Rs 1 crore (stricter for small caps).
  - ASSUMPTION: Position size 10% of capital per trade, max 10 positions as the book's example [p. 352].
  - ASSUMPTION: Pre-earnings exit cannot be coded; skip or approximate by avoiding quarter-result months for a stock if a calendar is ever available.

## 6. Verdict

- **Codeability:** Partly. Candle geometry, stochastics, volume spikes, confirmation, pattern-specific stops and equal-weight sizing are mechanical, but 'definite trend', trendlines, 'long' bodies, 'indecision', the earnings filter and the reward-risk target are discretionary and need assumed proxies.
- **Priority for backtesting:** Medium. The book supplies no statistics, so the claim of high probability needs testing, and the NSE data (3,700 stocks, 2005-2026) is ideal; however patterns are numerous, long-only, and the edge of raw candle patterns is likely small without the context filters.
- **Top 3 things a coder is most likely to get wrong:**
  1. Entering on the signal day instead of waiting for the next-day confirmation (and dropping the confirmation rule when the bearish patterns are used as exits).
  2. Candle-geometry details: Piercing and Dark Cloud need the open beyond the prior day's range, Engulfing/Harami compare bodies (not shadows), Harami allows an open equal to the prior close, and a Morning/Evening Star day-3 must pass the halfway point of day 1.
  3. Treating overbought/oversold stochastics as mandatory, and using a fixed percentage stop instead of the pattern-specific negation level (and mixing intraday vs close-basis stop rules).
