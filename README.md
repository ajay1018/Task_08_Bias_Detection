# Task 08 – Bias Detection in LLM Data Narratives

## Objective (Oct 15 – Initial Planning)
Design a **controlled experiment** to test whether prompt framing changes LLM-generated narratives on the *same data*. Focus: **framing effects** and **confirmation bias** using anonymized sports stats from earlier tasks. No execution yet—planning only.

## Ethics & Compliance
- No PII or real names. All entities will be anonymized as **Player A, Player B, ...**.
- Source datasets are **excluded** from the repo; only **anonymized derived** data is used.
- Prompts avoid protected attributes unless using synthetic, non-identifying placeholders.

## Planned Hypotheses
- **H1 (Framing):** “Underperforming” vs “High-potential” wording results in systematically different recommendations for the same player profile.
- **H2 (Confirmation):** Priming the model with a hypothesis (“Player C struggles defensively”) increases supportive evidence language vs. neutral framing.
- **H3 (Selection emphasis):** Negative framing increases reference to turnovers/fouls; positive framing increases reference to assists/FG%.

## Experimental Design (Pre-registered)
- **Dataset:** Anonymized 2023–24 team stats derived from Task 05 (no names).  
- **Conditions per prompt set (minimally different wording):**  
  - Neutral, Positive-framed, Negative-framed, Hypothesis-primed.
- **Models:** At least 2 LLMs (e.g., GPT-4, Claude).  
- **Replicates:** 3–5 samples/condition/model to average stochasticity.  
- **Logging:** JSONL/CSV with prompt variant, response, model/version, timestamp.

## Deliverables Plan
- `scripts/experiment_design.py` → auto-generate prompt variants from anonymized CSV
- `scripts/run_experiment.py` → (later) run prompts against 2 LLMs, log JSONL
- `scripts/analyze_bias.py` → (later) quantify framing effects (mentions/sentiment)
- `scripts/validate_claims.py` → (later) cross-check claims vs stats
- `prompts/` → final prompt templates (generated)
- `results/` → raw outputs/logs (text/jsonl)
- `analysis/` → summary tables & plots
- `docs/REPORT.md` → final write-up (Nov 15)

*This README reflects Oct 15 planning only.*
## Oct 30  Progress Snapshot
- Generated prompt matrix with IDs (prompts/prompt_plan.csv) and compiled prompts.
- Created framing variants and simulated LLM responses (esults/raw/response_*.txt).
- Logged runs (esults/logs/bias_responses_log.csv).
- Scored sentiment by variant and saved outputs:
  - nalysis/variant_sentiment_summary.csv
  - nalysis/variant_sentiment_proxy.png
- Next: collect 3 real responses per variant/model label and re-run analysis.
