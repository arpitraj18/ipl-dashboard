import streamlit as st

st.set_page_config(
    page_title="IPL Analytics",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Data loading ──────────────────────────────────────────────────────────────

@st.cache_data(show_spinner="Loading IPL data... (first time only)")
def load_data():
    import pandas as pd
    import gdown
    import os

    csv_path = "IPL.csv"

    if not os.path.exists(csv_path):
        # Replace with your actual Google Drive file ID
        # From your link: https://drive.google.com/file/d/FILE_ID/view
        file_id = "YOUR_GOOGLE_DRIVE_FILE_ID"
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, csv_path, quiet=False)

    df = pd.read_csv(csv_path, low_memory=False)

    # Basic cleaning
    season_map = {"2007/08": "2008", "2009/10": "2010", "2020/21": "2020"}
    df["season"] = df["season"].replace(season_map).astype(int)
    df["date"] = pd.to_datetime(df["date"])
    df["is_wicket"] = df["wicket_kind"].notna()
    df["is_six"]    = df["runs_batter"] == 6
    df["is_four"]   = df["runs_batter"] == 4
    df["is_dot"]    = (df["runs_batter"] == 0) & (df["valid_ball"] == 1)
    df["is_boundary"] = df["is_six"] | df["is_four"]
    df["is_knockout"]  = df["stage"] != "Unknown"

    return df


df = load_data()

# ── Sidebar navigation ────────────────────────────────────────────────────────

with st.sidebar:
    st.title("🏏 IPL Analytics")
    st.caption("2008 – 2025 • All seasons")
    st.divider()

    page = st.radio(
        "Navigate",
        [
            "🏠  Overview",
            "🏏  Player Stats",
            "🛡️  Team Stats",
            "🏟️  Venue Stats",
            "🔮  Predictions",
        ],
        label_visibility="collapsed"
    )

    st.divider()
    st.caption(f"📦 {len(df):,} deliveries loaded")
    st.caption(f"🎯 {df['match_id'].nunique()} matches")

# ── Page routing ──────────────────────────────────────────────────────────────

if   "Overview"     in page: from pages import overview;     overview.show(df)
elif "Player Stats" in page: from pages import players;      players.show(df)
elif "Team Stats"   in page: from pages import teams;        teams.show(df)
elif "Venue Stats"  in page: from pages import venues;       venues.show(df)
elif "Predictions"  in page: from pages import predictions;  predictions.show(df)
