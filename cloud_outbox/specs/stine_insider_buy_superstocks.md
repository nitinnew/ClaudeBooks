# Insider Buy Superstocks — Jesse C. Stine (self-published, 2013)

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/insider-buy-superstocks-by-jesse-stine LifeFeeling.pdf` (file id `1yH0jaqoceZCKJanhApZnuTB1UzedPRTO`, 5,034,655 bytes), 250 PDF pages with a text layer (pp. 1–2 and 250 are blank or cover images).
- **Text file used:** text/stine_insider_buy_superstocks.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file. The book's printed page numbers coincide with the PDF index here, but always take N from the marker.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use the table of contents (its numbers are offset).
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/stine_insider_buy_superstocks.md text/stine_insider_buy_superstocks.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 250]]. Chapters 1–5 (biography, media, manipulation and psychology) and Chapters 13, 14 and 16 are narrative. Their few rules (no day trading, no pyramiding, liquidity, cash in "winter") are captured in sections 3–4. Chapter 12 (case studies, pp. 154–184) and Appendices A–C (alerts and forecasts, pp. 204–249) were read in full; their numeric rules (price-target formula, Dow vs 34-week MA stretch, "canary" momentum-stock signal) are included. Chart images are not readable; their text annotations were.

## 1. The method in brief

Stine's "Superstock" method is an O'Neil-derived, weekly-chart small-cap momentum approach [p. 79–104, 152–153]. It works in four steps:

1. **Find candidates.** Look for a stock whose earnings jumped ("earnings winner"), at an annualised P/E ≤ 10, under $15, with a low float and ideally recent open-market insider buying, breaking out of a long base on 500–5,000% weekly volume above its 30-week MA.
2. **Don't buy the breakout.** Wait for a low-risk weekly entry:
   - a "light and tight" week on the stock's **magic line** (its best-fitting weekly MA, usually the 10-week);
   - a test of the earnings gap;
   - 2–3 weeks after the earnings breakout;
   - the lower trendline.
3. **Size by conviction (Kelly).** Never pyramid upward.
4. **Exit on a stack of sell signals:**
   - 7–10 weeks after a magic-line thrust, or ≥ 60% above the magic line;
   - 9 months into the advance;
   - a parabolic run or the largest weekly range;
   - a weekly exhaustion gap;
   - the first weekly close below the magic line;
   - $25–30;
   - an offering, a split, or a sequential earnings decline.

His track record (Oct 2003–Jan 2006, $45,721 → $6.85M) is self-reported, with prior drawdowns of 61–106% [p. 7, 14]. No systematic backtest is given.

## 2. Strategies

### 2.1 Superstock earnings-breakout: screen, low-risk weekly entry, sell-signal exit

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | small-cap momentum / earnings breakout (long) | 79–153 |
| Timeframe & holding period | Weekly charts. Typical advance 9–12 months; longest hold during his run was 8 months | 11, 79, 114 |
| Universe / eligibility filters | Price < $15 at breakout (sweet spot $3–15; $4–10 best; < $4 rarely); float < 10M (best 4–8M); market cap < $100M at the start; ≥ 12 months listed (avoid IPOs); avoid commodity producers; low debt; short interest < 20%; no secondary offering in the last 6 months; liquid enough to exit | 84, 95, 98, 101, 104, 192, 198 |
| Technical "must haves" at breakout | (1) Long strong base; (2) break above (or hold above) the 30-week MA; (3) weekly volume up 500–5,000%; (4) steep ~45° "angle of attack"; (5) under $15. Plus: clean, orderly chart (no single-day 30% drops); a prior momentum leader; respecting its magic line | 79–87 |
| Fundamental "dirty dozen" | Earnings jump after flat quarters; sustainable (new product, backlog, guidance); annualised P/E (quarterly EPS × 4) ≤ 10; sequential improvement; easy YoY comps; operating leverage; rising backlog; open-market insider buys by several officers or directors (not token, option or post-disaster buys); low float; a new "super theme"; conservative management; a simple blockbuster EPS headline | 88–97 |
| Price target | Quarterly EPS × 4 × 20 P/E (momentum can carry it to 30–40 P/E). Take only trades with ≥ 100% potential | 105, 158, 162 |
| Entry (low-risk weekly) | Do not chase the breakout. Buy: (a) the **magic line** (best-fitting weekly SMA, usually 10-week; hit every 10–12 weeks); (b) **"BLT" buy light and tight**: 1–3 weeks of near-identical closes with volume down to 30–50% of peak, ideally on the magic line; (c) the **earnings-gap test**; (d) **2–3 weeks after** the earnings breakout; (e) the **lower trendline** of the up-channel; (f) early in the advance (first months). Also: 10/20-day MA in strong runs; a rising 50-dma/10-wma meeting a base | 87, 107, 111–122 |
| Initial stop-loss | No fixed %; decided in advance from volume, price and volatility. Logically just below the base or gap; downside = distance to base support (e.g., $1 on an $11 breakout from a $10 base) | 105, 141 |
| Position sizing | Kelly-style: larger with higher conviction and skew. He concentrated up to 90% in 1–2 stocks (not recommended). Margin only in a separate 5–10% "experimental" account, max 2:1, and only when several positions sit at low-risk entries | 123–125 |
| Adding | Add at the next low-risk entry (magic line / BLT), never as price extends: no pyramiding | 190, 200 |
| Exits: technical (sell when several coincide) | ≥ 60% above the magic line after week 6; 7–10 weeks since the last magic-line thrust; 9–15 months since breakout (out at 9 months on a big gain); flattening or declining magic line after 6+ months; **first weekly close below the magic line**; 4th–5th surge off the magic line; parabolic run (largest daily move, far above the 5-dma, or a break of the 5-dma); largest weekly range on high volume; close back below the lower channel; wide, volatile closes when extended; weekly exhaustion gap; $25–30 price; 3 higher highs in 4–5 weeks; peers weakening; close back below the upper trendline; first close back inside the upper Bollinger Band | 130–144, 153 |
| Exits: fundamental | Price target hit; secondary offering or private placement; an EPS quarter meaningfully below the prior quarter; stock split; insiders selling most of their stake; media headlines; message-board euphoria; capacity expansion; confusing or one-off earnings; tax-loss reversal; pre-earnings euphoria; fluff PRs; stock advertising; "strategic alternatives" | 144–151, 153 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Price at breakout | < $15 | $3–15 band; $4–10 sweet spot | 79, 84, 198 |
| Annualised P/E | ≤ 10 (EPS_q × 4) | above 10 acceptable | 90 |
| Float | < 10M shares | 4–8M best | 95 |
| Market cap | < $100M | — | 95 |
| Breakout weekly volume | +500% to +5,000% vs base | — | 82 |
| Magic line | 10-week SMA | 5–30-week SMA fitted per stock (examples: 9, 13–17, 19, 30) | 87, 196 |
| BLT volume | 30–50% of peak weekly volume | 1–3 tight weeks | 113 |
| Post-earnings wait | 2–3 weeks | — | 116 |
| Target | EPS_q × 4 × 20 | P/E 30–40 at the peak | 105 |
| Extension sell | ≥ 60% above the magic line (after week 6) | 100% | 130 |
| Thrust sell | 7–10 weeks after a magic-line touch | — | 130 |
| Age sell | 9 months on a big gain | 9–15 months | 131 |
| Price sell | ~$25 | $25–30 | 141 |
| Post-offering wait | ≥ 6 months | — | 104, 145 |
| Experimental margin account | 5–10% of the portfolio, ≤ 2:1 | — | 124–125 |

**Key quotes**

- "at breakout, a killer Superstock will 1) be under $15, 2) break out of a strong base, 3) break out above its 30 week moving average, 4) show massive weekly volume, and 5) show a steep angle of attack." [p. 79]
- "volume will typically expand 500% to 5,000% and will remain at elevated levels for months on end." [p. 82]
- "The “Mack Daddy” ultimate support level or “magic line” for a Superstock generally is near its “10 week simple moving average” (10 wma)." [p. 87]
- "most Superstocks hit their magic line or 10 week moving average at least once every 10 to 12 weeks." [p. 87]
- "I had the good fortune of entering many of my biggest winners when their price to earnings “run rate” (quarterly EPS x 4) was 10 or less." [p. 90]
- "I would never, ever buy a stock simply because it has insider buying alone." [p. 94]
- "The best performing stocks generally have floats under 10 million shares." [p. 95]
- "I like to see at least 12 months of trading history before I consider investing in a stock." [p. 101]
- "my rule of thumb is to wait at least 6 months before a potential purchase." [p. 104]
- "based on a price/earnings multiple of 20, you determine that your target price is $28" [p. 105]
- "Ideally, we want to see volume decline to roughly 30%-50% of the peak volume seen during its biggest advancing weeks." [p. 113]
- "The best low risk entry points are when the stock apparently goes absolutely nowhere for 1-3 weeks on very little volume when compared to prior weeks." [p. 113]
- "The average high quality momentum stock will have a 9-12 month advance out of its base." [p. 114]
- "What we do know is that there is often a great low-risk entry 2-3 weeks after the breakout gap." [p. 116]
- "If your stock trades below the 50 dma for more than a week or two, it very well could be a dud." [p. 121]
- "if your chosen stock trades 60% or more above its magic line (possibly 10 wma or 50 dma) anytime after the first six weeks of its initial breakout, it may be time to take some chips off the table" [p. 130]
- "the strongest stocks hit an intermediate term peak no later than 7 to 10 weeks later." [p. 130]
- "if I’m sitting on a big gain at the 9 month mark, I’m out." [p. 131]
- "If your stock closes below the magic line at the end of the week for the first time, I would most likely sell and only re-enter if and when it rises back above the line." [p. 133]
- "if I missed 1 and 2, I would sell once the stock broke below its 5 day moving average." [p. 134]
- "Personally, I don’t have a “standard” stop loss." [p. 141]
- "it is probably a sensible idea to dump it if it trades anywhere close to $25." [p. 141]
- "The instant your company announces earnings that are meaningfully BELOW the previous quarter, SELL." [p. 145]
- "I would not consider adding risk as the positions moved higher." [p. 190]

**Pseudocode** (weekly bars, with daily data for earnings and gap dates)

```
# --- screen (evaluated on the earnings-breakout week w0) ---
eps_jump: EPS_q0 >= 1.5*max(EPS_q-1..q-4) and EPS_q-1..q-4 roughly flat (stdev/mean < 0.3)   # ASSUMPTION "jump after consistent quarters"
pe_run  : C_w0 / (4*EPS_q0) <= 10
price   : C_w0 < 15 (NSE ASSUMPTION: Rs.30-500 band, see s.5)
float   : free_float_shares < 10e6 (NSE ASSUMPTION: free-float mcap < Rs.500 cr)
base    : >= 12 weeks with (max H - min L)/min L <= 35% before w0     # ASSUMPTION for "long strong base"
volume  : V_w0 >= 5*SMA(V_weekly,10 before w0)
ma30    : C_w0 > SMA(C_weekly,30)
listed  : >= 52 weeks ; no equity offering in last 26 weeks
insider : open-market buys by >= 1 officer/director in last 26 weeks (bonus; not required)
target  = 4*EPS_q0*20 ; require target >= 2*C_w0

# --- magic line: per stock, choose n in [5..30] maximising weekly closes >= SMA(n) with touches since w0 (fit on data up to entry only) ---
# --- entries (first that triggers within 26 weeks of w0) ---
gap_test : weekly low <= earnings-gap top and close > gap bottom           (weeks 1..8)
post_wait: weeks 2-3 after w0 and weekly range < 0.6*avg range of w0..w0+1
BLT      : last 2 weekly closes within 2% of each other and V_w <= 0.5*max(V since w0) and L_w <= 1.03*MagicLine
buy at weekly close ; stop = min(base support, MagicLine*0.93)   # ASSUMPTION: book gives no fixed stop
# --- exits (sell all when any 2 technical signals coincide, or any 1 fundamental) ---
ext   : C >= 1.6*MagicLine and weeks_since_w0 > 6
thrust: weeks since last magic-line touch >= 7 and C at new high
age   : weeks_since_w0 >= 39 and gain >= 100%
close_below_ml: first weekly close < MagicLine after >= 8 weeks above   # single-signal exit
climax: weekly range = max since w0 and V_w >= 2*SMA(V,10)
gap_ex: weekly open > prior weekly high by >= 3% while C >= 1.4*MagicLine
price : C >= 25 (NSE: >= 6x entry, ASSUMPTION mapping $4->$25)
fund  : EPS_q < EPS_q-1 materially (<-10%) ; equity offering ; split/bonus announced ; promoter sells > 50% of holding
no pyramiding above entry; re-entry only at the next BLT/magic-line setup
```

**Ambiguities & assumptions**

- "Long base", "steep angle", "clean chart", "super theme" and "conservative management" are qualitative. The thresholds above are assumptions.
- The magic line is fitted per stock by trial and error [p. 87]. To avoid look-ahead, fit only on data before each decision and cap the candidate periods.
- No fixed stop; the author sells when several sell signals trigger at the same time [p. 130]. ASSUMPTION: two concurrent technical signals, or one decisive one (first weekly close below the magic line).
- The $15/$25/$30 thresholds are US-dollar and nominal. They encode "low price, big % move" and a psychological ceiling, and must be translated for NSE (section 5).

### 2.2 "BCD" three-lower-lows dip buy in an uptrend (with lower-Bollinger re-entry); mirror sell signals

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | pullback mean reversion inside a multi-month uptrend | 118–119, 141, 144 |
| Setup | Stock (or market) in a multi-month uptrend makes three lower lows within ~4–5 weeks, the third ideally below the trend of the first two ("Buy, Cry, Die"). Hammer reversals are a plus | 118 |
| Alternative trigger | A sharp drop below the lower Bollinger Band, then the first daily close back above the lower band | 118–119 |
| Entry | At the third low / the first close back inside the band | 118 |
| Mirror sell | 3 higher highs within 4–5 weeks (third above the trend of the first two); the first close back inside the upper Bollinger Band after trading outside it | 141, 144 |
| Exit | Not specified beyond the 2.1 sell rules | — |

**Key quotes**

- "My rule of thumb is to look for a stock (or the market) to make three lower lows with the third low ideally even slightly below the trend of the first two." [p. 118]
- "a sharp pullback below a stock’s lower Bollinger Band followed by the first daily close ABOVE its lower Bollinger Band can be a great entry point." [p. 118]

**Pseudocode**

```
uptrend: C > SMA(C,200) and SMA(C,50) > SMA(C,200)   # ASSUMPTION for "multi-month uptrend"
BCD: three swing lows (5-bar pivots) L1 > L2 > L3 within 25 sessions and L3 < line(L1,L2) extrapolated
     buy at close of first up day after L3 ; stop = L3*0.98 (ASSUMPTION)
BB : prior day C < BB_lower(20,2) and today C > BB_lower -> buy at close
exit: 10 sessions or C > BB_mid(20) or 2.1 sell signals (ASSUMPTION)
```

### 2.3 "Canary in a coal mine" and index-stretch market-risk filter

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | market timing / risk-off filter | 204–207, 213–221 |
| Canary signal | A dozen or so "in play" momentum leaders fall hard together while the index holds or rises. Expect a market drop within 1–6 sessions; get defensive | 204, 216–220 |
| Stretch signal | Dow 750–1,200 points above its 34-week MA has preceded every major correction since 2009 (examples: +1,000 → −800; +850 → −1,300; +1,150 → −900) | 205, 213–214 |
| Leaders | The SOX index leads the market intraday and at turns; global markets (China, India, Brazil) signal turns before the US | 206 |
| Bottoms | Former leaders build low-level bases while the index falls; sentiment extremes (put/call, VIX, newsletter shorts, media "crisis" crescendo, Drudge finance headlines) | 53–54, 205, 207 |
| Regime ("seasons") | Ideal "springtime" conditions occur < 10% of the time; otherwise hold cash | 126 |

**Key quotes**

- "There’s a good chance that the rest of the market will follow suit sometime within the next 1-6 market sessions." [p. 204]
- "EVERY SINGLE time it gets stretched 750-1,200 points ABOVE its 34 week moving average, a major crash comes out of nowhere to surprise everyone." [p. 205]
- "I would say that these springtime conditions are present less than 10 percent of the time." [p. 126]

**Pseudocode**

```
leaders = top-12 stocks by 26-week return with ADV >= threshold (proxy for "momo stocks in play")
canary(d): median(1-day return of leaders) <= -4% and index 1-day return >= -0.3%   # ASSUMPTION thresholds
           -> no new longs for 6 sessions; tighten stops to the 10-dma
stretch(w): (C_idx - SMA(C_idx,34 weeks)) / SMA34 >= 7%   # 750-1,200 Dow points ≈ 7-10% of Dow 10-13k in 2010-11 (ASSUMPTION conversion)
           -> no new longs until C_idx <= SMA34*1.03
```

## 3. Risk & money-management rules

- Decide the downside before entry; buy only where the downside to base support is small relative to a ≥ 100% target (e.g., 17:1) [p. 105].
- No pyramiding as the price rises. Leverage only in a separate 5–10% account, at most 2:1, and only at low-risk entries [p. 124–125, 190].
- Liquidity: never enter a stock you cannot exit quickly. If stuck, sell steadily (his Fuwei Films loss was $675,824) [p. 192].
- No day trading, no options, no index ETFs for the core strategy, no revenge trades [p. 189, 191, 193].
- Hold cash when there are no fat pitches; ideal conditions occur < 10% of the time [p. 126, 197].
- Ignore account fluctuations; don't watch intraday [p. 65–66, 127].

## 4. Non-codable guidance

- Avoid the mass media and groupthink; headlines are a contrarian sentiment gauge [p. 44–54].
- Talk to management at small companies; read 10-Qs and earnings-call Q&A for sustainability clues [p. 89–90].
- Message-board quality: quiet and informed is good; euphoric is a sell signal [p. 100, 147].
- The "it factor" or super theme, and a memorable ticker [p. 95–98].
- Visualise the worst case before entering; stay disciplined; exercise and diet (Ch. 5) [p. 59–70].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - weekly and daily OHLCV;
  - quarterly EPS (standalone and consolidated) with result dates;
  - free float or promoter holding (shareholding pattern);
  - insider/promoter open-market purchases (SEBI PIT disclosures, Reg 7(2) / SAST);
  - corporate actions (QIP/preferential/rights issues, splits, bonuses);
  - market cap.
- **Testability with our data:** 2.1 is testable from about 2010 if quarterly EPS and SEBI insider-trading disclosures are available. Without insider data, run it as the "bonus" variant (insider buying is not required [p. 94]). 2.2 and 2.3 are fully testable on price data.
- **Market-structure differences:**
  - **Price filters:** NSE prices are not comparable to US dollar prices. Replace "< $15" with a market-cap filter: free-float market cap < Rs. 500 crore. Use a minimum price of Rs. 20 to avoid illiquid penny stocks (ASSUMPTION).
  - **Exit at "$25–30":** replace with "≥ 5–6× the entry price".
  - **Insider buying:** promoter open-market purchases (and creeping acquisitions) are the analogue. Exclude inter-se promoter transfers and pledge invocations, the same kind of exclusion the book makes for related-party transfers [p. 94].
  - **Offerings:** QIPs and preferential allotments are the analogue of secondary offerings. Apply the 6-month exclusion [p. 104].
  - **Circuit limits:** 5–20% bands on small caps. Earnings breakouts may print as locked upper circuits; entries come on the gap-test or "2–3 weeks later" rules anyway.
  - **Liquidity:** require 20-day median traded value ≥ Rs. 1 crore (ASSUMPTION), given the book's own illiquidity loss [p. 192].

## 6. Verdict

- **Codeability:** Partial. The screen (P/E run-rate, earnings jump, float, price, volume surge, 30-week MA, insider buys), the entries (BLT, gap test, 2–3-week wait, magic line) and most sell signals can be quantified. "Base quality", "super theme", management quality and the per-stock magic-line fit are discretionary.
- **Priority for backtesting:** Medium. It is a rich, mostly codeable small-cap earnings-momentum system with a distinctive exit set (time-since-thrust, % above MA, 9-month age, first weekly close below the MA). It fits NSE small caps if fundamentals and insider data are available. The author's results are anecdotal and survivorship-heavy.
- **Top 3 things a coder is most likely to get wrong**
  1. Buying the breakout week. Stine explicitly waits for a low-risk weekly entry: BLT (tight closes, volume at 30–50% of peak), magic line, gap test, or 2–3 weeks after earnings [p. 107, 113, 116].
  2. Fitting the magic-line MA period using the whole history (look-ahead). Fit it only on data up to the decision point, or default to the 10-week SMA [p. 87].
  3. Using a single trailing stop instead of the signal stack: ≥ 60% above the magic line after week 6, 7–10 weeks after a thrust, the 9-month age limit, the climax range, an exhaustion gap, and the first weekly close below the magic line [p. 130–134, 153].
