# 🏏 IPL Analytics Dashboard

An all-in-one IPL analytics platform covering every ball from 2008 to 2025.

## Features (live)
- **Overview** — season-wise runs, boundaries, dismissals
- **Player Stats** — batting & bowling profiles, phase-wise breakdown
- **Team Stats** — win/loss records, top performers
- **Venue Stats** — ground profiles, toss impact

## Features (coming soon)
- Win probability predictor (XGBoost)
- Innings score forecaster (LSTM)
- Batter vs bowler matchup engine
- Fantasy XI optimizer
- Player of the Match predictor

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Data
Ball-by-ball IPL data from 2008–2025 (278,205 deliveries, 1,169 matches).  
Dataset loaded from Google Drive on first run via `gdown`.

## Stack
- **Frontend/UI** — Streamlit
- **Visualization** — Plotly
- **ML** — scikit-learn, TensorFlow (coming soon)
- **Data** — Pandas, NumPy
