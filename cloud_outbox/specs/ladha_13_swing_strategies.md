# 13 Swing Trading Strategies — Pankaj Ladha & Anant Ladha

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/13_Swing_Trading_Strategies_Pankaj_Ladha,_Anant_Ladha_2022.pdf` (file id `1NSxWN05RU8i5P1i5ZRsG9uH1doeQcmLP`, 5,622,734 bytes; Invincible Publishers, first edition 2022, ISBN 978-93-90542-58-1 [p. 1–2])
- **Text file used:** text/ladha_13_swing_strategies.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter. (This PDF is a two-up scan: each PDF page holds about two printed pages, so printed numbers run roughly 1.2× the PDF index.)
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/ladha_13_swing_strategies.md text/ladha_13_swing_strategies.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 171]]. All 171 PDF pages have a text layer, but the example chart pages after each strategy are images whose only text is garbled watermark/caption fragments (e.g. [p. 56–57, 64, 74–78, 88–89, 95–97, 102–104, 112–118, 124–127, 141–142, 148–150, 156, 163–164]). Those charts' captions (stock names, dates) cannot be read and no rules were taken from them. Part 1 chapters (swing-trading basics, risk/reward, psychology) [p. 11–49] read; they hold the general rules used in Section 3.

## 1. The method in brief

A practitioner's handbook of thirteen long-side swing setups for Indian (NSE) cash equities, each laid out in the same frame: "ground level strategy" (filters), "base mindset" (market regime), "look for the place to enter", stop-loss, "quantity and risk capital", and "exit at the right point". The swing horizon is about one to three weeks [p. 11, 13]: the authors look for "gains in the range of 8 to 12%" with a 3–4% stop, a 1:3 risk/reward [p. 13–14, 34]. Most setups are momentum/breakout trades taken only when the broad indices (Nifty, Midcap, Smallcap) are above their 50-day averages; two (mean reversion, support/resistance) are meant for range-bound markets, and the closing chapter maps each setup to a market phase [p. 165–166]. Common filters across almost every setup: share price at least Rs. 300 and average daily traded value at least Rs. 1 crore [p. 50, 58, 67, 79, 105, 121, 129].

The book presents no backtests or track record. Evidence is anecdotal Indian examples (Reliance/JIO, GNFC, Deepak Nitrite, Latent View, ICRA, Zomato, Mrs Bectors) [p. 51, 69, 81–83, 120, 133, 154] and a mention of Jim Simons' ~51% hit rate and two-day holding period [p. 32, 62]. The Strategy 6 chapter recommends the reader backtest crossovers themselves [p. 98]; no results are given.

## 2. Strategies

Shared exit template used by Strategies 1, 2, 3, 7, 8 (and with 2.5–8 days in 9): sell **half** of the position 2.5 to 5 trading days after entry; sell the rest on a **close** below the 10-, 20- or 50-day EMA [p. 53, 61, 72, 109, 123]. "2.5 days" is the authors' own unit (two full sessions plus half of the third) [p. 93]. ASSUMPTION for daily-bar backtests: "2.5–5 days" = exit half at the close of day 3 (minimum) or day 5 (maximum); test both.

### 2.1 Strategy 1 — "The big bang": volume blast

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout / growth-momentum (volume event) | 49–50 |
| Timeframe & holding period | 60-minute or daily candles; move can continue "for several weeks"; may be followed by a 2.5- to 21-day consolidation or pullback to the 10/20/50-day EMA before another leg | 52 |
| Universe / eligibility filters | Price ≥ Rs. 300; avoid "false alarms" such as de-mergers and stock splits; prefer stocks "not in very high float"; there should be a fundamental reason (news) behind the volume | 50–52 |
| Market / regime filter | Nifty and Sensex (at least the large indices) must be in an uptrend | 50, 52 |
| Setup conditions | Day's gain > 5%; volume ≥ 10× daily average **and** greater than the previous day's volume; stock breaking out of a recent consolidation | 50 |
| Entry trigger & order type | Buy the volume-blast breakout (daily or 60-minute candle); order type not stated | 50, 52 |
| Initial stop-loss | At "the base" bought from, or 7–8% below the buy price; beginners 4–5% | 52–53 |
| Exits: profit-taking | Seek at least 3:1 reward:risk ("big 10 to 1 or even 20 to 1"); if in profit, sell half 2.5–5 days after entry | 53 |
| Exits: trailing / time / signal | Rest on a close below the 10-, 20- or 50-day EMA | 53 |
| Position sizing | Risk 0.5–1% of capital per trade (worked example: 10% of capital with an 8% stop = 0.8% risk) | 53–54 |
| Adding to / pyramiding | Average up only, never down, with a strict revised trailing stop | 54–55 |
| Portfolio limits | Not stated for this setup; book-wide 15% of capital per stock (Section 3) | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Day gain | > 5% | — | 50 |
| Volume multiple | ≥ 10× daily average | average length not stated | 50 |
| Stop | 7–8% below entry | 4–5% (beginners); "the base" | 53 |
| Risk per trade | 0.5–1% | — | 53 |
| First partial exit | half after 2.5–5 days | — | 53 |
| Trailing EMA | 10, 20 or 50 day (close below) | — | 53 |

**Key quotes**

- "Daily price gain must be over 5%, anything less than this will not indicate a volume blast in the share." [p. 50]
- "We should look for a minimum 10X of daily average and for sure it must be more than the previous day volume." [p. 50]
- "if the share is getting out of recent consolidation then it’s a sure shot buy." [p. 50]
- "stoploss at the base he bought or 7 to 8% below the buying level." [p. 53]
- "a trader can sell half of the position engaged in next 2.5 to 5 days and rest can be sold when a stock closes below a 10, 20 or 50-day EMA." [p. 53]

**Pseudocode** (daily bars; `ADV50 = SMA(volume, 50)`, `TV20 = SMA(close×volume, 20)`)

```
eligible_t = C_t >= 300 and TV20_t >= 1e7 and regime_up_t            # regime: see Section 3
signal_t   = eligible_t and C_t/C_{t-1} - 1 > 0.05
             and V_t >= 10 * ADV50_{t-1} and V_t > V_{t-1}
             and C_t > max(H_{t-20..t-1})                             # ASSUMPTION: "consolidation breakout" = close above prior 20-day high
enter long at O_{t+1}
stop       = entry * (1 - 0.08)                                       # ASSUMPTION: 8% (book's main value)
shares     = floor(risk_pct * equity / (entry - stop)),  risk_pct = 0.01 (0.005 alt)
on close of day entry+3 (alt: +5), if C > entry: sell 50%
remaining: exit next open after C < EMA20 (alt EMA10 / EMA50); stop always active
```

**Ambiguities & assumptions**

- **"Daily average" volume length** not given [p. 50]. ASSUMPTION: 50-day average, the length the book uses in Strategy 7 [p. 105].
- **Stop**: "the base" or 7–8%, beginners 4–5% [p. 53], against the book-wide 3–4% swing stop [p. 33]. ASSUMPTION: 8% for this setup (the authors explain the wide stop is deliberate to avoid shake-outs [p. 53]); test 4–5% as a variant.
- **Consolidation breakout** is not defined numerically [p. 50]. ASSUMPTION: close above the prior 20-day high.
- **News filter** ("track the reason behind it" [p. 50]) and the "false alarm" exclusion (de-mergers, splits) [p. 51] are discretionary. ASSUMPTION: exclude days within ±5 sessions of a corporate action in the adjustment table; otherwise ignore the news requirement.
- **Which trailing EMA** (10, 20 or 50) is left to the trader [p. 53]. ASSUMPTION: EMA20 base case; EMA10 and EMA50 as variants.

### 2.2 Strategy 2 — Breakout trades (range breakout to new 10/20-day high)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout | 57 |
| Timeframe & holding period | Daily; half out after 2.5–5 trading days, rest trailed | 61 |
| Universe / eligibility filters | Price ≥ Rs. 300; average daily traded value > Rs. 1 crore | 58 |
| Market / regime filter | Nifty and Bank Nifty in a confirmed uptrend; Smallcap, Midcap and Nifty above their 50-day moving averages; helps if Smallcap index is above its 10/20-day EMA. "breakout doesn’t work in a range bound or corrective market" | 58, 60 |
| Setup conditions | Consolidation / range contraction above the 10- and 20-day EMAs | 57–58 |
| Entry trigger & order type | Buy on the day of a 3–5%+ breakout to a fresh 10- or 20-day high (or next day); alternatives: buy in the consolidation in anticipation (confirmed uptrend only) or on a pullback to a rising 10/20/50-day EMA | 57–58, 61 |
| Initial stop-loss | About 1% below the entry day's low; alternative below the 10/20-day EMA | 61 |
| Exits: profit-taking | Sell half 2.5–5 trading days after entry | 61 |
| Exits: trailing / time / signal | Rest trailed to the 10/20-day EMA on a closing basis | 61 |
| Position sizing | Risk 0.5–1% of capital; shares = risk ÷ (entry − stop) (example: Rs. 1 crore, 0.5% risk, buy 460 / stop 425 → 1,428 shares ≈ 6.56% of capital) | 61 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Never more than 15% of capital in one stock | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Breakout day gain | 3–5% | "more than 3-5%" | 58, 61 |
| New high lookback | 10 or 20 days | — | 58 |
| Stop | 1% below entry-day low | below 10/20-day EMA | 61 |
| Risk per trade | 0.5–1% | — | 61 |
| Max position | 15% of capital | — | 63 |

**Key quotes**

- "3-5% breakout to achieve at new 10 or 20-day high." [p. 58]
- "Always remember that breakout doesn’t work in a range bound or corrective market" [p. 60]
- "large caps (NIFTY) are trading above their 50-day moving averages" [p. 60]
- "Put your stoploss around one percent below the lows of entry day." [p. 61]
- "In general we sell half 2.5 to 5 trading days after your entry. Pending quantity can be sold and trail to 10/20 day EMA on closing basis." [p. 61]
- "you should never put more than 15% of your capital in a single stock while you swing trade." [p. 63]

**Pseudocode**

```
signal_t = C_t >= 300 and TV20_t >= 1e7 and regime_up_t
           and C_t/C_{t-1} - 1 >= 0.03                      # ASSUMPTION: 3% minimum (5% as variant)
           and C_t > max(H_{t-N..t-1}),  N in {10, 20}
enter long at C_t (end-of-day)                              # book: buy on breakout day; ASSUMPTION fill at close; next-open as variant
stop   = 0.99 * L_t
shares = min(floor(risk_pct*equity/(entry-stop)), floor(0.15*equity/entry)),  risk_pct in {0.005, 0.01}
day entry+3 (alt +5): sell 50%
remaining: exit next open after C < EMA20 (alt EMA10)
```

**Ambiguities & assumptions**

- **"3-5% breakout"**: whether 3–5% is a band (exclude > 5%) or a minimum ("more than 3-5%" [p. 61]). ASSUMPTION: minimum 3%, no upper cap; test a 3–5% band as a variant.
- **Regime test**: indices "above their 50-day moving averages" [p. 60] vs. "Range contraction is above 10 and 20-day EMAs" [p. 58] (the latter reads as a stock-level condition). ASSUMPTION: regime = index above its 50-day SMA; stock-level = close above EMA10 and EMA20 on the day before the breakout.
- **Entry day vs next day** [p. 57, 61]. ASSUMPTION: breakout-day close; next-day open as a variant.

### 2.3 Strategy 3 — Buying the dip (pullback to a rising EMA)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following pullback | 65–66 |
| Timeframe & holding period | Daily; half out after 2.5–5 days; profit target 6–10% for the 50-EMA variant | 69, 72 |
| Universe / eligibility filters | Momentum: up > 20% in 30 days, or > 30% in 90 days, or > 50% in 180 days; price > Rs. 300; traded value ≥ Rs. 1 crore/day; prefer industry leaders/blue chips in favoured industries | 67, 70 |
| Market / regime filter | Broad market in an uptrend (not a dead-cat bounce); "confirmed uptrend": stock above its 50 DMA and 50 DMA above 200 DMA; track Nifty and Bank Nifty | 67, 70 |
| Setup conditions | Pullback to a **rising** 10, 20 or 50-day EMA on **low volume**; time or price consolidation | 67–68 |
| Entry trigger & order type | Wait for a 3–5% bounce from the rising EMA before buying; 50-EMA variant: price bounces near the 50 EMA and closes above it, or dips below intraday and closes above, or closes below then closes back above next day; alternative entry: new 20-day high | 68–69, 71 |
| Initial stop-loss | 0.5% below the entry day's low, or below the 10 or 20/50-day EMA | 71 |
| Exits: profit-taking | Half after 2.5–5 days; 50-EMA variant target 6–10% | 69, 72 |
| Exits: trailing / time / signal | Rest on a close below the 10/20/50-day EMA | 72 |
| Position sizing | Risk 0.5–1% of capital; cap the position at 20% of the account (example: 20 lakh, 1% risk, 2300/2200 → 200 shares = 4.6 lakh, cut to 4 lakh) | 71–72 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 20% of account per position (this chapter) | 72 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Momentum filter | > 20% / 30d or > 30% / 90d or > 50% / 180d | — | 67 |
| Pullback EMA | 10, 20 or 50 day (rising) | 50-day called "higher probability" | 68 |
| Bounce confirmation | 3–5% off the EMA | — | 68, 71 |
| Stop | 0.5% below entry-day low | below EMA | 71 |
| Target (50-EMA variant) | 6–10% | — | 69 |
| Risk / cap | 0.5–1% / 20% of account | 15% book-wide | 71–72, 63 |

**Key quotes**

- "those stocks which are up more than 20% in the past 30 days or more than 30% in the past 90 days or more than 50% in the past 180 days." [p. 67]
- "we buy pullbacks if it is happening with low volumes." [p. 68]
- "Usually a 3-5% bounce near a stock’s 10 or 20 or 50-day EMAs (exponential moving averages) is good signal to work on it" [p. 68]
- "Proﬁt target could be in the range of 6-10 %." [p. 69]
- "the stocks must be above its 50 DMA and this 50 DMA must be above its 200 DMA." [p. 70]
- "You should put your stop at half a percent below the entry day’s low or a stock’s 10 or 20/50-day EMA." [p. 71]
- "We must restrict it to 20% of the account" [p. 72]

**Pseudocode**

```
mom_t     = (C_t/C_{t-21} > 1.20) or (C_t/C_{t-63} > 1.30) or (C_t/C_{t-126} > 1.50)   # ASSUMPTION: 30/90/180 calendar days ≈ 21/63/126 sessions
trend_t   = C_t > SMA50_t and SMA50_t > SMA200_t and regime_up_t
for E in {EMA10, EMA20, EMA50}:
  touched   = min(L_{t-5..t}) <= E * 1.01 and E_t > E_{t-5}                              # ASSUMPTION: within 1% of a rising EMA in last 5 sessions
  low_vol   = mean(V over pullback days) < ADV50
  bounce    = C_t >= min(L_{t-5..t}) * 1.03                                               # 3% bounce off the pullback low
signal_t = C_t>=300 and TV20_t>=1e7 and mom_t and trend_t and touched and low_vol and bounce
enter at C_t; stop = 0.995 * L_t
shares = min(floor(risk*equity/(entry-stop)), floor(0.20*equity/entry))
day +3 (alt +5): sell 50%; rest exit on close < E (the same EMA)
50-EMA variant: target = entry*1.06..1.10 for the whole position
```

**Ambiguities & assumptions**

- **Bounce reference** (3–5% "near" vs "from" the EMA) [p. 68, 71] is not defined. ASSUMPTION: 3% above the pullback low, measured on close.
- **Low volume** has no threshold [p. 68]. ASSUMPTION: average volume of the pullback days below the 50-day average.
- **Position cap 20%** [p. 72] vs book-wide 15% [p. 63]. ASSUMPTION: 15% (stricter, applies "while you swing trade"); 20% as a variant.
- **Regime**: moving averages called both DMA and EMA. ASSUMPTION: SMA for the 50/200 trend test [p. 70], EMA for the pullback level [p. 68].

### 2.4 Strategy 4 — IPO trading (recent listings)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout / growth-momentum | 78–79 |
| Timeframe & holding period | 2.5–8-day swing trades or 2.5–8-week position trades; opportunities for the first twelve months after listing | 85, 87 |
| Universe / eligibility filters | Listed not more than one year; price ≥ Rs. 300; average traded value Rs. 1 crore/day; often best 40–50% below the all-time high; favoured/"exuberant" industry; small float preferred | 79, 81 |
| Market / regime filter | Super bull market: Nifty and Bank Nifty above their 20, 50 and 200-day MAs; or a few days after a correction, generally a 10% decline in the Nifty 50 | 79, 82 |
| Setup conditions | Ranged consolidation of 10–20% (contraction expected to be followed by range explosion) | 79, 84 |
| Entry trigger & order type | (1) Enter after a 3–5% move around the breakout from the consolidation; (2) enter in anticipation when the breakout is near (sudden high volume or more up-days than down-days) | 84 |
| Initial stop-loss | Breakout entry: the breakout day's low. Anticipation entry: about 1% below the low of the established range | 84 |
| Exits: profit-taking | Not stated beyond holding period (example: 2400 → 4000 = 6R) | 85 |
| Exits: trailing / time / signal | Time: 2.5–8 days (swing) or 2.5–8 weeks (position) | 85 |
| Position sizing | Risk at most about 1% of capital (example: 20 lakh, 2400/2200 → 100 shares, 12% of capital) | 84–85 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated in chapter; 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Listing age | ≤ 1 year | "at least ﬁrst twelve months" | 79, 87 |
| Base depth | 10–20% range | — | 79 |
| Breakout move | 3–5% | — | 79, 84 |
| Distance from ATH | 40–50% below often best | "might be a good thing" to trade at ATH | 79 |
| Risk | ~1% | — | 84 |
| Holding | 2.5–8 days | 2.5–8 weeks (position) | 85 |

**Key quotes**

- "We must trade in recently listed shares which give priority to those ones which are not more than one year old." [p. 79]
- "this type of breakout generally comes after a ranged consolidation of 10 to 20%." [p. 79]
- "all major stock indices like NIFTY and Bank NIFTY are trading above their 20, 50 and 200-day moving averages." [p. 82]
- "If you are buying on the 3-5% breakout day then keep your stoploss at breakout day’s low." [p. 84]
- "2.5 to 8-day swing trades or 2.5 to 8-week position trades is good trading strategy while trading in an IPO." [p. 85]

**Pseudocode**

```
age_t     = sessions since first traded bar <= 250
base      = (max(H_{t-20..t-1}) / min(L_{t-20..t-1}) - 1) between 0.10 and 0.20      # ASSUMPTION: base measured over 20 sessions
regime_t  = Nifty proxy > SMA20, SMA50 and SMA200
signal_t  = age_t and C_t>=300 and TV20_t>=1e7 and regime_t and base
            and C_t > max(H_{t-20..t-1}) and C_t/C_{t-1}-1 >= 0.03
enter at C_t; stop = L_t; shares = floor(0.01*equity/(entry-stop)) capped at 15% of equity
exit at close of day entry+8 (alt: +3; position variant +40 sessions), or stop
```

**Ambiguities & assumptions**

- **Profit-taking** is not specified beyond holding periods [p. 85]. ASSUMPTION: time exit at 8 sessions, plus the shared half-at-2.5–5-days / EMA20-trail template as a variant.
- **Base window** length not stated [p. 79, 84]. ASSUMPTION: 20 sessions.
- **Listing date**: the panel's first bar is the listing date. IPOs without 200 sessions of history cannot have a 200-day MA; the regime test uses the index, so that is fine.
- **Regime**: either a super bull market or right after a ~10% Nifty correction [p. 82]. ASSUMPTION: base case requires the index above its 20/50/200-day SMAs; the post-correction entry is a variant.

### 2.5 Strategy 5 — "2.5 days funda" (three-day profit-booking dip)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following pullback (short-term reversal inside an uptrend) | 89–90 |
| Timeframe & holding period | Daily; dip lasts 2.5 days, "some time for five days"; target 5–8% | 91, 93 |
| Universe / eligibility filters | Stock in a strong uptrend, good fundamentals, not a speculative counter | 90–91, 94 |
| Market / regime filter | Market also in uptrend; uptrend only (newcomers), not in bear or neutral markets | 90, 92, 94 |
| Setup conditions | Day 1: falls with heavy volume; day 2: opens about 2–3% lower with lower volume than day 1; day 3: opens red on thinner volume. A breakdown on very low volume does not qualify | 91–92 |
| Entry trigger & order type | Never buy on day 1 or day 2; buy in the first half of day 3 when volume is lower than the previous two days (even if day 3 opens up with the index) | 93 |
| Initial stop-loss | 2–3%, or 1% below the low of the three days | 93 |
| Exits: profit-taking | Target around 5–8% | 93 |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | Risk 0.5–1% of capital | 93 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Dip length | 2.5 days | up to 5 days | 91 |
| Day-2 gap | opens ~2–3% lower | — | 91 |
| Stop | 2–3% | 1% below 3-day low | 93 |
| Target | 5–8% | — | 93 |
| Risk | 0.5–1% | — | 93 |

**Key quotes**

- "fall with volume on the ﬁrst day and fall with low volumes on the second day" [p. 90]
- "in general it will open around 2-3% lower but with lesser volume than the ﬁrst day." [p. 91]
- "if the breakdown of the stock is happening on very low volumes than it does not ﬁt in the strategy" [p. 92]
- "We must never enter into stock on day-1 and day 2. The best time enter is at ﬁrst half on third day" [p. 93]
- "Keeping the stop loss of 2 to 3% is important or you may keep your stop loss just 1% below the low of three days." [p. 93]
- "Targeting around 5 to 8% proﬁt in these kinds of stock is not a bad idea" [p. 93]

**Pseudocode**

```
uptrend   = C_{t-3} > SMA50 and SMA50 > SMA200 and regime_up                   # ASSUMPTION: "perfect uptrend" definition
day1 (t-2): C < C_prev and V >= 1.5*ADV50                                      # ASSUMPTION: heavy = 1.5x avg
day2 (t-1): O <= C_day1*0.98 and C < C_day1 and V < V_day1
day3 (t):   O < C_day2 and entry at O_t                                        # daily bars cannot see "first half"; ASSUMPTION buy at open
            (variant: enter at C_t only if V_t < V_day2 and C_t > O_t)
stop   = max(entry*0.97, 0.99*min(L_day1..L_day3))   # ASSUMPTION: tighter of 3% and 1% below 3-day low (day-3 low unknown at open → use 3% at open, then min(...))
target = entry*1.06 (range 1.05–1.08); time exit after 5 sessions if neither hit   # ASSUMPTION: time stop not in book
risk 0.5–1% of equity
```

**Ambiguities & assumptions**

- **Intraday timing**: entry is "first half on third day" with lower first-half volume [p. 93]; daily data cannot check this. ASSUMPTION: buy at day-3 open; variant buys at day-3 close only if day-3 closed up on lower volume.
- **"Heavy volume"** on day 1 has no number [p. 91]. ASSUMPTION: ≥ 1.5× 50-day average.
- **No time exit** is given. ASSUMPTION: 5 sessions (the book says the dip itself is 2.5–5 days [p. 91]).

### 2.6 Strategy 6 — EMA crossovers

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 97 |
| Timeframe & holding period | Daily; trades "that last a few days to weeks" | 98 |
| Universe / eligibility filters | Pre-decided watch list or indices; 10/20 cross said to work on many recent IPOs | 98–99 |
| Market / regime filter | Not stated for this setup | — |
| Setup conditions | One of three pairs: 10 EMA × 20 EMA, 20 EMA × 50 EMA, 50 EMA × 200 EMA; pick the pair that has worked historically for that stock/market (backtest) | 98–99 |
| Entry trigger & order type | End of day, when the short EMA crosses and **closes** above the long EMA; avoid entering late after much of the move | 99–100 |
| Initial stop-loss | Short EMA crossing back under the long EMA | 100 |
| Exits: profit-taking | Book profit above ~10% from entry (if backtest shows average winner ~12%) | 100 |
| Exits: trailing / time / signal | Trail until the reverse cross; or trail with a close below the previous day's low or a large bearish reversal candle | 100 |
| Position sizing | Risk not more than 1% of capital | 100 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| EMA pairs | 10/20, 20/50, 50/200 | — | 98 |
| Profit target | > 10% | backtest-derived (12% average winner example) | 100 |
| Risk | ≤ 1% | — | 100 |

**Key quotes**

- "1. 10 days EMA crosses 20 days EMA 2. 20 days EMA crosses 50 days EMA 3. 50 days EMA crosses 200 days EMA" [p. 98]
- "Enter at the end of day based on short-term moving average crossing and closing over the long term moving average." [p. 99]
- "You can also use a trailing stop of a close below the previous day’s low or a large bearish reversal candle" [p. 100]
- "a trader should book proﬁts when the stock is trading above 10% from the entry point." [p. 100]

**Pseudocode**

```
for (s,l) in {(10,20),(20,50),(50,200)}:
  entry when EMA_s[t] > EMA_l[t] and EMA_s[t-1] <= EMA_l[t-1]; fill at C_t
  exit A (signal): EMA_s < EMA_l at close → sell next open
  exit B (target): C >= entry*1.10 → sell at close
  exit C (trail):  C_t < L_{t-1} → sell next open
  risk sizing: stop distance unknown at entry → ASSUMPTION: size by 1% risk with notional stop = min(L_{t-1..t}) or 2×ATR20, cap 15% of equity
```

**Ambiguities & assumptions**

- **No fixed stop price**: the stop is the reverse crossover, so 1% risk cannot be computed from the book [p. 100]. ASSUMPTION: size against a notional stop (prior two-day low), cap at 15% of equity.
- **Exit combination**: three alternatives are listed [p. 100]. ASSUMPTION: test each exit separately, plus "first of B or C".
- **Pair selection by historical backtest** [p. 99] is look-ahead if done on the full sample. ASSUMPTION: test each pair across the universe; any per-stock choice uses walk-forward only.

### 2.7 Strategy 7 — Post-earnings announcement drift (PEAD)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | growth-momentum / event | 104–105 |
| Timeframe & holding period | Swing: 2.5–8 trading days; position: 2.5–8 weeks (book also says about one week swing, about 3–10 weeks position) | 105, 109 |
| Universe / eligibility filters | Price > Rs. 300; traded value > Rs. 1 crore; trading above its 50-day price MA | 105 |
| Market / regime filter | Risk 1% when large- and small-cap indices are above their 50-day MAs; 0.5% in range-bound markets. Also said to work "beautifully" in downturns | 107, 109 |
| Setup conditions | Earnings announcement; stock gains > 3–5% on volume > 3× its 50-day average and ≥ 50% above the previous day's volume | 105 |
| Entry trigger & order type | (1) On announcement: small base above VWAP / intraday breakout; (2) next day, on taking out the earnings day's high; (3) breakout from a sideways consolidation above a rising 10/20-day EMA | 108 |
| Initial stop-loss | 0.5% below the entry day's low, or right below the 10/20-day EMA | 108 |
| Exits: profit-taking | Swing: sell half 2.5–5 days after buying; position: sell 50% after 2.5 up-weeks in a row | 109 |
| Exits: trailing / time / signal | Swing: rest on a close below the 10/20-day EMA; position: rest on a close below the 50-day SMA; overall within 2.5–8 days (swing) | 109 |
| Position sizing | Risk 1% (uptrend) / 0.5% (range-bound) | 109 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Event-day gain | > 3–5% | — | 105 |
| Volume vs 50-day avg | > 3× | — | 105 |
| Volume vs previous day | ≥ +50% | — | 105 |
| Stop | 0.5% below entry-day low | below 10/20 EMA | 108 |
| Risk | 1% uptrend / 0.5% range | — | 109 |
| Swing holding | 2.5–8 days | — | 109 |

**Key quotes**

- "The stock which has gained more than 3-5% on more than three times its 50-day average daily traded volume." [p. 105]
- "The volume should be at least 50% higher than previous day" [p. 105]
- "Buying in the next day of earning is also good if we get levels of earlier day’s high." [p. 108]
- "The stoploss is half a percent below the lows of the entry day or right below a stock’s 10/20 day EMA." [p. 108]
- "Risk 0.5% of capital during range-bound markets when some of the major indices are below 50-day EMA" [p. 109]
- "the trader must sell 50% of position after 2.5 up weeks in a row. Sell the rest 50% on a close below a stock’s 50-day simple moving" [p. 109]

**Pseudocode**

```
event_t = (earnings date == t or t-1)          # NEEDS earnings calendar; see Section 5
          and C_t/C_{t-1}-1 > 0.03 and V_t > 3*ADV50_{t-1} and V_t >= 1.5*V_{t-1}
          and C_t > SMA50_t and C_t >= 300 and TV20_t >= 1e7
entry (variant 2): on t+1 buy stop at H_t; fill = max(O_{t+1}, H_t) if H_{t+1} > H_t
stop  = 0.995 * L_{entry day}
risk  = 1% if all index proxies > 50-day MA else 0.5%
swing: day +3 (alt +5) sell 50%; rest on close < EMA20 (alt EMA10); hard time exit day +8
position variant: sell 50% after the 3rd consecutive up week; rest on close < SMA50
```

**Ambiguities & assumptions**

- **Earnings date** is required but not in our data (Section 5). ASSUMPTION: run an "earnings-agnostic" version that fires on the price/volume event alone, and flag it as a different strategy; true PEAD only once earnings dates are sourced.
- **"2.5 up weeks in a row"** [p. 109]. ASSUMPTION: three consecutive weekly closes above the prior week's close.
- **Regime index MA**: 50-day "moving averages" and "50-day EMA" in the same paragraph [p. 109]. ASSUMPTION: 50-day EMA.

### 2.8 Strategy 8 — Relative strength ("better than others")

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | growth-momentum / relative strength | 119 |
| Timeframe & holding period | Swing (half after 2.5–5 days) or positional | 122–123 |
| Universe / eligibility filters | Gained 10–50% over the last 1, 3 to 6 months; price ≥ Rs. 300; average daily turnover > Rs. 1 crore; leadership measured against Nifty/Sensex (example: GNFC 20% above its low when Nifty bottomed) | 120–121 |
| Market / regime filter | Works in all trends; best entries as the market recovers after a Nifty correction of 10% or more | 122 |
| Setup conditions | Stock held up/consolidated while the index fell; above its 50-day MA | 120, 122–123 |
| Entry trigger & order type | Breakout to a new 50-day high, or a 3–5%+ bounce with volume from a rising 10 or 20-day EMA; breakouts near the 50-day MA or after long consolidation | 121–122 |
| Initial stop-loss | 0.5% below the entry day's low, or at the current 10/20/50-day EMA | 122 |
| Exits: profit-taking | Swing trader seeks 5–20%; sell after a 2.5–5 day upward move | 123 |
| Exits: trailing / time / signal | Or a close below the 10/20/50-day EMA as trailing stop | 123 |
| Position sizing | Risk not more than 1% (worked example garbled; see Ambiguities) | 123 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RS gain | 10–50% over 1–6 months | — | 120 |
| Breakout lookback | 50-day high | 3–5% bounce off rising EMA10/20 | 121 |
| Index correction trigger | ≥ 10% | — | 122 |
| Stop | 0.5% below entry-day low | 10/20/50 EMA | 122 |
| Risk | ≤ 1% | — | 123 |

**Key quotes**

- "Have a track of those stocks which have signiﬁcantly gained in terms of pricing for last month, 3 months to 6 months, this price range can be from 10 to 50%." [p. 120]
- "A trader can buy on a breakout to new 50-day highs or after bigger than 3 to 5% bounce with volume from a rising 10 or 20 day EMA." [p. 121]
- "Look for a recovery after a correction of 10% or above in NIFTY." [p. 122]
- "The stop loss at half a percent below the lows of your entry day or at the current 10/20 or 50 day EMA." [p. 122]

**Pseudocode**

```
index = Nifty proxy; dd_t = index_t / max(index_{t-250..t}) - 1
recovery_window_t = (min(dd over last 60 sessions) <= -0.10) and index_t > min(index over last 60) * 1.03  # ASSUMPTION
rs_t = C_t/C_{t-63} - index_t/index_{t-63}         # ASSUMPTION: 3-month excess return; rank top decile
gain_ok = 0.10 <= C_t/C_{t-21..t-126}-1 <= 0.50 for at least one of 21/63/126
signal_t = recovery_window_t and rs top decile and gain_ok and C_t>=300 and TV20_t>=1e7
           and (C_t > max(H_{t-50..t-1}) or [3% bounce with V>ADV50 from rising EMA10/20])
enter C_t; stop = 0.995*L_t; risk 1%; half at +3 (alt +5); rest on close < EMA20
```

**Ambiguities & assumptions**

- **10–50% gain** is a range, not a floor [p. 120]. Unclear whether > 50% should be excluded. ASSUMPTION: ≥ 10%, no upper cap; 10–50% band as a variant.
- **Relative strength vs the index** is described only by example (GNFC vs Nifty) [p. 120]. ASSUMPTION: excess return over the index proxy over 63 sessions, ranked.
- **Sizing example**: buy Power Grid at Rs. 120 with the stop Rs. 8 below; 1% of a 7-lakh risk capital = Rs. 7,000 → 875 shares [p. 123]. That would be about 15% of capital (875 × 120 = 1.05 lakh), at the book-wide cap. Rule used: shares = 1% of equity ÷ (entry − stop), capped at 15% of equity.
- **Regime**: "works in all type of market trends" [p. 122] yet entries are timed to a recovery after a ≥ 10% correction. ASSUMPTION: base case = any regime; variant = only within 60 sessions after a ≥ 10% index drawdown.

### 2.9 Strategy 9 — Trap the short sellers (short squeeze)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | growth-momentum / event (short squeeze) | 128 |
| Timeframe & holding period | Half within 2.5–8 days; rest trailed; alternative 2.5-week follow | 134 |
| Universe / eligibility filters | Less liquid stocks with heavy short activity; price ≥ Rs. 300; ADTV ≥ Rs. 1 crore; low float; short quantity via open interest ÷ free float | 129–130 |
| Market / regime filter | Confirmed uptrend after a recent correction: major stocks above their 50-day MA and 10/20-day EMAs (Nifty, Midcap, Smallcap); best at market extremes: new multi-year highs, or near lows before reversal | 131–132 |
| Setup conditions | Heavy short positions; F&O expiry days; stocks up > 12% with action after 3:15 pm | 131 |
| Entry trigger & order type | Two points: confirmed uptrend (stock up 50–75% likely to repeat), or oversold after a 50–75% fall | 133 |
| Initial stop-loss | About 0.5% below the entry day's low, or just below the 10-day or 20-day EMA | 133 |
| Exits: profit-taking | First half within 2.5–8 days | 134 |
| Exits: trailing / time / signal | Second half on a close below the 10/20-day EMA; or follow 2.5 weeks and check the third week's range is larger than the first two | 134 |
| Position sizing | Risk ≤ 1% of capital; newcomers ≤ 0.5% | 134 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Stop | 0.5% below entry-day low | below EMA10/20 | 133 |
| Risk | ≤ 1% | 0.5% newcomers | 134 |
| First exit | half within 2.5–8 days | — | 134 |

**Key quotes**

- "A trader must search those stocks which are very less liquid in market trades and very highly active in terms of shorting" [p. 129]
- "If we divide open interest with total free ﬂoat we can get short quantity." [p. 130]
- "The initial stop must be around 0.5% below the lows of the entry day or right below the stock’s 10-day EMA or 20-day EMA." [p. 133]
- "the ﬁrst half of the position can be liquidated in next 2.5 to 8 days" [p. 134]

**Pseudocode**

```
NOT BACKTESTABLE as specified: requires F&O open interest and free-float data (Section 5).
Price-only proxy (label as different strategy): stocks in F&O list, on expiry day t,
  C_t/C_{t-1}-1 >= 0.05 and regime_up; enter C_t; stop 0.995*L_t; half by day +3..+8; rest on close < EMA20
```

**Ambiguities & assumptions**

- **Short interest** is defined as open interest ÷ free float [p. 130], which is not a measure of short positions (OI counts both sides). ASSUMPTION: if OI data are later sourced, use OI ÷ free float as the authors' screen, recorded as their definition.
- **Entry trigger** is not concrete beyond "confirmed uptrend" or "oversold" [p. 133]. Not codable without discretion.

### 2.10 Strategy 10 — Mean reversion (bottom fishing)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion | 134–135 |
| Timeframe & holding period | Swing; target 10–20%; after a market bottom hold ~10 weeks for 50–100% | 139, 166 |
| Universe / eligibility filters | Beaten-down stocks at a multi-month low; stocks that refuse to fall on bad news | 135–137 |
| Market / regime filter | Not in trending markets; range-bound markets where Sensex/Nifty are above their 50 DMA and Midcap/Smallcap below; or after a major correction / bottoming process | 137–138, 166 |
| Setup conditions | Day closes green and at the day's high while at a multi-month low; positive momentum divergence (new low not confirmed by RS indicator) | 135–136 |
| Entry trigger & order type | Buy around the day's end (close) | 136 |
| Initial stop-loss | That day's low | 136, 139 |
| Exits: profit-taking | Target the declining 50-day SMA, or near the 50 or 200 DMA; 10–20% above entry | 136, 139 |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | Risk 0.5–1% of capital | 139 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Low lookback | "multi month" | — | 135 |
| Target | 50-day SMA | 200 DMA; 10–20% | 136, 139 |
| Stop | day's low | — | 136 |
| Risk | 0.5–1% | — | 139 |

**Key quotes**

- "Search for the beaten down stocks which are at multi month low but in a day’s trade closing on greener part as well as at the day’s high." [p. 135]
- "your stop loss to be at the low for the day and target can be declining 50 day simple moving average." [p. 136]
- "Contrarian mean reversal strategy do not work in trending market." [p. 137]
- "Targets for exiting can be around 10 to 20% of buying price." [p. 139]
- "Never try to buy dips in any stock if the stock is making multi month low in general bull market." [p. 140]

**Pseudocode**

```
regime_range_t = (Nifty proxy > SMA50) and (small/mid proxies < SMA50)      # book's range-bound definition
setup_t = L_t <= min(L_{t-126..t-1}) and C_t > O_t and C_t > C_{t-1}
          and (H_t - C_t) <= 0.1*(H_t - L_t)                                # ASSUMPTION: "at the day's high" = close in top 10% of range; 6-month low
          and SMA50_t < SMA50_{t-5} and C_t >= 300 and TV20_t >= 1e7
enter at C_t if regime_range_t; stop = L_t
target = min(SMA50 at entry, entry*1.20); floor target entry*1.10 if SMA50 < entry*1.10   # ASSUMPTION
risk 0.5–1% of equity; time stop 20 sessions (ASSUMPTION)
```

**Ambiguities & assumptions**

- **Regime**: range-bound [p. 137] vs "after a major market correction" [p. 138] vs bottoming process [p. 166]. And "never buy dips … making multi month low in general bull market" [p. 140]. ASSUMPTION: base case only in the book's range-bound regime; variant after a ≥ 20% index drawdown.
- **"Multi month low"** undefined. ASSUMPTION: 126-session (6-month) low; 63-session variant.
- **Target** given three ways (declining 50 SMA; 50 or 200 DMA; 10–20%) [p. 136, 139]. ASSUMPTION: the 50-day SMA at entry, bounded to 10–20%.

### 2.11 Strategy 11 — Support and resistance (range trading)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion (range) | 143 |
| Timeframe & holding period | Daily, swing | 143–147 |
| Universe / eligibility filters | Range-bound/sideways stocks in consolidation or flat base | 145, 147 |
| Market / regime filter | Range-bound market | 145, 165 |
| Setup conditions | Exact (not round-number) support/resistance; a level is usable the first 2–3 times, weak from the 4th test | 144–145 |
| Entry trigger & order type | Buy when price hits previous support and holds; or breaks support then re-enters the range; market orders (limit orders only for large size) | 144–147 |
| Initial stop-loss | A close below the lowest price in the support zone | 146 |
| Exits: profit-taking | Book profit at 2–3× the stop distance; maximum target the upper resistance zone | 147 |
| Exits: trailing / time / signal | If price leaves the range for two consecutive days, find a new range | 147 |
| Position sizing | Risk 1% of total capital per trade | 147 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Valid tests of a level | 1st–3rd | weak from 4th | 145 |
| Reward:risk | 2–3× | max = upper resistance | 147 |
| Range break confirmation | 2 consecutive days | — | 147 |
| Risk | 1% | — | 147 |

**Key quotes**

- "Base or resistance can be easily used for ﬁrst 2-3 times but always remember as a particular base or resistance becomes weak on 4th time onwards." [p. 145]
- "The stoploss must be kept at a close below the lowest price in that support zone." [p. 146]
- "Price of a stock hitting previous support zone and holding it out is always a buy zone." [p. 146]
- "Book your proﬁts when the ratio of price to the stoploss is 2 to 3 times." [p. 147]
- "If the stock crosses the trading range and does it for two consecutive days than we will look for another range bound opportunity." [p. 147]

**Pseudocode**

```
range: over last 60 sessions, R = max(H), S = min(L); require (R/S-1) between 0.08 and 0.25      # ASSUMPTION
       and at least 2 prior touches of S (L within 1.5% of S) and <= 3 prior touches
regime_range_t (as 2.10)
entry: L_t <= S*1.015 and C_t > S  → buy at C_t
       or C_{t-1} < S and C_t > S (false break re-entry)
stop:  exit at next open if C < S_zone_low (= min(L of touches))
target: entry + 2.5*(entry - S_zone_low), capped at R*0.99
abandon range if 2 consecutive closes outside [S, R]
risk 1% of equity
```

**Ambiguities & assumptions**

- **Identifying "exact" levels** is discretionary [p. 144]. ASSUMPTION: rolling 60-session high/low box with a touch count.
- **"ratio of price to the stoploss is 2 to 3 times"** [p. 147] read as reward:risk 2–3. ASSUMPTION: 2.5R; whichever of 2.5R and the resistance comes first.

### 2.12 Strategy 12 — OFS and bulk deals

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | event | 150–151 |
| Timeframe & holding period | 2.5–5 days for ~6%; intraday ~3% | 155 |
| Universe / eligibility filters | Fundamentally sound companies with announced bulk/block deals or government OFS (stake 0.5–5%) | 151–152 |
| Market / regime filter | Not stated | — |
| Setup conditions | Deal announced in advance; stock often grinds lower in the days before the deal | 151, 153 |
| Entry trigger & order type | Buy in the lower part of the deal price range (deals usually at a 4–6% discount to market); alternative: buy as the stock grinds lower before the deal day | 153 |
| Initial stop-loss | 2% below the bulk-deal price (intraday traders: 1% below) | 154 |
| Exits: profit-taking | ~6% in 2.5–5 days; intraday ~3% | 155 |
| Exits: trailing / time / signal | Hold longer while the stock holds its weighted average trading price | 154 |
| Position sizing | Risk 0.5–1% of capital | 154 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Deal discount | 4–6% | "0 to 5%" (Kotak example) | 153 |
| Stop | 2% below deal price | 1% intraday | 154 |
| Target | ~6% in 2.5–5 days | 3% intraday | 155 |
| Risk | 0.5–1% | — | 154 |

**Key quotes**

- "In general the block deals are done below 4 to 6% discount to the current market price of the stock." [p. 153]
- "Under this strategy stop loss will be at 2% below the price of bulk deal" [p. 154]
- "in general we are looking for around 6% gains in 2. 5 to 5 days" [p. 155]

**Pseudocode**

```
NOT BACKTESTABLE with current data: needs NSE bulk/block deal records (date, price, quantity) — see Section 5.
If sourced: on deal day d, buy at deal_price (limit) ; stop deal_price*0.98 ; target entry*1.06 ; time exit d+5
```

**Ambiguities & assumptions**

- **Bulk vs block deals** are used interchangeably [p. 151, 153]. ASSUMPTION: both, plus OFS.
- **Discount** 4–6% [p. 153] vs the Kotak example at "0 to 5%" [p. 153]. Use the actual deal price.

### 2.13 Strategy 13 — Industry (sector) momentum

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | growth-momentum / sector rotation | 156–157 |
| Timeframe & holding period | Swing to weeks/months (sector rotation lasts weeks or months) | 162 |
| Universe / eligibility filters | Best-performing industry; industry leaders with earnings and price-volume action; industries up > 3–5% last week; industry near a breakout | 158 |
| Market / regime filter | Any regime ("You don’t need any speciﬁc market scenario") | 160 |
| Setup conditions | Stock in a hot industry and near a breakout / range contraction | 158, 161 |
| Entry trigger & order type | Breakout to a new 50-day high, or in anticipation; or pullback to a rising 10/20/50-day EMA in an uptrend | 158, 160 |
| Initial stop-loss | 3–4% from the buy price, or per the setup used | 161 |
| Exits: profit-taking | Not stated concretely (hot industry trades can make 50%; un-favoured 8–10%) | 161–162 |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | Risk not more than 1% of capital | 161 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | 15% book-wide | 63 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Industry weekly gain | > 3–5% | — | 158 |
| Breakout | new 50-day high | pullback to rising EMA10/20/50 | 158, 160 |
| Stop | 3–4% | setup's own stop | 161 |
| Risk | ≤ 1% | — | 161 |

**Key quotes**

- "Past week’s performance is important, look for those which are up more than 3 to 5 % in last week." [p. 158]
- "We can either buy them on a breakout to new 50-day highs or in anticipation of a breakout." [p. 160]
- "Just keep the stoploss of 3-4% from your buy price" [p. 161]
- "More than 1% of capital should not be risked in this strategy" [p. 161]

**Pseudocode**

```
industry index I_k = equal-weight mean of member daily returns (needs sector map)
hot_k(week w) = I_k weekly return > 3% and I_k at 50-day high or within 3% of it      # ASSUMPTION
stock in hot_k, rank by 63-day return within industry (top 3 = "leaders")              # ASSUMPTION
entry: C_t > max(H_{t-50..t-1}) → buy C_t; stop entry*0.965; risk 1%
exit: shared template (half +3..+5 days, rest close < EMA20)                           # ASSUMPTION (book silent)
```

**Ambiguities & assumptions**

- **"Industry"** has no definition or data source in the book. ASSUMPTION: NSE industry classification; a current snapshot creates look-ahead for delisted/reclassified names.
- **Exit** not specified [p. 161–162]. ASSUMPTION: shared exit template.
- **"up more than 3 to 5 % in last week"** [p. 158] — stocks or industries? The sentence sits under "ways to identify the leading industries". ASSUMPTION: industry.

## 3. Risk & money-management rules

- **Swing targets/stops (book-wide):** target 8–12%, stop 3–4% [p. 13–14, 33]. Bad markets: target 7–8%, stop 2–3%; positional: target 20–30%, stop 8–10% [p. 33]. "we look for a target of 8-12% and stoploss at 3-4%." [p. 33]
- **Risk/reward:** about 1:3 [p. 13, 34]; time dimension: hold winners 3–9 or 7–21 days, losers 1–3 or 1–7 days [p. 34].
- **Risk per trade:** 0.5–1% of capital for most setups [p. 53–54, 61, 71, 93, 139, 154]; 1% max [p. 84, 100, 123, 147, 161]; 0.5% for newcomers on short squeezes [p. 134].
- **Regime-scaled risk (closing chapter):** bullish (Nifty, Midcap and Smallcap above the 50 EMA): 0.5–1%; range-bound: cut to 0.25–0.50%; bearish (all three below the 50 EMA): mostly cash, no breakouts [p. 165–166]. "at this stage the risk capital must be reduced to .25% - .50% from 1% level." [p. 165]
- **Concentration:** "never put more than 15% of your capital in a single stock" [p. 63]; Strategy 3 caps at 20% [p. 72] (see ASSUMPTION in 2.3).
- **Averaging:** average up only, with a revised trailing stop; never average down [p. 54–55].
- **Leverage:** avoid over-leverage [p. 63, 170].
- **Stops are mandatory:** "Stop loss is the most important" [p. 167].

**Regime → strategy map** [p. 165–166]: Bullish → IPO, volume blast, breakout. Range-bound → wait for quarterly results (PEAD) and support/resistance. Bearish → cash. Bottoming → mean reversion (hold ~10 weeks) and relative strength.

## 4. Non-codable guidance

- Pick the strategy to fit the market phase; sit out when unsure [p. 62, 166].
- Expect to be wrong up to 50% of the time even in bull markets; a minority of trades make most profit ("Twenty percent of your trades") [p. 53, 63].
- Look for the reason behind volume (news, re-rating) and avoid "false alarms" [p. 50–51, 54].
- For PEAD, follow the market's reaction, not your own reading of the results [p. 110].
- Post-trade review questions (did the strategy fit the market, was the entry good, was the stop honoured) [p. 72–73].
- Take breaks; trading every day is not necessary [p. 169].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV (all setups); volume averages (S1, S2, S5, S7); 10/20/50/200-day EMAs/SMAs (all); index levels for Nifty, Bank Nifty, Midcap, Smallcap (regime); listing dates (S4, from first bar); earnings announcement dates (S7); F&O open interest and free float (S9); bulk/block/OFS deal records (S12); industry classification (S13).
- **Testability with our data:**
  - Backtestable 2005–2026 on prices: S1, S2, S3, S4, S5, S6, S8, S10, S11, and S13 if a sector map is added.
  - S7 needs earnings dates; without them only the price/volume event proxy can be tested (a different strategy).
  - S9 and S12 need data we don't have (OI/free float; bulk-deal records). Not testable as specified.
  - Regime: Nifty only from 2024. ASSUMPTION: use NIFTYBEES (or an equal-weight index of the top 50 by trailing 1-year traded value) for "Nifty"; equal-weight indices of rank 101–250 and 251–500 by trailing traded value for "Midcap" and "Smallcap"; Bank Nifty proxy = equal-weight of the panel's largest banks by traded value.
  - No fundamental filter is required by any setup, so the Feb-2026 fundamentals are not needed. The "fundamentally sound" remarks (S5, S12) are discretionary.
- **Market-structure differences:**
  - The book is written for NSE, so the Rs. 300 price floor and Rs. 1 crore turnover floor apply directly. ASSUMPTION: apply the Rs. 300 test to unadjusted prices if available (adjusted historical prices understate pre-split levels); inflation-adjust neither.
  - Long-only fits the cash market; the book's short ideas (bearish phase "or short" [p. 165], breakdown candidates [p. 138]) are excluded.
  - Circuit limits: skip entries on upper-circuit days (no fill) — matters for S1 (>5% days) and S4 IPOs. ASSUMPTION: treat a close equal to the high with a gain ≥ the stock's band minus 0.5% as unfillable.
  - Costs: STT, brokerage, ~0.1% slippage per side. With 3–4% stops and 5–8% targets (S5, S12), costs take a meaningful share of each trade; report results net.
  - Intraday/first-half entries (S5, S7, S12) are approximated by open/close fills.

## 6. Verdict

- **Codeability:** Partly. Nine setups are fully rule-based on daily prices once the book's vague terms are pinned down; S7 needs earnings dates; S9 and S12 need data we don't have.
- **Priority for backtesting:** Medium. It is written for NSE with explicit Indian filters and risk numbers, and S2/S3/S7 are standard, testable swing setups; but there is no evidence offered and many thresholds are ranges.
- **Top 3 things a coder is most likely to get wrong**
  1. The shared exit: half the position after 2.5–5 days *only if* in profit (S1) or unconditionally (S2/S3/S7), and the remainder on a **close** below the EMA (not an intraday touch).
  2. The regime filter: it uses three indices (large, mid, small) above their 50-day average, not just the Nifty, and pre-2024 needs proxies; risk is scaled down to 0.25–0.5% in range-bound markets.
  3. Applying the Rs. 300 floor on split-adjusted prices, which wrongly excludes stocks that later split.
