# Indian intraday material (bundle) — Stock Trader; Yuvraj Kumar (pptx)

- **Source file:** Google Drive bundle "Indian intraday material": (a) "Intraday Trading Strategy - Learn An Advance Intraday Trading Strategy In Banknifty Futures.pdf" (author "Stock Trader", 2021, 151 KB; Drive plain-text rendering); (b) "BANK NIFTY  STRATEGY (3).pptx" (12 slides, TradingView screenshots by Yuvraj_Kumar, Dec 2021, Hinglish text). NOT included: "25 DAY TRADING STRATEGIES IN NIFTY & BANK NIFTY.pdf" (7.6 MB, over the ~7 MB connector limit, blocked_size), so none of its strategies are captured here.
- **Text file used:** text/intraday_indian_misc.txt  (page basis: coordinator-split sections for the PDF, pp. 1-4; slides for the pptx, pp. 5-16, slide n = page n+4)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (not the book's printed page numbers, which are not available)
  - pp. 1-4 are NOT real PDF pages: the Drive rendering had no page breaks, so the coordinator split it into one page per section (p.1 title/copyright/intro, p.2 buy/sell/exit rules, p.3 Pine Script v5 code, p.4 performance metrics/conclusion).
  - pp. 5-16 are slides 1-12 of the pptx.
  - Verified with `python ../work/bin/verify_citations.py specs/intraday_indian_misc.md text/intraday_indian_misc.txt`.
- **Coverage:** Read lines 1-470 of text/intraday_indian_misc.txt in full, up to and including the last marker [[PAGE 16]]; nothing skimmed. The Pine Script on p.3 had been collapsed onto a few lines by the Drive rendering and the coordinator restored the line breaks only (no wording or token changed). Slides on pp. 6-16 (slides 2-12) are OCR'd TradingView screenshots; chart OCR lines (price axes, OHLC headers, times) are noise except labels such as HIGH, LOW, STICKE PRICE SELECT, SuperTrend(13,3), VWAP, "109 POINTS MOVEMENT TILL NOW". Page 5 (slide 1) has no text. The oversized PDF "25 DAY TRADING STRATEGIES IN NIFTY & BANK NIFTY.pdf" (7.6 MB) was excluded (blocked_size) and is NOT covered. *Coordinator check: pp.1-4 are the BankNifty-futures PDF from Drive's plain-text rendering, split by section. Pine Script line breaks were restored by the coordinator and no tokens were changed. pp.5-16 are the pptx slides: slide text comes from the slide XML, and the 9 embedded screenshots were OCR'd with RapidOCR. Correction: p.6 (slide 2) and p.9 (slide 5) carry real slide text; p.9 has no image and was not OCR'd, and p.6 has slide text plus an OCR'd screenshot. The coordinator re-ran verify_citations (22/22 ok) and an exact-page strict check (0 off-by-one), and confirmed both field tables have exactly the 12 template rows. Spot-checked by grep: net profit 31.48%, PF 1.69 and DD 6.29 p.4; sessions 0915-1430 / 1445-1500 and crossover(RSI,55) p.3; SuperTrend 13,3 and SL 30-60 p.9; 9:45 p.6; all matched.*

## 1. The method in brief

The bundle holds two unrelated intraday systems for Bank Nifty, both needing intraday data. (1) "Stock Trader" gives a fully specified intraday BankNifty futures system: go long when price closes above VWAP, ADX is below 30 and RSI crosses above 55; go short when price closes below VWAP, ADX is below 30 and RSI crosses below 35; exit on a close back across VWAP or at the afternoon square-off; entries only 09:15-14:30 [p. 2]. A complete Pine Script v5 implementation is given (15-min timeframe input, ADX length 20, DI length 10, RSI 14, VWAP of (high+low)/2) [p. 3]. The author reports a one-year backtest (2020-2021), 0.03% commission and slippage, net profit 31.48%, 105 closed trades, profit factor 1.69, max drawdown 6.29 [p. 4]. The book is explicitly educational and offers no guarantee [p. 1].

(2) The pptx (Yuvraj_Kumar, TradingView screenshots dated Dec 7, 2021 [p. 6]) shows a discretionary options-buying routine on Bank Nifty: mark the high and low of the current-month futures between 9:15 and 9:45, select an ITM strike, switch to the option's 3-minute chart with SuperTrend(13,3) and VWAP, and buy on a SuperTrend or VWAP breakout after 10:00 with a 30-60 point stop [p. 6, 9]. Screenshots of 3 Dec and 6 Dec 2021 trades are shown, one annotated "109 POINTS MOVEMENT TILL NOW" [p. 14]. No statistics are given for this setup.

## 2. Strategies

### 2.1 BankNifty futures VWAP + ADX + RSI-cross intraday system (Stock Trader)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday momentum / RSI-threshold-cross entry filtered by VWAP side and low-ADX regime; long and short; all positions flat by the afternoon square-off | 2, 3 |
| Timeframe & holding period | Prose gives no bar size. Code: `timeframe` input default '15' (15-min), used for the session test. Intraday only; positions squared off "after the 3.00" in prose; in code the square-off session is 14:45-15:00 | 2, 3 |
| Universe / eligibility filters | BankNifty futures (title). No liquidity or contract-roll filter stated | 1 |
| Market / regime filter | ADX below 30 (code: ADX smoothing length 20, DI length 10, level 30) on both buy and sell | 2, 3 |
| Setup conditions | Buy: close above VWAP and ADX below 30. Sell: close below VWAP and ADX below 30. VWAP = VWAP of (high+low)/2 | 2, 3 |
| Entry trigger & order type | Buy when RSI(14) crosses and closes above 55; sell when RSI(14) crosses and closes below 35; only between 09:15 and 14:30. Code uses `strategy.entry` (market order) when `buy`/`sell` is true; no limit or stop orders | 2, 3 |
| Initial stop-loss | - | - |
| Exits: profit-taking | - | - |
| Exits: trailing / time / signal | Buy exit: close below VWAP or the 3 pm square-off. Sell exit: close above VWAP or the 3 pm square-off. No trailing stop | 2, 3 |
| Position sizing | Code input `quantity` default 1 (min 1, max 500); backtest initial capital 300000. No risk-based sizing | 3, 4 |
| Adding to / pyramiding | No adding stated. Code allows one entry per direction (islong/isshort flags suppress repeat signals) | 3 |
| Portfolio limits (max positions, correlation, heat) | Single instrument. Code holds at most one position, long or short (a new opposite signal reverses via `strategy.entry`) | 3 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Bar timeframe | 15 (minutes), `timeframe` input | input.timeframe; no alternatives suggested | 3 |
| VWAP source | (high + low) / 2 | - | 3 |
| ADX length (`LengthADX`) | 20 | input range 1-100 | 3 |
| DI length (`DIlength`) | 10 | input range 1-100 | 3 |
| ADX level (`ADXLEVEL`) | 30 (entry only when ADX < 30) | input range 1-100 | 2, 3 |
| RSI length | 14 | input range 1-100 | 3 |
| RSI buy threshold | 55 (cross above) | - | 2, 3 |
| RSI sell threshold | 35 (cross below) | - | 2, 3 |
| Trade (entry) session | 09:15-14:30 | input.session | 2, 3 |
| Square-off session (code) | 14:45-15:00 (exit fires on the first bar of the session) | input.session | 3 |
| EOD flag-reset session (code) | 15:15-15:30 | input.session | 3 |
| Prose square-off time | "after the 3.00" | - | 2 |
| Quantity | 1 | 1-500 | 3 |
| Initial capital | 300000 | - | 3, 4 |
| Commission and slippage | 0.03% | - | 4 |
| Reported backtest | 2020-2021 (1 year); net profit 31.48%; 105 closed trades; profit factor 1.69; max drawdown 6.29 (unit not given) | - | 4 |

**Key quotes**

- "Prices should close above the VWAP." [p. 2]
- "ADX should be below the 30 level." [p. 2]
- "RSI should cross and close above the 55 level." [p. 2]
- "RSI should cross and close below the 35 level." [p. 2]
- "Prices should close below the VWAP or after the 3.00 the buy position will automatically get squared off." [p. 2]
- "I have added one more condition that the buy and sell trades should happen between 09.15 & 14.30" [p. 2]
- "VWAP = ta.vwap((high + low) / 2)" [p. 3]
- "buy = bvwap and adx < ADXLEVEL and insession and ta.crossover(RSI,55)" [p. 3]
- "sell = svwap and adx < ADXLEVEL and insession and ta.crossunder(RSI,35)" [p. 3]
- "buyexit = close < VWAP or squareoffpos" [p. 3]
- "sqsession = input.session(title='squareofftime', defval='1445-1500')" [p. 3]
- "BACKTESTING LENGTH IS OF 1 YEAR" [p. 4]

**Pseudocode** (intraday bars of size TF = 15 min; indicators on the chart timeframe)

```
inputs: TF=15m, ADXlen=20, DIlen=10, ADXlevel=30, RSIlen=14,
        buyRSI=55, sellRSI=35, entryWindow=[09:15,14:30], sqWindow=[14:45,15:00], eodWindow=[15:15,15:30]
each bar b (on bar close):
  VWAP   = vwap_of(hl2 = (high+low)/2, volume)        # session-anchored (ASSUMPTION)
  RSI    = rsi(close, 14)
  ADX    = dmi(DIlen=10, ADXsmoothing=20).adx
  inWin  = b.time in entryWindow
  sqNow  = b is the first bar inside sqWindow
  buySig  = close > VWAP and ADX < 30 and inWin and RSI[1] <= 55 and RSI > 55
  sellSig = close < VWAP and ADX < 30 and inWin and RSI[1] >= 35 and RSI < 35
  buySig  = buySig  and not islong
  sellSig = sellSig and not isshort
  if buySig:  islong=true;  isshort=false
  if sellSig: islong=false; isshort=true
  if b is first bar inside eodWindow: islong=false; isshort=false
  if buySig:  enter long qty=1 (market)      # a short open is reversed
  if sellSig: enter short qty=1 (market)     # a long open is reversed
  if long  open and (close < VWAP or sqNow): close long
  if short open and (close > VWAP or sqNow): close short
  # note: islong/isshort are NOT cleared on exit, only by an opposite signal or the EOD window
```

**Ambiguities & assumptions**

- Prose vs code on square-off: prose says exit "after the 3.00" [p. 2]; code exits on the first bar of the 14:45-15:00 session [p. 3] (on 15-min bars, the 14:45 bar), and a separate 15:15-15:30 EOD session only resets the islong/isshort flags and does not close positions [p. 3]. ASSUMPTION: flatten at the close of the 14:45 bar (code behaviour, about 15:00), since the code produced the reported results.
- Timeframe: prose never names a bar size; the code input defaults to '15' but is only used in the session test (`time(timeframe, tradetime)`), while indicators run on the chart's timeframe [p. 3]. ASSUMPTION: 15-min chart, matching the input default.
- Re-entry flags: `islong`/`isshort` are not reset on a VWAP-cross exit, only by an opposite signal or the EOD window [p. 3]. So after a long is stopped out by the VWAP re-cross, no new long can be taken until a short signal occurs or the next day's EOD reset. Prose does not mention this. ASSUMPTION: replicate the code (one entry per direction per run of same-side signals); give a variant with re-entry allowed after exit as a sensitivity test.
- Entry-window check applies to buys and sells in code but exits are unrestricted by time [p. 3].
- VWAP reset: the text does not state whether VWAP resets daily. ASSUMPTION: daily (session) anchor, as in the intraday VWAP default.
- Fill price: not stated; `strategy.entry` with no price is a market order. ASSUMPTION: fill at the next bar's open after the signal bar's close.
- Sell RSI 35 versus buy RSI 55 is asymmetric (not 45/65 mirrored); both are as stated [p. 2].
- No stop-loss and no profit target are stated (not found in this text). ASSUMPTION: none (replicate); exit via VWAP re-cross only.
- Reported max drawdown "6.29" has no unit (likely %); the net profit is 31.48% on 300000 capital with qty 1 [p. 4], so contract multiplier and lot size effects are unclear. ASSUMPTION: treat results as percent of capital with lot size unspecified.
- "ADX should below the 30 level" in the sell rule [p. 2] is a typo; read as ADX < 30 (code agrees [p. 3]).
- Backtest period is "2020 - 2021" and one year [p. 4]; exact dates and the contract roll method are not given.

### 2.2 BankNifty opening-range marking and ITM option buying on SuperTrend/VWAP breakout (pptx, Yuvraj_Kumar)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday options buying; opening-range (9:15-9:45) reference levels with a SuperTrend/VWAP breakout trigger on the option chart; discretionary | 6, 9 |
| Timeframe & holding period | Index-futures chart of 3-minute bars (chart header shows ",3,"); option chart set to 3 min; orders only from 10:00 am; intraday (screenshots run to about 15:21) | 6, 9, 11 |
| Universe / eligibility filters | BankNifty current-monthly futures chart for the range; BankNifty weekly option, ITM strike selected (examples: 36100 PE and 36700 PE, 9 Dec 2021 expiry) | 6, 10, 14 |
| Market / regime filter | - | - |
| Setup conditions | On the current monthly BankNifty futures chart, mark the high and low from 9:15 to 9:45 am; select an ITM strike price; open that option's chart with SuperTrend(13,3) and VWAP | 6, 9 |
| Entry trigger & order type | Buy the option on a breakout of SuperTrend or of VWAP, executing from 10:00 am. Order type not stated | 9 |
| Initial stop-loss | 30, 40, 50 or 60 (max of that range); units not stated | 9 |
| Exits: profit-taking | - (a screenshot is annotated "109 POINTS MOVEMENT TILL NOW" as an example of profit, not a target) | 14 |
| Exits: trailing / time / signal | - | - |
| Position sizing | - | - |
| Adding to / pyramiding | - | - |
| Portfolio limits (max positions, correlation, heat) | - | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Range-marking window | 9:15 to 9:45 am on BankNifty current-month futures | - | 6 |
| Strike selection | ITM strike (screenshot labels "STICKE PRICE SELECT" at the high and low levels) | - | 6, 8 |
| Option chart timeframe | 3 min | - | 9 |
| SuperTrend | (13, 3) (period 13, multiplier 3) | - | 9, 11 |
| VWAP | on the option chart, default settings | - | 9, 11 |
| Order start time | 10:00 am | - | 9 |
| Stop-loss | 30, 40, 50, 60 (max) | range 30-60 | 9 |
| Example trades | 6 Dec 2021 BANKNIFTY 9 Dec 36100 PE; 3 Dec 2021 BANKNIFTY 9 Dec 36700 PE ("109 POINTS MOVEMENT TILL NOW") | - | 10, 11, 14 |

**Key quotes**

- "BANK NIFTY FUT CHART SELECT CURRENT MONTHLY 9:45 AM" [p. 6]
- "CHART PE 9:15 SE 9:45 AM TAK KA" [p. 6]
- "HIGH-LOW MARK KARE" [p. 6]
- "ITM - STRIKE PRICE SELECT" [p. 6]
- "Order execute to 10:00 am after" [p. 9]
- "Super trend ke breakout pe ya to vwap ke break out pe buy kar sakte hai" [p. 9]
- "30,40,50,60 max ke range me" [p. 9]
- "109POINTSMOVEMENTTILL" [p. 14]

**Pseudocode** (needs BankNifty monthly-futures 3-min bars and the option's 3-min bars with volume)

```
for each trading day:
  fut = BankNifty current-month futures, 3-min bars
  rangeHigh = max(fut.high for 09:15 <= t < 09:45)
  rangeLow  = min(fut.low  for 09:15 <= t < 09:45)
  strike = choose ITM strike from the index at/after 09:45          # rule not specified
  opt = option(strike, weekly expiry), 3-min bars
  ST = supertrend(opt, period=13, mult=3); V = vwap(opt)            # intraday-anchored
  from 10:00 on each opt bar:
    if flat and (breakout of ST or breakout of V, definition not given):
       buy opt (market, assumed)
       stop = entry - S   where S in {30,40,50,60}                  # units assumed points of premium
  exit: not specified (no target, no trail, no time exit)
```

**Ambiguities & assumptions**

- Text is Hinglish and fragmentary; slide 1 (p. 5) has no text and the numbered steps 1-4 are not present in the text, only "5." [p. 9]. Steps 1-4 are inferred from p. 6 only.
- Direction: all examples are puts (PE); the text never states how the range high/low maps to call or put purchase. The label "PE" appears near the LOW lines in the OCR of p. 8 and p. 13, suggesting a break of the range low leads to a put purchase, with the high leading to a call. ASSUMPTION: break below rangeLow -> buy ITM PE; break above rangeHigh -> buy ITM CE.
- How the 9:15-9:45 high/low is used (as a trigger, a filter, or only for choosing strike) is not stated. ASSUMPTION: use as direction filter only (an option buy is allowed in the direction of the first futures break of the range after 9:45).
- ITM definition (how many strikes in the money, which strike relative to the 9:45 spot) is not stated; the example strikes (36100 PE with a 9:15-9:45 range of about 36231-36489 on 6 Dec; 36700 PE with a range of about 36630-36968 on 3 Dec) cannot be reconciled with a single rule from the OCR. ASSUMPTION: first strike in the money at 09:45 spot.
- "Breakout" of SuperTrend or VWAP is undefined (close above VWAP? flip of SuperTrend to bullish on the option chart?). ASSUMPTION: either a SuperTrend(13,3) flip to up-trend on the option chart, or a close crossing above option VWAP, whichever occurs first from 10:00.
- "Order execute to 10:00 am after" [p. 9] is read as orders from 10:00 am onward.
- Stop-loss units (premium points) and choice among 30/40/50/60 are not stated. ASSUMPTION: 40 points of option premium.
- Exit rules, profit targets, position sizing, number of trades per day, and weekly expiry choice: not found in this text. ASSUMPTION: exit at SuperTrend flip back down or 15:15 square-off.
- No performance statistics; only two screenshots (3 Dec and 6 Dec 2021) are shown, one with "109 POINTS" move [p. 14].

## 3. Risk & money-management rules

- Backtest assumptions: initial capital 300000, quantity 1, commission and slippage 0.03% [p. 3, 4].
- No stop-loss or position-sizing rule in system 2.1; risk control is the VWAP re-cross exit and the intraday square-off [p. 2].
- System 2.2: stop-loss of 30, 40, 50 or 60 (max) [p. 9].
- The author states risk is high and that past performance is no guide [p. 1].
- No account-level drawdown, daily loss or maximum exposure rules are stated (not found in this text).

## 4. Non-codable guidance

- The author's aim is for traders to build their own strategies; the book gives rules only, not market basics [p. 1, 4].
- "Execution techniques will differ from trader to trader" [p. 1].
- In 2.2, choice of stop distance within 30-60, of ITM strike and of which breakout (SuperTrend vs VWAP) is left to the trader's judgment [p. 6, 9].

## 5. Adapting to NSE (Indian equities)

- **Data required:** For 2.1: BankNifty futures 15-min OHLCV (volume needed for VWAP), continuous contract with roll rules; ADX/DI/RSI computed on the 15-min bars. For 2.2: BankNifty current-month futures 3-min OHLC (09:15-09:45 range) plus 3-min OHLCV for individual weekly option strikes (CE/PE), option chain for ITM selection.
- **Testability with our data:** We have daily NSE equity OHLCV only (2005-2026, adjusted), delivery % in recent years, and Nifty index only from 2024 (NIFTYBEES earlier). Neither system can be backtested: both need intraday (15-min / 3-min) bars and index-futures / options data, which we do not have. Neither relies on fundamentals.
- **Proxy:** 2.2 has no meaningful daily-bar proxy (the 9:15-9:45 range, option premiums, SuperTrend on the option chart and 30-60 point stops are all intra-session and option-specific). For 2.1 no daily proxy is faithful, because VWAP, 15-min RSI crossings and the 3 pm square-off are intraday concepts. ASSUMPTION (optional, low value, not the author's system): a daily-bar analogue on NIFTYBEES or liquid stocks, long-only, with a rolling 20-day volume-weighted (high+low)/2 as "VWAP", ADX(DI 10, smoothing 20) < 30, RSI(14) crossing above 55 to enter and a close below the rolling VWAP to exit. This would only test indicator plumbing and should not be read as validating the book's results.
- **Market-structure differences:** The cash market has no overnight shorting, so the short side of 2.1 is only possible via futures/options (intraday short selling of cash stocks is allowed but would need intraday data). Futures/options costs (STT on options sell-side premium, brokerage, exchange charges) and about 0.1% slippage are higher than the author's 0.03% [p. 4]. Option-premium slippage and bid-ask spreads on ITM strikes matter for 2.2. Circuit limits apply to stocks and not to BankNifty index futures in the same way. The 2021 backtest is a single trending year and Bank Nifty contract and expiry rules have changed since.

## 6. Verdict

- **Codeability:** 2.1 Fully (every rule and the Pine code are given, with minor prose-versus-code differences); 2.2 Partly (hinglish, entry breakout, ITM, direction and exits are undefined). Neither is testable on our data.
- **Priority for backtesting:** Low. Both need intraday futures/options data we do not have, the 2.1 evidence is a one-year backtest of 105 trades, and 2.2 has no statistics.
- **Top 3 things a coder is most likely to get wrong:**
  1. Replicating the Pine state flags: `islong`/`isshort` persist after a VWAP exit, blocking same-side re-entry until an opposite signal or the EOD reset [p. 3].
  2. Square-off timing and session windows: code exits on the first bar of 14:45-15:00 (not 3:00 sharp), entries stop at 14:30, and the 15:15-15:30 EOD window only resets flags [p. 2, 3].
  3. Treating the RSI conditions as levels rather than crossings (RSI must cross 55 or 35 on that bar), and using a non-session-anchored or close-based VWAP instead of VWAP of (high+low)/2 with ADX computed as dmi(DI 10, ADX smoothing 20) [p. 3].
