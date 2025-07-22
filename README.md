# Text Sentiment Capstone Project

This capstone tests whether transformer‑based sentiment (FinBERT) out‑predicts a classic rule‑based lexicon (VADER) for same‑day percentage moves in the S&P 500.

## Structure
- `data/raw`: Original dataset
- `data/processed`: Cleaned and engineered data
- `notebooks/`: Jupyter Notebooks for each step of the process
- `reports/`: Final report and presentation materials

## Methods
- NLP (TextBlob, VADER)
- LASSO for feature selection
- XGBoost for modeling
- Optional: Conformal predictors for uncertainty estimation

