# Mitesh Sir's Positional and Expiry Option Selling (Twitter threads) — Aditya Todmal & Niki Poojary (curating @Mitesh_Engr)

- **Source file:** Google Drive invest/"Thread by @AdityaTodmal on Thread Reader App – Thread Reader App" and invest/"Thread by @niki_poojary on Thread Reader App – Thread Reader App" (both .mhtml web-page captures, July 2021)
- **Text file used:** text/todmal_poojary_threads.txt  (page basis: tweets (one [[PAGE N]] per tweet block; p. 1 and p. 35 are file headers). The coordinator extracted the text from the .mhtml files; there are no PDF pages.)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (one tweet block per marker), not any printed page number.
  - [p. 1]-[p. 34] = @AdityaTodmal capture: pp. 2-16 are the main thread "Mitesh Sir's Positional Option Selling 101"; pp. 17-34 are a "Master Thread of all my threads" with short summaries of other threads (strangles, per-order vs per-lot brokerage, @ITRADE191 strike selection, @sourabhsiso19, @SarangSood).
  - [p. 35]-[p. 52] = @niki_poojary capture: "Mitesh Sir's EXPIRY Option Selling 101".
- **Coverage:** Read all 297 lines of the text file, through the last marker [[PAGE 52]]; nothing skimmed. IMPORTANT LIMITATION: most tweets are only headlines (bullet lists of topics) over SCREENSHOT IMAGES of @Mitesh_Engr's original tweets (and of @ITRADE191's). The images are NOT in the extracted text, so the detailed rules (exact entry/exit levels, the ratio examples, SL placement, the worked examples for expiry of 15 July 2021, the position-sizing steps) are MISSING from this spec. What is captured is only the headline summary of each image. Several tweets only link to other threads (pp. 18, 19, 21, 22, 30, 31, 33, 34), whose content is not in the text. Reading done by a Sonnet sub-agent. Text preparation by the coordinator: both .mhtml captures were decoded and the Thread Reader "content-tweet" blocks extracted, one [[PAGE N]] each (Todmal 33 tweet blocks = pp. 2-34, Poojary 17 = pp. 36-52). The coordinator re-ran the verifier and an exact-page check and spot-checked 12 table citations (pp. 3, 4, 5, 7, 8, 9, 10, 27, 28, 40, 42, 43).

## 1. The method in brief
The threads are curated summaries (by Aditya Todmal and Niki Poojary) of how Mitesh Patel (@Mitesh_Engr) sells index options (Bank Nifty, "BNF", and Nifty) on NSE. The positional method is explicitly directional: direction comes from support/resistance on daily and 75-minute charts plus the intraday trend, and "Never trades in strategies" [p. 3]. In weekly expiry, strikes are chosen from the weekly candle high/low, selling options 1% away, with exit when those levels are breached [p. 4]. Capital is deployed in stages: first 20%, then pyramiding the next day [p. 5]. Stop-loss is derived from underlying (index or Bank Nifty futures) levels mapped to option prices [p. 9]. He dismisses IV and Greeks [p. 10, p. 12].

The expiry-day method looks at Bank Nifty technicals, its heavyweight stocks and weekly-timeframe support/resistance [p. 38], follows trend only, chooses strikes by price action rather than premium [p. 39], uses strangles in a range and directional sells on a breakout, with 70/30 or 80/20 ratios [p. 40], and avoids selling Rs. 1-3 options [p. 43]. Return claims: 2% a month "easily", 4-5% with little risk, 0.5% weekly for beginners [p. 7], and "2X of his original capital per month" [p. 13]. No audited track record is presented; evidence is screenshots (not in text).

Two further curated items are covered: @ITRADE191's weekday strike selection [pp. 26-28] and short teasers of other threads (strangles, brokerage, @sourabhsiso19, @SarangSood).

## 2. Strategies

### 2.1 Mitesh positional weekly option selling (directional)
Codability: Partly (direction and level inputs can be defined from OHLC; all option pricing, premiums and the details are not in text).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: directional index option selling (short options), based on support/resistance | 3 |
| Timeframe & holding period | Positional within weekly expiry; one-day-later pyramiding; overnight positions allowed with sizing control or hedge | 4, 5, 8 |
| Universe / eligibility filters | Index options (Bank Nifty future levels used for SL; weekly expiry) | 4, 9 |
| Market / regime filter | Not found in this text (IV explicitly not used: "Doesn't serve much purpose") | 10 |
| Setup conditions | Direction from daily chart S/R, 75 min chart S/R and intraday trend; always directional, never strategies | 3 |
| Entry trigger & order type | Sell options 1% away from the weekly candle High/Low (which side for call/put and exact reference not stated in text); order type not found | 4 |
| Initial stop-loss | Take options levels / Bank Nifty future levels; at that level check the option price and keep that as SL | 9 |
| Exits: profit-taking | Not found in this text (exit criteria are listed as a topic only) | 2 |
| Exits: trailing / time / signal | Exit when levels breached; cut losses immediately; theta decay lowers the SL further | 4, 8, 9 |
| Position sizing | First sell 20% (of capital), then pyramid the next day; "Max risk per day" and "What % risk he takes" are image-only | 2, 5, 6 |
| Adding to / pyramiding | Pyramid the next day; never average losers | 5, 8 |
| Portfolio limits (max positions, correlation, heat) | Overnight positions: control position sizing / hedge. Other limits not found | 8 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Direction timeframes | Daily S/R and 75 min S/R plus intraday trend | - | 3 |
| Strike distance from weekly high/low | 1% away | not found | 4 |
| Initial deployment | 20% | rest deployed by pyramiding next day (amounts not in text) | 5 |
| Monthly return expectation | 2% "easily" | 4-5% with little risk | 7 |
| Beginners weekly target | 0.5% | - | 7 |
| Aggressive claim | 2X original capital per month | no cap such as "1% per week" | 13, 15 |
| Stop-loss | option price at the index/Bank Nifty futures level | - | 9 |
| Max risk per day | image only, value not in text | - | 6 |

**Key quotes**
- "Weekly candle High/Low" [p. 4]
- "Sell 1% away options from those" [p. 4]
- "Exit when levels breached" [p. 4]
- "First sell 20%" [p. 5]
- "Pyramid the next day" [p. 5]
- "Always play directional" [p. 3]
- "Never average losers" [p. 8]
- "Cut losses immediately" [p. 8]
- "At that level check option price and keep that as an SL" [p. 9]
- "Rely on theta decay to help you" [p. 9]

**Pseudocode** (requires option chain data; shown for completeness, NOT runnable on our data)
```
each week W:
  levels = weekly candle high/low (of prior/current week; ASSUMPTION)
  direction = f(daily S/R, 75-min S/R, intraday trend)   # rule for f not in text
  if direction == bullish: short PUT at strike nearest (weekly_low * 0.99)   # ASSUMPTION
  if direction == bearish: short CALL at strike nearest (weekly_high * 1.01)  # ASSUMPTION
  day 1: deploy 20% of intended capital
  day 2: if view intact, deploy remaining (pyramid)    # amount not in text
  SL: underlying level L (option/BNF-future S/R); SL_price = option premium when underlying == L
  exit if underlying breaches the level or option price >= SL_price
  never add to a losing position
```

**Ambiguities & assumptions**
- How S/R is defined on daily and 75-min charts is not stated. ASSUMPTION: prior swing high/low pivots (e.g. 5-bar fractals).
- "1% away from weekly High/Low" is ambiguous (which week; which side; 1% of index or premium). ASSUMPTION: put strike = floor((prior-week low x 0.99)), call strike = ceil((prior-week high x 1.01)), 1% of index price.
- "Pyramid the next day" does not say how much or under what condition. ASSUMPTION: add 80% only if the index is still on the right side of the level.
- Profit-taking, risk per day, what to do "when view goes wrong" and what to do with idle capital are listed on p. 5 and p. 6 as topics only (images missing). Not found in this text.
- Whether the SL is in index points or option premium: the text says keep the option price at that level as SL [p. 9], so premium-based.

### 2.2 Mitesh expiry-day option selling (Bank Nifty)
Codability: Partly (only the technical-level framing; no numeric rules available in text).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: expiry-day intraday option selling (range strangles / directional by breakout) | 40, 48 |
| Timeframe & holding period | Intraday on expiry day; weekly S/R for levels; monthly expiry also covered | 38, 44, 48 |
| Universe / eligibility filters | Bank Nifty options (BNF), 36000 strike cited in example | 38, 50 |
| Market / regime filter | If BNF in a range then strangles; if breakout/breakdown from a range then directional. For event days: no view ahead of the event, decide after the event | 40, 45 |
| Setup conditions | Technicals of BNF; heavyweight stocks of BNF; support/resistance of BNF on weekly TF; daily chart ready for breakout; supports derived on hourly charts | 38, 47 |
| Entry trigger & order type | Follow only trend; price action decides strike, not premium; option below ATP (average traded price) treated as weak/sell-side; sell higher premiums | 39, 43, 49, 50 |
| Initial stop-loss | SL should not hit easily given spikes on expiry day; keep SL below range (exit when hit) | 41, 42 |
| Exits: profit-taking | Sell higher premiums and book them at Rs. 2-5; never wait for options to go to zero | 39, 43 |
| Exits: trailing / time / signal | Exit when SL hit; re-enter when index enters the range again | 42 |
| Position sizing | Limited qty with high premiums; selling 70/30 or 80/20 ratios (what the ratio refers to is only in images) | 40, 43 |
| Adding to / pyramiding | Ability to take re-entry multiple times | 43 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Strike selection basis | trend and price action, not premium | - | 39 |
| Ratio | 70/30 | or 80/20 | 40 |
| Do not sell | Rs. 1-3 options | - | 43 |
| Profit booking level | Rs. 2-5 on higher-premium sells | - | 43 |
| Re-entries | multiple allowed | number not stated | 43 |
| Structure | strangle if range; directional if breakout | - | 40 |
| Hourly/daily levels | derived supports on hourly charts; daily chart breakout | - | 47 |
| Intraday filter | options trading below ATP; resistance at 36000 on the day | - | 49, 50 |

**Key quotes**
- "You can't sell based on premium" [p. 39]
- "Price action is best to sell on expiry day" [p. 39]
- "Never wait for the options to go to zero" [p. 39]
- "If BNF is in a range then strangles" [p. 40]
- "Selling 70/30 or 80/20 ratios" [p. 40]
- "Keep Stop loss below range" [p. 42]
- "Re-enter when index enters range" [p. 42]
- "Don't sell Rs. 1-3 options" [p. 43]
- "Sell higher premiums and book them at Rs. 2-5" [p. 43]
- "No expiry view ahead of the event" [p. 45]
- "Never assume option writers will defend their positions" [p. 44]

**Pseudocode** (requires intraday option data; NOT runnable on our data)
```
on expiry day (Thursday; 15 Jul 2021 example):
  if event scheduled: wait until after the event, then use price action
  range = weekly S/R of BNF (hourly-derived supports)
  if BNF inside range: sell strangle (strikes by trend/price action, premium >= ~Rs 5?)   # ASSUMPTION
  elif breakout/breakdown from range: sell directional side only
  split quantity using 70/30 or 80/20 across the two sides   # meaning unclear
  SL: below the range (underlying level)   # exact placement in images
  if SL hit: exit; re-enter when index re-enters range (repeat)
  book profit at Rs 2-5 on higher-premium sells; do not hold to zero
  skip selling Rs 1-3 options
```

**Ambiguities & assumptions**
- The 70/30 or 80/20 ratio is described only as "Using Ratios to Sell" [p. 40]; it could be call:put quantity weighting or capital split. ASSUMPTION: weights between call-side and put-side of the strangle (heavier on the side with trend).
- "Sell higher premiums and book them at Rs. 2-5" [p. 43] gives no minimum entry premium. Not found in this text.
- SL numeric placement ("Logical explanation") is in images [p. 41]. Not found in this text.
- Monthly expiry: "Play according to day trend" and "No prediction" [p. 44]; no further rules.
- ATP-based filter (p. 49, 50) is an observation in a worked example, not an explicit rule. ASSUMPTION: treat options below ATP as weakening, supportive of selling.

### 2.3 @ITRADE191 weekday strike selection (Nifty weekly options)
Codability: Partly (a short rule set; needs option chain premiums).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: short option strike selection by day of week | 27, 28 |
| Timeframe & holding period | Weekly expiry cycle; start of week to expiry | 27, 28 |
| Universe / eligibility filters | Nifty options | 27 |
| Market / regime filter | Not found in this text (flat market gives huge reward) | 28 |
| Setup conditions | Day of week determines strike: Friday and Monday sell OTM options of 50 rs premium, 4-5 strikes away; Tue/Wed/Fri ATM or near OTM | 27, 28 |
| Entry trigger & order type | Sell the OTM strike with about 50 rs premium at week start | 27 |
| Initial stop-loss | Risk management shown in pictures only; not found in text | 26 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Week-start premium target | 50 rs | strikes 4-5 away | 27 |
| Mid-week strike | ATM or near OTM | - | 28 |
| Days (start) | Friday and Monday | - | 27 |
| Days (mid) | Tue/Wed/Fri | - | 28 |

**Key quotes**
- "prefers to sell OTM options of 50 rs premium in Nifty" [p. 27]
- "ATM options won't decay a lot at the beginning" [p. 27]
- "He prefers to trade in ATM or near OTM options" [p. 28]
- "ATM options have the highest theta decay" [p. 28]

**Pseudocode** (requires option chain; NOT runnable on our data)
```
if weekday in {Fri, Mon}: sell Nifty OTM strike whose premium ~ Rs 50 (4-5 strikes OTM)
elif weekday in {Tue, Wed, Fri*}: sell ATM or nearest OTM strike
(*Friday conflict, see below)
```

**Ambiguities & assumptions**
- Friday appears in both lists (start of week [p. 27] and Tue/Wed/Fri [p. 28]); likely a typo for Thursday in the second list, but the text says Fri. ASSUMPTION: Friday and Monday -> far OTM; Tuesday, Wednesday, Thursday -> ATM/near OTM. The "start of week on Friday" is also odd for Nifty expiry (Thursday), implying Friday of the previous week.
- Which option (call or put, or both) and risk management are not in the text.
- "DJ Sir" [p. 27] is the nickname used for @ITRADE191; its sizing is not in the text.

### 2.4 Non-codable: teaser and summary tweets (no rules in text)
- Mitesh weekly strangles: "How to sell Strangles in weekly expiry" with topics "When to sell", "How to do Adjustments", "Exit Criteria" are only links [p. 21]; "how to sell low premium strangles yourself without paying anyone" [p. 22]. The master strangles thread lists positional/intraday strangles, position sizing, adjustments, when to avoid, exit criteria [p. 20]. No rules are in the text, so not codable.
- @SarangSood: follows volatility closely, makes 7-8 strategies and trades the one with highest profit [p. 33]; theta falls where the market is headed [p. 34]. Discretionary, not codable.
- @sourabhsiso19 curated topics (Bank Nifty strangles/straddles, expiry trading, directional trading, pivot system, DHS pattern) [p. 29] are links only.
- Per order vs per lot brokerage [pp. 23-25]: per-lot brokerage of Rs 10 per lot for 3 lots is Rs 30 on the buy side and Rs 30 on the sell side, overall Rs 60 plus other charges [p. 25]; cost note only.
- Free courses / 15 scanners [pp. 18, 19]: links only.

## 3. Risk & money-management rules
- Deploy only 20% first; pyramid the next day [p. 5].
- Never average losers; cut losses immediately [p. 8].
- Overnight positions: control position sizing / hedge [p. 8].
- SL set at the option price corresponding to a key underlying level [p. 9]; theta decay is expected to lower the SL further [p. 9].
- "Max risk per day" and "What % risk he takes" are topics only [pp. 2, 6]; values are in images (not in text).
- Return expectations: 2% monthly via index options, 4-5% with little risk, 0.5% weekly for beginners [p. 7]; no "1% per week" limit [p. 15].
- Expiry day: SL should not hit easily on spikes but must prevent a huge loss in a violent move [p. 41]; keep SL below the range and exit when hit [p. 42]; limited quantity with high premiums [p. 43].
- Do not sell Rs. 1-3 options: unfavourable risk reward ("Lose heavy one time") [p. 43, p. 46].

## 4. Non-codable guidance
- Remember levels of stocks / index; simple trading [p. 8, p. 12].
- Doesn't believe in Greeks; IV serves little purpose [p. 10, p. 12].
- Gather knowledge and play directional; never play strategies [p. 6].
- Consistency first, "Trade fearlessly later" [p. 7].
- Skill of the driver matters more than the power of the car (de Bono quote) [p. 37].
- Conviction to re-enter multiple times [p. 43]; be on toes for adjustments [p. 38].
- Never assume option writers will defend positions; no prediction on monthly expiry [p. 44].
- Event days: avoid volatility by deciding after the event [p. 45].

## 5. Adapting to NSE (Indian equities)
- **Data required:** historical Nifty / Bank Nifty option chains (strike-wise intraday and daily premiums, OI, ATP), weekly/monthly expiry calendar, option prices at SL levels, lot sizes and margins, plus IV history if IV is to be tested. For underlying logic: Nifty and Bank Nifty index OHLC (daily and 75-minute).
- **Testability with our data:** NONE of the option-selling rules (strike 1% away, 20% then pyramid, 70/30 or 80/20 ratios, premium-based SL, Rs 2-5 booking, Rs 1-3 avoidance, weekday strike selection with Rs 50 premium) can be backtested on our data, because it has no options data (no option chain, premiums, IV, ATP). Our data is daily NSE stock OHLCV (2005-2026), delivery %, Nifty index only from 2024 (NIFTYBEES or an equal-weight index before that), and fundamentals only from 2026. Data needed to test: option chain history for Nifty/Bank Nifty with premiums (ideally intraday), and Bank Nifty index/futures intraday history.
- ASSUMPTION: A small, partial proxy is possible on equity/index OHLCV: weekly high/low levels (p. 4), daily support/resistance direction (p. 3) and a breakout-from-range regime filter (p. 40) can be computed on NIFTYBEES or index daily data and used to test direction accuracy (e.g. whether price stays above weekly low minus 1% over the next week), but this does not measure option P&L. Bank Nifty history is not in our data (only Nifty index from 2024), so a Bank Nifty proxy would use constituent bank stocks.
- **Market-structure differences:** these are short-option strategies on index weekly/monthly expiry, with margins and unlimited risk. The NSE cash market has no overnight shorting, so they cannot be mimicked with stocks. ASSUMPTION: any stock proxy is long-only (e.g. use the directional signal to hold NIFTYBEES or bank stocks only). Weekly expiry days and lot sizes have changed since 2021 (the threads date from July 2021), so day-of-week rules may not hold today; STT on option sell premiums and per-order brokerage matter [p. 24, p. 25].

## 6. Verdict
- **Codeability:** Partly (positional and expiry methods) — only headline rules are in text; the detailed rules sit in screenshots not captured. The strike selection rule by weekday is a short rule set but needs option data.
- **Priority for backtesting:** Low — no options data in our dataset, no quantified rules beyond 1% / 20% / Rs 50 / Rs 2-5, and the source is anecdotal.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the headline bullets as complete rules: the image-only rules (SL, risk per day, ratios, profit exit) are missing and must not be invented.
  2. Misreading "1% away from weekly High/Low" (which week, which side, 1% of index not of premium) and "20% then pyramid" (20% of what capital).
  3. Treating the expiry ratios (70/30 or 80/20) and the Rs 2-5 / Rs 1-3 premium thresholds as testable on spot data, and mixing the Friday in the @ITRADE191 weekday lists.
