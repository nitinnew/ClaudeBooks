# The Winning RSI Playbook — Hima Reddy (Celer Wealth LLC / HimaReddy.com, 2017; promotional ebook)

- **Source file:** Google Drive `The-Winning-RSI-Playbook-ebook.pdf` (file id `1QsISr2JGIDca0svupL2Mr90skd45AnC-`, 2,712,722 bytes), 27 PDF pages with a text layer (p. 1 is a cover image).
  - The author is identified in the text: "Founder & Head Trader, HimaReddy.com", signed "Hima" [p. 2]. The inventory key keeps the `unknown_` prefix for stability.
- **Text file used:** text/unknown_winning_rsi_playbook.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index; printed "Page X of 26" = PDF page X + 1). Always take N from the marker.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/unknown_winning_rsi_playbook.md text/unknown_winning_rsi_playbook.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 27]].
  - Pages 2–12 are an analogy-based introduction (racetrack, football field) with no rules.
  - Chart images are not readable. Their captions and printed RSI values were read.
  - The ebook ends by teasing a paid strategy ("The Bull Bear RSI Faceoff"); its entry/exit rules are **not** in this PDF [p. 27].

## 1. The method in brief

The book replaces fixed RSI 70/30 overbought/oversold levels with regime-dependent "Power Zones" on a **14-period RSI** (any timeframe) [p. 16–17]:

| Regime | Resistance zone | Support zone |
|---|---|---|
| Bear / down-trend | 55–65 | 20–30 |
| Bull / up-trend | 80–90 | 40–50 |

**Reading the regime**
- A rally that stalls in 55–65 without reaching 70 marks a bear regime [p. 21, 27].
- Pullbacks that hold 40–50 mark a bull regime [p. 22–23].
- A break above a prior price high hints at a trend change from down to up [p. 22, 25].

**Signals**
- Traditional 70/30 cross-backs are acknowledged as sometimes working: tighten stops, or watch for a reversal [p. 19, 25–26].
- The book argues they fail in strong trends [p. 14, 24].
- Evidence: 2 chart walk-throughs (ES 60-min, May 12–25 [year not given]; CL daily, Feb–Aug 2016). No statistics.

## 2. Strategies

| # | Strategy | Timeframe | Entry rule (as stated) | Stop / exit (as stated) | Page |
|---|---|---|---|---|---|
| 2.1 | RSI Power Zone regime trading (trend continuation) | Any timeframe with RSI(14) (examples: ES 60-min, CL daily) | Bull regime: buy/hold as RSI pulls back into and holds 40–50, with price consolidating after breaking a prior high; expect a move toward RSI 80–90. Bear regime (implied mirror): sell rallies that stall with RSI in 55–65; expect a drop toward 20–30 | Not specified. Reaching the regime's resistance zone (80–90) is shown as the objective of the bull leg | 16–17, 22–24 |
| 2.2 | Traditional RSI 70/30 cross-back, used as a caution signal only | Any | RSI crosses above 70 and falls back below → tighten stops on longs / watch for a top. RSI below 30 then back above → watch for a buy. Filter: in a bear regime, ignore buy signals whose subsequent rally fails to reach 55–65 (the "painful" case) | Not specified | 13–14, 19–21, 25–26 |

**Parameters**

- RSI period 14, fixed: "these zones only work if the period setting is 14" [p. 17].
- Bear zones: resistance 55–65, support 20–30. Bull zones: resistance 80–90, support 40–50 [p. 16].
- Traditional thresholds: 70 overbought, 30 oversold [p. 13–14].

**Key quotes**

- "RSI Bear Resistance Power Zone: 55 to 65" [p. 16]
- "RSI Bear Support Power Zone: 20 to 30" [p. 16]
- "RSI Bull Resistance Power Zone: 80 to 90" [p. 16]
- "RSI Bull Support Power Zone: 40 to 50" [p. 16]
- "Down trending or bear markets generally find resistance when the RSI is in the Power Resistance Zone from 55 to 65." [p. 16]
- "Instead, bull markets generally stabilize ahead of the Power Support Zone from 40 to 50." [p. 17]
- "these zones only work if the period setting is 14" [p. 17]
- "This signal offered a fine opportunity to tighten up stops on long positions, or keep an eye out for a potential trend reversal (topping pattern)." [p. 19]
- "And the clue that the Power Zones give is that the rally from 26.66 didn’t quite get back to the Bear Market Resistance Power Zone (55 to 65)." [p. 21]
- "The key point here is that the ES broke above a previous high, then consolidated (traded sideways)." [p. 22]
- "The issue I’ve noticed with many of the sell from above 70 or buy from below 30 signals is that they can be short-lived, especially when the market’s in a strong uptrend." [p. 14]

**Pseudocode** (ASSUMPTIONS are needed because the book gives no explicit entry/exit rules)

```
rsi = RSI(close, 14)                        # Wilder
# regime state (ASSUMPTION: book infers regime from zone behaviour + price structure)
bull_regime when (max(rsi, last 20 bars) >= 70 and min(rsi, last 20 bars) >= 40)      # ASSUMPTION
            or (close > prior swing high and rsi holds >= 40 on pullback)              # p.22
bear_regime when (max(rsi, last 20 bars) <= 65 and min(rsi, last 20 bars) <= 30)       # ASSUMPTION
# 2.1 long (bull continuation)
if bull_regime and rsi crosses up from 40-50 band (rsi[-1] in [40,50] and rsi > 50): buy   # ASSUMPTION trigger
exit long: rsi enters 80-90 (target)  or  rsi closes < 40 (zone failure, ASSUMPTION)
# 2.1 short (bear continuation, mirror)
if bear_regime and rsi turns down from 55-65 band (rsi[-1] in [55,65] and rsi < 55): sell
exit short: rsi enters 20-30  or  rsi closes > 65 (ASSUMPTION)
# 2.2 caution flags
flag_top  when rsi[-1] > 70 and rsi <= 70     -> tighten long stops (no auto-short)
flag_buy  when rsi[-1] < 30 and rsi >= 30     -> only act if regime is bull (ASSUMPTION per p.21)
```

**Ambiguities & assumptions**

- **No explicit entry, exit, stop or sizing rules** are given; these are reserved for a paid product [p. 27]. Every trigger above is an ASSUMPTION built from chart commentary.
- **Regime identification is discretionary:** "break of a previous high" plus where RSI peaks and troughs. The look-back windows are ASSUMPTIONS.
- **The price/RSI divergence** ("price and RSI moving away from each other") is highlighted three times but never defined [p. 20–21, 27].
- **The ES example year is not stated** ("May 12th – May 25th") [p. 17].

## 3. Risk & money-management rules

- None stated, beyond using the RSI > 70 cross-back as a cue to tighten stops on longs [p. 19].

## 4. Non-codable guidance

- Momentum leads price: momentum peaks before price tops and bottoms before price bottoms [p. 7–9].
- A 24-hour (Globex-inclusive) chart is used for ES [p. 23].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily and 60-minute OHLC for NIFTY/BANKNIFTY futures, liquid F&O stocks and sector indices; RSI(14).
- **Testability with our data:** 2.1 and 2.2 are testable after the assumed triggers above. They suit a regime-filter study: do zone-defined regimes improve forward returns vs plain 70/30?
- **Market-structure differences:**
  - NSE has no 24-hour session; use regular-session bars (09:15–15:30). RSI levels will differ from a 24-hour ES chart.
  - Gap openings are more frequent, so 60-min RSI may jump between zones at the open.

## 6. Verdict

- **Codeability:** Low–partial. The zone thresholds are explicit numbers, but the triggers, regime definition, exits and stops are left to chart interpretation or a paid add-on.
- **Priority for backtesting:** Low as a standalone strategy. Useful as a cheap regime-filter feature (RSI(14) range shift: 40–90 bull vs 20–65 bear) to test as a filter on other strategies.
- **Top 3 things a coder is most likely to get wrong**
  1. Using RSI with a period other than 14. The author says the zones only hold for 14 [p. 17].
  2. Treating the zones as stand-alone overbought/oversold reversal levels. They are regime-specific: 40–50 is support only in a bull regime, 55–65 resistance only in a bear regime [p. 16–17].
  3. Coding the teased divergence or "Bull Bear RSI Faceoff" rules as if specified here. They are not in this PDF [p. 27].
