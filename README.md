# 🧪 SU OPT Research – Bias Detection in LLM Narratives (Task 08)

This repository contains my research work for **Task 08** of the Syracuse University OPT Research Program.  
The goal of this task is to **design and execute a controlled experiment** that detects whether a Large Language Model (LLM) produces **biased narratives** when given identical data but differently framed questions.

The work is completed in **three stages**:

- **October 15** – Experimental planning, repository setup  
- **October 30** – Prompt matrix design + initial bias detection pipeline  
- **November 15** – Final experiment runs + full analysis + written report  

All data used in this project is **anonymized** and no raw datasets or PII are stored in the repository.

---

## 📁 Repository Structure

Task_08_Bias_Detection:
  data:
    - "(raw anonymized datasets – excluded from repo)"
  
  prompts:
    variants:
      - neutral/
      - positive/
      - negative/
      - confirmation/
    compiled:
      - "(auto-generated prompt sets)"
    - prompt_plan.csv

  scripts:
    - create_prompt_matrix.py
    - open_prompt.py
    - run_final_bias_experiment.py
    - analyze_bias.py
    - score_sentiment_variants.py
    - analyze_final_bias.py

  results:
    raw:
      - "(LLM raw outputs)"
    logs:
      - variant_test_log.csv
      - final_bias_log.csv
    analysis:
      - final_bias_summary.csv
      - final_sentiment_boxplot.png
      - final_sentiment_means.png

  analysis:
    - "(consolidated CSVs + charts)"

  docs:
    - TASK08_Final_Report.md

  README.md: "(main documentation)"


---

## 🟦 **Stage 1 — October 15: Initial Planning & Setup**

### ✔️ Completed
- Created repository structure  
- Added **safe `.gitignore`** to prevent committing PII/raw data  
- Designed the initial experiment concept  
- Defined framing conditions:
  - Neutral  
  - Positive  
  - Negative  
  - Confirmation-primed (planned)  
- Created `responses_schema.csv` for structured LLM response logging  
- Submitted mid-cycle Qualtrics + email  

---

## 🟧 **Stage 2 — October 30: Prompt Matrix & Early Experimentation**

### ✔️ Completed
- Implemented `create_prompt_matrix.py` to generate:
  - Prompt variants  
  - Embedded dataset into each prompt  
  - Replicate runs  
- Saved compiled prompts in `prompts/compiled/`  
- Created `prompt_plan.csv` mapping every run  
- Implemented simple sentiment scoring (positive/negative keywords)  
- Ran initial (simulated) bias tests to validate the pipeline  
- Logged early outputs in `results/logs/variant_test_log.csv`

---

## 🟥 **Stage 3 — November 15: Final Experiment & Analysis**

### ✔️ Completed
- Ran full framing experiment using:

scripts/run_final_bias_experiment.py
- Logged structured runs into:

results/logs/final_bias_log.csv
- Executed final sentiment scoring + variance analysis:

scripts/analyze_final_bias.py
- Generated:
- `analysis/final_bias_summary.csv`
- `analysis/final_sentiment_boxplot.png`
- `analysis/final_sentiment_means.png`

- Wrote full final report:
docs/TASK08_Final_Report.md


---

## 📊 **Key Findings (High-Level)**

- **Framing strongly shifts narrative tone**, even though the dataset is identical.
- **Positive prompts** consistently produced more optimistic wording.
- **Negative prompts** reinforced weaknesses and problems.
- **Neutral prompts** generated the most consistent factual summaries.
- Confirms that **LLMs are sensitive to question framing**, a reproducible form of prompt bias.

For detailed analysis, see the full report:  
📄 `docs/TASK08_Final_Report.md`

---

## 🛡️ Privacy & Compliance

- All data is **anonymized** (Player A, Player B, …).  
- No PII or raw university datasets are committed.  
- `.gitignore` prevents committing sensitive/large files.  
- Pipeline is API-agnostic and works with manual copy/paste collection.

---

## 🚀 Status: **Task 08 Completed ✔️**

All deliverables for **Oct 15, Oct 30, and Nov 15** are fully completed, documented, and committed.

