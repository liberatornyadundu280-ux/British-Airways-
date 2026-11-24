# British Airways Lounge Eligibility Lookup (Task 1)

## Project purpose

This project builds a reusable lookup model to estimate lounge-eligible passenger demand for British Airways departures from London Heathrow (LHR), with the assignment focused on Terminal 3. The model groups flights into broad operational categories so planning estimates can still be made when future flight numbers, destinations, schedules, or aircraft assignments change.

## Deliverable

- **British Airways Lounge Eligibility Lookup - Completed.xlsx** — completed two-tab workbook. The *Lounge Eligibility Lookup Table* contains the flight buckets and Tier 1, Tier 2, and Tier 3 rates. The *Justification* tab records the grouping, assumptions, and intended future use.

## Data and scope

The source is the supplied British Airways summer schedule dataset. The analysis filters to BA flights departing LHR. It uses the 10,000 schedule records in the file and groups them by:

- **Haul:** SHORT or LONG, as provided in the data.
- **Local departure time:** Early morning (06:00-10:59), midday (11:00-16:59), evening (17:00-21:59), and night (22:00-05:59). Long-haul flights use three combined periods: morning, midday/afternoon, and evening/night.

The lookup has seven mutually exclusive haul/time buckets. Destinations listed in the workbook are examples from the source schedule.

## How the rates were calculated

For each bucket and tier:

`Rate = Sum of tier-eligible passenger counts / Sum of total seats`

`Total seats = First Class seats + Business Class seats + Economy seats`

The resulting ratios are capacity-weighted, since bucket totals are divided by bucket seat capacity. Rates are rounded to two decimal percentage points in the workbook. Use a rate as a lookup assumption, then multiply it by the estimated passenger volume for a future flight or schedule and sum estimated eligible passengers by tier.

## Lounge tiers in the assignment

- **Tier 1:** Concorde Room demand indicator; modeled as a hypothetical planning measure for LHR T3.
- **Tier 2:** First Lounge eligibility.
- **Tier 3:** Club Lounge eligibility.

The model treats the three supplied tier-eligible passenger fields as separate tiers. When applying the estimates, count each passenger in only one tier so the same person is not double-counted across lounge demand totals.

## Interpretation and limitations

These rates are historical, seat-capacity-based proxies from the supplied seasonal schedule. They do not measure actual future lounge visits or actual passenger loads. The dataset does not provide a complete breakdown of future passenger volumes, loyalty status, or lounge choices. Tier 1 should be interpreted as a hypothetical demand indicator, not evidence that a Concorde Room is currently available at T3.

The night short-haul bucket has 372 schedule records, fewer than the other buckets; treat its rate as less stable. Before using the estimates for a capacity or investment decision, validate them against actual flown loads, current BA tier eligibility rules, observed lounge usage, and a more recent schedule. Recalculate the bucket rates when the underlying data changes.

## Reuse steps

1. Filter the new schedule to BA departures from LHR (and to T3 if terminal-level data is available).
2. Assign each flight to a haul/time bucket using the same definitions.
3. Look up the three tier rates from the workbook.
4. Multiply each rate by the flight’s estimated passenger volume.
5. Sum estimated eligible passengers by tier for the planning day or period.
6. Compare the estimates with observed passenger and lounge-use data, then refresh the rates if needed.

## Project files

- `British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx` — input schedule.
- `Problem statement.pdf` — assignment brief.
- `Lounge Eligibility Lookup Template - Task 1.xlsx` — supplied blank template.
- `British Airways Lounge Eligibility Lookup - Completed.xlsx` — completed lookup and written methodology.
