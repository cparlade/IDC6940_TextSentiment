# Headline-News Sentiment — VADER vs FinBERT  
Capstone for IDC 6940 / STA 6257 (Summer 2025)

This project measures how much accuracy you gain when you swap a free
rule-based sentiment tool (VADER) for a finance-tuned transformer
(FinBERT) on the **Financial PhraseBank** “All Agree” corpus.  
Outputs include the written report, the reveal-js slide deck, the
trained FinBERT checkpoint, and prediction CSVs.

---

## Repo layout

| Path | What it contains |
|------|------------------|
| `data/raw/` | Original *Sentences_AllAgree.txt* (or mirror) |
| `data/processed/` | Train / test CSVs, model predictions |
| `notebooks/` | <br>• `01_data_prep.ipynb` – split & save CSVs  <br>• `02_eda.ipynb` – class counts, length plots  <br>• `03_modeling.ipynb` – VADER baseline  <br>• `finbert_finetune.ipynb` – three-epoch fine-tune  <br>• `04_reporting.ipynb` – metrics & confusion matrices |
| `results/` | `summary_metrics.csv` (Macro-F1, Accuracy) |
| `docs/` | Rendered site (index.html, slides.html) |
| `slides.qmd` | Reveal-js source for the presentation |
| `index.qmd` | Quarto source for the paper |

---

## Quick start (Codespace or local)

```bash
# clone and enter
git clone https://github.com/cparlade/IDC6940_TextSentiment.git
cd IDC6940_TextSentiment

# create env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 1) prepare data
python notebooks/01_data_prep.ipynb       # or run in Jupyter

# 2) run baselines
python notebooks/03_modeling.ipynb        # VADER preds → csv

# 3) fine-tune FinBERT (needs 1 GPU or ~35 min CPU)
python notebooks/finbert_finetune.ipynb

# 4) collect metrics / figs
python notebooks/04_reporting.ipynb

# 5) render paper + slides
quarto render