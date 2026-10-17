# How to Think Like Benjamin Graham and Invest Like Warren Buffett — Lawrence A. Cunningham

- **Source file:** Google Drive "How_To_Think_Like_Benjamin_Graham_and_Invest_like_Warren_Buffett.pdf" (289 pages). McGraw-Hill, New York, copyright 2001 (copyright page confirms "Copyright © 2001 by the McGraw-Hill Companies, Inc.") [p. 5]
- **Text file used:** text/cunningham_think_like_graham.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter (printed page = PDF page minus 19 in the body).
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/<key>.md text/<key>.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read the entire text file, lines 1-11834, in sequential chunks; last marker reached `[[PAGE 289]]`. Blank/divider pages with no content: pp. 1, 3, 9, 21, 35, 69, 87, 109, 171, 189, 211, 261, 275 (pp. 20, 108, 188 are Part title pages with only the part title). Front matter (title, copyright, contents, acknowledgements, pp. 2-11) read and not used for rules. The Notes (pp. 264-274) were read: source citations only, except one number used here (Washington Post cost vs value, p. 264). The Company, Name and Subject indexes (pp. 276-286) and the About-the-Author/endorsement pages (pp. 287-289) were moved through quickly after confirming they hold only page references, no rules. Nothing was unreadable or garbled except that the PDF text layer renders the ligatures fi/fl as single glyphs (these do not affect meaning). Part I (pp. 20-107, market efficiency, chaos theory, volatility) and Part III (pp. 188-260, governance, CEO letters of Welch, Eisner, Goizueta) were read in full; they contain almost no numeric rules. *Coordinator check: the coordinator re-ran verify_citations (49/49 ok) and an exact-page strict check (0 off-by-one), and confirmed all eight field tables have exactly the 12 template rows. 11 unquoted citations were spot-checked by grep and page read: net current assets and half of fixed-asset original cost p.156, current ratio p.140-141, cap rates ~10% / 15-25% / 30-40% p.159, 6-8% and 8-12% p.160, 5-10 (Buffett) vs 10-30 (Graham) stocks p.95, Washington Post 80% margin of safety p.32, value beats growth 8-10% p.67, 75% of day traders p.83; all matched. 'Owner earnings' and 'moat' indeed do not occur in the text.*

## 1. The method in brief

Cunningham's book is a narrative synthesis, not a trading system. Its thesis is that price and value are different things, that stock market efficiency is at most about 80% true and getting less so [p. 88] (Mr. Market, Graham's manic-depressive market), and that an investor should therefore act as a business analyst: (1) stay inside a personal circle of competence, (2) estimate the intrinsic value of a business as the present value of the cash it will generate for its owners (by capitalizing normalized earnings or discounting cash flows / dividends), (3) check liquidity, debt, efficiency and return ratios from the financial statements, (4) judge whether management is trustworthy and owner-oriented, and (5) buy only with a margin of safety between price and value [p. 12, 16, 153]. The edge claimed is the persistent separation of price from value created by noisy, emotional, short-term trading (day traders, rumours, rebalancing, momentum and sector-rotation trading) [p. 85, 86]. Time frame: long-run, wait-and-see, minimum four years [p. 106]. Market: US large-cap examples (GE, Microsoft, Amazon, Coca-Cola, Disney); no market-specific rules.

Differences the author sees between his two masters: Buffett places somewhat more significance on managers, is less beholden to Graham-style bargain purchases, is a bit less committed to diversification and pays more attention to intangible asset values [p. 18].

Quantitative content is limited to: Graham's net-current-asset rule and a half-fixed-asset variant [p. 156], a set of ratio rules of thumb (current ratio, quick ratio, coverage, turns, margins, returns) [p. 139-150], price-ratio guideposts (P/B, P/S, P/E) [p. 166-169], capitalization-rate ranges for earnings capitalization [p. 159-161], position-count guidance of 5-10 (Buffett) and 10-30 (Graham) stocks [p. 95], and a handful of earnings-quality red flags [p. 173-186, 229-236].

Evidence/track records cited (none is a backtest of a rule set):
- Buffett bought the Washington Post in mid-1973 at about a fifth of intrinsic value, "an 80% margin of safety" [p. 32]; the endnote gives $5.63 a share, $100 million in aggregate, against a value of $400 to $500 million [p. 264].
- Buffett generated most of Berkshire's wealth from about ten investments over about forty years [p. 32].
- John Neff (Windsor Fund, 1964-1995) beat the average by a steady 3% annually, at times with as much as 40% of the fund in one business sector [p. 33].
- Behavioral-finance studies (Shleifer): "value" stocks outperform "growth" stocks by spreads of about 8 to 10% annually over long horizons [p. 67]; Shiller and Campbell estimate only 27% (later 15%) of annual return volatility is justified by fundamentals [p. 68].
- 75% of day traders lose money and a market-timer must be right 70% of the time to profit [p. 83].
- Coca-Cola under Goizueta: 24% compound annual share-price growth 1980-1995 versus 12% for the Dow and 11% for the S&P 500 [p. 254]; GE under Welch: average return on equity above 24% [p. 242]. These illustrate management quality, not a rule.

## 2. Strategies

Eight separately testable items are extracted. All of them are long-only, none gives an order type, and none gives a stop-loss; where the book is silent the table says "Not found in this text" (page `-`). Every fundamental input comes from financial statements, so these are forward-test candidates only on our data (see section 5).

### 2.1 Graham net-current-asset (NCAV, "net-net") rule

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value (deep asset value, bargain hunting) | 156 |
| Timeframe & holding period | Not found in this text for this screen. General guidance: investors should look beyond days; "a minimum time frame for anyone serious about investing is four years" | 106 |
| Universe / eligibility filters | Common stocks. The author says such companies are "so rare today" that the rule in pure form is of little use, but smaller companies may still turn up. Must be inside the investor's circle of competence | 156, 124 |
| Market / regime filter | Not found in this text (author says he has no opinion on where the stock market, rates or business activity will be) | 123 |
| Setup conditions | Price per share is less than net current assets per share, i.e. a price equal to per-share working capital, so the buyer pays nothing for fixed assets. Working capital is the difference between short-term needs and resources | 156, 139 |
| Entry trigger & order type | Buy when the condition holds; order type not found. Warning: do not buy a 'dying fish'; prudent investors prefer fair prices on strong businesses to cheap prices on weak ones | 156 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found for this screen. General sell triggers (price exceeds value by large amounts, better opportunities, deterioration, management change) are in 2.6 | 83, 84 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text (see 2.6 for the book's portfolio guidance) | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | For well-chosen stocks with a margin of safety Graham says 10 to 30 stocks; no sector limits given | 95 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Price / net current assets per share | below 1.0 (price less than NCA per share) | none | 156 |
| Credit given to fixed assets | 0% | 50% in variant 2.2 | 156 |
| Number of holdings | 10 to 30 (Graham) | 5 to 10 (Buffett) | 95 |

**Key quotes**
- "can be bought at a price equivalent to less than the company’s net current assets" [p. 156]
- "Such companies are so rare today that this tool in its pristine form is of little use." [p. 156]
- "it is better to buy a great business at a fair price than a fair business at a great price" [p. 156]

**Pseudocode**
```
for each stock s at date t (fundamentals snapshot):
    NCA = current_assets - current_liabilities          # text: net current assets = working capital
    NCAV_ps = NCA / shares_outstanding
    if NCAV_ps > 0 and price < NCAV_ps:
        candidate(s)
rank candidates by price / NCAV_ps ascending
hold the top N (N = 10..30), equal weight, no stop; exit per 2.6
```

**Ambiguities & assumptions**
- Book defines the rule only as "net current assets", "that is, a price equal to per share working capital" [p. 156]; it does not say whether long-term debt or preferred stock is deducted. ASSUMPTION: NCA = total current assets minus total current liabilities, nothing else deducted (literal reading); a stricter variant also deducting long-term debt can be run as a sensitivity.
- No dying-fish test is given beyond the warning [p. 156]. ASSUMPTION: require positive operating cash flow, current ratio at least 1.5 and interest coverage at least 3 (values from 2.3) to avoid distressed names.
- Threshold of exactly 1.0 and no margin on top of it is the book's literal wording; ASSUMPTION: also test price below 0.67 x NCAV_ps as a stricter variant.
- Holding period, exit and sizing not found in this book. ASSUMPTION: equal weight, exit per 2.6, minimum horizon four years only as a test parameter.

### 2.2 Net current assets plus half of fixed-asset cost (Graham variation)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value (asset-based, relaxed net-net) | 156 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Common stocks, particularly smaller companies; inside circle of competence | 156, 124 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | A business qualifies if it can be bought for its net current assets plus, say, half the original cost of its fixed assets: the investor pays for net working capital at stated value and gets a 50% discount on all other assets | 156 |
| Entry trigger & order type | Buy when condition holds; order type not found | 156 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | 10 to 30 (Graham), 5 to 10 (Buffett) | 95 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fraction of original fixed-asset cost counted | 0.5 ("say, half") | none | 156 |
| Price ceiling | NCA + 0.5 x original cost of fixed assets, per share | none | 156 |

**Key quotes**
- "net current assets plus, say, half the original cost of its" [p. 156]
- "the investor pays for net working capital at the stated value and gets a 50% discount for all the other assets" [p. 156]

**Pseudocode**
```
ceiling_ps = (current_assets - current_liabilities + 0.5 * gross_fixed_assets_at_cost) / shares_outstanding
if price < ceiling_ps: candidate
rank by price / ceiling_ps ascending; hold N = 10..30 equal weight
```

**Ambiguities & assumptions**
- "Original cost" of fixed assets could be gross block (before depreciation) or net carrying value. The author's "original cost" suggests gross block. ASSUMPTION: gross block (cost before accumulated depreciation); test net block as a sensitivity.
- Intangibles and land revaluation not mentioned; the author warns fixed assets "must not be taken too seriously" and intangibles deserve "little if any weight" (Graham quoted) [p. 157]. ASSUMPTION: exclude goodwill and intangibles from fixed assets.
- Everything else as in 2.1.

### 2.3 Low price-ratio plus business-quality ratio screen

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value / quality-filtered value (Graham-Buffett business analysis) | 166, 138 |
| Timeframe & holding period | Not found as a rule; author says look at returns over five to ten years and invest long term (minimum four years) | 147, 106 |
| Universe / eligibility filters | Companies inside the investor's circle of competence (understand products, customers, selling environment). Beware of third-party screening databases: data integrity and missing footnotes/MD&A | 124, 126, 138, 139 |
| Market / regime filter | Not found in this text. Risk-free rate and economy affect required returns (higher rates lower values) but no timing rule | 121, 160 |
| Setup conditions | Make the value call first, then compare to price ratios: low P/B, P/S, P/E are 'a good place to look', especially when all price ratios are low and return on equity is high. Quality gates: working capital/current ratio about 1.5; quick ratio at least 1; debt-to-equity and interest coverage 3 to 4 or better; inventory and receivable turns good versus peers and credit terms; profit margin toward the high end of the range; return on equity/investment/assets high over five to ten years; trends over several years | 166, 140, 141, 142, 143, 144, 145, 147 |
| Entry trigger & order type | Buy when price is below estimated value by a margin of safety and the ratio checks pass; order type not found | 162, 166 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found as a number; see 2.6 | 83 |
| Exits: trailing / time / signal | Deterioration of economic characteristics or management is a sell signal; see 2.6 | 83, 84 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | 5 to 10 (Buffett), 10 to 30 (Graham) | 95 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Current ratio | ideal around 1.5 | 3-4 or more signals idle resources; 1 or less is a warning, investigate liquidity | 140 |
| Quick (acid-test) ratio | minimum 1 | higher is generally better, up to a point | 141 |
| Working capital / sales | not a threshold; supermarket about 10-15%, aircraft maker about 25-35% | negative is acceptable for cash businesses (restaurants) | 139 |
| Debt-to-equity | no threshold; S&P 500 about 1:1 at 2000; conglomerates about 3:1 | 7:1 (1980s), 4:1 (early 1990s) | 142 |
| Interest coverage (earnings / interest) | 3 to 4 prudent for industrial companies | S&P 500 near 11; GE about 2.5 | 143 |
| Inventory turns | COGS / average inventory; higher is better; S&P 500 about 10 | GE 8, computer industry about 15 | 144 |
| Receivable turns | credit sales / average receivables; days = days in year / turns; trouble if days exceed credit terms | GE about 8 turns (45 days) | 145 |
| Profit margin | operating income / net sales; S&P 500 about 17.5%; toward the high end, not extreme, is ideal | net and gross margin alternatives | 145, 146, 147 |
| Return on equity | earnings / shareholder equity, judged over five to ten years; S&P 500 about 22% | ROI about 14%; ROA hardest test | 147, 148, 149 |
| P/B | below 1 warrants investigation; market average 2 to 3.5 | tech up to 20+ | 166 |
| P/S | price at or below sales per share gives a good margin of safety | S&P-type names 5-20 not bargains | 167 |
| P/E | historical breakpoint 15 (below low, above high); above 50 very high; P/E of 5 gives a thick margin of safety | implied cap rate = 1/PE | 167, 168 |

**Key quotes**
- "Market price is the last thing an investor should look at in a valuation exercise." [p. 91]
- "a stock trading below a P/B ratio of 1, you can buy that stock for a price below the company’s net worth" [p. 166]
- "if you can buy a stock for a price that is equal to or less than the company’s sales, you are on your way to getting a good margin of safety" [p. 167]
- "The historical breakpoint for high and low P/E ratios has been 15" [p. 167]
- "Now that sounds like a deal with a thick margin of safety." [p. 168]
- "for most businesses the ideal current ratio is around 1.5" [p. 140]
- "A minimum quick ratio of 1 is desirable, and higher ratios are generally better" [p. 141]
- "an interest coverage ratio in the range of 3 to 4 is considered prudent" [p. 143]
- "Something in between, toward the high end, is ideal." [p. 147]

**Pseudocode**
```
inputs per stock: price, shares, book_equity, sales, eps_diluted, current_assets, current_liabilities,
  cash, receivables, inventory, total_debt, ebit, interest_expense, cogs, net_income, history 5-10y
compute:
  CR = CA / CL ;  QR = (cash + receivables) / CL
  DE = total_debt / book_equity ;  COV = ebit / interest_expense
  INV_TURN = cogs / avg(inventory) ;  REC_DAYS = 365 / (sales / avg(receivables))
  MARGIN = ebit / sales ;  ROE_avg = mean(net_income / equity) over available years (5-10)
  PB = price / (book_equity / shares) ; PS = price*shares / sales ; PE = price / eps_diluted_normalized
filter (all must pass):
  1.0 <= CR <= 3.0 ; QR >= 1 ; COV >= 3 ; REC_DAYS <= stated credit terms (or <= sector median)
  MARGIN in upper half of sector but not extreme ; ROE_avg >= sector median
price test (any one makes the stock a 'look closer' candidate; deeper = more margin):
  PB < 1  or  PS <= 1  or  PE < 15  (PE <= 5 = thick margin of safety)
final decision requires value estimate from 2.4/2.5 with price << value
```

**Ambiguities & assumptions**
- The ratios are explicitly industry-relative rules of thumb, not hard cutoffs (the author gives different norms for supermarkets, computers, conglomerates) [p. 139, 140, 141]. ASSUMPTION: use the stated numbers as defaults for non-financial companies and sector-median comparisons for turns and margins.
- The book never says how many of P/B, P/S, P/E must be low; it says they are 'a good place to look' and not a guarantee [p. 166]. ASSUMPTION: require at least one of the three plus ROE_avg above sector median; order candidates by number of tests passed.
- ROE threshold: only "return on equity is high" [p. 166], with S&P 500 average 22% as reference [p. 147]. ASSUMPTION: ROE_avg above the universe median over up to 10 years (needs history we do not have before 2026; forward test only).
- Financial companies: book says banks have margins around 10% and different norms [p. 146]; no screen rules given. ASSUMPTION: exclude banks/NBFCs/insurers from this screen.
- Circle of competence is not mechanizable; ASSUMPTION: whole NSE universe after a liquidity filter.

### 2.4 Earnings-capitalization intrinsic value with margin of safety

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value (intrinsic value vs price) | 162, 153 |
| Timeframe & holding period | Not found as a rule; long term, minimum four years; Buffett buys only businesses he would hold forever | 106, 107 |
| Universe / eligibility filters | Businesses inside circle of competence with a reasonably predictable earnings record | 124, 159 |
| Market / regime filter | Not found as a timing rule; cap rate is to be raised when interest rates rise or the economy slows | 160 |
| Setup conditions | Choose a representative earnings figure: diluted EPS; the most recent year, or the average of the last four years when there is a steady trend, or seven to ten years for companies with periodic extraordinary events; or a projected average (GE example: 10% growth). Divide by the capitalization rate = risk-free rate plus a risk premium; compute a range of values; the margin of safety means the price paid is way below the low end of the range | 157, 158, 159, 160, 161, 162 |
| Entry trigger & order type | Buy when price is way lower than the low end of the valuation range; no numeric margin given (Washington Post: price about a fifth of value) | 162, 32 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Sell when price exceeds value by large amounts (see 2.6) | 83 |
| Exits: trailing / time / signal | Re-value when interest rates change ("changes in interest rates require revising any valuations") and when management trust changes | 122, 220 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | 5 to 10 (Buffett), 10 to 30 (Graham) | 95 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Earnings basis | diluted EPS | basic EPS rejected | 157 |
| Earnings window | last 4 years average when trend is steady | 7 to 10 years if extraordinary items recur; most recent year; projected average | 158 |
| Projected growth (GE example) | 10% conservative | GE actual 12-15% in late 1990s | 158 |
| Risk-free rate | long bond (about 3%) | 3.5% historical average; 4% inflation-protected bonds | 161 |
| Equity risk premium | 3 to 3.5% (equities average about 7%) | multiply by beta (author rejects) | 161, 162 |
| Cap rate, high certainty of continued performance | about 10% | stable consumer products 6-8% | 159, 160 |
| Cap rate, moderate risk | 15 to 25% | banks/insurers 8-12% | 159, 160 |
| Cap rate, highly uncertain | 30 to 40% up to 100% | none | 159 |
| Cap rate, GE example | 5% (risk-free plus a small premium); 4% and 6% as alternatives | value = EPS / cap rate | 160, 161 |
| Value formula | value per share = earnings estimate / cap rate | equals P/E = 100 / required % return | 160, 114 |
| Margin of safety | price way below low end of range | Washington Post price about 1/5 of value (80%) | 162, 32 |
| Option-cost adjustment | reduce earnings for option cost; average cost about 5% of S&P 500 earnings | Cisco 24%, Microsoft 12%, IBM 8%, Oracle 16% | 229, 230 |
| Trust adjustment | lower the discount rate for high trustworthiness, raise it for moderate trustworthiness, stay away from anti-owner management | none | 220 |

**Key quotes**
- "set according to the risk-free rate, the risks of a particular business, and those of industry in general" [p. 160]
- "dividing the earnings estimate by the cap rate" [p. 160]
- "averaging the earnings over the last four years makes sense" [p. 158]
- "lengthen the period to seven to ten years to iron out those bumps" [p. 158]
- "a cap rate in the range of around 10% is appropriate" [p. 159]
- "the price you pay is way lower than the low end of your valuation estimate" [p. 162]
- "most investing errors are made not so much by paying too high a price for high-quality stocks as by buying low-quality stocks during times of economic prosperity" [p. 162]
- "If these factors indicate high trustworthiness, lower your discount rate on a good business; if they suggest moderate trustworthiness, raise it upward." [p. 220]

**Pseudocode**
```
EPS_norm = mean(diluted_eps over last 4 fiscal years)            # use 7-10y if history volatile/cyclical
EPS_adj  = EPS_norm * (1 - option_cost_fraction)                 # option_cost_fraction default 5%
rf       = long_bond_yield                                       # external input
r_mid    = rf + premium_by_risk_class                            # premium 3-3.5% base; tiers per Parameters
r_hi     = r_mid + 0.01 ; r_lo = r_mid - 0.01                    # sensitivity band (book: 1-2 point changes matter)
V_low  = EPS_low  / r_hi ;  V_high = EPS_high / r_lo             # EPS_low = worst of last 4y, EPS_high = projected
if price <= V_low * (1 - MoS):  buy candidate                    # MoS: not specified; test 0.33, 0.5, 0.8
```

**Ambiguities & assumptions**
- The book's cap-rate guidance is internally inconsistent: about 10% for businesses with high certainty [p. 159], 6 to 8% for stable consumer products [p. 160], 8 to 12% for banks/insurers [p. 159-160], and 5% for GE [p. 160]; the P/E breakpoint of 15 implies about 6.7% [p. 167]. Versions recorded; ASSUMPTION: cap rate = long-bond yield + 3.5% for the highest-quality class, + 7% mid, + 15% or more for uncertain, because that preserves the book's ordering (lower risk, lower cap rate) while anchoring to the risk-free rate [p. 159, 161].
- Margin of safety size is never quantified; examples: price about 1/5 of value (80% margin) [p. 32]; a stock at half of intrinsic value is described as a rare bargain [p. 235]. ASSUMPTION: test MoS of 33%, 50% and 80% below V_low.
- The author states precision is impossible (a 1% change in the premium shifts the S&P by about 200 points) and quotes Carret to 'ignore mechanical formulas' [p. 162]; coded version is therefore a mechanical proxy for a judgment process.
- Growth is not modeled explicitly beyond a 10% projection example; Buffett's 'owner earnings' is not defined in this book (not found in this book).
- Risk-free rate for India is not in our data. ASSUMPTION: use the 10-year government bond yield as an external constant.

### 2.5 Discounted cash flow / dividend discount valuation

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value (intrinsic value from future cash flows) | 152, 163 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Business inside circle of competence; the method works for non-dividend payers by estimating cash flows rather than dividends | 152, 153 |
| Market / regime filter | Not found; the risk-free rate is the base of the discount rate | 121, 116 |
| Setup conditions | Value is the present value of expected future cash flows (including salvage value), probability-weighted, discounted at the risk-free rate plus a risk premium. Parable: expected cash flow 25% at 40, 50% at 50, 25% at 60 gives a mean of 50 for five years, then 40 for ten years, plus 20 salvage; discounted at 15% gives about 270, versus about 389 at an 8% risk-free rate. Dividend version: share value is the present value of expected dividends, equal to earnings capitalization if retained earnings earn the cap rate | 116, 117, 163, 164 |
| Entry trigger & order type | Buy when price is well below the computed value (margin of safety); order type not found | 153, 162 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | See 2.6 | 83 |
| Exits: trailing / time / signal | Revalue when discount rates change | 122 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | 5 to 10 (Buffett), 10 to 30 (Graham) | 95 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Discount rate (parable, risky tree) | 15% | risk-free 8% in the parable; 5% insured savings | 116 |
| Cash-flow scenario weights | 25% / 50% / 25% on low / mid / high | none | 116 |
| Explicit forecast horizon (parable) | 5 years at the mean, then 10 years at a lower level | tree life 15 years | 116 |
| Rule of 72 | years to double = 72 / rate of return | 9% doubles in 8 years; 6% in 12 | 120 |
| WACC as discount rate | author rejects as circular (cost of equity from market expectations) | own judgment plus margin of safety instead | 164 |
| P/E equivalence | P/E = 100 / required rate of return (20% gives 5; 8% gives 12.5) | none | 114, 115 |

**Key quotes**
- "A share of stock or the aggregate of all shares in a market index have an intrinsic value." [p. 12]
- "Ultimately, the value of a business is the present value of all the cash it will generate for its owners over future time." [p. 16]
- "You are better off forming your own value judgment." [p. 164]

**Pseudocode**
```
CF_t = sum_s p_s * CF_{t,s}                      # scenario-weighted expected cash flow, t = 1..T
V = sum_{t=1..T} CF_t / (1 + r)^t + salvage / (1 + r)^T   # r = rf + premium (parable: 15% vs 8% rf)
dividend version: V = D1 / (r - g) is NOT given; book only says value = expected dividend stream / discount rate
buy if price <= V * (1 - MoS)
```

**Ambiguities & assumptions**
- Only the apple-tree parable gives numbers; no multi-stage DCF formula, terminal value rule or growth rate is given for real companies. ASSUMPTION: use free cash flow (CFO minus capex) with a 10-year explicit period, zero terminal growth, discount rate from 2.4's risk-class table.
- Dividend discount is described only conceptually; ASSUMPTION: applicable only to dividend payers and cross-checked against 2.4.
- The author says either method gives the same answer if perfectly applied, and that cash avoids depreciation judgment while earnings avoid lumpy items [p. 117].

### 2.6 Concentrated, no-rebalance portfolio with value-based sell rules

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other (portfolio construction and sell discipline for value picks) | 94, 95, 83 |
| Timeframe & holding period | Wait-and-see approach, no penalty for waiting ('no called strike'); minimum time frame four years; Buffett holds businesses he would be happy to hold forever | 106, 107 |
| Universe / eligibility filters | Only well-chosen common stocks that carry a margin of safety between price paid and reasonable value | 95 |
| Market / regime filter | None; do not stop and restart purchases to time the market | 94 |
| Setup conditions | Buy only when a stock is offered substantially below value; do not start with a dozen stocks on day one because that many bargains will not be found at once; concentration is acceptable | 94 |
| Entry trigger & order type | Purchase when price is far below value; order type not found | 94, 162 |
| Initial stop-loss | None. A stock that declines in both price and value to where it no longer meets the holding requirements is sold, which also gives a tax deduction for the loss | 93 |
| Exits: profit-taking | Sell good performers only if (a) price exceeds value by large amounts, (b) clearly superior opportunities exist with wider price-value gaps, (c) economic characteristics have deteriorated, or (d) management has changed hands for the worse | 83, 84 |
| Exits: trailing / time / signal | No periodic rebalancing; if selling part of a portfolio, sell the weakest first (losses, small profits) and keep the best issues last (Loeb) | 83, 84 |
| Position sizing | No formula. Concentration can be fine: buying only two cheap stocks 'may be all you need'; Loeb test: would you be comfortable committing a large portion of your resources to the single stock; Neff held as much as 40% of a fund in one sector | 94, 33 |
| Adding to / pyramiding | Not found as a rule; DCA only if price is below value (2.7) | 94 |
| Portfolio limits (max positions, correlation, heat) | For well-chosen stocks: Buffett 5 to 10, Graham 10 to 30; professionals running large money need wide diversification like casino houses; avoid over-diversification because bad stocks 'free ride' | 95 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of stocks | 5 to 10 (Buffett) | 10 to 30 (Graham); 2 stocks may be enough | 95, 94 |
| Max in one sector | not a rule; Neff reached 40% | none | 33 |
| Rebalancing | none (book calls it among the dumbest practices) | none | 83 |
| Minimum horizon | 4 years | 'wait-and-see'; hold forever for core holdings | 106, 107 |
| Sell trigger: price vs value | price exceeds value 'by large amounts' (no number) | none | 83 |
| Sell order when trimming | weakest first | none | 84 |

**Key quotes**
- "the price exceeds the value by large amounts" [p. 83]
- "Always get rid of the weakest and keep your best" [p. 84]
- "This must rank among the dumbest things people could do with investments" [p. 83]
- "between 5 and 10 stocks would be sensible; Graham says between 10 and 30" [p. 95]
- "most of the really great fortunes were made by concentration" [p. 94]
- "there is no such thing as a called strike in investing" [p. 106]
- "a minimum time frame for anyone serious about investing is four years" [p. 106]

**Pseudocode**
```
each review date (e.g., quarterly, on new fundamentals):
    for each holding h: V_h = value estimate (2.4/2.5)
        sell h if  price_h > V_h * (1 + premium_threshold)          # 'large amounts'; ASSUMPTION premium_threshold = 0.5
                or exists candidate c with (V_c/price_c) - (V_h/price_h) > gap_threshold   # ASSUMPTION 0.5
                or quality_flag_h (ratios deteriorated per 2.3 or red flag per 2.8)
                or management_flag_h
    never trim winners merely to restore target weights
    buy candidates with price <= V*(1-MoS) until holdings = N_max (default 10); leave cash otherwise
    if need to sell part: sell lowest return/lowest value-gap first
```

**Ambiguities & assumptions**
- "Large amounts" and "wider price-value gaps" are never quantified [p. 83, 84]. ASSUMPTION: sell when price exceeds the base-case value, i.e. margin of safety is gone (premium_threshold = 0), tested also at +25% and +50%.
- Position count is contradictory between masters (5-10 vs 10-30) and the author adds that 2 stocks can be enough [p. 94, 95]. ASSUMPTION: 10 positions, equal weight at purchase, no rebalancing; cash when fewer than 10 candidates exist.
- Idle cash: the author supports asset allocation to bonds/cash when stocks are not offered at prices below value [p. 95]. ASSUMPTION: unspent slots earn nothing in the backtest, or are parked in a liquid ETF as a sensitivity.
- Stop-loss: not found in this book; ASSUMPTION: none.

### 2.7 Dollar-cost averaging / dividend reinvestment, conditional on price below value

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other (systematic accumulation; mean-reversion flavoured by value) | 93, 94 |
| Timeframe & holding period | Long-term; regular purchases at set intervals (monthly in the example), through DRIPs | 93 |
| Universe / eligibility filters | Individual stocks with a basis for believing price is less than value; alternatively a broad index fund as the free-rider option, provided one has a reasonable basis that the index is cheap relative to the value it contains | 94, 92, 93 |
| Market / regime filter | Do not time the market by terminating and later resuming participation; works only if one participates during Mr. Market's gloomy moods | 94 |
| Setup conditions | Staying the course is prudent only if there is a basis for deciding that price is less than value; monitor the relationship of the stock price to value | 94 |
| Entry trigger & order type | Buy a fixed dollar amount each month (or other interval) | 93 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Stop buying if the price-value condition no longer holds | 94 |
| Position sizing | Fixed dollar amount per period; example $200 per month | 93, 94 |
| Adding to / pyramiding | The method itself; buys more shares when price is low | 93 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Contribution | $200 per month (example) | any set dollar amount | 93, 94 |
| Interval | monthly | 'or another interval' | 93 |
| Example prices | P&G at $80, $120, $100: average price $100 but average cost $97 (6.16 shares for $600) | none | 94 |
| Price-below-value gate | required for staying the course | none | 94 |

**Key quotes**
- "regular purchases of a particular stock in set dollar amounts each month (or another interval) lower the average cost of those shares" [p. 93]
- "Staying the course is prudent only if there is a basis for deciding that price is less than value." [p. 94]
- "dollar-cost averaging works to reduce your average purchase price only if you participate during Mr. Market’s gloomy moods" [p. 94]

**Pseudocode**
```
every month m:
    for each stock s in watchlist where price_s < V_s * (1 - MoS):    # value gate (needs fundamentals)
        buy floor(CONTRIB / price_s) shares
    reinvest dividends in the same stock
naive price-only variant (no gate): buy CONTRIB of stock/NIFTYBEES each month   # book does not endorse unconditionally
```

**Ambiguities & assumptions**
- The book's approval is conditional on price below value; a gate-free DCA is not what the author recommends. ASSUMPTION: backtest the naive price-only variant only as a baseline and treat the gated version as forward-test only.
- No exit or sell rule is given for DCA positions; ASSUMPTION: exit per 2.6.
- Compounding illustrations (rule of 72, tax deferral) [p. 120, 122] are arithmetic, not signals.

### 2.8 Earnings-quality and management red-flag exclusion filter

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other (exclusion / adjustment overlay on any of 2.1-2.7) | 172, 220 |
| Timeframe & holding period | Applied at purchase and at every review | 83, 84 |
| Universe / eligibility filters | Applied to all candidates; stay away from anti-owner management | 220 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Exclude or penalize companies showing: (a) a balance-sheet 'Other Assets' or deferred-cost asset that explodes (Mercury Finance: $24.6 million to $121 million in one year; AOL: deferred subscriber acquisition costs reached $385 million and became the largest asset); (b) receivable collection days rising above credit terms, or sales growth bought with looser credit; (c) low quality of income (operating cash flow / operating income); (d) income growth driven by large cuts in R&D; (e) big-bath, merger-magic, cookie-jar reserves, materiality (5% earnings) and premature revenue recognition patterns; (f) heavy option programs (overhang averaging nearly 15% of shares; option cost averaging about 5% of S&P 500 earnings) | 183, 184, 145, 150, 173, 174, 229, 230 |
| Entry trigger & order type | Not an entry rule; filter result is exclude / raise the discount rate | 220 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Sell if red flags appear after purchase (deterioration, management change) | 83, 84 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Jump in 'other assets' | roughly 5x in a year is a red flag (24.6 to 121 million) | no formal threshold | 183 |
| Receivable days vs credit terms | trouble if average days exceed policy (e.g. 70 days vs 30 or 60) | none | 145 |
| Quality of income | operating cash flow / operating income | no threshold | 150 |
| Materiality rule of thumb | about 5% of earnings (used by auditors; the book says it can mislead) | none | 174 |
| Option overhang | average rose from under 10% to nearly 15% of the company | none | 229 |
| Option cost | average about 5% of earnings, some companies about half | adjust earnings down | 229, 230 |
| Retention test | retain unrestricted earnings only if each dollar retained creates at least one dollar of market value | restricted earnings must be reinvested | 235 |
| Stock splits | 'universal folly' (frequent splits flag market-oriented management) | none | 236 |
| Board size | minimum probably six; larger boards less manageable | none | 219 |
| Combined buyback and option issuance | judge more discriminatingly | none | 235 |
| Large acquisition when core growth is falling | warning pattern (Mattel) | KPMG: 83% of mergers brought no benefit | 232, 231 |

**Key quotes**
- "The Other Assets account on its balance sheet rocketed from $24.6 million at the end of 1994 to $121 million a year later." [p. 183]
- "Mushrooming to $385 million between August 1995 and October 1996" [p. 184]
- "whether a particular item entails more than, say, a 5% impact on a company’s earnings" [p. 174]
- "Aggressive or irregular accounting is not a sign of business promise." [p. 186]
- "Stay away from options and stay as far away as possible from companies in which options constitute a" [p. 100]
- "Accordingly, you must adjust earnings" [p. 229]
- "about 5% of annual earnings among S&P 500 companies" [p. 230]
- "unrestricted earnings, which should be retained only when there is a reasonable prospect that for every dollar retained, at least one dollar of market value will be created for shareholders" [p. 235]
- "Investors should pay more for a business that is lodged in the hands of a manager with demonstrated pro-shareholder leanings" [p. 191]

**Pseudocode**
```
flags = 0
if other_assets_t / other_assets_{t-1} > 3 or deferred_cost_asset is the largest asset: flags += 1
if receivable_days_t > receivable_days_{t-1} * 1.2 and sales_growth > median: flags += 1
if CFO / operating_income < 0.7 (3-yr avg): flags += 1                      # no book threshold
if option_overhang > 0.15: flags += 1
if (market_cap_t - market_cap_{t-5}) < cumulative_retained_earnings_5y: flags += 1   # Buffett retention test, proxy
if flags >= 2: exclude;  elif flags == 1: raise cap rate by 25%
```

**Ambiguities & assumptions**
- The book names the red flags but gives thresholds only for the 5% materiality rule of thumb and the average option overhang/cost; the multipliers 3x, 1.2x, 0.7 in the pseudocode are ASSUMPTIONS.
- Governance items (independent directors, CEO/chair split, age limits) are explicitly dismissed as unreliable signals [p. 216, 217, 218]; ASSUMPTION: do not code them as positive scores. The CEO/chair split is treated by the author as a warning signal for investors [p. 217].
- Retention test is described by Buffett as a dividend policy test; using five-year market-cap change versus retained earnings is our ASSUMPTION.
- Management trust (letters, integrity) is not codable; see section 4.

## 3. Risk & money-management rules

- Margin of safety is the central risk control: price paid must be way below the low end of the valuation range, which also absorbs errors and bad luck [p. 162]. No number is prescribed; Washington Post example: about 1/5 of value [p. 32].
- Position count: 5 to 10 stocks (Buffett), 10 to 30 (Graham), for margin-of-safety stocks; large institutions need wide diversification; do not begin with a dozen stocks on day one [p. 94, 95].
- Concentration test (Loeb): ask whether you would be comfortable committing a large portion of resources to the single stock [p. 33].
- No portfolio rebalancing; trim only when fundamentals or price-value gap change; sell the weakest first [p. 83, 84].
- No margin borrowing: margin traders get margin calls when loans reach about half the portfolio value; pay off high-interest debts (credit cards 10-18%, auto 8-12%, mortgage 6-8%) before buying stocks [p. 97, 98].
- Avoid options, derivatives and companies in which options form a significant portion of capital [p. 99, 100].
- Asset allocation: do not put 100% of wealth in stocks; asset diversification is more important than stock diversification [p. 95, 96].
- Decision confidence: conservative decision makers want about 90% confidence; Buffett would not accept a 99:1 odds bet that risks distress [p. 135, 136]. Losses are weighed about 2.5 times gains by most people [p. 136].
- Time: minimum four years; prefer to wait for the pitch [p. 106].
- Tax: deferral of gains compounds (15% pre-tax return for 30 years gives about 13.3% after tax if deferred versus about 9.75% if taxed yearly) [p. 122].
- No drawdown rules, no stop-losses, no volatility-based sizing (beta and price volatility are rejected as risk measures) [p. 50, 51].

## 4. Non-codable guidance

- Mr. Market metaphor: price quotes are not value; use his mood swings, do not follow them [p. 23, 24].
- Circle of competence: stay inside businesses you can understand; the circle must be nurtured and its boundaries known ("The size of that circle is not very important; knowing its boundaries, however, is vital.") [p. 124, 125, 128]. Key questions on products, customers, distribution, geography, adaptability [p. 126, 127].
- Business-pattern judgments: brand versus commodity, supply, distribution, customer habits, organization; companies Buffett calls the Inevitables [p. 130, 131].
- Franchise / economic goodwill (ability to raise prices without losing volume) is discussed qualitatively; not given a metric [p. 126, 155, 156]. No 'moat' or 'owner earnings' wording in this text.
- Management trust: Buffett's like, trust and admire; son-in-law test; read the CEO's own letters (Welch, Eisner, Goizueta profiled); integrity first among seven traits [p. 212, 240, 241]. Owner orientation shows in good performance, reasonable pay and capital allocation [p. 224].
- Board's five jobs (CEO selection, pay, takeovers, capital allocation, reporting integrity) [p. 224]; governance templates (independent directors, split CEO/chair, term and age limits) are not reliable signals [p. 216, 217, 218].
- Psychology: overconfidence, confirmation and pattern-seeking biases; write down the reason for a decision, but do not invent one [p. 136, 137]; "An investor needs to do very few things right as long as he or she avoids big mistakes." [p. 137]
- Avoid tips, rumours, IPOs and start-ups you cannot analyse, day trading and sector rotation; 75% of day traders lose [p. 13, 75, 83].
- Avoid forecasting macro variables: "We do not have, never have had, and never will have an opinion about where the stock market, interest rates, or business activity will be a year from now." [p. 123]
- Do not trust unchecked screening databases or reported accounting figures without reading footnotes and MD&A [p. 138, 139].

## 5. Adapting to NSE (Indian equities)

- **Data required:** For 2.1-2.5: current assets, current liabilities, cash, receivables, inventory, total debt, shareholders' equity, shares outstanding, sales, COGS, operating income (EBIT), interest expense, net income, diluted EPS (4 to 10 years of history), gross fixed assets at cost, operating cash flow, capex, dividends; for 2.8: other-assets lines, receivable days, ESOP outstanding/overhang, retained earnings, board size. Price data: daily close and market cap for the entry test and for 2.7. External: 10-year government bond yield (not in our data) for the cap rate.
- **Testability with our data:** All value, ratio and quality rules (2.1-2.6, 2.8) depend on fundamentals, which exist only as point-in-time snapshots from Feb 2026 (3-year growth fields from May 2026) — so they can only be forward-tested, not backtested over 2005-2026. What is backtestable on the 2005-2026 price panel without fundamentals: (a) the naive price-only DCA baseline of 2.7 versus lump sum, on NIFTYBEES or stocks; (b) the book's claim that rebalancing hurts (compare equal-weight buy-and-hold vs periodic rebalance) [p. 83]; (c) holding-period and concentration mechanics (equal weight N = 5, 10, 30) applied to any externally supplied signal. The book offers no price-only entry signal (no 52-week-low or momentum rule; it rejects momentum and sector rotation [p. 40, 41]), so there is no price-only version of its value rules. Needs data we do not have: a risk-free rate series, long fundamental history (ROE over 5-10 years, 4-year EPS average), ESOP/option overhang, auditor and governance information, MD&A text.
- **Market-structure differences:**
  - The method is long-only, so the missing overnight shorting is not a problem.
  - NCAV and half-fixed-asset names in India are typically illiquid micro/small caps subject to circuit bands (5-20%) and surveillance restrictions. ASSUMPTION: require a minimum average daily traded value (for example 10 million rupees) and cap each position at 5% of 20-day average value; assume 0.5%+ slippage for such names versus the 0.1% base.
  - STT on delivery trades, brokerage and stamp duty are paid on every buy and sell; with a four-year horizon these are negligible, but DCA monthly buys (2.7) pay costs 12 times a year per stock.
  - Indian reporting: use consolidated Ind AS statements (ASSUMPTION), treat promoter holding as a weak proxy for owner orientation [p. 34] and promoter pledging as a negative flag (ASSUMPTION; the book has no pledging concept).
  - The author's US ratio norms (S&P 500 averages) are not Indian norms; ASSUMPTION: replace universe-average references with NSE sector medians computed from the Feb 2026 snapshot.
  - Exclude banks, NBFCs and insurers from ratio screens (liquidity ratios are not meaningful; the book itself notes different norms for banks [p. 146]).

## 6. Verdict

- **Codeability:** Partly. A few numeric screens (net-current-asset rule, P/B, P/S, P/E, current/quick ratio, coverage, turns, margins, ROE, position count) are codable, but the core method (estimating intrinsic value, circle of competence, management integrity) is explicitly judgment.
- **Priority for backtesting:** Low. The book is a framework without an executable entry/exit system or reported test results, its screens are generic value ratios, and everything fundamental can only be forward-tested on our data from Feb 2026. Items 2.1/2.2 (net-net rules) and 2.3 are the only ones worth a forward watch-list.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the ratio rules of thumb (current ratio 1.5, coverage 3-4, margins, turns) as universal hard cutoffs; the book gives different norms by industry and says very high or very low values are both warnings [p. 139, 140, 147].
  2. Using a single year of trailing EPS or a market-derived/beta discount rate and omitting the margin of safety; the book normalizes earnings (4-year average, 7-10 years for cyclicals), builds the rate from the risk-free rate plus a business-risk premium, rejects beta, and buys only way below the low end of the range [p. 158, 159, 161, 162].
  3. Importing rebalancing, equal-weight wide diversification, or mechanical stops into the portfolio; the book calls rebalancing among the dumbest practices, wants 5-30 concentrated positions, and sells only on value gap, deterioration or management change [p. 83, 84, 95].
