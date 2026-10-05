# The Handbook of Portfolio Mathematics: Formulas for Optimal Allocation & Leverage — Ralph Vince (John Wiley & Sons, 2007)

- **Source file:** Google Drive `Vince, Ralph - The Handbook of Portfolio Mathematics_ Formulas for Optimal Allocation & Leverage-John Wiley & Sons, Inc (2008).pdf` (file id `1lvjfeEskPixljpjPhr6neRmHannulPzP`, 3,816,214 bytes), 446 PDF pages with a text layer.
- **Text file used:** text/vince_portfolio_mathematics.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index). The printed page number is usually PDF page − 24 (printed p. 117 = [[PAGE 141]]), but always take N from the marker.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/vince_portfolio_mathematics.md text/vince_portfolio_mathematics.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage (redo under correction 4, replaces the 17 KB condensed version):**
  - **Read sequentially, cover to cover: [[PAGE 1]] to [[PAGE 446]]**, covering front matter, Preface, Introduction, Ch. 1–12, Postscript and Index.
  - **How it was read.** I read a filtered view of the text file. It drops lines made only of digits, signs and symbols (table cells, stray equation glyphs) and keeps every prose line with its original line number. Every prose line, formula line and code line was read.
  - **Tables were therefore not read cell by cell:** Ch. 4 f-value/TWR grids ([[PAGE 158]]–[[PAGE 167]]), Ch. 7 matrix row-operation tables ([[PAGE 268]]–[[PAGE 283]]), Ch. 9 correlation grids ([[PAGE 316]]–[[PAGE 319]]), and the Ch. 12 RR(b) tables ([[PAGE 410]], [[PAGE 428]], [[PAGE 434]]). The prose stating each table's conclusion was read.
  - **Index ([[PAGE 441]]–[[PAGE 446]]) scanned only.**
  - **Corrections to the previous version of this spec (stated for the laptop importer):**
    - The old Coverage line said Chapter 2 ([[PAGE 67]]–[[PAGE 122]]) "contains no trading or sizing rules" and was skipped. **That was wrong.** Ch. 2 contains the binomial system-validation rule ([[PAGE 99]]–[[PAGE 102]]), now 2.8, plus the ≥5-per-bin chi-square and Student's-t-under-30 rules.
    - The old version also listed [[PAGE 1]]–[[PAGE 66]] as read, but the opening front-matter lines had not been read. They have been now.
  - This book contains **no entry/exit signals**. Every strategy below is a position-sizing, allocation or validation algorithm meant to be layered on a separate trading system (the "host system").

## 1. The method in brief

**The thesis**
- Vince's thesis: for any positive-expectancy stream of independent outcomes, growth is maximised by betting a **fixed fraction** of equity [p. 136–138].
- The best fraction, **optimal f**, maximises the geometric mean holding-period return (HPR), equivalently the Terminal Wealth Relative (TWR = product of HPRs) [p. 146–150].
- f is not "percent of equity to bet". It is a divisor of the biggest loss: trade one unit per **f$ = |biggest loss| / f** of equity [p. 142, 150].
- The keystone rule: no money-management scheme can turn a non-positive mathematical expectation into a positive one [p. 42, 134].

**Part I (Ch. 1–6): sizing a single system**
- Chapter 1 gives dependency tests: runs test, lag-1 correlation and turning points [p. 51–65].
- Chapter 2 gives statistical validation of a system's win rate [p. 99–102].
- Chapter 4 gives optimal f, Kelly as a special case, equalized f and scenario-based f [p. 141–198].
- Chapter 5 gives small-account and threshold rules, fractional-f conversions, and the fundamental equation of trading, TWR = (A² − S²)^(T/2) [p. 199–226].
- Chapter 6 shows that, over a known finite horizon, the growth-maximising f is slightly above optimal f [p. 233–240].

**Part I (Ch. 7–8): mean–variance portfolios with optimal-f inputs**
- Ch. 7–8 rebuild Markowitz mean–variance using optimal-f-based HPRs as inputs.
- They find the geometric-optimal unconstrained portfolio and convert its weights back into adjusted f$ per component [p. 255–310].

**The new model (Ch. 9–10): Leverage Space Model**
- Ch. 9 replaces correlation with **joint scenario probabilities**. It maximises the portfolio geometric mean G(f1…fn) over an (n+1)-dimensional landscape, using a genetic algorithm [p. 311–346].
- Ch. 10 covers dilution (static vs dynamic fractional f), reallocation, the margin cap, continuous dominance, points "to the left" of the peak, and drawdown management [p. 347–387].

**Part II (Ch. 11–12): practice**
- Ch. 11 describes how large trend-following CTAs actually size: risk 0–2% per trade, a volatility stop, and a value-at-risk (VaR) scaling factor [p. 391–400].
- Ch. 12 gives the final model: **maximise TWR subject to RD(b) ≤ an acceptable probability of a drawdown to b**. RD is estimated by enumerating or sampling outcome permutations and fitting an asymptote [p. 401–438].

## 2. Strategies

Codability ratings: **Fully** = all inputs and rules stated; **Partly** = formula stated but key inputs are judgmental or the author leaves a choice open.

| # | Strategy | Codable | Pages |
|---|---|---|---|
| 2.1 | Optimal f from a trade list (TWR search) | Fully | 141–157 |
| 2.2 | Kelly formula (fixed-size outcomes only) | Fully (restricted) | 144–146, 155 |
| 2.3 | Equalized optimal f and daily HPRs | Fully | 175–180, 302 |
| 2.4 | Scenario-spectrum optimal f | Fully (inputs judgmental) | 185–198 |
| 2.5 | Small-account first-contract allocation | Fully | 199–200 |
| 2.6 | Threshold to geometric (constant contract → fixed fraction) | Fully | 177–178, 201–204 |
| 2.7 | Dependency gate and per-state f | Partly | 51–65, 206–207 |
| 2.8 | Binomial validation gate | Fully | 99–102 |
| 2.9 | Static fractional f | Fully | 174–175, 212–216, 350–351 |
| 2.10 | Dynamic fractional f (split equity) with reallocation | Fully | 347–369 |
| 2.11 | Continuous dominance (gradient switching) | Fully | 369–375 |
| 2.12 | Drawdown-defined f$ and composite-f exposure | Fully | 359, 377–378, 386–387 |
| 2.13 | Margin-constrained upside limit on active equity | Fully | 365–366 |
| 2.14 | Geometric-optimal mean–variance portfolio on optimal-f inputs | Fully | 259–310 |
| 2.15 | Leverage Space Model: max G via genetic algorithm | Fully | 323–346 |
| 2.16 | Leverage Space Model with drawdown constraint RD(b) | Fully | 401–438 |
| 2.17 | Practitioner risk-per-trade / VaR sizing (Ch. 11) | Fully | 391–400 |
| 2.18 | Finite-horizon f targets (EACG, GRR, left inflection) | Partly | 233–240, 376–382 |
| 2.19 | Utility-weighted (utils) optimal f | Partly | 250–253 |

Fields that do not apply to a sizing layer are marked "n/a (host system)". The host trading system supplies entries and exits.

### 2.1 Optimal f from a trade list (TWR search)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position-sizing algorithm (fixed fractional, growth-optimal) | 141–150 |
| Timeframe & holding period | Any. Uses the host system's closed-trade P&L list on a 1-unit basis | 149 |
| Universe / eligibility filters | Only systems with positive mathematical expectation; "optimal f" does not exist otherwise | 42, 134, 141 |
| Market / regime filter | n/a (host system) | — |
| Setup conditions | Trade list of the host system (1 unit). Include realistic slippage and commission | 130, 149 |
| Entry trigger & order type | n/a (host system). Size each new trade at INT(equity / f$) units | 150 |
| Initial stop-loss | n/a (host system). The biggest historical loss is the sizing anchor | 146, 150 |
| Exits: profit-taking | n/a (host system) | — |
| Exits: trailing / time / signal | n/a (host system) | — |
| Position sizing | HPR_i = 1 + f·(−trade_i / biggest loss); TWR = Π HPR_i; G = TWR^(1/N). Choose the f in (0,1] that maximises TWR. Units = equity / (biggest loss / −f) | 146–150 |
| Adding to / pyramiding | Re-size as equity changes. Realign as often as costs allow (ideally continuously); per trade is the minimum | 171 |
| Portfolio limits | Per-unit dollars needed = max(initial margin, f$) | 171 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| f search grid | .01 to 1.00 step .01 | iterative bracketing; parabolic interpolation, tolerance .005 | 147, 181–185 |
| Anchor | biggest losing trade (1 unit) | not max drawdown | 163, 168 |
| Rounding | integer units | larger stakes make integer ≈ fractional | 157 |
| Example | +2/−1 coin: f = .25, TWR 10.55 after 40 plays; f = .1 or .4 → 4.66; f = .5 breakeven | +5/−1: f = .4; 20% miss → under 1/10 the gain | 161–163 |
| Geometric average trade | GAT = (G − 1)·(biggest loss / −f) | — | 152 |

**Key quotes**
- "optimal ﬁxed fraction (f) between 0 and 1 as a divisor of your biggest loss" [p. 142]
- "Optimal f is not in itself the percentage of our total stake to bet" [p. 142]
- "By looping through all values for f between .01 and 1, we can ﬁnd that value for f which results in the highest TWR." [p. 147]
- "The optimal f is that which yields the highest TWR." [p. 149]
- "the amount required per contract in real life is the greater of the initial margin requirement or the dollar amount per contract dictated by the optimal f." [p. 171]
- "Ideally, you will realign yourself with optimal f on as close to a continuous basis as possible" [p. 171]
- "It is not unusual for a market system trading one contract under optimal f to see 80 to 95% of its equity erased in the bad drawdowns." [p. 170]

**Pseudocode**
```
trades = host_system.closed_trade_pnl(units=1, net_of_costs=True)      # p.130
require mean(trades) > 0                                               # p.42, 134
BL = min(trades)                                                        # biggest loss (negative)
def TWR(f): return prod(1 + f * (-t / BL) for t in trades)              # p.146
f_opt = argmax_{f in 0.01..1.00 step 0.01} TWR(f)                       # p.147 (refine by parabolic interp, p.181)
G = TWR(f_opt) ** (1/len(trades))
f_dollars = BL / -f_opt                                                 # p.150
per_unit = max(initial_margin, f_dollars)                               # p.171
units = floor(equity / per_unit)            # recompute before every trade, or daily (p.171)
```

**Ambiguities & assumptions**
- **Which equity.** The book uses "account equity". ASSUMPTION: total equity marked to market (closed plus open), as stated for the dynamic variant [p. 348].
- **Future biggest loss.** The book warns not to shrink the biggest loss for low volatility and to budget for a larger loss [p. 217–218]. ASSUMPTION: anchor on the historical biggest loss × 1.0, and test a 1.5× stress as a variant.
- **Rounding.** Not specified beyond integer contracts. ASSUMPTION: floor.

### 2.2 Kelly formula (fixed-size outcomes only)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position-sizing formula, a special case of 2.1 | 144–146 |
| Timeframe & holding period | Any | — |
| Universe / eligibility filters | Valid only when all wins are one fixed size and all losses one fixed size (Bernoulli outcomes) | 145–146, 150 |
| Market / regime filter | n/a (host system) | — |
| Setup conditions | Known win probability P and payoff ratio B | 144–145 |
| Entry trigger & order type | n/a (host system) | — |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Equal win and loss sizes: f = 2P − 1. Unequal fixed sizes: f = ((B + 1)·P − 1)/B. Units as in 2.1 (f$ = loss / f) | 144–145, 150 |
| Adding to / pyramiding | As 2.1 | — |
| Portfolio limits | As 2.1 | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| P | win probability | — | 144 |
| B | win/loss ratio | — | 145 |
| Wrong use | averaging wins and losses gives f = .16 vs true .24 | makes 37.5% as much after 900 trades | 155 |

**Key quotes**
- "We cannot average our wins and losses from trading and obtain the true optimal f using the Kelly formula." [p. 155]
- "Any of the three methods will give you the same answer when all wins and losses are for the same amount." [p. 150]
- "Regardless of constraints, the optimal f via the highest TWR will always meet the four desirable properties of a money-management strategy." [p. 150]

**Pseudocode**
```
if all wins equal and all losses equal:
    f = 2*P - 1 if win == -loss else ((B+1)*P - 1)/B      # p.144-145
else:
    f = optimal_f_from_trade_list(trades)                 # 2.1; never average into Kelly (p.155)
```

**Ambiguities & assumptions**
- None material. Use only as a unit test for the 2.1 implementation (both must agree on Bernoulli data [p. 186]).

### 2.3 Equalized optimal f and daily HPRs

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position-sizing algorithm (price-normalised optimal f) | 175–180 |
| Timeframe & holding period | Trade list, converted to percentages; daily mark-to-market HPRs for portfolio inputs | 176, 178, 302 |
| Universe / eligibility filters | Instruments whose price level changed a lot over the test history (author's preference: always equalize) | 175, 180 |
| Market / regime filter | n/a (host system) | — |
| Setup conditions | P&L% = exit/entry − 1 (longs); entry/exit − 1 (shorts); or P&L points / entry. Deduct costs from the exit price | 176 |
| Entry trigger & order type | n/a (host system) | — |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Run 2.1 on the % stream to get f. Then f$ = biggest % loss × current price × $/point / −f, recomputed daily from last night's close | 176–178 |
| Adding to / pyramiding | f$ changes with price, so position size adjusts daily; units = equity / f$ | 177 |
| Portfolio limits | For portfolios, daily HPR = D$/f$ + 1 (D$ = 1-unit daily $ change). All components must be either all equalized or all raw | 178, 302 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Example | % stream +.1, −.15, +.2, −.1 → f = .09; price 100 → f$ = 166.67/share | price 102 → f$ = 170 | 176, 178 |
| Threshold to geometric (equalized) | T = AAT/GAT × f$ | — | 178 |
| Look-back | not fixed; "if it does matter a great deal … you're probably using too much data" | — | 180 |

**Key quotes**
- "P&L% = Exit Price/Entry Price −1" [p. 176]
- "f $ = Biggest % Loss * Current Price * $per Point/−f" [p. 176]
- "Using the equalized optimal f makes it more likely that adjusting your position size daily will be beneﬁcial." [p. 177]
- "the equalized data is a fairer representation of the distribution of possible outcomes on the next trade." [p. 180]

**Pseudocode**
```
pct = [(exit_adj/entry - 1) if long else (entry/exit_adj - 1) for each trade]   # p.176 (costs in exit_adj)
f = optimal_f(pct)                                     # 2.1 on the % stream
BLpct = min(pct)
each day: f_dollars = BLpct * close_prev * dollars_per_point / -f   # p.176-178
          units = floor(equity / max(margin, f_dollars))
          daily_HPR = (close - close_prev)*dollars_per_point / f_dollars + 1   # p.178, for portfolio inputs
```

**Ambiguities & assumptions**
- **Which equation for shorts.** (4.10b) and (4.11) give different answers for shorts [p. 180]. ASSUMPTION: use (4.10a)/(4.10b) as primary.
- **Current price.** Sizing uses "current price"; the daily-HPR definition uses last night's close [p. 178]. ASSUMPTION: last close for both.

### 2.4 Scenario-spectrum optimal f

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position-sizing / decision algorithm on subjective or binned outcome distributions | 185–198 |
| Timeframe & holding period | One common holding period for every scenario in the spectrum | 198 |
| Universe / eligibility filters | Probabilities sum to exactly 1; at least one negative outcome; arithmetic expectation > 0 | 188 |
| Market / regime filter | n/a | — |
| Setup conditions | Spectrum ordered worst → best, non-overlapping scenarios, covering ~99% of possible outcomes; avoid the 3-scenario (best/worst/same) trap | 189, 198 |
| Entry trigger & order type | n/a | — |
| Initial stop-loss | The worst scenario W acts as the biggest loss | 186 |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | HPR_i = (1 + A_i/(W/−f))^P_i; TWR = Π HPR_i; G = TWR^(1/ΣP). Maximise over f; f$ = W/−f | 186 |
| Adding to / pyramiding | Update scenarios each holding period | — |
| Portfolio limits | Choose between alternatives by highest G at their optimal f, not highest expectation | 194–195 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Examples | XYZ country scenarios: f = .57 → $877,192 per unit | soybeans: f = .02 → 1 contract per $375,000 | 192, 194 |
| Interpretation | f = .65 means 65% of equity "in the market" for scenario types expressed as % returns | — | 193 |
| White vs black | expectation $3.00, f = .17 vs the alternative | pick higher G | 195 |

**Key quotes**
- "the sum of the probabilities of all of the scenarios we are considering must equal 1 exactly." [p. 188]
- "You must have at least one scenario with a negative outcome in order to use this technique. This is mandatory." [p. 188]
- "selecting the scenario whose geometric mean corresponding to its optimal f is greatest will maximize our decision in an asymptotic sense." [p. 194]
- "All scenarios within a given spectrum must pertain to outcomes of a given holding period." [p. 198]

**Pseudocode**
```
assert abs(sum(P) - 1) < 1e-9 and min(A) < 0 and dot(A, P) > 0         # p.188
W = min(A)
def G(f): return prod((1 + a/(W/-f))**p for a, p in zip(A, P)) ** (1/sum(P))   # p.186
f_opt = argmax G(f) on (0,1]
f_dollars = W / -f_opt ; units = floor(equity / f_dollars)
```

**Ambiguities & assumptions**
- **Where scenarios come from.** Judgmental, or empirical bins. The book allows empirical bins with equal probabilities [p. 420 fn]. ASSUMPTION: build from a histogram of the host system's 1-unit holding-period P&L, with 10–20 bins.

### 2.5 Small-account first-contract allocation

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position-sizing rule for accounts trading 1–few contracts | 199–200 |
| Timeframe & holding period | Daily recalculation | 200 |
| Universe / eligibility filters | Small accounts starting at one contract | 199 |
| Market / regime filter | n/a | — |
| Setup conditions | Know f, the biggest loss, max historical drawdown (1 unit) and initial margin | 199 |
| Entry trigger & order type | n/a (host system) | — |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | A = MAX(BL/−f, margin + ABS(max DD)). Contracts = INT((equity − A)/(BL/−f)) + 1 | 199–200 |
| Adding to / pyramiding | Recompute daily | 200 |
| Portfolio limits | Fewer than 1 contract if equity < A (ASSUMPTION: stand aside) | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Example | f .4, BL −$3,000, DD −$6,000, margin $2,500 → A = $8,500 | equity $22,500 → 2 contracts (pure f: 3) | 200 |

**Key quotes**
- "The amount of funds allocated toward the ﬁrst contract should be the greater of the optimal f amount in dollars or the margin plus the maximum historic drawdown" [p. 199]
- "The answer obtained will be rounded down to the integer, and 1 will be added." [p. 200]

**Pseudocode**
```
fd = BL / -f
A = max(fd, margin + abs(maxDD))                      # p.199
contracts = 0 if equity < A else floor((equity - A) / fd) + 1   # p.200
```

**Ambiguities & assumptions**
- **Equity below A.** Not covered. ASSUMPTION: zero contracts.

### 2.6 Threshold to geometric (constant contract → fixed fraction)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mode-switch rule: constant-contract trading until an equity threshold, then fixed fractional | 201–204 |
| Timeframe & holding period | Per trade | 201 |
| Universe / eligibility filters | Useful when going from 1 to 2 contracts; beneficial only if AAT > 2·GAT and units are not fractional | 203–204 |
| Market / regime filter | n/a | — |
| Setup conditions | Average arithmetic trade (AAT), geometric average trade (GAT), BL, f | 201 |
| Entry trigger & order type | n/a (host system) | — |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | T = AAT/GAT × (BL/−f). Converted T = EQ + T − (BL/−f). Below converted T trade a constant N; at or above it trade N + 1, then geometrically | 201–203 |
| Adding to / pyramiding | If equity falls back below the threshold, revert to a constant N | 203 |
| Portfolio limits | Not valid for advancing beyond 2 contracts unless you never trim back | 203 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Example | 2:1 coin, f .25: T = $8.24; EQ $400 → converted T $404.24 (100 → 101 bets) | — | 202–203 |

**Key quotes**
- "the threshold to geometric tells us at what point we should switch over to ﬁxed fractional trading, assuming we are starting out constant-contract trading." [p. 201]
- "the geometric threshold is a very valid technique for determining at what equity level to start trading two contracts" [p. 203]

**Pseudocode**
```
fd = BL / -f ; T = AAT / GAT * fd                     # p.201
threshold = start_equity + T - fd                     # p.202
units = N_const if equity < threshold else floor(equity / fd)
```

**Ambiguities & assumptions**
- **Beyond two contracts.** The author limits validity there. ASSUMPTION: use only for the 1 → 2 step, then switch to 2.1 or 2.11.

### 2.7 Dependency gate and per-state f

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Statistical filter on the trade sequence; conditional sizing | 51–65, 206–207 |
| Timeframe & holding period | Trade sequence of the host system | 51 |
| Universe / eligibility filters | ≥ 30 closed trades (Student's t below 30 for the correlation test) | 51, 65 |
| Market / regime filter | n/a | — |
| Setup conditions | Runs test: X = 2·W·L; Z = (N·(R − .5) − X)/√(X·(X − N)/(N − 1)); zero P&L counts as a loss. Lag-1 correlation of P&Ls; turning-points and phase-length tests | 52–54, 56–64 |
| Entry trigger & order type | Act on dependency only above 95.45% confidence (some require > 99%), across markets and parameter values | 55, 61–62 |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | If dependency is proven, segregate trades by state (e.g. after win / after loss) and compute f per state. Do not bet in a state with negative expectation | 206–207 |
| Adding to / pyramiding | n/a | — |
| Portfolio limits | n/a | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Minimum trades | 30 | — | 51 |
| Confidence | 95.45% (2σ) minimum | > 99% | 55 |
| Lag-1 correlation of note | \|r\| > .25–.30 | — | 59 |
| Turning points | E = 2/3·(N − 2); Var = (16N − 29)/90 | — | 62–63 |
| Example | 423 trades, Z = −1.9739: "pass trades after a loss until a would-be winner is passed" improved the system | — | 55–56 |
| Per-state example | P(win) .55 after a win → f .325; .45 after a loss → f .175 | after-loss P .3 → negative expectation → no bet | 206–207 |

**Key quotes**
- "you will need a minimum of 30 closed trades." [p. 51]
- "You really need to exceed 95.45% as a bare minimum to assume that there is dependency involved" [p. 55]
- "Even if a system showed dependency to a 95% conﬁdence limit for all values of a parameter, that conﬁdence limit is hardly high enough" [p. 62]
- "you would bet the optimal amount only after a win, and you would not bet after a loss." [p. 207]
- "you must segregate the trades of the market system based upon the dependency and treat the segregated trades as separate market systems." [p. 207]

**Pseudocode**
```
w = [1 if t > 0 else 0 for t in trades]                # zero counts as loss (p.52)
N=len(w); W=sum(w); L=N-W; R=number_of_runs(w); X=2*W*L
Z = (N*(R-.5) - X) / sqrt(X*(X-N)/(N-1))               # p.52-54
dependent = N >= 30 and abs(Z) >= 2.0 and holds across markets/params   # p.55, 61-62
if dependent:
    for state in {after_win, after_loss}:
        sub = trades following that state
        f[state] = optimal_f(sub) if mean(sub) > 0 else 0   # p.206-207
```

**Ambiguities & assumptions**
- **Partly codable:** "across markets and parameters" is not quantified. ASSUMPTION: require |Z| ≥ 2 in ≥ 80% of tested markets and parameter values; otherwise treat the trades as independent.

### 2.8 Binomial validation gate

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Statistical validation of a system's (or indicator's) hit rate | 99–102 |
| Timeframe & holding period | Any sample of N trades or forecasts | 100 |
| Universe / eligibility filters | Trades independent, classifiable into two exclusive groups, constant probability | 101 |
| Market / regime filter | n/a | — |
| Setup conditions | Observed win rate P over N trades; choose Z (σ) | 100 |
| Entry trigger & order type | Accept the system only if its lower bound clears breakeven (e.g. > 50% at 1:1 payoff) | 101–102 |
| Initial stop-loss | n/a | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | n/a | — |
| Adding to / pyramiding | n/a | — |
| Portfolio limits | n/a | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lower bound | L = P − Z·√(P·(1 − P)/(N − 1)) | — | 100 |
| Example | P .51, N 100, Z 3 → L = 35.93% | 99.865% one-tailed | 100 |
| Trials needed | 51% at 1:1, 3σ → N = 22,492 | any Z | 101–102 |

**Key quotes**
- "This technique can also be used for statistical validation of trading systems." [p. 100]
- "the technique can also be used to determine the conﬁdence level for a given market indicator." [p. 101]

**Pseudocode**
```
L = P - Z*sqrt(P*(1-P)/(N-1))                         # p.100
pass = L > breakeven_win_rate(payoff)                  # p.101-102
N_required = Z**2 * P*(1-P)/(P - breakeven)**2 + 1
```

**Ambiguities & assumptions**
- **Unequal payoffs.** Breakeven for unequal payoffs is not given. ASSUMPTION: breakeven = avg_loss/(avg_win + avg_loss).

### 2.9 Static fractional f

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Diluted fixed-fraction sizing | 174–175, 212–215 |
| Timeframe & holding period | Per trade or holding period | — |
| Universe / eligibility filters | Any system with optimal f from 2.1, 2.3 or 2.4 | — |
| Market / regime filter | n/a | — |
| Setup conditions | Choose FRAC in (0,1) | 174 |
| Entry trigger & order type | n/a (host system) | — |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Units = equity / (f$/FRAC). Expected: FAHPR = (AHPR − 1)·FRAC + 1; FSD = SD·FRAC; FGHPR = √(FAHPR² − FSD²) | 213–214, 351 |
| Adding to / pyramiding | Re-size with total equity | — |
| Portfolio limits | Hedge ratio H = Σf_i × FRAC | 363 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| FRAC | .5 (half f) | 0 … optimal; .2, .1 examples | 174, 351 |
| Time to goal | T = ln(goal)/ln(FGHPR) | half f doubles in 15.47 vs 11.77 plays (2:1 coin) | 215, 353 |

**Key quotes**
- "This price is not as steep as being too far to the right, so if you must err, err to the left." [p. 175]
- "you reduce your drawdowns arithmetically. How- ever, you also reduce your returns geometrically." [p. 175]

**Pseudocode**
```
units = floor(equity * FRAC / f_dollars)
FAHPR = (AHPR-1)*FRAC + 1 ; FSD = SD*FRAC ; FGHPR = sqrt(FAHPR**2 - FSD**2)   # p.213-214
```

**Ambiguities & assumptions**
- The author prefers 2.10 over 2.9 in the long run [p. 356]. ASSUMPTION: implement 2.9 as the baseline for comparison only.

### 2.10 Dynamic fractional f (split equity) with reallocation

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Diluted sizing with built-in portfolio insurance | 347–369 |
| Timeframe & holding period | Daily re-sizing; reallocation infrequent | 348, 358 |
| Universe / eligibility filters | Any system or portfolio with optimal fs | 348 |
| Market / regime filter | n/a | — |
| Setup conditions | Initial active fraction FRAC; inactive$ = (1 − FRAC)·start equity, held constant | 348 |
| Entry trigger & order type | n/a (host system) | — |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Daily: active = total equity (marked to market) − inactive$; units = active / f$ at FULL optimal f | 348, 356 |
| Adding to / pyramiding | Reallocate (reset the split) only after T periods from (10.05) or at the upside target Y = FRAC·G^T − FRAC; ideally never | 354–355, 358, 367–368 |
| Portfolio limits | Initial active ≈ half the maximum tolerable drawdown; sum f across components; hedge ratio H = Σf_i·active/total | 359, 363 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| FRAC (initial active) | .5 example; rule of thumb = ½ max tolerable DD (20% DD → 10%) | .2, .1, .05 examples | 348, 359 |
| Overtake test | FGHPR^T ≤ G^T·FRAC + 1 − FRAC | quarterly T = 63 passes at G 1.01933, FRAC .2 | 354–355 |
| Upside reallocation target | 5% initial → +13.63% on the account (independent of G and T) | active then 16.395% | 368–369 |
| Time to goal (dynamic) | T = ln((goal − 1)/FRAC + 1)/ln(G) | .1 active doubles in 125 vs static 269 days | 352–354 |

**Key quotes**
- "It is the equity in the active subaccount that you use to determine how many units to trade." [p. 348]
- "You always use the full optimal fs with this technique." [p. 348]
- "In the long run, you are better off to practice asset allocation with a dynamic fractional f technique." [p. 356]
- "Ideally, you will only make this division between active and inactive equity once, at the outset of the program." [p. 358]
- "Set your initial active equity at one half of the maximum drawdown you can tolerate." [p. 359]
- "most money managers will ﬁnd it advantageous to reallocate based on upside progress rather than elapsed holding periods." [p. 368]

**Pseudocode**
```
inactive = (1 - FRAC) * start_equity                  # FRAC ~ maxDD_tolerable/2 (p.359)
each day:
    active = total_equity_mtm - inactive              # p.348
    for each component i: units_i = floor(active / f_dollars_i)   # full optimal f (p.348)
    if total_equity >= start_equity * (1 + FRAC*G**T_star - FRAC):  # upside target (p.367-368)
        start_equity = total_equity ; inactive = (1 - FRAC) * start_equity   # reallocate
    if active <= 0: stop trading                      # floor = inactive (p.349, 363)
```

**Ambiguities & assumptions**
- **Downside reallocation.** Not specified; the author says reallocation also adds equity after drawdowns but discourages frequent resets [p. 358]. ASSUMPTION: no downside reallocation; stop at the floor.
- **T* for the upside target.** Solve (10.05) by iteration [p. 355]. ASSUMPTION: integer search on T.
- **Portfolio-insurance reallocation** (set active% = call delta / Σf) is described [p. 364] but the author says it "probably isn't such a good idea" because it reallocates constantly. ASSUMPTION: excluded.

### 2.11 Continuous dominance (gradient switching)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mode-switching overlay for diluted f: constant contract → static f → dynamic f | 369–375 |
| Timeframe & holding period | Re-evaluated before each holding period | 372–373 |
| Universe / eligibility filters | Accounts trading a diluted f (FRAC < 1) | 369–370 |
| Market / regime filter | n/a | — |
| Setup conditions | FRAC, G at full f, AHPR at full f, FGHPR (2.9) | 372 |
| Entry trigger & order type | Use the mode whose gradient is highest at the current T: constant contract (AHPR − 1)·FRAC; static FGHPR^T·ln FGHPR; dynamic G^T·ln(G)·FRAC | 372–373 |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Constant contract: units fixed at the initial FRAC sizing. Static: equity/(f$/FRAC). Dynamic: (equity − inactive)/f$ | 374–375 |
| Adding to / pyramiding | Preferred: switch at upside % gains (T converted to Y via 10.12/10.13) | 375 |
| Portfolio limits | Sensitive to landscape changes; better suited to drawdown-minimising small f | 386–387 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Example | 2:1 coin, FRAC .2, G 1.06066, AHPR 1.125, SD .375: constant contract periods 1–2, static from 3, dynamic from 17 | $200 start: bet $10; play 17: (292 − 160)/4 = 33 bets | 373–375 |

**Key quotes**
- "Whichever of these three equations results in the greatest value is the technique we go with." [p. 373]
- "by always trading that technique which has the highest gradient at the moment, we ensure the probability of the account being at its greatest equity at any point in time." [p. 370]

**Pseudocode**
```
grad_cc  = (AHPR-1)*FRAC                               # 10.14
grad_st  = FGHPR**T * ln(FGHPR)                        # 10.15
grad_dyn = G**T * ln(G) * FRAC                         # 10.16
mode = argmax(grad_cc, grad_st, grad_dyn)  (evaluated at elapsed periods T)   # p.373
units = {cc: units0, st: floor(equity*FRAC/fd), dyn: floor((equity - (1-FRAC)*E0)/fd)}[mode]
```

**Ambiguities & assumptions**
- **Monotone switching.** The text implies modes progress one way. ASSUMPTION: never switch back to an earlier mode.

### 2.12 Drawdown-defined f$ and composite-f exposure

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Sizing rule fixing the worst-scenario drawdown in advance | 377–378 |
| Timeframe & holding period | Per holding period | — |
| Universe / eligibility filters | Money managers with a hard drawdown tolerance | 377 |
| Market / regime filter | n/a | — |
| Setup conditions | Max tolerable DD% must not exceed optimal f, else you are right of the peak | 377 |
| Entry trigger & order type | n/a (host system) | — |
| Initial stop-loss | n/a (host system) | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | f$ = \|biggest loss scenario\| / maxDD%; with n components, f$ = \|BL\| / (maxDD%/n) | 377 |
| Adding to / pyramiding | n/a | — |
| Portfolio limits | Composite f = Σf_i is the drawdown you must expect when worst cases coincide; trade few components with small f and many holding periods | 359, 387 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Example | 20% DD, worst −$1,000 → f$ $5,000 | if optimal f is .1, DD .2 is right of the peak | 377 |
| Low-f growth equivalence | f .01 needs 484 plays to match 40 plays at .25 (TWR 10.55) | — | 386 |

**Key quotes**
- "what he has accomplished is that the drawdown to be experienced with the manifestation of the single catastrophic event is deﬁned in advance." [p. 377]
- "the money manager must make certain that the maximum drawdown percent is not greater than the optimal f" [p. 377]
- "if a trader must minimize drawdowns, he or she is far better off to trade at a very low f value and get off many more holding periods in the same span of time." [p. 386]
- "we trade as few components as possible, with as small an f for each component as possible" [p. 387]

**Pseudocode**
```
dd = min(maxDD_tolerable, f_opt)                       # guard (p.377)
f_dollars_i = abs(BL_i) / (dd / n_components)          # 10.17b
assert sum(abs(BL_i)/f_dollars_i) <= maxDD_tolerable   # composite f (p.359, 387)
```

**Ambiguities & assumptions**
- **Clamping.** The book warns but does not say what to do when DD% > f. ASSUMPTION: clamp to f.

### 2.13 Margin-constrained upside limit on active equity

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Portfolio constraint (maximum fraction without an initial margin call) | 365–366 |
| Timeframe & holding period | At each re-size | — |
| Universe / eligibility filters | Margined instruments (futures, F&O) | 365 |
| Market / regime filter | n/a | — |
| Setup conditions | f$_k and initial margin_k for every component | 365 |
| Entry trigger & order type | n/a | — |
| Initial stop-loss | n/a | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | L = max f$ / Σ_k((max f$ / f$_k)·margin_k). Active fraction (dynamic) or FRAC (static) ≤ L | 365–366 |
| Adding to / pyramiding | n/a | — |
| Portfolio limits | Prefer ~3 spectrums at full f over 10 heavily diluted; optimal count is "but a handful" | 366 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Example | f$ $2,500 and $1,500 → L = 17.434%; $100k → margin $99,943.93 | — | 366 |

**Key quotes**
- "you are usually better off to trade three scenario spectrums at the full optimal f levels than to trade 10 at dramatically re- duced levels" [p. 366]

**Pseudocode**
```
mx = max(fd_k)
L = mx / sum((mx/fd_k) * margin_k for k)              # 10.08
FRAC_eff = min(FRAC, L)
```

**Ambiguities & assumptions**
- None material.

### 2.14 Geometric-optimal mean–variance portfolio on optimal-f inputs

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Portfolio allocation (Markowitz E–V, levered to the geometric optimum) | 259–310 |
| Timeframe & holding period | Fixed-length HPRs (days, weeks, months) identical for all components and correlations | 260, 302 |
| Universe / eligibility filters | Market systems with optimal f; inputs must have finite variance | 259 |
| Market / regime filter | n/a | — |
| Setup conditions | Per component: daily HPR = A/f$ + 1 (or equalized D$/f$ + 1); E = mean(HPR) − 1; V = var(HPR); pairwise correlations of HPRs | 302 |
| Entry trigger & order type | n/a | — |
| Initial stop-loss | n/a | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Solve the Lagrangian system for min V at a given E (Gauss–Jordan or inverse matrix). Drop any component with a negative weight and re-solve. Add NIC (HPR 1, variance 0) with Σweights = 3 × #systems. Iterate E until AHPR − 1 = V (geometric optimal); raise S until NIC appears. Adjusted f$_i = f$_i / weight_i | 264–268, 279–280, 291, 297–303 |
| Adding to / pyramiding | Recompute daily with equalized f$ if used | 303 |
| Portfolio limits | Shorts: return = expected % gain − dividends; multiply the correlations of the shorted component by −1. Remove a zero-variance component with AHPR > 1. RFR > 0: subtract the RFR from component returns (not NIC); RFR = 0 for futures | 283–284, 300, 308, 310 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Σ weights for the unconstrained problem | 3 × number of systems (e.g. 12) | raise until NIC is in the solution | 298, 301 |
| Geometric optimum condition | AHPR − 1 = V (8.05) | L1 = −2 (unconstrained); L2 = 0 when Σ = 1 | 291, 306 |
| Leverage factor | q ≈ (E − RFR)/V on the tangent portfolio | example 1.9195 | 307–308 |
| Example | Toxico adjusted f$ $2,436.69 | — | 303 |

**Key quotes**
- "A good initial value is three times the number of market systems" [p. 298]
- "If NIC is not one of the components in the geometric optimal portfolio, then you must make your sum of the weights constraint, S, higher." [p. 301]
- "The way to do this is to divide the optimal fs for each component by its corresponding weight." [p. 303]

**Pseudocode**
```
for i: hpr_i[t] = pnl_1unit_i[t]/fd_i + 1 ; E_i = mean(hpr_i)-1 ; V_i = var(hpr_i)    # p.302
C = cov matrix of hpr series (+ NIC row/col of zeros, E_NIC = 0)                      # p.298-299
def solve(E, S): minimise x'Cx s.t. sum(x*E_vec)=E, sum(x)=S  (drop negatives, re-solve)   # p.279-280
S = 3*n
repeat: E* = bisect E until (E) == V(x(E)) ; if x_NIC == 0: S *= 1.5            # p.297, 301
adj_fd_i = fd_i / x_i  for non-NIC i ; units_i = floor(equity / adj_fd_i)        # p.303
```

**Ambiguities & assumptions**
- **Solver.** The book solves by hand (row operations). ASSUMPTION: any QP solver with non-negativity; this reproduces the drop-and-resolve rule.
- **Correlation detrending.** Optional detrending of equity curves before correlation, with cautions [p. 304–305]. ASSUMPTION: off by default.
- The author later rejects correlation as the joint-movement parameter (correlations jump in big moves, [p. 313–320]), so 2.15/2.16 supersede this. Keep 2.14 as a benchmark.

### 2.15 Leverage Space Model: max G via genetic algorithm

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Portfolio allocation over joint scenario spectrums | 323–346 |
| Timeframe & holding period | One common holding period for all spectrums | 412 |
| Universe / eligibility filters | Scenario spectrums (2.4) per market system; joint probabilities between spectrums | 329–331 |
| Market / regime filter | n/a | — |
| Setup conditions | m = Π(#scenarios); k runs odometrically over all combinations; Prob_k from joint probabilities | 329–330 |
| Entry trigger & order type | n/a | — |
| Initial stop-loss | n/a | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Maximise G(f1…fn) = (Π_k HPR_k)^(1/ΣProb_k), with HPR_k = (1 + Σ_i f_i·(−PL_k,i/BL_i))^Prob_k and f_i > 0 (may exceed 1). Then f$_i = BL_i / −f_i | 329, 332, 336 |
| Adding to / pyramiding | Re-optimise each holding period as scenarios change (f shift) | 366–367 |
| Portfolio limits | Use a few spectrums; composite f = Σf_i is the simultaneous worst-case loss | 359, 366 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Joint-probability proxy | Prob_k = (Π pairwise P)^(1/(n−1)) | valid only for n ≤ 2 or zero correlation; use empirical joint frequencies | 329–331 |
| Example | 3 coins, f .1 → G 1.119131; optimum .21 each → G 1.174516; f$ 4.76 | 2 coins uncorrelated .23 each; +1 correlation .125 each | 323, 335–336 |
| GA gene | 12 bits per variable, divisor 1,000 (0–4.095) | — | 341–342 |
| GA crossover / mutation | .6–.9 (per bit: prob/gene length); mutation ≤ .001 | with elitism: crossover 2, mutation .05 | 343, 345 |
| GA stop | X unimproved generations | larger population and X → exact | 344–346 |

**Key quotes**
- "This is the objective function, the equation we wish to maximize." [p. 332]
- "(Important: Objective function values must be non-negative!)" [p. 342]
- "It is often advantageous to carry the strongest individual’s code to the next generation in its entirety." [p. 345]
- "If you bet 25% or more on each game, you will now go broke" [p. 323–324]

**Pseudocode**
```
combos = product(*[range(len(spec_i)) for spec_i in spectra])     # odometric (p.330)
def G(fvec):
    logsum = 0; psum = 0
    for k in combos:
        p = joint_prob(k)                                         # empirical (p.331)
        c = 1 + sum(fvec[i] * (-spectra[i][k[i]].pl / BL[i]) for i)
        if c <= 0: return 0                                       # ruin -> non-negative objective (p.342)
        logsum += p*ln(c); psum += p
    return exp(logsum/psum)                                       # 9.01-9.04
f_star = genetic_algorithm(G, bits=12, divisor=1000, pop=..., pc=.6-.9, pm<=.001, elitism, stop=X_unimproved)   # p.341-345
fd_i = BL[i] / -f_star[i]
```

**Ambiguities & assumptions**
- **Joint probabilities.** The (9.03) estimator is admitted to be invalid beyond 2 spectrums with nonzero correlation [p. 331]. ASSUMPTION: estimate Prob_k from co-occurrence counts of binned historical holding-period outcomes.
- **Population size and X.** Not given. ASSUMPTION: population 100, X = 50.

### 2.16 Leverage Space Model with drawdown constraint RD(b)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Portfolio allocation: maximise growth subject to a drawdown-probability limit | 401–438 |
| Timeframe & holding period | Horizon q = holding periods to a target, T = log_G(target), or a fixed period (e.g. a quarter) | 437–438 |
| Universe / eligibility filters | As 2.15. Assumes no serial dependency, or encodes dependency rules into the outcome stream | 411, 422–423 |
| Market / regime filter | n/a | — |
| Setup conditions | b = 1 − tolerable drawdown (e.g. .8 for 20%); acceptable probability x | 423 |
| Entry trigger & order type | n/a | — |
| Initial stop-loss | n/a | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Maximise G (2.15) subject to RD(b, q) ≤ x. RD = Σ_k β_k·p_k / Σp_k over all n^q outcome sequences. β_k = 0 if the running product, capped at 1.0 from equity highs, ever ≤ b. Multi-spectrum HPR = arithmetic mean of component HPRs | 412–413, 421–424 |
| Adding to / pyramiding | Re-solve each period | — |
| Portfolio limits | Sampling when n^q > (s/x)²·.25 (6,250,000 at 5σ/.001). Fit RX(q) = asymptote − A·e^(−Bq); for RD fix the asymptote at 1 | 425–427, 433–435 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| b | 1 − DD (e.g. .8 for 20%) | .6 examples | 404, 423 |
| Example | 2:1 coin, f .25: RR(.6) = .25 at q = 2–4, .3125 at q = 5, asymptote .48406 | — | 404–411 |
| Sample size | (s/x)²·p(1 − p), p = .5 | s 2, 3, 5; x .001 | 425–426 |
| Real example | 10-scenario spectrum, f .45: RR(.6, 10) = .1906955154 | — | 427 |
| Horizon | T = log_G(target): 1.5 at G 1.1 → 4.254164 | next quarter | 437 |
| RNG | Mersenne Twister | — | 426 |

**Key quotes**
- "Maximize TWR where RD(b) < = an acceptable probability of hitting b." [p. 424]
- "if at any time in the running product of HPRs, if the running product is greater than 1.0, then the value 1.0 is replaced for the running product at that point." [p. 414]
- "We can use it to know, for instance, what the probability of drawdown is over, say, the next quarter." [p. 437]
- "in risk-of-ruin calculations, order does matter(!)" [p. 406]

**Pseudocode**
```
def beta(seq, b, drawdown=True):                       # 12.03a, Java B() p.417
    run = 1.0
    for h in seq:
        run = (min(run, 1.0) if drawdown else run) * h
        if run <= b: return 0
    return 1
def RD(fvec, b, q):
    hpr_k, prob_k = composite outcomes (mean HPR across spectra, joint prob)   # p.412, 421
    N = len(hpr_k)
    if N**q <= 6_250_000: seqs = all sequences          # p.427
    else: seqs = random sample of 6_250_000 (Mersenne Twister)
    num = sum((1 - beta(s,b)) * prod(prob[s])) ; den = sum(prod(prob[s]))
    return num/den
f_star = GA maximise G(f) with penalty: G := 0 if RD(f, b, q_horizon) > x      # p.424
```

**Ambiguities & assumptions**
- **Choice of q.** The book offers either the horizon to a target return or a calendar horizon [p. 437–438]. ASSUMPTION: q = number of holding periods in one quarter.
- **The book's β.** Its β is computed as the integer of Σ(TWR − b)/Σ|TWR − b| [p. 405]. The Java `B()` returns 0 or 1 by that formula. ASSUMPTION: the explicit "ever ≤ b" test above. It matches the stated definition ("if at any arbitrary q, we have a value <= 0, … ruin has occurred" [p. 405]) but may differ from the Java at exact equality.

### 2.17 Practitioner risk-per-trade / VaR sizing (Ch. 11)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position sizing as practised by large trend-following CTAs (described, not endorsed) | 391–400 |
| Timeframe & holding period | Long-term trend following; re-size anything from continuously to at rollover | 393 |
| Universe / eligibility filters | About 20 liquid markets (give or take 6); some trade all markets | 393 |
| Market / regime filter | n/a (host system) | — |
| Setup conditions | Per-market risk % chosen so that ≤ 1% of months (3 of 300 in 25 years) lose > 20%. Then a portfolio scaling factor so the whole portfolio meets the same test | 398–399 |
| Entry trigger & order type | n/a (host system); staggered entries via parameter arrays are common | 394 |
| Initial stop-loss | Volatility-based: e.g. 3 × average range of the last X bars, or the lowest low of X bars | 392 |
| Exits: profit-taking | Rarely any; trailing stop that exits or flips | 395 |
| Exits: trailing / time / signal | Trailing stop | 395 |
| Position sizing | Contracts = equity × risk% × scaling factor / risk per contract (entry-to-stop $) | 391, 399 |
| Adding to / pyramiding | Almost never | 395 |
| Portfolio limits | Correlation largely ignored; conservative scaling = 1/#systems | 392, 399 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Risk per trade | 1% | 0–2% | 391–392 |
| Example | $1,000,000 × .04 × .7 / $5,000 = 5.6 contracts | — | 399 |
| Allocation to trading | 20% "mainstream" | 5–50%; stop = lesser of 2% or 20%/#markets | 397 |

**Key quotes**
- "Typically, this is in the neighborhood of 0 to 2 % per trade." [p. 392]
- "There is always seemingly a recent volatility metric that is employed in the quantity calculation." [p. 392]
- "The techniques shown in this chapter will give an overly optimistic assessment of the potential risk." [p. 400]

**Pseudocode**
```
stop_dist = 3 * ATR(X)            # or entry - lowest_low(X)   (p.392)
risk_pct_m = calibrate so <=1% of historical months lose >20%     # p.398
scale = calibrate portfolio-wide (or 1/n_systems)                 # p.399
contracts = floor(equity * risk_pct_m * scale / (stop_dist * dollars_per_point))
```

**Ambiguities & assumptions**
- **X and multiplier.** Not fixed; "3" is the example multiplier. ASSUMPTION: X = 20 bars.
- The author states this method understates risk relative to 2.16 [p. 400]. Use 2.17 as an industry baseline.

### 2.18 Finite-horizon f targets (EACG, GRR, left inflection)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Alternative f targets when the horizon T is known | 233–240, 376–382 |
| Timeframe & holding period | Known number of holding periods T (e.g. 63 days per quarter) | 382 |
| Universe / eligibility filters | Positive-expectancy spectrums | — |
| Market / regime filter | n/a | — |
| Setup conditions | Scenario spectrum or trade list | — |
| Entry trigger & order type | n/a | — |
| Initial stop-loss | n/a | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | EACG: uniform f maximising the expected average compound growth over T plays (2:1 coin: T = 1 → 1.0, 2 → .5, 3 → .37868, ∞ → .25). GRR: maximise TWR_T / Σf. Left inflection: f where d²TWR_T/df² = 0, left of the peak | 233–240, 378–381 |
| Adding to / pyramiding | n/a | — |
| Portfolio limits | Multi-spectrum inflection may not exist | 382 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Quarter horizon | T = 63 daily periods | — | 382 |
| Left inflection, 2:1 coin | → .23 at T = 800 | converges to optimal f as T → ∞ | 381 |

**Key quotes**
- "the f that is optimal—for ﬁnite as well as inﬁnite streams—is uniform." [p. 235]
- "He would use a value of 63 for T and set himself at those coordi- nates to be optimal for each quarter." [p. 382]

**Pseudocode**
```
EACG(f, T) = mean over all 2^T (n^T) outcome paths of (prod HPR)^(1/T)   # p.236-239
GRR(f, T)  = TWR(f)**T / sum(f)                                           # 10.18
f_infl     = root of d2/df2 [G(f)**T] for f < f_opt                       # p.380-382
```

**Ambiguities & assumptions**
- **Partly codable:** the book gives no rule for choosing among the three targets. ASSUMPTION: report all three as diagnostics; trade at min(f_infl, f_opt).

### 2.19 Utility-weighted (utils) optimal f

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Sizing for investors whose utility is not ln | 250–253 |
| Timeframe & holding period | Re-solved each holding period | 251 |
| Universe / eligibility filters | Scenario spectrums with outcomes restated in utils; at least one negative-util scenario; positive util expectation | 251 |
| Market / regime filter | n/a | — |
| Setup conditions | Map each scenario's $ outcome to utils given current wealth (utility curve via certainty equivalents, [p. 246–250]) | 251 |
| Entry trigger & order type | n/a | — |
| Initial stop-loss | n/a | — |
| Exits: profit-taking | n/a | — |
| Exits: trailing / time / signal | n/a | — |
| Position sizing | Optimal f on utils; contracts = cumulative utils / util-f$. The $-f becomes non-uniform over time | 251–252 |
| Adding to / pyramiding | Update the util values as wealth changes | 252 |
| Portfolio limits | You still pay for being sub-optimal on the wealth landscape | 253 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Example | 2:1 coin with win = 1.5 utils, loss −1 → f .166666 | next period win 1.4 utils | 252 |
| Utility questionnaire | extremes 3–5 × largest expected trade win/loss; computed utility = U·P(best) + V·P(worst) | — | 246, 248 |

**Key quotes**
- "you simply substitute utils in lieu of dollars." [p. 251]

**Pseudocode**
```
utils_k = U(wealth + pnl_k) - U(wealth)              # ASSUMPTION: utility from questionnaire
f_u = optimal_f(scenarios with outcomes utils_k)     # 2.4
contracts = floor(cum_utils / (min(utils_k) / -f_u))
```

**Ambiguities & assumptions**
- **Partly codable:** the utility function is personal and elicited by questionnaire. ASSUMPTION: a CRRA power utility as a placeholder.

### Non-codable / no-rule material (summary)

| Item | Content | Page |
|---|---|---|
| Growth functions, why f is optimal | Exponential vs hyperbolic growth; Rolle's theorem proof of a single peak; f indifferent to T | 227–233 |
| Utility theory background | Expected-utility theorem, risk-aversion derivatives, Wentworth's survival hypothesis | 241–246 |
| Correlation instability study | 8 markets 1987–2006: CL/GC .18 all days, .61 on CL > 3σ days, .09 within 1σ | 313–320 |
| Why the new framework | Leverage = borrowing AND the schedule of progressing quantity | 321–322 |
| Optimiser families | Simplex, Powell, conjugate gradient, quasi-Newton, natural simulation | 339–341 |
| f shift | Peak moves; recent winners tend to underperform; build scenarios accordingly | 366–367 |
| Drawdown causes | Liquidity (single-trade disasters), not knowing your position, protracted losing streaks | 383 |
| CTA practice notes | Parameter arrays, staggered entries, optimisation in thirds/fourths, anti-trend overlays, Turtles | 393–397 |
| Feller gambler's ruin | Constant-stake ruin formula; in an unfavourable game bet big and quit early | 402–403 |

## 3. Risk & money-management rules

- Never size a negative-expectation system; no money-management scheme fixes it [p. 42, 134].
- Size off the largest losing trade, not the maximum drawdown. The drawdown is sequence-dependent; the largest loss is controllable [p. 163, 168].
- Expect a historical drawdown of at least f% at optimal f [p. 168], and 80–95% drawdowns are common [p. 170].
- Use a single combined bankroll and recapitalise sub-allocations daily [p. 204–206].
- If you must err, err to the left of optimal f [p. 175].
- For portfolios, Σf is the worst-case simultaneous loss on active equity; "All correlations revert to one" [p. 359, 387].
- Margin cap L (2.13) [p. 365–366]. Dollars per contract = max(initial margin, f$) [p. 171].
- Reallocate between active and inactive equity rarely; prefer upside triggers [p. 358, 368].
- Liquidity is the common cause of single-trade disasters; always know your position [p. 383].

## 4. Non-codable guidance

- Risk is the probability of touching a lower equity barrier (ruin or drawdown), not variance [p. 16, 413].
- Building a personal utility-preference curve via certainty equivalents [p. 246–250].
- Scenario construction: cover ~99% of outcomes, avoid the three-scenario trap, use one holding period [p. 189, 198].
- Diversification increases the number of holding periods per unit time; it does not reduce risk at optimal leverage [p. 313, 382].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - per-trade 1-unit P&L for each host strategy on NSE instruments;
  - daily closes for equalisation (2.3);
  - F&O lot sizes and SPAN + exposure margins (2.1 per-unit max, 2.13);
  - binned joint daily or weekly outcomes across components (2.15–2.16).
- **Testability with our data:** 2.1–2.13 and 2.17 are mechanical given a trade list and prices. 2.14–2.16 need a solver or GA plus joint-outcome histograms; with sampling, they are feasible.
- **Market-structure differences:**
  - NSE index and stock-future lots are large relative to small accounts, so integer constraints bite. Use 2.5/2.6, or cash equity with share-level units.
  - Equalised f (2.3) suits cash equities where price levels change a lot.
  - Circuit limits and overnight gaps can exceed the historical biggest loss. ASSUMPTION: stress BL × 1.5 in 2.1 and 2.12.
  - Cash short selling is intraday only, so short-side scenarios should use futures; 2.14 flips the correlation sign for shorts [p. 284].
  - RFR = 0 for futures portfolios per the book [p. 308]; use the T-bill rate only for cash-equity leverage.

## 6. Verdict

- **Codeability:** High. 15 of 19 sections are fully specified formulas with worked examples (2.1–2.6, 2.8–2.17). 2.7, 2.18 and 2.19 need judgment calls. No entry/exit logic.
- **Priority for backtesting:** High as a sizing/allocation library for every other spec. Implement in this order:
  1. 2.1 + 2.3 (optimal f diagnostics);
  2. 2.10 with the half-max-drawdown rule and 2.13;
  3. 2.16 (RD-constrained allocation) for multi-strategy portfolios;
  4. 2.17 as the industry baseline to compare against.
- **Top 3 things a coder is most likely to get wrong**
  1. Using Kelly on average win / average loss, or treating f as "percent of equity". Run the TWR search on the actual trade list and convert with f$ = biggest loss / −f [p. 142, 155].
  2. Sizing a portfolio with each component's standalone f. The fs must be solved jointly (two uncorrelated 2:1 coins: .23 each, not .25), and Σf is the simultaneous worst-case loss [p. 207–208, 313, 359].
  3. Implementing dynamic fractional f as a static fraction, or reallocating it every period. Keep the inactive dollars constant, size on equity − inactive at full f, and reallocate only after the T or upside threshold [p. 348, 358, 368].
