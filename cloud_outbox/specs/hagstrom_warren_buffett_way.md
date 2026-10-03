# The Warren Buffett Way, Second Edition — Robert G. Hagstrom (John Wiley & Sons, 2005)

- **Source file:** Google Drive `The Warren Buffett way - Robert G. Hagstorm.pdf` (file id `1Vb-VZ7KOROLMFgAncoWT60QnPKkvh550`, 1,784,754 bytes), 267 PDF pages with a text layer.
- **Text file used:** text/hagstrom_warren_buffett_way.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index; printed page ≈ PDF page − 26 in the body, e.g. printed 61 = [[PAGE 87]]). Always take N from the marker.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/hagstrom_warren_buffett_way.md text/hagstrom_warren_buffett_way.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 267]].
  - The PDF is missing two printed pages: printed p. 18 (between [[PAGE 44]] and [[PAGE 45]], Fisher's points) and printed p. 118 (between [[PAGE 143]] and [[PAGE 144]], the end of the one-dollar premise test). Their content is not in the text and cannot be specified.
  - Chapters 1–4 and the "Case in Point" boxes are history and deal narratives; rules extracted from them are cited.
  - The Appendix ([[PAGE 235]]–[[PAGE 247]], Tables A.1–A.27) is Berkshire's year-end portfolio holdings. It was scanned for names and notes only; it contains no rules.
  - Notes ([[PAGE 247]]–[[PAGE 255]]) were read; note 5 of Ch. 8 gives the two-stage DCF arithmetic [p. 252]. Acknowledgments and Index ([[PAGE 257]]–[[PAGE 267]]) contain no rules.
  - Charts and figures (e.g. Figures 4.1–8.2) are not readable; captions were read.

## 1. The method in brief

A long-only, buy-and-hold **business-ownership** method: buy a few businesses that pass 12 tenets, at a discount to owner-earnings DCF value, concentrate in them, and hold for years.

- **The 12 tenets** [p. 85, 88]
  - Business: simple and understandable; consistent operating history; favorable long-term prospects.
  - Management: rational; candid with shareholders; resists the institutional imperative.
  - Financial: return on equity; owner earnings; profit margins; at least $1 of market value per $1 retained.
  - Value: the value of the company; whether it can be bought at a significant discount to that value.
- **Valuation:** the value of a business is its future net cash flows (owner earnings), discounted at a risk-free rate with no equity risk premium [p. 147–149].
- **Portfolio:** "focus investing". Hold 10–20 stocks, put the bulk in the best ones, hold 5–10 years, and keep turnover low [p. 185, 188].
- **Evidence:** case studies (Coca-Cola, Washington Post, Gillette, Wells Fargo, GEICO and others) and the track records of Munger, Ruane (Sequoia) and Simpson (GEICO) [p. 193–198]. There is no systematic backtest.
- **Influences:** Graham (margin of safety, net-net and low-P/E approaches), Fisher (qualitative, concentrated), J. B. Williams (DCF) and Munger (quality at a fair price) [p. 39–54].

## 2. Strategies

| # | Strategy | Timeframe | Entry rule (as stated) | Stop / exit (as stated) | Page |
|---|---|---|---|---|---|
| 2.1 | 12-tenet quality screen + owner-earnings DCF with margin-of-safety buy (the core "Warren Buffett Way") | Annual fundamentals, judged on 4–5-year averages; holding period 5–10 years or "forever" | Passes the business, management and financial tenets, AND price is at a significant discount to intrinsic value (DCF of owner earnings at the long-term government bond yield, floor 10% when yields are below 7%) | No price stop. Hold while the company "continues to generate above-average economics" and management allocates capital rationally; sell lousy companies (turnover is required there). New buys must beat the best existing holding | 85, 135–143, 147–152, 156, 198 |
| 2.2 | Two-stage owner-earnings DCF valuation model | Annual | Value = PV of 10 years of owner earnings at growth g1 + PV of a terminal value at growth g2 (5%) capitalised at (k − g2); k = risk-free rate. Buy when price ≪ value | Not specified beyond the margin-of-safety logic | 150–152, 252 |
| 2.3 | Graham net-net (net current asset value) | Not specified | Buy when price < ⅔ of net current assets per share (current assets minus ALL short- and long-term liabilities; plant and equipment given zero weight) | Not specified. The book notes Buffett abandoned pure net-nets after buying "genuine losers" | 42, 51 |
| 2.4 | Graham low-P/E bargain | Not specified | Stock down in price, low P/E, and positive net asset value ("must owe less than its worth") | Not specified | 42 |
| 2.5 | One-dollar premise (retained-earnings efficiency test) | Multi-year, e.g. 5 years (ASSUMPTION) | Increase in market value ≥ cumulative retained earnings, dollar for dollar | Used as a screen, not a trade rule | 85, 143 |
| 2.6 | Focus-portfolio construction and turnover rules | 5–10-year holding | 10–20 holdings; at least 10% of net worth per conviction position; larger weights to the highest-probability names | Annual turnover 10–20% (also given as 0–20%); sell only for something better or for deteriorating economics | 185–188, 198–199 |
| 2.7 | Risk arbitrage on announced deals | Deal life (months) | Only announced, friendly deals; evaluate the four questions (probability of completion, time tied up, chance of a better bid, downside if it fails) | Exit at deal completion; no rule given for a broken deal | 175–176 |

**Parameters**

- **Evaluation window:** 4–5-year averages rather than single years [p. 135].
- **ROE**
  - Operating earnings ÷ shareholders' equity [p. 136].
  - Value marketable securities at cost [p. 136].
  - Exclude capital gains/losses and extraordinary items [p. 136].
  - No undue leverage. No numeric debt limit is given [p. 137].
- **Owner earnings:** net income + depreciation, depletion and amortization − capital expenditures − any additional working capital needed [p. 140]. In the worked examples, working capital is omitted (NI + D&A − capex) [p. 140, 153].
- **Discount rate**
  - Ch. 2 gives the 10-year US bond yield, or the market's average return when rates are very low [p. 47].
  - Ch. 8 gives the long-term (30-year) government bond yield, raised to 10% once bond yields fell below 7% [p. 149].
  - No equity risk premium [p. 149].
- **Two-stage DCF example (Coca-Cola, 1988)** [p. 150–152, 252]:
  - Owner earnings $828M, 15% growth for 10 years, then 5%, k = 9%.
  - Result: $48.377B; the PV of years 1–10 is $11.248B and the terminal PV is $37.129B.
  - Sensitivities: 12% growth gives $38.163B; 10% gives $32.497B; 5% flat gives $20.7B.
- **Single-stage growth example (Larson-Juhl):** cash from operations $30.8M ÷ (10% − 3%) ≈ $440M, against a $223M price [p. 158–159].
- **Margin of safety:** a worked example of buying at 75% of value (25% discount) [p. 156]. The discounts achieved in the cases were 27–70% for Coca-Cola [p. 159] and 25–50% for Gillette [p. 160–161].
- **Portfolio**
  - 10–20 stocks [p. 185].
  - At least 10% of net worth per stock [p. 187].
  - Turnover 10–20% a year, i.e. 5–10-year holds [p. 188]; 0–20% for after-tax returns [p. 199].
  - Fifteen stocks give 85% diversification [p. 186].
- **Graham net-net:** price < ⅔ of net current assets [p. 42].

**Key quotes**

- "The first approach was buying a company for less than two-thirds of its net asset value, and the second was focusing on stocks with low price-to-earnings (P/E) ratios." [p. 42]
- "Additionally, the company must have some net asset value; it must owe less than its worth." [p. 42]
- "He uses either the interest rate for long-term (meaning ten-year) U.S. bonds, or when interest rates are very low, he uses the average cumulative rate of return of the overall stock market." [p. 47]
- "10. Has the company created at least one dollar of market value for every dollar retained?" [p. 85]
- "12. Can it be purchased at a significant discount to its value?" [p. 85]
- "Severe change and exceptional returns usually don’t mix" [p. 94]
- "He defines a franchise as a company whose product or service (1) is needed or desired, (2) has no close substitute, and (3) is not regulated." [p. 96]
- "If the extra cash, reinvested internally, can produce an above-average return on equity—a return that is higher than the cost of capital—then the company should retain all its earnings and reinvest them." [p. 111]
- "If a company’s stock price is $50 and its intrinsic value is $100, then each time management buys its stock, they are acquiring $2 of intrinsic value for every $1 spent." [p. 116]
- "Instead, he focuses on four- or five-year averages." [p. 135]
- "To measure a company’s annual performance, Buffett prefers return on equity—the ratio of operating earnings to shareholders’ equity." [p. 136]
- "First, all marketable securities should be valued at cost and not at market value" [p. 136]
- "Buffett excludes all capital gains and losses as well as any extraordinary items" [p. 136]
- "Investors should be wary of companies that can earn good returns on equity only by employing significant debt." [p. 137]
- "a company’s net income plus depreciation, depletion, and amortization, less the amount of capital expenditures and any additional working capital that might be needed." [p. 140]
- "Buffett’s goal is to select companies in which each dollar of retained earnings is translated into at least one dollar of market value." [p. 143]
- "The increased market value should at the very least match the amount of retained earnings, dollar for dollar." [p. 143]
- "If he is unable to project with confidence what the future cash flows of a business will be, he will not attempt to value the company." [p. 148]
- "When bond yields dipped below 7 percent, Buffett upped his discount rate to 10 percent, and that is what he commonly uses today." [p. 149]
- "Buffett does not add a risk premium." [p. 149]
- "When a company is able to grow owner earnings without additional capital, it is appropriate to discount owner earnings by the difference between the risk-free rate of return and the expected growth of owner earnings." [p. 150]
- "If Buffett is able to purchase a company at 75 percent of its intrinsic value (a 25 percent discount) and the value subsequently declines by 10 percent, his original purchase price will still yield an adequate return." [p. 156]
- "Using his standard 10 percent dividend discount rate, adjusted for a very reasonable 3 percent growth rate" [p. 158]
- "When the probabilities of success are very high, make a big bet." [p. 160]
- "The two value tenets are crucial." [p. 164]
- "He limited his participation to deals that were announced and friendly, and he refused to speculate about potential takeovers or the prospects for greenmail." [p. 175]
- "Ten to twenty is good, more than twenty is asking for trouble." [p. 185]
- "With each investment you make, you should have the courage and the conviction to place at least ten percent of your net worth in that stock." [p. 187]
- "As a general rule of thumb, we should aim for a turnover rate between 20 and 10 percent, which means holding the stock for somewhere between five and ten years." [p. 188]
- "If the new thing you are considering purchasing is not better than what you already know is available" [p. 198]
- "so long as the company continues to generate above-average economics and management allocates the earnings of the company in a rational manner" [p. 198]
- "The best strategy for achieving high aftertax returns is to keep your average portfolio turnover ratio somewhere between 0 and 20 percent." [p. 199]

**Pseudocode** (annual rebalance; fundamentals point-in-time; thresholds marked ASSUMPTION where the book gives none)

```
for each stock s at fiscal year-end t (use 5-year windows, p.135):
  # --- financial tenets (codeable proxies) ---
  roe_5y      = mean(op_earnings_ex_gains / equity_with_securities_at_cost, t-4..t)   # p.136
  owner_earn  = NI + DDA - capex - delta_working_capital                              # p.140
  oe_growth   = CAGR(owner_earn, t-5..t)
  margin_ok   = pretax_margin_5y >= industry_median                                   # ASSUMPTION (p.140-143 give no number)
  lev_ok      = debt_to_equity <= 0.5                                                 # ASSUMPTION (no number given, p.137)
  retained    = sum(NI - dividends, t-4..t)
  one_dollar  = (mktcap_t - mktcap_{t-5}) >= retained                                 # p.143
  # --- business tenets (proxies) ---
  consistent  = NI > 0 in all of t-9..t  and  sales_cv_10y < 0.25                     # ASSUMPTION proxy for p.93-94
  quality_ok  = roe_5y >= 15% and roe_5y achieved with lev_ok                         # ASSUMPTION 15% (p.157 compares 15% vs 10% ROE)
  pass_screen = quality_ok and margin_ok and one_dollar and consistent

  # --- value tenets: two-stage DCF (p.150, note p.252) ---
  rf   = long_gov_bond_yield(t);  k = max(rf, 10%) if rf < 7% else rf                 # p.149
  g1   = min(oe_growth, k + x)  ; g2 = 5%                                             # g1 choice is judgment (ASSUMPTION: cap at historical)
  pv1  = sum(owner_earn*(1+g1)^i / (1+k)^i for i in 1..10)
  tv   = owner_earn*(1+g1)^10*(1+g2) / (k - g2)          # requires k > g2
  iv   = pv1 + tv/(1+k)^10
  mos  = 1 - mktcap_t / iv
  buy_candidate = pass_screen and mos >= 25%                                          # 25% from p.156 example; ASSUMPTION as threshold

portfolio (p.185-188, 198-199):
  rank buy_candidates by mos * quality score (ASSUMPTION)
  hold 10..20 names; conviction weights >= 10% each; overweight top names
  add new name only if it beats the BEST existing holding ("measuring stick", p.198)
  sell when: pass_screen fails on 5y averages (economics deteriorate) or a clearly better candidate exists
  target annual turnover 10..20%; no price-based stop loss

# 2.3 Graham net-net (p.42)
ncav = current_assets - total_liabilities
buy if price < (2/3) * ncav / shares
# 2.4 Graham low-P/E (p.42)
buy if pe in bottom quintile (ASSUMPTION) and price fell over trailing 12m (ASSUMPTION) and equity > 0
```

**Ambiguities & assumptions**

- **The discount rate is stated two ways:** the 10-year bond yield or the market return [p. 47], versus the 30-year bond yield with a 10% floor [p. 149]. The examples use the 30-year yield (9% for Coca-Cola 1988, 8.62%→9% for Gillette) [p. 150, 152].
- **Turnover is given two ways:** 10–20% [p. 188] and 0–20% [p. 199].
- **No numeric thresholds** are given for ROE, margins, debt or the margin of safety. The 25% figure is an illustration [p. 156], and the discounts actually achieved ranged from 27% to 70% [p. 159].
- **The first-stage growth rate is a judgment call.** The book picks rates "lower than the company's previous seven-year average" [p. 150].
- **A text error in note 5:** it says year-ten earnings "will be $4.349 billion", but Table 8.1 shows $3,349M [p. 151, 252].
- **The one-dollar test's window and wording are incomplete,** because printed p. 118 is missing.
- **Management tenets (rationality, candor, institutional imperative) are qualitative.** Proxies are possible: buybacks below intrinsic value, segment disclosure, acquisition-heavy capital allocation. They are not specified in the book.

## 3. Risk & money-management rules

- **Risk** is "the possibility of harm" (misjudging the business), not price volatility. A price drop is treated as an opportunity [p. 190].
- **Margin of safety:** do not buy when value is only slightly above price [p. 156]. For economically riskier (e.g. technology) businesses, demand a greater margin of safety [p. 231].
- **Concentration**
  - 10–20 names [p. 185].
  - At least 10% per position [p. 187].
  - Bet big on high-probability events [p. 160, 187].
  - Example: 40% of the partnership in American Express [p. 187].
- **No stop-loss:** "Volatility happens. Carry on." [p. 185]. Investors should be able to sit through a 50% decline in their holdings without panic [p. 204].
- **Low turnover** cuts costs and taxes. The doubling-$1 example over 20 years gives $25,200 net when sold yearly versus $692,000 when held [p. 199].
- **Leverage:** good returns should come "with no aid from leverage" [p. 136].
- **Bank stress test (Wells Fargo):** if 10% of loans go bad with a 30% loss, the bank still breaks even [p. 155].
- **Patience rule:** act as if you had a 20-punch lifetime decision card [p. 205].

## 4. Non-codable guidance

- **Circle of competence:** "It’s not how big the circle is that counts, it’s how well you define the parameters" [p. 89]. Avoid businesses whose cash flows cannot be projected [p. 148].
- **Franchise / moat assessment:** product needed, no close substitute, unregulated; pricing power [p. 96–97].
- **Scuttlebutt research (Fisher):** talk to customers, suppliers, ex-employees and competitors [p. 45].
- **Management evaluation**
  - Compare past annual-report plans with results [p. 132–133].
  - Red flags: not expensing options, unintelligible footnotes, companies that "trumpet earnings projections" [p. 134].
- **Avoid turnarounds, hostile takeovers and companies undergoing major change** [p. 69, 94].
- **Temperament:** "be fearful when others are greedy" [p. 206]; ignore Mr. Market [p. 206–207]; ignore the economy and macro forecasts [p. 219].
- **Fixed income:** buy "stigmatized" bonds that are misappraised, i.e. fallen angels and distressed bonds such as WPPSS, RJR, Level 3 and Amazon [p. 168–174]. Treat convertible preferreds as fixed income first [p. 176–179].
- **Annual check-up:** return on beginning equity; changes in margins, debt and capex needs; cash generation [p. 217].
- **Afterword (Hagstrom/Miller):** apply the same DCF to technology, with a larger margin of safety. Mauboussin's study of 1992–2002 outperformers found about 30% turnover and 37% of assets in the top 10 names [p. 231–232].

## 5. Adapting to NSE (Indian equities)

- **Data required**
  - 10+ years of annual statements: operating profit excluding other income and exceptional items, D&A, capex, working capital, equity, dividends, debt.
  - Market caps and shares outstanding.
  - The 10-year and longer G-sec yields.
  - Sources: Screener/Capitaline/Prowess-type datasets, point-in-time to avoid look-ahead.
- **Testability with our data**
  - 2.1, 2.2, 2.3, 2.4 and 2.5 are codeable as annual screens with a 5–10-year hold, but only as fundamental-factor backtests. Long annual histories are needed, plus survivorship-free universes (include delisted stocks).
  - Management tenets need proxies. Examples: promoter pledging, related-party transactions, buybacks/dividends versus ROE, auditor qualifications.
  - 2.7 (risk arbitrage) has a small sample on NSE (open offers, delisting offers, schemes of arrangement). It would need deal-level data.
- **Market-structure differences**
  - Indian risk-free yields (10-year G-sec) have mostly been 6–8%. The book's "raise to 10% when bonds < 7%" rule would bind often.
  - Indian nominal growth is higher, so the terminal g2 = 5% may be conservative. Test sensitivities, and keep k − g2 positive and meaningful.
  - Net-nets (2.3) cluster in illiquid small caps on NSE/BSE. Apply ADV/liquidity filters and promoter-quality filters.
  - Taxes differ: Indian LTCG/STCG rules and dividend taxation change the after-tax turnover arithmetic. Use the current rates.
  - Large promoter holdings make the "management candor/rationality" tenets especially relevant (governance proxies).

## 6. Verdict

- **Codeability:** Partial.
  - The financial and value tenets (ROE on 4–5-year averages, owner earnings, one-dollar test, two-stage DCF with a stated discount-rate rule) and the Graham net-net/low-P/E screens are codeable.
  - The business and management tenets need proxies.
  - There are no price-based entry timing or exit rules.
- **Priority for backtesting:** Medium, as a long-horizon fundamental factor (quality + owner-earnings DCF discount) with annual rebalancing. It is not suitable for short-term trading backtests. It is best run as a forward test or long-history fundamental backtest on NSE.
- **Top 3 things a coder is most likely to get wrong**
  1. Using reported EPS growth or plain operating cash flow instead of owner earnings (NI + D&A − capex − extra working capital), or single-year figures instead of 4–5-year averages [p. 135, 140].
  2. Adding an equity risk premium or a CAPM beta to the discount rate. The book uses the long government bond yield, floored at 10% when yields are below 7%, with no risk premium [p. 149].
  3. Equal-weighting a broad portfolio with frequent rebalancing. The method is 10–20 concentrated positions of at least 10% each, 10–20% annual turnover, and no stop-losses [p. 185–188].
