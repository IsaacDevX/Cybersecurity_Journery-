# Risk Management

**Date started:** 2026-10-12
**Source:** Professor Messer Security+ SY0-701

## What Risk Management Is

The process of identifying, assessing, and treating risks before they become problems. Every project has risks — risk management is how we deal with them.

---

## The Core Terms

| Term | Meaning |
|------|---------|
| **Risk** | The chance that something bad happens |
| **Threat** | What could cause harm (hacker, flood, fire) |
| **Vulnerability** | A weakness that allows a threat to succeed |
| **Likelihood** | How likely is it to happen? |
| **Impact** | What's the damage if it happens? |

---

## Risk Assessment Types

### Continuous Assessment
- Part of an existing process
- Runs all the time

### Ad Hoc Assessment
- Done when the situation requires it
- No formal process exists

### Recurring Assessment
- Runs on a standard schedule (monthly, quarterly, yearly)

---

## Risk Appetite vs Risk Tolerance

**Risk Appetite:** The acceptable level of risk (like a speed limit)
- Conservative — very low risk allowed
- Neutral — moderate risk allowed
- Expansionary — high risk allowed

**Risk Tolerance:** The wiggle room before action is taken
- "We accept 55km/h, but we only ticket above 60km/h"

---

## Risk Register

A spreadsheet that tracks every risk:

| Risk | Likelihood | Impact | Owner | Mitigation | Status |
|------|-----------|--------|-------|-----------|--------|
| Example | Medium | High | Name | Action | Open |

---

## Likelihood vs Probability

- **Likelihood** = descriptive (rare, possible, likely, almost certain)
- **Probability** = numeric (5%, 30%, 75%)

**The Risk Matrix:** Combines likelihood × consequence to determine risk level. Higher = worse = act first.

---

## Impact Types

1. **Life** — most important
2. **Safety** — dangerous environments
3. **Property** — physical assets

---

## Quantitative Risk Assessment

**Formula:**

| Symbol | Full Name | Meaning |
|--------|-----------|---------|
| AV | Asset Value | What it's worth |
| EF | Exposure Factor | % lost in one event |
| SLE | Single Loss Expectancy | Loss from one event |
| ARO | Annualized Rate of Occurrence | Events per year |
| ALE | Annualized Loss Expectancy | Expected yearly loss |

**Example:**
- Laptop = ₦500,000 (AV)
- Stolen = full loss (EF = 1.0)
- SLE = ₦500,000
- 7 stolen/year (ARO = 7)
- ALE = ₦3,500,000/year

**Use it to justify security spending.** If controls cost less than the ALE, buy them.

---

## Qualitative Risk Assessment

Used when exact numbers aren't available. Uses colors or ratings:

| Rating | Meaning |
|--------|---------|
| 🟢 Green | Low — fine |
| 🟡 Yellow | Medium — monitor |
| 🔴 Red | High — act now |

---

## The 4 Risk Treatments

1. **Accept** — the risk is small, live with it
2. **Avoid** — stop the activity that creates the risk
3. **Transfer** — buy insurance or outsource (transfer the risk to someone else)
4. **Mitigate** — reduce the risk with controls

---

## Key Takeaways

1. Risk = threat × vulnerability × impact
2. Use quantitative math (SLE/ALE) when you can — justify spending with numbers
3. Use qualitative (green/yellow/red) when numbers aren't available
4. Every risk needs an owner
5. The 4 treatments: Accept, Avoid, Transfer, Mitigate

---

*Last updated: October 2026*
