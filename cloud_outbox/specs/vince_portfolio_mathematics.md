# The Handbook of Portfolio Mathematics: Formulas for Optimal Allocation & Leverage — Ralph Vince (John Wiley & Sons, 2007)

- **Source file:** Google Drive `Vince, Ralph - The Handbook of Portfolio Mathematics_ Formulas for Optimal Allocation & Leverage-John Wiley & Sons, Inc (2008).pdf` (file id `1lvjfeEskPixljpjPhr6neRmHannulPzP`, 3,816,214 bytes), 446 PDF pages with a text layer.
- **Text file used:** text/vince_portfolio_mathematics.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index). The printed page number is usually PDF page − 24 (printed p. 117 = [[PAGE 141]]), but always take N from the marker.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/vince_portfolio_mathematics.md text/vince_portfolio_mathematics.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read sequentially:
  - [[PAGE 1]] to [[PAGE 66]] (front matter, Preface, Introduction, Ch. 1);
  - [[PAGE 123]] to [[PAGE 446]] (Ch. 3–12, Postscript, Index).
  - **Skipped:** Chapter 2 "Probability Distributions", [[PAGE 67]]–[[PAGE 122]]. It is a statistics primer (moments; Normal, Lognormal, Binomial, Poisson, Student's and other distributions) and contains no trading or sizing rules.
  - **Scanned, not read cell by cell:** the long numeric spreadsheet tables (Ch. 4 f-value/TWR grids, [[PAGE 158]]–[[PAGE 167]]; Ch. 7 matrix row operations, [[PAGE 268]]–[[PAGE 283]]; Ch. 9 correlation grids, [[PAGE 316]]–[[PAGE 319]]). The prose stating their conclusions was read.
  - This book contains **no entry/exit signals**. Every "strategy" below is a position-sizing or allocation algorithm meant to be layered on a separate trading system.

## 1. The method in brief

Vince's thesis: for any positive-expectancy stream of independent outcomes, growth is maximised by betting a **fixed fraction** of equity. The best such fraction, **optimal f**, maximises the geometric mean HPR (equivalently the Terminal Wealth Relative, TWR) [p. 141–150].

**Core quantities**
- Contracts are sized as one unit per **f$ = |biggest loss| / f** of equity [p. 150].
- Kelly's formula equals optimal f only when all wins and all losses are fixed sizes [p. 145–146, 155].

**Sizing to the right of the peak**
- Betting to the right of the optimal-f peak cuts growth and can turn a winning system into a losing one [p. 161–163, 175].
- Optimal f implies historical drawdowns of at least f% of equity [p. 168–169].
- Practical users therefore dilute: static fractional f, or the preferred **dynamic fractional f** (split equity into active and inactive parts) [p. 347–359].

**Portfolios: the Leverage Space Model**
- For multiple systems, Part I generalises to the **Leverage Space Model**: choose the f vector that maximises the joint geometric mean G over joint scenario probabilities [p. 311–336].
- Part II (Ch. 12) adds the real-world constraint: maximise G subject to the **probability of a given drawdown** staying below a threshold [p. 401–438].

**Evidence:** mathematical derivation plus coin-toss and toy examples. There are no market backtests, apart from a correlation study of 8 markets (1986–2006) showing that correlations jump on > 3-sigma days [p. 314–320].

## 2. Strategies

| # | Strategy | Timeframe | Entry rule (as stated) | Stop / exit (as stated) | Page |
|---|---|---|---|---|---|
| 2.1 | Empirical optimal f sizing | Any (per trade) | From the system's trade P&L list: HPR_i = 1 + f·(−trade_i/biggest loss); TWR = ∏HPR_i. Search f in (0,1] for max TWR (loop by .01, bracketing, or parabolic interpolation). Trade 1 unit per f$ = biggest loss/−f of equity; re-size as equity changes (ideally every trade or day) | Not an exit rule. Requires positive expectation; f > optimal is never beneficial | 146–150, 156, 170–171, 181–184 |
| 2.2 | Kelly (Bernoulli-only shortcut) | Any | If all wins equal and all losses equal: f = ((B+1)·P − 1)/B (or f = 2P − 1 when B = 1) | Do not use averaged wins/losses as B (gives the wrong f, .16 vs true .24 in the example) | 144–146, 155 |
| 2.3 | Equalized optimal f (stocks) | Any | Convert past trades to % of entry price (long: exit/entry − 1; short: entry/exit − 1, net of costs). Find f on these. f$ = biggest % loss × current price × $/point / −f, recomputed as price changes | — | 175–177, 180 |
| 2.4 | Small-account start + threshold to geometric | Per trade | Allocate to the first contract A = max(BL/−f, margin + abs(max DD)). Contracts = INT((equity − A)/(BL/−f)) + 1. Or trade 1 contract until equity reaches T = (AAT/GAT)·(BL/−f), then go to 2 | — | 199–203 |
| 2.5 | Dynamic fractional f (split equity) with reallocation | Daily/holding period | Choose an initial active fraction FRAC (rule of thumb: half the maximum tolerable drawdown). Inactive $ = (1 − FRAC)·equity, held constant. Each period trade full optimal f on active$ = equity − inactive$. Reallocate rarely: only after T periods where FGHPR^T ≤ G^T·FRAC + 1 − FRAC, or equivalently at the upside profit Y = FRAC·G^T − FRAC (e.g., +13.63% for FRAC = 5%) | Built-in floor: trading stops when equity reaches the inactive amount (portfolio-insurance-like) | 347–359, 363, 367–369 |
| 2.6 | Continuous dominance (switching rule) | Per holding period | With a chosen FRAC: start constant-contract; switch to static fractional f when its gradient FGHPR^T·ln(FGHPR) exceeds the constant-contract gradient; switch to dynamic f when G^T·ln(G)·FRAC exceeds the static gradient (coin-toss example: static from period 3, dynamic from period 17) | — | 369–375 |
| 2.7 | Drawdown-budget f$ | Per trade | f$ = abs(biggest loss scenario) / (max tolerable drawdown % / n), n = number of components. Must not put the f used above the optimal f | — | 377 |
| 2.8 | Leverage Space Model, drawdown-constrained | Per holding period | Build scenario spectra (outcome, probability) per component over a common holding period plus joint probabilities. Maximise G(f1..fn) = (∏HPR_k)^(1/ΣProb_k) with HPR_k = (1 + Σ f_i·(−PL_k,i/BL_i))^Prob_k, subject to RD(b) over horizon q ≤ acceptable probability. Search with the genetic algorithm; RD(b) estimated by sampled permutations | Drawdown barrier b re-measured from equity highs (running product capped at 1.0) | 329–336, 341–346, 404–424, 433–438 |
| 2.9 | Practitioner fixed-fractional risk (trend-following funds, as described) | Per trade | Risk x% (typically 0–2%) of equity per trade; contracts = equity × risk% / (stop distance in $), stop = volatility multiple (e.g., 3× average range, or lowest low of X bars). VaR variant: contracts = equity × market risk% × portfolio scaling factor / per-contract stop risk | Mostly trailing stops; no profit targets; no pyramiding | 392, 395, 397–399 |
| 2.10 | Dependency-conditioned sizing (runs test) | Per trade | Only if the runs-test Z score (≥ 30 trades) and serial correlation show dependency at ≥ 95.45% confidence that holds across markets and parameter values: segregate trades by condition, e.g., skip trades after a loss until a winner would have occurred, or use a different f after wins vs losses | — | 51–56, 61–62, 206–207 |

**Parameters**

- **f search:** f ∈ (0,1] by .01 for single systems; parabolic-interpolation tolerance .005 [p. 147, 182].
- **Runs test:** at least 30 closed trades; dependency only at ≥ 95.45% confidence (preferably high-90s) [p. 51, 55].
- **Practitioners:** 1–2% risk per trade; about 20 markets; 25 years of monthly data with ≤ 1% of months losing > 20% [p. 392–393, 398].
- **Sample size for RD estimation:** (s/x)²·p(1 − p), with s = 5, x = .001, p = .5 → 6,250,000 permutations per q [p. 425–427].

**Key quotes**

- "there exists an optimal ﬁxed fraction (f) between 0 and 1 as a divisor of your biggest loss to bet on each and every event." [p. 142]
- "HPR = 1 + f * (−trade/biggest loss)" [p. 146]
- "By looping through all values for f between .01 and 1, we can ﬁnd that value for f which results in the highest TWR." [p. 147]
- "Once the highest f is found, it can readily be turned into a dollar amount by dividing the biggest loss by the negative optimal f." [p. 150]
- "Applying Kelly when wins are not all for the same amount and/or losses are not all for the same amount is a mistake." [p. 145]
- "It does not pay to risk more than the optimal f—in fact, you pay a price to do so!" [p. 163]
- "the drawdown you can expect with ﬁxed fractional trading, as a percentage retracement of your account equity, historically would have been at least as much as f percent." [p. 168]
- "This price is not as steep as being too far to the right, so if you must err, err to the left." [p. 175]
- "The amount of funds allocated toward the ﬁrst contract should be the greater of the optimal f amount in dollars or the margin plus the maximum historic drawdown (on a one-unit basis)" [p. 199]
- "When using ﬁxed fractional trading you are best off operating from a single combined bank." [p. 206]
- "Generally, then, you are better off not to “shrink” your largest historical loss to reﬂect a current low-volatility marketplace." [p. 218]
- "Set your initial active equity at one half of the maximum drawdown you can tolerate." [p. 359]
- "Ideally, you will only make this division between active and inactive equity once, at the outset of the program." [p. 358]
- "Thus, a 5% initial active equity level will always see the dynamic overtake the static at a 13.63% proﬁt on the account!" [p. 368]
- "Most everyone is risking x percent per trade on a given market system." [p. 392]
- "Typically, this is in the neighborhood of 0 to 2 % per trade." [p. 392]
- "Big moves in one market amplify the correlation between other markets, and vice versa." [p. 320]
- "Maximize TWR where RD(b) < = an acceptable probability of hitting b." [p. 424]
- "First, you will need a minimum of 30 closed trades." [p. 51]
- "You really need to exceed 95.45% as a bare minimum to assume that there is dependency involved that can be capital-ized upon to make a substantial difference." [p. 55]

**Pseudocode** (2.1, 2.5, 2.8)

```
# 2.1 Empirical optimal f
trades = list of P&L per 1 unit (net of costs); BL = min(trades)  # negative
require mean(trades) > 0
def TWR(f): return prod(1 + f * (-t / BL) for t in trades)
f_opt = argmax_{f in 0.01..1.00 step .01} TWR(f)          # refine by parabolic interpolation, TOL=.005
G = TWR(f_opt) ** (1/len(trades))
f_dollar = BL / -f_opt                                     # $ equity per unit
units_today = floor(equity / f_dollar)                     # re-size every trade/day (finer = better)

# 2.5 Dynamic fractional f
FRAC = 0.5 * max_tolerable_drawdown                        # rule of thumb from text
inactive = (1 - FRAC) * equity0                            # constant
each period: active = equity - inactive ; units = floor(active / f_dollar)
reallocate only when equity/equity_at_last_realloc - 1 >= FRAC * G**T - FRAC
   where T solves FGHPR**T <= G**T * FRAC + 1 - FRAC ,
   FGHPR = sqrt(((AHPR-1)*FRAC+1)**2 - (SD*FRAC)**2)

# 2.8 Drawdown-constrained Leverage Space (single holding period scenarios)
for candidate f-vector (genetic algorithm):
   G = geometric mean HPR over joint scenarios (eq. 9.01/9.04)
   RD = estimate P(drawdown to b from running equity high within q periods)
        by sampling sequences of q joint outcomes (cap running product at 1.0)
   fitness = G if RD <= x else 0
choose f-vector with max fitness ; f$_i = BL_i / -f_i
```

**Ambiguities & assumptions**

- **"Biggest loss" is historical, but the future can be worse** [p. 217–218]. Vince recommends scenario/parametric methods that budget for a larger loss, but gives no numeric buffer. ASSUMPTION for testing: use BL × 1.25 (or a stress scenario) as a sensitivity check.
- **The Ch. 12 drawdown probabilities are not given numerically** for any real system. Thresholds x and b are user utility choices.
- **The joint-probability estimate (eq. 9.03) is only valid** for two components or zero pairwise correlation. Vince says to use empirical joint probabilities instead [p. 331].
- **The text has typos in derived numbers.** Example: [p. 353] prints "ln(21)/ln(1.01933) = 1590201" (should be ≈ 159.02). Equation numbering is inconsistent: (10.05) vs (10.09); (12.10) vs (12.11) [p. 368–369, 434].
- **Practitioner methods (2.9) are described, not endorsed.** Vince says their VaR approach gives an "overly optimistic assessment of the potential risk" (paraphrase of p. 400).

## 3. Risk & money-management rules

- Never size a negative-expectation system; no money-management scheme fixes it [p. 42, 134].
- Size off the largest losing trade, not the maximum drawdown. Drawdown is sequence-dependent and arbitrary, whereas the largest loss is controllable [p. 163, 168].
- Use a single combined bankroll and recapitalise sub-allocations daily [p. 204–206].
- Prefer erring to the left of optimal f [p. 175]. Half f takes ~31% longer to double in the coin-toss example but halves drawdown and variance [p. 215].
- For portfolios, the sum of the component f values is the worst-case simultaneous loss on active equity. Treat it as an expected drawdown, since all correlations revert to one in crises [p. 359, 387].
- **Margin cap:** upper fraction L = max f$ / Σ((max f$/f$_k)·margin_k). Never trade a fraction above L [p. 365–366].
- **Small accounts:** trade lower-priced or smaller contracts so the account can track f more finely [p. 171].
- **Liquidity** is the most common cause of single-trade disasters. Always know your position [p. 383].

## 4. Non-codable guidance

- Utility: risk is "the probability of being ruined" or touching a lower equity barrier. Most investors are ln-utility maximisers only within a drawdown constraint [p. 16, 21].
- Building a personal utility-preference curve via certainty equivalents [p. 246–250].
- Scenario construction: cover ~99% of outcomes, avoid the three-scenario (optimistic/pessimistic/same) trap, use one common holding period [p. 188–189, 198].
- f shift: markets that performed well tend to underperform next period. Build scenarios with that in mind [p. 367].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - per-trade P&L history (or daily mark-to-market) of each strategy run on NSE instruments;
  - prices for equalisation (2.3);
  - F&O margin requirements (SPAN + exposure) for the margin cap;
  - joint daily outcome histories across components for 2.8.
- **Testability with our data:** 2.1–2.7, 2.9 and 2.10 are fully mechanical given a trade list. 2.8 is computationally heavy but feasible with sampling (6.25M permutations per q at 5σ/.001 error).
- **Market-structure differences:**
  - NSE lot sizes (e.g., index futures) are large relative to small accounts, so integer constraints bite. Use the small-account rule 2.4 or trade stock futures / cash equity for finer granularity.
  - Equalised f (2.3) suits cash equities where price levels change a lot.
  - Circuit limits and gap risk on F&O stocks mean the historical biggest loss can be exceeded overnight; stress BL (ASSUMPTION).
  - Short selling in cash is intraday only, so short-side scenarios should come from futures.

## 6. Verdict

- **Codeability:** High for the sizing algorithms (2.1–2.7, 2.9, 2.10): fully specified formulas with worked examples. Medium for 2.8 (well-defined objective but heavy computation and joint-probability estimation). No entry/exit logic.
- **Priority for backtesting:** High as an overlay library. Every strategy spec from other resources needs a sizing layer, and this book supplies:
  - optimal f / f$ diagnostics;
  - dynamic fractional f with the half-max-drawdown rule;
  - a drawdown-probability estimator for portfolio allocation.

  Implement 2.1 + 2.5 + the RD(b) estimator first.
- **Top 3 things a coder is most likely to get wrong**
  1. Computing Kelly from average win / average loss and treating it as optimal f. Use the TWR search over the actual trade list (HPR = 1 + f·(−trade/biggest loss)) and convert with f$ = biggest loss/−f [p. 145–150].
  2. Sizing a portfolio by applying each component's standalone f. The f values must be solved jointly (e.g., two uncorrelated 2:1 coins: .23 each, not .25). Their sum is the simultaneous-loss exposure on active equity [p. 207–208, 313, 359].
  3. Dynamic fractional f implemented as a static fraction, or reallocated too often. Keep the inactive amount constant and size on equity − inactive. Reallocate only after the T/upside threshold, otherwise the dynamic version underperforms the static one [p. 357–358, 367–368].
