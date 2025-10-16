# Pre-Registration — Task 08 (Oct 15 Planning)

## Research Questions / Hypotheses
- H1 (Framing): Positive vs negative wording changes recommendations for the same data.
- H2 (Confirmation): Priming with a hypothesis increases agreement-support language relative to neutral.
- H3 (Selection Emphasis): Negative framing increases reference to turnovers/fouls; positive framing increases assists/FG% mentions.

## Dataset
- Anonymized team stats (2023–24), columns: Player, GP-GS, PTS, AVG, Rebounds, Assists, Steals, Blocks, FG%, 3PT%, FT%.  
- No PII; mapped to Player A/B/C.

## Experimental Factors
- Conditions: Neutral, Positive, Negative, Confirmation-primed.
- Models: ≥2 (e.g., GPT-4, Claude).
- Replicates: 3–5 responses per prompt/model.

## Outcome Measures
- Mentions: which players/metrics referenced per condition.
- Sentiment (lexical): positive/negative/neutral phrasing counts.
- Recommendation types: individual vs team, offensive vs defensive.
- Agreement rate with primed hypothesis.

## Controls
- Same dataset text across conditions.
- Record model version, temp, seed; keep lengths balanced.

## Analysis Plan (later)
- Chi-square or Fisher tests for categorical differences in mentions.
- t-test/Mann–Whitney for counts where applicable.
- Qualitative examples of language differences; hallucination flags vs stats.

## Limitations
- Single season; small sample; narrative subjectivity.

*Filed on Oct 15 as initial planning milestone.*
