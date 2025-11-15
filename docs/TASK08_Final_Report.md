\# Task 08 – Bias Detection in LLM-Generated Narratives  

\*\*Student:\*\* Ajay Ashok Shinde  

\*\*Project:\*\* SU OPT Research – Sports Analytics / LLM Bias Experiments  



---



\## 1. Objective



The goal of this task was to design and execute a \*\*controlled experiment\*\* to see whether the \*\*same underlying dataset\*\* can lead to \*\*systematically different narratives\*\* from a Large Language Model (LLM), depending only on how the question is framed.  



Rather than proving that a model is “biased” in an absolute sense, the focus is on documenting:



\- How framing (neutral / positive / negative / confirmation-primed) shapes narratives.  

\- How to build a reproducible pipeline that logs prompts, responses, and simple metrics.  

\- How to check for consistency and possible bias in AI-generated sports analysis.



All experiments were done with \*\*anonymized player identifiers\*\* (e.g., “Player A”) and without storing any raw source data or PII in GitHub.



---



\## 2. Dataset and Anonymization



I reused the \*\*Syracuse Men’s Basketball 2023–24 season stats\*\* that I had previously cleaned in earlier tasks:



\- Base file (local only): `data/basketball\_2023\_clean.csv`  

\- An anonymized version was created (example): `data/anonymized\_stats.csv`  



In the anonymized table:



\- Real names were replaced with generic labels such as `Player A`, `Player B`, etc.  

\- Only high-level performance metrics like PTS, AVG, Rebounds, Assists, Steals, Blocks, FG%, 3PT%, FT% were preserved.  

\- No personally identifying information (names, IDs, demographics) was kept.  



The raw dataset and any original PDFs remain \*\*excluded\*\* from the repository via `.gitignore` to comply with the instructions and OPT/PII constraints.



---



\## 3. Experimental Design



\### 3.1 Prompt Framing Conditions



I designed four conceptual framing conditions (for this period I implemented three concretely in code, and planned the fourth):



1\. \*\*Neutral framing\*\*  

&nbsp;  - Objective, factual summary: “Summarize the team’s season using the provided metrics. Provide an objective, data-focused description.”



2\. \*\*Positive framing\*\*  

&nbsp;  - Emphasizes strengths and progress: “Highlight achievements, growth, and strengths while remaining data-driven.”



3\. \*\*Negative framing\*\*  

&nbsp;  - Emphasizes weaknesses and problems: “Focus on concerns, weaknesses, and areas needing major improvement.”



4\. \*\*Confirmation-primed framing\*\* (planned / scaffolded)  

&nbsp;  - Starts with a hypothesis such as “Player C struggles defensively” and asks if the model agrees or disagrees, with evidence.



The core dataset is identical in all conditions; only the \*\*wording of the question\*\* changes. This isolates \*\*framing\*\* as the main variable.



\### 3.2 Prompt Matrix \& IDs



To make the experiment reproducible, I created a \*\*prompt matrix\*\* with IDs in:



\- `prompts/prompt\_plan.csv`  

\- Compiled prompt text files: `prompts/compiled/\*.txt`



Each row in the plan links:



\- `Prompt\_ID` – a unique identifier (e.g., `neutral\_Model\_A\_1`)  

\- `Prompt\_Variant` – neutral / positive / negative / confirm\_prime  

\- `Model\_Label` – a label such as `Model\_A` or `Model\_B` (so I can later map to actual LLMs if needed)  

\- `Replicate` – replicate number (e.g., 1–3)  

\- `Prompt\_File` – which text file contains the full dataset + question



This matrix allows repeated runs and structured logging without relying on any specific API.



---



\## 4. Implementation and Workflow



\### 4.1 Directory Structure



The project is organized as:



\- `data/` – anonymized CSVs and intermediate derived files (not raw source data).  

\- `prompts/` – framing variants, compiled prompts, and `prompt\_plan.csv`.  

\- `results/raw/` – raw LLM responses (or simulations) as `.txt` files.  

\- `results/logs/` – CSV logs of which prompt/variant/model was run.  

\- `analysis/` – scored outputs, summaries, and plots.  

\- `scripts/` – Python scripts to generate prompts, simulate or collect responses, and analyze bias.  

\- `docs/` – written reports like this one.



A Python-focused `.gitignore` ensures that \*\*raw datasets, audio, and large binaries\*\* are not committed.



\### 4.2 Prompt Generation



Key script:



\- `scripts/create\_prompt\_matrix.py`  



This script:



1\. Loads the anonymized stats from `data/anonymized\_stats.csv`.  

2\. Selects core columns (Player, GP-GS, PTS, AVG, Rebounds, Assists, Steals, Blocks, FG%, 3PT%, FT%).  

3\. Embeds that table as CSV text inside each prompt.  

4\. Attaches different framing questions (neutral, positive, negative, confirm-primed).  

5\. Writes compiled prompts to `prompts/compiled/\*.txt`.  

6\. Creates `prompts/prompt\_plan.csv` with one row per (variant, model label, replicate).



The result is a \*\*reusable, fully-specified prompt matrix\*\*.



\### 4.3 Response Collection (Manual / API-Free)



Because this research must be portable and not bound to a specific API or key, I used a \*\*manual collection approach\*\*:



\- I added a structured CSV template:  

&nbsp; `results/raw/collection\_template.csv`  



\- Columns include:  

&nbsp; - `Prompt\_ID`  

&nbsp; - `Prompt\_Variant`  

&nbsp; - `Model\_Label`  

&nbsp; - `Replicate`  

&nbsp; - `Timestamp`  

&nbsp; - `Response\_Text`  

&nbsp; - `Notes`  



\- I created a small helper script, `scripts/open\_prompt.py`, which prints the full text of any prompt based on `Prompt\_ID`.  

&nbsp; - I can copy that prompt into the LLM UI, then paste the resulting answer back into the CSV.



For the November 15 experiment, I also created a small simulation script to generate consistent structure and verify the pipeline:



\- `scripts/run\_final\_bias\_experiment.py`  

&nbsp; - Writes responses such as `results/raw/round3\_\[variant]\_\[run].txt`  

&nbsp; - Logs them in `results/logs/final\_bias\_log.csv`  



Even though this uses simulated text for this checkpoint, the \*\*same pipeline\*\* works with real LLM outputs.



---



\## 5. Bias Metrics and Analysis



\### 5.1 Sentiment / Framing Proxies



I implemented keyword-based proxies in scripts such as:



\- `scripts/analyze\_bias.py`  

\- `scripts/score\_sentiment\_variants.py`  

\- `scripts/analyze\_final\_bias.py`



The general idea:



\- Define \*\*positive terms\*\* (e.g., “improve”, “growth”, “potential”, “progress”, “strength”, “resilience”).  

\- Define \*\*negative terms\*\* (e.g., “underperform”, “weakness”, “struggle”, “concern”, “decline”, “lapses”).  

\- For each response, count how often each list appears.  

\- Compute a \*\*sentiment\_proxy = pos\_hits − neg\_hits\*\*.  



This is a very simple but transparent way to see whether \*\*positive framing\*\* tends to produce more positive wording than \*\*negative framing\*\*, even though the underlying stats are unchanged.



\### 5.2 Final Bias Experiment (Nov 15)



For the final deliverable, I used:



\- `results/logs/final\_bias\_log.csv` – log of runs for each variant.  

\- `scripts/analyze\_final\_bias.py` – final aggregation and visualization script.



The script:



1\. Loads the log file with per-response sentiment scores.  

2\. Aggregates by `variant` to compute `mean`, `std`, and `count` of sentiment.  

3\. Saves the aggregation to:  

&nbsp;  - `analysis/final\_bias\_summary.csv`  



4\. Produces two plots:  

&nbsp;  - `analysis/final\_sentiment\_boxplot.png` – distribution of sentiment scores by variant.  

&nbsp;  - `analysis/final\_sentiment\_means.png` – bar chart of mean sentiment per variant.



These outputs allow me to visually compare whether the \*\*distribution or mean sentiment\*\* shifts when the model is asked the same underlying question with different framing.



Because the actual numeric sentiment values are generated in the current setup, this phase is less about the “true” sentiment level and more about:



\- Debugging the analysis pipeline.  

\- Demonstrating how to \*\*statistically compare\*\* different framings or models.  

\- Showing how this could be extended to real model outputs in a consistent way.



---



\## 6. Interpretation and Reflection



\### 6.1 What This Experiment Tests



The experiment is designed to answer questions like:



\- Does a \*\*positive framing\*\* systematically generate more “optimistic” language than a neutral framing when summarizing the same stats?  

\- Does a \*\*negative framing\*\* invite more focus on weaknesses, even when the dataset includes several strengths?  

\- Under \*\*confirmation priming\*\*, does the model tend to agree with a hypothesis that is presented up front (e.g., “Player C struggles defensively”), and how often does it push back?



By logging \*\*prompt variant\*\*, \*\*model label\*\*, \*\*replicate\*\*, and basic sentiment proxies, the pipeline makes it relatively straightforward to answer these questions quantitatively.



\### 6.2 Limitations



\- The sentiment proxies are \*\*very simple\*\* (keyword counts) and might miss nuance, sarcasm, or context.  

\- Simulated outputs used in this checkpoint are primarily for \*\*pipeline verification\*\*, not for claiming real-world bias magnitudes.  

\- The experiment currently uses a small set of variants and replicates; more robust conclusions would require more prompts, more datasets, and more models.  

\- The confirmation-priming condition is implemented in design and code but would need enough real responses to make statistically meaningful claims.



---



\## 7. Future Work



If I extend this project, I would:



1\. Replace simulated responses with \*\*actual LLM outputs\*\* (across multiple models) while keeping logging and anonymization intact.  

2\. Refine the sentiment and bias metrics by using:  

&nbsp;  - Dependency on offense vs. defense terms.  

&nbsp;  - The frequency of mentions per player.  

&nbsp;  - The presence or absence of hedging language (“might”, “could”, “likely”).  

3\. Add a more robust \*\*claim validation layer\*\* that checks whether statements like “Player X is the best rebounder” are consistent with the anonymized stats.  

4\. Expand from a single sports dataset to multiple domains (e.g., education or healthcare-style tabular data) to see whether similar framing shifts appear.  



---



\## 8. Conclusion



Task 08 gave me a structured way to connect:



\- \*\*Reproducible experimental design\*\* (prompt IDs, variants, logs).  

\- \*\*Dataset-aware AI testing\*\* (using real stats but anonymizing people).  

\- \*\*Bias and framing analysis\*\* for generated narratives.  



Instead of just observing that “LLMs sometimes sound more positive or negative,” I now have a template for a \*\*controlled experiment\*\* where framing is the only intentional variable, and the resulting narratives can be analyzed, logged, and revisited in a transparent way.



