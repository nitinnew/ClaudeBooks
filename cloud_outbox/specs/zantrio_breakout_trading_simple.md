# Breakout Trading: Simple, Proven Strategies for Identifying and Profiting from Breakouts — Zantrio, LLC (no author named)

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/Private/Breakout_Trading_Simple_Proven_Strategies.pdf` (file id `1HydNy2uiP2ETzTqhfidN4u4XKt2Z-I_H`, 362,355 bytes; © 2014 Zantrio, LLC [p. 5]). Key renamed from `unknown_breakout_trading_simple`; no personal author is named anywhere in the text.
- **Text file used:** text/zantrio_breakout_trading_simple.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/zantrio_breakout_trading_simple.md text/zantrio_breakout_trading_simple.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read, [[PAGE 1]] to [[PAGE 16]]. Page 1 is the cover (no text). Charts (EURGBP channel, reversal breakout, triangle, Bollinger squeeze) are images. Pages 5–8 and 16 are legal text and promotions.

## 1. The method in brief

A 16-page introductory pamphlet, written mostly with forex in mind (it notes volume is unavailable in forex) [p. 12]. It describes breakouts from channels, trend lines, consolidations and triangles [p. 9–11]; says low volatility (narrowing Bollinger Bands, falling ATR, converging triangle sides) predicts breakouts [p. 12]; says most breakouts are false and should be confirmed with MACD/RSI momentum and a fundamental news driver [p. 13–15]. It gives a three-step checklist [p. 14] but **no entry trigger, stop-loss, exit, position-size or parameter values**, and no evidence. It is a framework, not a rule set.

## 2. Strategies

### 2.1 Low-volatility pattern breakout with momentum confirmation (framework only)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout (continuation or reversal) | 9–10 |
| Timeframe & holding period | Not stated | — |
| Universe / eligibility filters | Stocks and currency pairs | 4 |
| Market / regime filter | Not stated | — |
| Setup conditions | Chart pattern (trend line, ascending/descending channel, continuation pattern, triangle) plus low volatility (moving averages, Bollinger Bands, ATR); ascending triangles "often lead to a breakout to the upside" | 11–12, 14 |
| Entry trigger & order type | Not stated beyond "breaks out of its trading range"; confirm with MACD/RSI and a fundamental/news driver | 4, 13–14 |
| Initial stop-loss | Not stated | — |
| Exits: profit-taking | Not stated | — |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | Not stated | — |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RSI overbought / oversold | 70 / 30 | 50 = no momentum | 13 |
| Volatility tools | MA, Bollinger Bands, ATR | — | 12, 14 |

**Key quotes**

- "The goal is to look for securities with low volatility, since low volatility can indicate an upcoming breakout." [p. 12]
- "Beware of false breakouts, which often happen when the apparent breakout isn’t supported by these indicators." [p. 14]
- "if prices are rising and the MACD is strongly positive, then any downside breakout that occurs is likely to be a false one" [p. 13]
- "If there isn’t, then there is a good chance that the breakout isn’t real." [p. 13]

**Pseudocode** (coder's construction; almost every value is an ASSUMPTION because the pamphlet gives none)

```
squeeze_t   = BBwidth(20,2)_t in lowest 10% of last 120 days  or  ATR(14)/C in lowest 20% of last 120 days
breakout_t  = C_t > max(H_{t-20..t-1})                        # "breaks out of its trading range"
momentum_t  = MACD(12,26,9) line > 0 and RSI14_t > 50          # "supported by these indicators"
enter at C_t when squeeze within last 5 days and breakout_t and momentum_t
stop = min(L_{t-20..t-1}) ; exit: 2R target or close < SMA20   # not in the book
news filter: not implementable (no news data)
```

**Ambiguities & assumptions**

- Entry, stop, target, timeframe and all thresholds are absent. ASSUMPTION: as in pseudocode; any result is a test of the coder's rules, not of this book.
- "Fundamental news" confirmation [p. 13–14] cannot be coded with our data. ASSUMPTION: omitted.

## 3. Risk & money-management rules

None beyond a generic risk disclaimer ("do NOT invest money you cannot afford to lose") [p. 5].

## 4. Non-codable guidance

- Most breakouts are fake-outs; institutions trade against breakouts [p. 13, 15].
- Decide whether a breakout is likely a continuation or a reversal [p. 14].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV; Bollinger Bands, ATR, MACD, RSI.
- **Testability with our data:** A coder-defined version is backtestable on 2005–2026 prices, but it would duplicate the more specific squeeze/breakout specs (Persic, Giannino setups 18/26, Ladha Strategy 2). The news-confirmation filter cannot be tested.
- **Market-structure differences:** Written for forex; volume is available for NSE stocks, so a volume filter (not in the book) would be a natural addition. Long-only for the NSE cash market; STT, brokerage, ~0.1% slippage.

## 6. Verdict

- **Codeability:** Not codable as written. It has no entry trigger, stop, exit or parameter values; any implementation is the coder's own rules.
- **Priority for backtesting:** Low. A generic introductory pamphlet; the same ideas are specified concretely in other specs already delivered.
- **Top 3 things a coder is most likely to get wrong**
  1. Attributing results to this book: the rules would be invented, not extracted.
  2. Reading "low volatility" as a fixed threshold; the book only names the tools (MA, Bollinger, ATR) [p. 12].
  3. Ignoring that its momentum check is directional: a strongly positive MACD argues against a *downside* breakout [p. 13].
