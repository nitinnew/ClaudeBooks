# Evidence-Based Technical Analysis — David R. Aronson (Wiley, 2007)

- **Source file:** Google Drive (file id `18t3f7btlb5ktG8wuLTIwlEAgJ84qN2l5`), 528 PDF pages with a text layer.
- **Text file used:** text/aronson_evidence_based_ta.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number; printed page ≈ PDF page − 2 in Part II and ≈ PDF page − 8 in Part I)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/aronson_evidence_based_ta.md text/aronson_evidence_based_ta.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:**
  - Read sequentially: [[PAGE 1]] to [[PAGE 69]] (introduction, Ch. 1 on objective rules and their evaluation, and most of Ch. 2 on cognitive biases).
  - Read sequentially: [[PAGE 390]] to [[PAGE 453]] (Ch. 8, the rule definitions, and Ch. 9, the results and critique).
  - Also read: the Ch. 9 note on the best rule [p. 511].
  - Skimmed by keyword search for rule content: Ch. 3–7 (philosophy of science, statistics, data-mining bias, behavioral finance) and pp. 453–528 (future of TA, appendix, notes). These chapters contain methods and theory, not trading rules.

## 1. The method in brief

This is a methods book, not a trading system.

- **Testing standard.** Aronson argues that technical-analysis rules must be objective, back-tested and judged by statistical inference that corrects for data-mining bias.
- **Test design.** Every tested rule is a binary long/short reversal rule on the S&P 500, with:
  - signals from data known at the close;
  - execution at the next day's open [p. 36–37];
  - returns measured on detrended data, so a long or short bias earns nothing [p. 392–393].
- **The rule set (Part II).** 6,402 rules, tested over Nov 1980 – Jul 2005 [p. 390], built from three themes [p. 392] on 39 input series (price indices, breadth, volume, bonds, rate spreads; Table 8.2 [p. 419]):
  - **Trend:** a channel breakout on an input series.
  - **Extreme/transition:** threshold crossings of a smoothed, channel-normalised series.
  - **Divergence:** a double channel-normalised gap between a companion series and the S&P 500.
- **Result: nothing survived.** The best rule earned 10.25% a year on detrended data but had a data-mining-adjusted p-value of 0.82 [p. 442–443]. About 320 rules would have looked significant under a naive test, which is exactly what chance predicts [p. 445].

**Use to us:**
- A ready-made, fully specified rule grammar that can be ported to NSE breadth and price data.
- A testing protocol (detrend, next-open execution, White's Reality Check / Monte Carlo permutation) for every other spec in this project.
- Pointers to anomalies that published research found real: 3–12-month relative strength, sector momentum and 52-week-high proximity [p. 17–18]. Aronson also suggests simple rules may work better on indices of younger companies [p. 17, 452].

## 2. Strategies

### 2.1 Channel-breakout trend rules (TT traditional / TI inverse)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following (and its inverse) | 420 |
| Timeframe & holding period | Daily; always in the market (long/short reversal); holding is whatever the signal gives | 420–421, 451 |
| Universe / eligibility filters | Trades the S&P 500 index only; the signal comes from one of 39 input series (Table 8.2; the S&P 500 open is excluded as redundant) | 419–420 |
| Market / regime filter | None | — |
| Setup conditions | Channel-breakout operator (CBO) on the input series: the channel is the max/min of the past n periods, excluding the current one | 398 |
| Entry trigger & order type | Traditional: the input breaks above its n-day max → long S&P (+1); breaks below its n-day min → short (−1). Inverse (TI): the opposite. Execute at the next day's open | 398, 421, 36–37 |
| Initial stop-loss | None (the reversal signal is the only exit) | 451 |
| Exits: profit-taking | None; the position reverses on the opposite breakout | 421 |
| Exits: trailing / time / signal | Opposite channel breakout | 398 |
| Position sizing | Unit position ±1 | 395–396 |
| Adding to / pyramiding | No | — |
| Portfolio limits | Single instrument | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| CBO look-back n | 11 values: 3, 5, 8, 12, 18, 27, 41, 61, 91, 137, 205 days (×≈1.5 steps) | adaptive CBO not tested | 399, 421 |
| Input series | 39 of the 40 in Table 8.2 | — | 419–420 |
| Rule count | 858 (429 traditional + 429 inverse) | — | 421 |
| Naming | TT/TI–series–lookback, e.g. TT-15-137 | — | 421 |

**Key quotes**

- "the channel breakout operator signals long positions if the analyzed series exceeds its maximum value established over the past n-periods." [p. 398]
- "They were 3, 5, 8, 12, 18, 27, 41, 61, 91, 137, and 205 days." [p. 421]
- "This resulted in a total of 858 trend rules, 429 (39 × 11) based on a traditional TA interpretation, and an additional 429 inverse-trend rules." [p. 421]
- "the rule tests assume execution at the opening price on the following day." [p. 36]

**Pseudocode** (daily bars)

```
for series X in inputs, n in [3,5,8,12,18,27,41,61,91,137,205]:
    hi_n = max(X[t-n .. t-1]); lo_n = min(X[t-n .. t-1])
    if X[t] > hi_n: state = +1
    elif X[t] < lo_n: state = -1          # else keep previous state
    pos_TT[t] = state ; pos_TI[t] = -state
    ret[t] = pos[t] * log(Open[t+2]/Open[t+1]) - ALR    # detrended, next-open execution
```

**Ambiguities & assumptions**

- Initial state before the first breakout is not stated. ASSUMPTION: flat until the first breakout, then always ±1.

### 2.2 Extreme-value and transition rules (E rules), including the best rule E-12-28-10-30

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion / threshold (12 types cover both momentum and contrarian readings) | 420–423 |
| Timeframe & holding period | Daily; long/short reversal | 422–423 |
| Universe / eligibility filters | S&P 500 traded; 39 input series | 421 |
| Market / regime filter | None | — |
| Setup conditions | Indicator = CN(LMA(input, 4), N): a 4-day linearly weighted MA of the input, then channel normalisation (stochastic, 0–100) over N days | 400–402, 421 |
| Entry trigger & order type | Upper/lower thresholds at 50 ± displacement. Four events: (1) lower threshold crossed down, (2) lower crossed up, (3) upper crossed up, (4) upper crossed down. Each type pairs one event for long entry/short exit with one for short entry/long exit (Table 8.3, types 1–12). Next-day open execution | 422–423 |
| Initial stop-loss | None | — |
| Exits | Opposite event of the pair | 422 |
| Position sizing | ±1 | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Rule type | 1–12 (Table 8.3) | types 7–12 are inversions of 1–6 | 422–423 |
| Smoother | 4-day linearly weighted MA (weights 4,3,2,1 / 10) | — | 400–401 |
| CN look-back N | 15, 30, 60 days | — | 429 |
| Threshold displacement | 10 (60/40) or 20 (70/30) | — | 429 |
| Rule count | 2,808 (12 × 39 × 2 × 3) | — | 429 |
| Best rule | E-12-28-10-30: type 12, input 28 = 10-day MA of the NYSE up/down volume ratio, thresholds 60/40, CN 30 days | — | 442, 511 |

**Key quotes**

- "Two different values for the threshold displacement parameter were tested: 10 and 20." [p. 430]
- "Three different values were considered for the channel normalization look-back span: 15, 30, and 60." [p. 430]
- "The rule with the best performance, E-12-28-10-30,1 generated a mean annualized return of 10.25 percent, on detrended market data." [p. 442]
- "Type 12 is short although the indicator is above the upper threshold, long at all other times." [p. 511]

**Pseudocode**

```
S  = LMA(X, 4)                                   # (4X_t + 3X_t-1 + 2X_t-2 + X_t-3)/10
CN = 100 * (S - min(S, N)) / (max(S, N) - min(S, N))
U = 50 + d ; L = 50 - d
events: e1 = CN crosses below L; e2 = CN crosses above L; e3 = CN crosses above U; e4 = CN crosses below U
type k -> (long_event, short_event) from Table 8.3, e.g. type 12 = (e4, e3)
if long_event: pos = +1 ; if short_event: pos = -1 ; else hold
# best rule: X = MA(NVR,10), NVR = (upvol - dnvol)/(upvol + dnvol + unchvol); d = 10; N = 30; type 12
#   -> short after CN crosses above 60, long after CN crosses back below 60
```

**Ambiguities & assumptions**

- Table 8.3 lists types by event pairs; the figures show the same. The input-28 label is "Up Down Volume Ratio 10-Day MA" in Table 8.2 [p. 419], while the formula text calls it the net volume ratio, (upvol − dnvol)/(upvol + dnvol + unchvol) [p. 416]. ASSUMPTION: they are the same series.
- Whether the CN window includes the current bar is not stated. ASSUMPTION: it includes the current bar (unlike CBO).

### 2.3 Divergence rules (D rules)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | divergence / intermarket | 430 |
| Timeframe & holding period | Daily; long/short reversal | 438–439 |
| Universe / eligibility filters | S&P 500 traded; 38 companion series | 435, 439 |
| Setup conditions | Divergence indicator = CN{CN(companion, n) − CN(S&P 500, n), 10n}: double channel normalisation, so one threshold fits all pairs (the second window is 10× the first, e.g. 60 → 600 days) | 437–439 |
| Entry trigger & order type | Above the upper threshold = bullish divergence (companion stronger); below the lower = bearish. 12 types as for E rules: type 6 = basic bullish, type 7 = basic bearish, 12 and 1 are their inversions (Table 8.4). Next-day open | 438–440 |
| Exits | Opposite threshold event | 440 |
| Position sizing | ±1 | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| First CN look-back n | 15, 30, 60 | — | 439 |
| Second CN look-back | 10n | — | 439 |
| Threshold displacement | 10 or 20 | — | 439 |
| Rule count | 2,736 (12 × 38 × 2 × 3) | — | 439 |
| Inspiration | Heiby: divergence when one series CN ≥ 75 and the other ≤ 25 (50-day range) | — | 404, 433 |
| Not used | Cointegration / error-correction divergence (suggested as better) | Fosback Index | 435–436 |

**Key quotes**

- "a bullish divergence rule, which would call for long positions in the S&P 500 when the divergence indicator was above the upper threshold" [p. 440]
- "The look-back span for the second level of channel normalization was set at 10 times the look-back interval used for ﬁrst level." [p. 439]

**Pseudocode**

```
raw = CN(Companion, n) - CN(SPX, n)          # range -100..+100
DI  = CN(raw, 10*n)                          # 0..100
apply the E-rule event logic (Table 8.4 type k, thresholds 50±d) to DI
```

### 2.4 Zweig double 9:1 up/down-volume rule (third-party rule, discussed but excluded from the study)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breadth thrust (long only) | 391 |
| Timeframe & holding period | Daily signal; tested over the following 3, 6, 9 and 12 months | 391 |
| Universe | NYSE breadth → stock market | 391 |
| Entry trigger | NYSE upside/downside volume ratio > 9 on two days within a three-month window → long | 391 |
| Exits | Fixed horizons (3–12 months) in the students' test; not specified as a trading rule | 391 |
| Evidence | Aronson's students found predictive power at 3–12 months, valid only if Zweig did not data-mine the 9 / 2 / 3 parameters | 391 |

**Key quotes**

- "This rule signals long positions when the daily ratio of upside to downside volume on the NYSE exceeds a threshold value of 9 on two instances within a three-month time window." [p. 391]

**Pseudocode**

```
r[t] = UVOL[t] / DVOL[t]
if r[t] > 9 and any(r[s] > 9 for s in t-63 .. t-1): signal long; hold h in {63,126,189,252} sessions
```

## 3. Risk & money-management rules

- Detrend before testing: subtract the average daily log return so position-biased rules gain nothing from the market's drift [p. 34–35, 392–393].
- Avoid look-ahead bias: close-based signals execute at the next open, and lagged or revised data must be lagged [p. 36–37].
- Trading costs were excluded on purpose because the aim was to detect predictive power; a stand-alone trading test must include commissions and slippage [p. 38].
- Judge the best of many rules with White's Reality Check or Monte Carlo permutation, not a single-rule test. Here a 10.25% return gave p = 0.0005 naively but 0.82 after adjustment [p. 442–444].
- Avoid data snooping: don't add rules because earlier studies found them profitable unless the amount of mining behind them is known [p. 391–392, 450].
- Make falsifiable forecasts: state in advance what outcome proves the call wrong [p. 64].

## 4. Non-codable guidance

- Subjective chart reading is prone to hindsight and confirmation bias; the same chart can be read as a bull flag or a head-and-shoulders [p. 58–61].
- Unaided judgement handles only about three variables configurally; combine indicators with a formal model [p. 48–50].
- Complex (multi-rule) and tri-state (long/neutral/short) rules are probably better than single reversal rules but were not tested [p. 451–452].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLC for NIFTY 50 / NIFTY 500 and sector indices. NSE breadth (advances, declines, unchanged), up/down volume and 52-week highs/lows rebuild inputs 24–32. G-sec yields and T-bill prices rebuild the rate-spread inputs.
- **Testability with our data:** Fully backtestable for price-based inputs from 2005. Breadth inputs need a daily constituent-level aggregation (possible from bhavcopy archives).
- **Market-structure differences:**
  - Shorting the index needs futures; for a long-only cash test, convert the reversal rules to long/flat, which Aronson himself suggests may suit occasional inefficiency [p. 452].
  - Aronson suggests less-seasoned markets may be more predictable [p. 452], a reason to test on NSE mid/small-cap indices.
  - Pre-register the rule grid and apply a Reality Check / permutation test to the whole NSE grid.

## 6. Verdict

- **Codeability:** Yes. Every rule is fully specified (operators, parameter grids, naming convention), and the testing protocol is explicit.
- **Priority for backtesting:** Medium. On the S&P 500 none of the 6,402 rules survived, so expect little from single reversal rules. The book's main value is as the project's statistical-testing standard and as a grammar for an NSE grid test (long/flat, breadth inputs, mid/small caps).
- **Top 3 things a coder is most likely to get wrong**
  1. Executing at the signal day's close instead of the next open (open+1 to open+2 return) [p. 36–37].
  2. Reporting raw rather than detrended returns, which rewards long-biased rules in rising markets [p. 392–393].
  3. Testing the best of thousands of rules with an ordinary significance test: about 320 of 6,402 worthless rules pass at 0.05 [p. 445].
