# BREAKOUT Signals in Descending Channels (Drive title: "How to See a Breakout, before it…") — Sudhir Dixit

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/How to See a Breakout, before i - Dr.Sudhir Dixit.pdf` (file id `1fngYQ6i2tUf8kUJr79cONsFkmMMwIwY2`, 5,958,037 bytes; self-published, © 2020 Sudhir Dixit [p. 4])
- **Text file used:** text/dixit_see_breakout_before.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter. (This ePub-style PDF has no printed page numbers.)
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/dixit_see_breakout_before.md text/dixit_see_breakout_before.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 171]]. Pages 1–3 are cover images with no text. All charts are images; their trendlines, RSI values and volumes are only available where the text describes them. The "Table of Breakout Data" [p. 121–129] is extracted as broken columns but readable (20 stocks, daily/weekly RSI, volume comment). Appendix (Nifty 50 / Sensex member lists, 2020) [p. 162–170] read; contains no rules.

## 1. The method in brief

The book teaches one pattern, the **descending channel** (two parallel down-sloping trendlines through lower highs and lower lows), and one indicator, **RSI**, plus volume [p. 8]. The author argues the range inside a descending channel is mostly not worth trading for a long-only trader ("The best way to trade a descending channel range is not to trade it." [p. 58]) and that the money is in the **breakout** above the upper trendline, ideally anticipated by four "secret signals" (price swing failure, RSI cycle failure, double breakout, RSI divergence) so the trader can buy near the support line and still exit in profit if the breakout fails [p. 137, 153]. Breakout validity is judged by volume (double or more) and by the pre-breakout RSI (daily 50–70, weekly 40–60) [p. 76, 128]. Profit target is the channel width added to the breakout price (1:1) [p. 155–156]. Timeframes: direction from the monthly chart, price points from the weekly chart, sub-patterns from the daily chart [p. 64–65]. Designed for Indian equities (Nifty 50 focus for beginners [p. 49]), with US 15-minute/60-minute charts used for the signal chapter [p. 138–152].

Evidence: a hand-collected table of 20 Indian breakouts (pre-breakout RSI and volume, not returns): average daily RSI 58.5 and weekly RSI 49; 75% of breakouts had daily RSI 51–70 [p. 128–129]. The author claims anticipation works with "approximately 70% success rate" [p. 130], without a test. No backtest or P&L statistics.

## 2. Strategies

### 2.1 Descending channel breakout (confirmed)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout (trend reversal out of a downtrend) | 74–75 |
| Timeframe & holding period | Daily, weekly or monthly channels; hold until 1:1 channel-width target; weak breakouts: take quick profits | 95, 155, 159 |
| Universe / eligibility filters | Price ≥ Rs. 10 (no penny stocks); liquid: daily volume > 5 lakh shares; beginners: Nifty 50 / Sensex stocks; avoid low-volume, thinly traded stocks (irregular channels) | 48–49, 115, 161 |
| Market / regime filter | "The breakout should be in a bullish market" | 76 |
| Setup conditions | Descending channel with at least four contact points (two highs, two lows); not steep, not narrow; wide enough that price "should not show any urgency"; volume should decrease as the channel forms; longer channels give stronger breakouts (two months weak, two years strong) | 55–57, 75, 85, 161 |
| Entry trigger & order type | Price breaks above the resistance trendline with volume ≥ 2× normal (large caps; "some people" use +50%); small/mid caps 3–4×; volume must stay high for a few candles after; confirm by waiting for the close, or for the retest of the broken line (usually 2–3 days later, on low volume) and buy when price rises after it | 75–76, 84–85 |
| Initial stop-loss | Not specified as a level; "Calculate your stoploss. If the channel does not go your way, book loss." | 160 |
| Exits: profit-taking | Target = channel width (support-to-resistance price difference) + breakout price; "rather safe to be satisfied with 1:1" | 155–156 |
| Exits: trailing / time / signal | If RSI > 60 and volume ≥ 2× at breakout, may hold for more; if not, book profit immediately on the breakout; red candle on rising volume after breakout = weakening | 76, 153–154 |
| Position sizing | Beginners: trade 10% of intended capital, Rs. 1,000 per trade out of Rs. 10,000 (i.e. 10% of the trading account); Seykota quote: risk less than 1% per trade | 158–159 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Max 3 trades at a time; initially one channel each on monthly, weekly and daily charts | 158–160 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Breakout volume | ≥ 2× normal (large caps) | +50% ("some people"); 3–4× small/mid caps | 76 |
| Pre-breakout daily RSI | 50–70 | 51–70 covered 75% of examples; best "more than 60 and less than 70" | 128–129, 144 |
| Pre-breakout weekly RSI | 40–60 | average 49 in the 20 examples | 128 |
| Channel contact points | ≥ 4 (2 highs, 2 lows) | — | 161 |
| Retest timing | 2–3 days after breakout | not all breakouts retest | 85–86 |
| Target | channel width added to breakout price (1:1) | more if breakout strong | 155 |
| Reward:risk | 1:4 "due to brokerage and slippage" | — | 161 |
| RSI history | ≥ 150 candles | — | 106 |

**Key quotes**

- "The key factor is that volume should be high on breakout and it should remain high even after breakout for a few candles." [p. 75]
- "Usually the volume should be double or more for a valid breakout." [p. 76]
- "In largecaps, double volume is expected, though some people recommend that it should be 50% above its normal volume, whereas in small or midcaps, volume can be 3-4 times usual volume." [p. 76]
- "we can conclude that daily RSI should be ideally above 50 and below 70 (in the range of 50-70) on the pre-breakout candle." [p. 128]
- "Likewise we find that Weekly RSI should be ideally in 40-60 range on the pre-breakout candle." [p. 128]
- "Usually, the stock price tests the previous resistance level after 2-3 days." [p. 85]
- "Channel breakout target = The price range difference of the channel + Price at breakout point" [p. 156]
- "Always keep a risk-reward ratio of 1:4 due to brokerage and slippage." [p. 161]
- "Channels need at least four contact points, two of which are lows connected to each other and two of which are highs connected to each other." [p. 161]

**Pseudocode** (daily bars; weekly bars resampled Fri close; `RSI = Wilder RSI(14)` — period not stated, see Ambiguities)

```
# channel detection (book draws by hand; this is the coder's approximation)
pivots: swing high at t if H_t = max(H_{t-k..t+k}); swing low likewise, k = 5 (daily) / 3 (weekly)   # ASSUMPTION
over a window W (60–500 daily bars; ≥ 40 bars):                                                    # ASSUMPTION
  upper line U(t) = a_U + b*t fitted through ≥2 descending swing highs; lower L(t) = a_L + b*t (same slope b < 0) through ≥2 swing lows
  require: b < 0; all closes in window within [L(t)*0.97, U(t)*1.03]; touches ≥ 2 each side
  width_pct = (U(t)-L(t))/L(t) ∈ [0.10, 0.40]          # ASSUMPTION: not narrow, not huge
  slope_pct_per_bar = -b / C ≤ 0.004 (daily)            # ASSUMPTION: "not steep"
  vol trend: SMA(V,20) at window end < SMA(V,20) at window start   # volume should decrease while channel forms
breakout on day t:
  C_t > U(t) and C_{t-1} <= U(t-1)
  V_t >= 2 * SMA(V,20)_{t-1}  (variant: 1.5x; 3x for non-Nifty-100 names)
  50 <= RSI_d(t-1) <= 70  and  40 <= RSI_w(last completed week) <= 60
  regime: index proxy close > SMA50                     # ASSUMPTION for "bullish market"
  liquidity: SMA(V,20) >= 5e5 shares and C >= 10
entry A (close confirm): buy at C_t
entry B (retest): within t+1..t+5, if L <= U(t)*1.01 and close > U and V < V_t → buy next open
target = breakout_price + (U(t) - L(t))          # width measured at the breakout bar
stop   = ASSUMPTION: close back below L-line midpoint, i.e. close < (U(t)+L(t))/2 ; variant: close back inside channel (C < U)
weak-breakout rule: if RSI_d(t) < 60 or V_t < 2*SMA20 → exit at close of t+1 (book "book profit immediately")
size: risk 1% of equity on (entry - stop), cap 10% of equity; max 3 open positions
```

**Ambiguities & assumptions**

- **RSI period** is never given; the author tells readers to use Investing.com's RSI because "RSI readings are different on different softwares" [p. 18, 151]. ASSUMPTION: Wilder RSI(14), the usual default.
- **Channel drawing** is discretionary ("Charts are open to subjective interpretation" [p. 110]; draw on weekly/monthly then copy to daily [p. 104]). ASSUMPTION: pivot-based parallel-line fit as above; this is the largest source of implementation variance.
- **Stop-loss level** is not given [p. 160]. ASSUMPTION: close below the channel midline after entry; variant: close back inside the channel. Note the author's own example HDIL fell to Rs. 2 without a stop [p. 160–161].
- **"Normal" volume** is undefined; one example uses a "10 Day MA of volume" [p. 114] and another a "two week average" [p. 78]. ASSUMPTION: 20-day SMA; 10-day as a variant.
- **Volume multiple contradiction:** "double or more" [p. 76, 84] vs "+50%" alternative and 3–4× for small/mid caps [p. 76]. ASSUMPTION: 2× base; test 1.5× and 3×.
- **RSI band:** table conclusion 50–70 daily / 40–60 weekly [p. 128], vs. "RSI's best level at the time of breakout should be more than 60 and less than 70" [p. 144], vs. "during breakouts RSI near or above70 is considered good" [p. 89]. ASSUMPTION: 50–70 on the pre-breakout candle (the only rule derived from the author's data).
- **Bullish market** is not defined [p. 76]. ASSUMPTION: index proxy above its 50-day SMA.

### 2.2 Anticipatory entry at the support line (four "secret signals")

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion entry inside a channel, aiming for a breakout | 137 |
| Timeframe & holding period | Same channel timeframes; hold to breakout, then per 2.1 | 137, 153–154 |
| Universe / eligibility filters | As 2.1 | 48–49 |
| Market / regime filter | Not stated separately | — |
| Setup conditions | Price in a descending channel and at least one (preferably two) of: **(1) Price swing failure** – price reverses before touching the support line and heads back to resistance (moderate); **(2) RSI cycle failure** – RSI reverses from ~40 instead of reaching 30 (moderate); **(3) Double breakout** – price breaks below support, re-enters the channel, then breaks above resistance (high); **(4) RSI divergence** – price makes a fresh low but RSI does not (high). A double bottom inside the channel, or reversal candles (morning star, abandoned baby, doji star, dragonfly doji, inverted H&S) at the support line, add confirmation | 132–154 |
| Entry trigger & order type | "prepare yourself for the breakout and enter the stock near support line"; trade only signals 3 and 4, preferably in combination; don't buy while the price is still falling: "Let it stop and move up" | 67, 137, 153 |
| Initial stop-loss | Not stated as a level; morning star invalid if price makes a low below the second candle; abandoned baby invalid if price closes below it | 133–134, 160 |
| Exits: profit-taking | If no breakout: sell near the resistance line (in profit because bought at support); in weak (descending) stocks take profit when RSI reaches 60; if breakout: per 2.1 | 63, 137, 153–154 |
| Exits: trailing / time / signal | On breakout with RSI > 60 and volume ≥ 2×: hold for more; otherwise book profit on the breakout | 153–154 |
| Position sizing | As 2.1 | 158 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | As 2.1 | 158–160 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Signals traded | Double breakout, RSI divergence | all four; combinations preferred | 153 |
| RSI cycle-failure floor | reverses from ~40 (not 30) | ceiling 60 = weakness | 142 |
| RSI overbought in weak stocks | 60 | 70 normal | 63 |
| Claimed success | ~70% | — | 130 |

**Key quotes**

- "Whenever you see these signals, especially the signal of RSI divergence, prepare yourself for the breakout and enter the stock near support line." [p. 137]
- "If the price skips touching the support line and reverses in between and starts going towards resistance line, get prepared for a breakout on the resistance line." [p. 137]
- "Especially significant is the RSI cycle failure to go below 40, as it indicates that the stock is so strong that RSI refuses to go below 40." [p. 142]
- "whenever price breaks out of a channel on one side and after some time re-enters the channel, it is more likely to give a breakout on the opposite side" [p. 146]
- "Whenever the stock makes a new low, but RSI does not make a new low, there is RSI divergence (bullish)." [p. 148]
- "My advice is that you should only try the last two." [p. 153]
- "So while trading a descending channel, it is more safe to book your profit when RSI reaches 60." [p. 63]
- "Secret Tip: If I have to choose only one out of these four, I would choose RSI Divergence without any hesitation." [p. 154]

**Pseudocode**

```
given an active descending channel (2.1 detection) at day t:
divergence_t  = L_t is lowest low of channel's last 2 swing lows region
                and price swing low_2 < swing low_1 and RSI at low_2 > RSI at low_1 + 2      # ASSUMPTION: 2-point margin
double_brk_t  = exists s in [t-30, t): C_s < L(s)  and later close back > L  (re-entered)  # signal 3, first leg
near_support  = L_t <= L(t) * 1.03
turn_up       = C_t > H_{t-1}                                   # "Let it stop and move up"
signal = near_support and turn_up and (divergence or double_brk) # variant: require both
enter at C_t
stop   = min(L over last 5 bars) * 0.99                        # ASSUMPTION (book silent)
exit 1 (no breakout): sell when H >= U(t)*0.98 or RSI_d >= 60, whichever first
exit 2 (breakout C > U): apply 2.1 strong/weak rule and 1:1 target
```

**Ambiguities & assumptions**

- **Signal 3 ordering:** as a pre-breakout signal the author means "breakdown, then re-entry" (he says to enter near support), while its full definition includes the upside breakout [p. 145–146]. ASSUMPTION: the setup arms on re-entry after a breakdown; the upside breakout is then handled by 2.1.
- **Divergence pivots** are visual. ASSUMPTION: compare the two most recent swing lows (pivot k = 5) inside the channel.
- **Stop** not given. ASSUMPTION: 1% below the 5-day low at entry.
- Most of the signal chapter's examples are **US intraday** charts (15/60-minute) [p. 139–152]; the Indian daily/weekly examples are in Part II. ASSUMPTION: apply on daily and weekly NSE bars only.

### 2.3 Descending channel range trade (author discourages)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion | 52–53 |
| Timeframe & holding period | Prefer weekly/monthly channels (larger profit potential); daily for short-term | 58, 159 |
| Universe / eligibility filters | As 2.1; channel slope close to horizontal; descending channel inside an ascending channel allowed | 53, 58–59 |
| Market / regime filter | Not stated | — |
| Setup conditions | Wide, not steep, no large red marubozu candles; out-of-favour sector | 55–57 |
| Entry trigger & order type | "Buy on support; sell on resistance"; buy after price stops falling and turns up; RSI below 30 used in one example (Castrol, RSI 27) | 53, 62, 67 |
| Initial stop-loss | Not specified | 160 |
| Exits: profit-taking | Sell near resistance or when RSI reaches 60 (weak stock); don't wait for the "perfect finish" | 62–63 |
| Exits: trailing / time / signal | Sell on signs of fatigue/reversal | 62 |
| Position sizing | As 2.1 | 158 |
| Adding to / pyramiding | Do not average down (narrative) | 17, 61 |
| Portfolio limits | As 2.1 | 158 |

**Key quotes**

- "Secret tip: The best way to trade a descending channel range is not to trade it." [p. 58]
- "Or trade the range of descending channel only if the profit potential is large, as you can find in a weekly or monthly channel." [p. 58]
- "Exception: You can choose to buy a descending channel, if it is a part of Ascending channel." [p. 58]
- "While trading descending channels, don't wait for the perfect finish." [p. 62]

**Pseudocode**

```
weekly channel (2.1 detection on weekly bars), width_pct >= 0.20                         # ASSUMPTION: "large" potential
entry: L_w <= L(w)*1.03 and C_w > O_w (week closes up) → buy next week's open
exit: H >= U(w)*0.98 or weekly RSI >= 60 → sell; stop: weekly close < L(w)*0.95 (ASSUMPTION)
```

**Ambiguities & assumptions**

- The author's own advice is not to trade this [p. 58]; include only as a baseline to compare against 2.2 (same entry zone without the signal filter).
- **"Slope resembles the horizontal channel"** [p. 53] has no number. ASSUMPTION: weekly slope ≤ 0.5% of price per bar.

## 3. Risk & money-management rules

- Start with 10% of intended trading capital; Rs. 1,000 per trade on Rs. 10,000; no more than 3 trades at a time [p. 158].
- One channel per timeframe (monthly, weekly, daily) initially [p. 159–160].
- Always calculate entry, stop and target in advance; book the loss if the channel fails [p. 51, 160].
- Reward:risk at least 1:4 "due to brokerage and slippage" [p. 161].
- Quotes endorsing ≤ 1% risk per trade (Larry Hite [p. 47], Ed Seykota [p. 159]), offered as advice, not the author's own number.
- Avoid F&O as a beginner [p. 51, 54].

## 4. Non-codable guidance

- Read context: a descending channel that is the handle of a cup & handle, or part of a W/double bottom, is more trustworthy [p. 88–91, 106].
- Volume first: volume should rise on green candles and fall on red ones in a turning channel [p. 130]; "volume rises first, news comes later" [p. 43].
- After a failed breakout in one direction, expect a move the other way ("double/triple breakout") [p. 95, 101, 119].
- Use multiple timeframes; if daily and weekly disagree, follow the higher timeframe [p. 64–65, 119].
- Review 100 charts a day (Nifty 50 daily plus that day's 52-week-high stocks) [p. 158].
- Buying is "extra safe" at the crosspoint of supports from two timeframes [p. 120].
- Avoid IPO channels / newly listed stocks with short RSI history [p. 99, 106].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV (resampled to weekly and monthly); RSI(14) on daily and weekly bars; 20-day volume average; an index or index proxy for "bullish market"; Nifty 50 membership if the beginner universe is used.
- **Testability with our data:** Fully backtestable on 2005–2026 prices once channel detection is coded; no fundamentals needed. The 150-candle RSI warm-up excludes the first ~150 sessions (daily) or ~3 years (weekly) of each stock. Point-in-time Nifty 50 membership is not in our data. ASSUMPTION: replace "Nifty 50 stocks" with the top 50 by trailing 1-year traded value.
- **Market-structure differences:**
  - The book is written for NSE/BSE, so the volume (5 lakh shares/day) and price (≥ Rs. 10) floors apply directly. ASSUMPTION: also require ≥ Rs. 1 crore daily traded value, because a share-count floor favours low-priced stocks.
  - Long-only fits the cash market; the author's short-selling remarks are excluded.
  - Upper circuit on the breakout day prevents a close-confirmed fill. ASSUMPTION: if the breakout day closes at the upper band, fill at the next open.
  - Costs: the author asks for 1:4 reward:risk because of costs [p. 161]; charge STT, brokerage and ~0.1% slippage per side.

## 6. Verdict

- **Codeability:** Partly. The breakout filters (volume multiple, pre-breakout RSI bands, 1:1 width target) are numeric, but the channel itself is hand-drawn and no stop rule is given; a coded version depends on the trendline-fitting assumptions above.
- **Priority for backtesting:** Medium. It is an NSE-specific, single-pattern method with explicit volume/RSI thresholds derived from the author's 20-stock table, but the evidence is that table only (no returns), and the channel-detection step is costly to build.
- **Top 3 things a coder is most likely to get wrong**
  1. Measuring RSI on the **breakout** candle instead of the **pre-breakout** candle (the 50–70 / 40–60 bands apply to the candle before the breakout).
  2. Fitting the two trendlines independently (non-parallel); the book's channel has parallel lines with ≥ 2 touches each, and the target uses the vertical width at the breakout point.
  3. Treating any close above the line as the signal: the book requires ≥ 2× volume on the breakout **and** elevated volume for the next few candles, with lower volume while the channel formed.
