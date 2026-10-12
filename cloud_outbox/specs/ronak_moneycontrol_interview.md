# Interview with Ronak (Moneycontrol trader-interview Q&A) — Ronak (first name from file name only; surname not stated)

- **Source file:** Google Drive invest/Interview Ronak_Moneycontrol (1).pdf (5 pages)
- **Text file used:** text/ronak_moneycontrol_interview.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - Verified with `verify_citations.py specs/ronak_moneycontrol_interview.md text/ronak_moneycontrol_interview.txt`.
- **Coverage:** Read lines 1-147 of the text file (all of it), last `[[PAGE N]]` reached = 5. Nothing was skimmed. One screenshot referenced on p. 3 ("The screenshot below indicates that there is a huge unwinding on the in-the-money call options") is NOT in the text, so its strikes, values and date are unknown. This is a short Q&A interview (8 questions), so all statistics (7:3 win ratio, 1:1.5 reward:risk, 15-20% drawdowns) are self-reported and unaudited. The text never states the interviewee's surname. Reading done by a Sonnet sub-agent. The coordinator read the whole 147-line text itself, re-ran the verifier and an exact-page check, confirmed every table citation against pp. 1-5, and re-did the p. 4 arithmetic (7 x Rs 10 - 3 x Rs 15 = Rs 25, as stated).

## 1. The method in brief

Ronak is a salaried IT professional who has traded Nifty/Bank Nifty-type index options and index futures since 2014 (after a 2013 blow-up of 50% of Rs 4 lakh in 20 days) [p. 1]. The text says "index option and future" [p. 3] but never names the indices; "Nifty/Bank Nifty" is the file-note interpretation, not a quote. His trade mix is 70% option selling, 20% option buying and 10% index futures [p. 2], and 70% of trades are intraday, the rest positional [p. 5]. He says he does not use price charts; he reads derivative data (open interest, change in open interest, futures open interest) to define three support and resistance levels for the day and then waits for market activity around them [p. 3]. Negative change in call OI is read as bullish and negative change in put OI as bearish [p. 3].

He avoids naked options: a bearish view is expressed by selling a call plus selling a put worth 40-60% of the call premium, sometimes converted into a ratio spread; bought options are always debit spreads (buy ATM, sell OTM) [p. 4]. Risk control is a pre-defined loss per trade that sets position size, plus a stop on each strike and a stop on overall profit/loss [p. 2, p. 4]. Claimed edge: 7 winners to 3 losers in option selling, reward:risk of 1:1.5, drawdowns mostly 15-20% [p. 4]. No numeric thresholds for OI, no strike-selection rule, no stop sizes and no profit targets are given anywhere in the text.

## 2. Strategies

Two separately testable setups are described. The 10% index-futures leg is mentioned only as an allocation [p. 2]; the text gives no entry, exit or sizing rules for it specifically, so it is not captured as a subsection (the OI directional reading on p. 3 is stated for "index option and future" generally and is reused in 2.1 and 2.2).

### 2.1 OI-based directional hedged option selling (about 70% of trades)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: derivative-data (OI) driven directional/contrarian short-premium trading with an offsetting short leg | 3, 4 |
| Timeframe & holding period | Mix of intraday and positional; 70% of trades intraday, remainder positional; weekly options led to more intraday trades; wants to shift towards positional. No overnight position is left unhedged | 1, 2, 5 |
| Universe / eligibility filters | Index options (more liquid than stock options); index options and futures. Specific index, strikes and expiry not stated | 2, 3 |
| Market / regime filter | Not found in this text. (He says he trades "only when the setup is ready and I am in a sweet spot", undefined) | 3 |
| Setup conditions | Daily support/resistance levels (three) defined from OI, change in OI and futures OI. Market falling into immediate support with significant OI unwinding there: wait for support to break, then bearish view. Market falling with no significant unwinding: contra, bullish view. Change in call OI negative = bullish; change in put OI negative = bearish. Market rising while call-side change in OI is reducing = moderate bullishness, take bullish position cautiously | 3 |
| Entry trigger & order type | Bearish case: sell a call option, and sell a put on the opposite side with value 40-60% of the call sold (no OTM call bought as hedge). May convert position into a ratio spread. Order type, strikes, expiry and time of entry not stated | 4 |
| Initial stop-loss | Two stops: one on each strike and one on overall profit/loss; sizes not stated. Also a pre-defined loss per trade | 2, 4 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text (no exit rule beyond the stops) | - |
| Position sizing | Pre-defined loss in a particular trade decides position size; no unhedged overnight positions and position-sizing rules adopted after the 2013 blow-up | 1, 4 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Drawdown above 15-20% means rethink or change the strategy; his own drawdowns mostly 15-20% (about 20% in 2019). No max-position or exposure limit stated | 2, 4 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of daily S/R levels | 3 | none | 3 |
| OI inputs | OI, change in OI, futures OI | none | 3 |
| Premium of short put as % of short call premium | 40-60% | ratio spread as alternative | 4 |
| Strike on each leg | Not found in this text | - | - |
| Expiry (weekly/monthly) | Not found; weekly options mentioned as having raised intraday trading | - | 2 |
| "Significant" unwinding threshold | Not found in this text | - | - |
| Per-strike stop-loss | Exists; size not given | - | 2 |
| Overall P&L stop-loss | Exists; size not given | - | 2 |
| Pre-defined loss per trade | Exists; size not given | - | 4 |
| Win ratio / reward:risk (self-reported) | 7:3, 1:1.5 | - | 4 |
| Drawdown tolerance before rethink | 15-20% | - | 4 |

**Key quotes**
- "I do not look at a chart to trade but use derivative data" [p. 3]
- "These data help me define three support and resistance levels for the day." [p. 3]
- "I prefer to wait for the support to break and then form a bearish" [p. 3]
- "prefer to take a contra view and be ready to put in a bullish position" [p. 3]
- "if a change in call OI is negative, then it’s a bullish market, and if the change in the put OI is negative, then it’s a bearish market" [p. 3]
- "Here I would take a bullish position, but with a cautious view." [p. 3]
- "sell a put in the opposite side with a value which is 40-60" [p. 4]
- "At times I may convert my position into a ratio spread for hedging" [p. 4]
- "one is on each strike and the second is on the overall profit/loss" [p. 2]
- "have a pre-defined loss in a particular trade which also helps me in deciding my position size" [p. 4]

**Pseudocode** (cannot be run on our data; see section 5)
```
each trading day, before/at open:
    levels = ASSUMPTION_pick_3_levels(OI_by_strike, change_in_OI_by_strike, futures_OI)   # method not given
    pre_defined_loss = ASSUMPTION: fixed Rs or % of capital
for each tick/bar (intraday):
    near = nearest level to spot (within ASSUMPTION: tolerance)
    if spot falling and near is support:
        if put-side OI at near is "significantly" unwinding (ASSUMPTION threshold):
            wait; if spot closes below near: view = BEARISH
        else:
            view = BULLISH (contra)
    elif spot rising and call-side change_in_OI < 0 (reducing):
        view = BULLISH (cautious: ASSUMPTION half size)
    if change_in_call_OI < 0 (significant): view = BULLISH
    if change_in_put_OI  < 0 (significant): view = BEARISH
    if view == BEARISH and no open position:
        sell call (strike ASSUMPTION: ATM or first OTM)
        sell put  (strike chosen so put premium = 0.5 * call premium; allowed 0.4-0.6)
        optionally convert to ratio spread (trigger unstated)
        lots = pre_defined_loss / (per_lot_loss_at_strike_stop)
    if view == BULLISH: mirror image (ASSUMPTION: sell put, sell call at 40-60% of put premium)
    exit if: any strike stop hit OR combined P&L stop hit OR (ASSUMPTION) end of day for intraday trades
```

**Ambiguities & assumptions**
- How the "three support and resistance levels" are chosen from OI: not found in this text. ASSUMPTION: highest put OI strike = support, highest call OI strike = resistance, plus the highest change-in-OI strike as third level.
- "Significant" unwinding is never quantified. ASSUMPTION: change in OI at the strike is negative and at least 10% of that strike's previous-day OI (placeholder to be optimised, not from the text).
- The bearish example (sell call + sell put) is a short strangle-like structure; a short put adds downside risk and is not a hedge in the normal sense. The text says it is "hedging" through the opposite-side premium. Coded as stated. ASSUMPTION: premium ratio target 50%.
- Bullish mirror (sell put, sell call at 40-60% of put) is not stated. ASSUMPTION: symmetric.
- Mixed signals: p. 3 says negative call OI change is bullish, yet "wait for support to break then bearish" in unwinding at support. Both are given; priority between them is unstated. ASSUMPTION: the support-unwinding rule is applied only when price is at the support level, the sign-of-change rule otherwise.
- Stops, targets, strikes, expiry, entry time, risk per trade: not found in this text. ASSUMPTION: intraday positions closed by end of day (he states no overnight unhedged positions, but also that 30% of trades are positional).
- Ratio-spread conversion trigger and ratio: not found in this text.

### 2.2 OI-unwinding option buying via debit spreads (about 20% of trades)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: derivative-data-confirmed directional debit spread | 4 |
| Timeframe & holding period | Not stated specifically for buying; his general mix is 70% intraday, rest positional | 5 |
| Universe / eligibility filters | Index options; underlying and expiry not stated | 2, 3 |
| Market / regime filter | "market trend is also supporting" (trend measure not defined; he does not use charts) | 3, 4 |
| Setup conditions | Heavy unwinding on derivative data and the market trend supporting it | 4 |
| Entry trigger & order type | Buy an at-the-money option and sell an out-of-the-money option (debit spread). Order type not stated | 4 |
| Initial stop-loss | Not found for this leg specifically; general per-strike and overall P&L stops and a pre-defined loss per trade apply | 2, 4 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Pre-defined loss per trade determines size (stated generally) | 4 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | About 20% of trades are option buying; drawdown 15-20% triggers a strategy rethink | 2, 4 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Long leg | At-the-money option | none | 4 |
| Short leg | Out-of-the-money option (distance not stated) | none | 4 |
| Share of trades | about 20% | none | 2 |
| "Heavy" unwinding threshold | Not found in this text | - | - |
| "Trend supporting" definition | Not found in this text | - | - |

**Key quotes**
- "I buy options when I see there is heavy unwinding on derivative data" [p. 4]
- "I do debit spread, that is buy an at-the-money option" [p. 4]
- "20 percent are in option buying" [p. 2]

**Pseudocode** (cannot be run on our data)
```
if heavy_unwinding(call_OI) and trend_supports_up:       # direction ASSUMPTION from p. 3 rule
    buy ATM call; sell OTM call (distance ASSUMPTION: 1 strike step wide per index convention)
elif heavy_unwinding(put_OI) and trend_supports_down:
    buy ATM put; sell OTM put
lots = pre_defined_loss / max_loss_per_lot (debit paid = max loss; ASSUMPTION)
exit: stops per section 3 (levels unstated); ASSUMPTION: close by end of day
```

**Ambiguities & assumptions**
- Which side unwinding maps to which spread is not stated for buying. ASSUMPTION: call-OI unwinding gives a bull call debit spread, put-OI unwinding gives a bear put debit spread (consistent with the p. 3 reading).
- "Market trend is also supporting": no indicator named. ASSUMPTION: spot above (below) its intraday VWAP or previous close; cannot be tested without intraday data.
- Spread width, expiry, exit rules: not found in this text.

## 3. Risk & money-management rules

- A pre-defined loss per trade is set in advance and decides position size [p. 4].
- Stop-losses at two levels: one on each strike and one on overall profit/loss [p. 2]. Sizes not given.
- No unhedged overnight positions and proper position sizing, adopted after the 2013 loss [p. 1]; he reached his target of Rs 7 lakh from Rs 4 lakh in 2.5 years against a two-year goal [p. 1, p. 2].
- Prefers not to buy or sell naked options; hedges each position, with the hedging mode depending on market condition and his view [p. 4].
- Selling options carries unlimited risk, hence the pre-defined loss [p. 4].
- Drawdown above 15-20% means tweak or change the strategy; most of his drawdowns are in the 15-20% range, the highest about 20% in 2019 [p. 2, p. 4].
- After the 2019 drawdown he diversified: 70% option selling, 20% option buying, 10% index futures [p. 2].
- Self-reported edge: 7 of 10 trades win at Rs 10 each, 3 lose Rs 15 each [p. 4]. Arithmetic check: 7 x 10 = 70; 3 x 15 = 45; net = 25. The stated "net profit of Rs 25" is correct (expectancy Rs 2.5 per trade, units of the Rs 10 average win). Note the quoted ratio "reward to risk is 1:1.5" means the average loss is 1.5 times the average win.
- Be cautious when taking more risk intraday [p. 2].

## 4. Non-codable guidance

- Accept profit and loss emotionally as an outcome of a trade and focus on the trade in hand [p. 2].
- Do not trade every move: take trades only when the setup is ready; "not taking a trade is also a trade" [p. 3].
- Does not copy others' styles because each person has own conviction and risk comfort zone [p. 2].
- Index-only trading removes the need to track individual stocks, helpful with a full-time job [p. 2].
- Plans to reduce intraday trades and increase positional ones [p. 5].

## 5. Adapting to NSE (Indian equities)

- **Data required:** historical option chain with open interest and change in OI by strike and expiry (at intraday resolution, since levels are set daily and reacted to intraday); futures open interest; option prices (or IV) per strike for the 40-60% premium ratio and spread pricing; underlying index intraday prices; lot sizes and weekly-expiry calendars; margin/SPAN data for position sizing.
- **Testability with our data:** The OI-based rules in 2.1 and 2.2 CANNOT be backtested at all. Our data (Appendix A1) is daily NSE cash OHLCV and delivery %, with no options data, no open-interest data (option or futures), and Nifty index history only from 2024. Nothing in our panel can reproduce the three OI levels, the OI unwinding signals, the premium-matched short put, or the debit spreads. Cash-equity price data can at best test a crude price proxy of "support breaks / does not break", which is not his method. No forward testing is possible either without acquiring the OI data above. Fundamentals are irrelevant here.
- **Market-structure differences:**
  - The method is native to NSE index derivatives, so no US-to-India translation is needed; but our cash-equity backtest engine cannot represent short-option payoffs, margins or expiry. ASSUMPTION: this resource is kept as a reference for a future derivatives dataset, not coded against the stock panel.
  - Option costs differ from cash (STT on option premium and exercise, brokerage, bid-ask spread); the 0.1% slippage assumption in Appendix A1 is not applicable to option legs. ASSUMPTION: model slippage in premium points per leg once data exists.
  - Weekly expiry rules, lot sizes and index list have changed over time, so any future test must use the contract specification in force on each date.

## 6. Verdict

- **Codeability:** Partly. The directional OI logic and structure (short call + 40-60% short put, debit spread) are described, but OI thresholds, level selection, strikes, expiry and stop sizes are missing; also the data does not exist in our set.
- **Priority for backtesting:** Low. Cannot be tested with our data, rules are loose, and results are self-reported in a short interview.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating "significant unwinding" and "three support/resistance levels" as precisely defined; the text gives no thresholds or selection method, and the screenshot that illustrated it is missing.
  2. Assuming the sell-put leg is a hedge that caps risk. As described it adds a second short option, so risk is still large and the per-strike and overall stops are what bound it.
  3. Misreading the statistics: "reward to risk 1:1.5" means loss is larger than win (7 x 10 - 3 x 15 = +25 per 10 trades), and the figures are self-reported, not a validated backtest.
