import pandas as pd
import numpy as np

# TASK 1: IPL - Load Dataset & Display First 5 Rows
ipl_df = pd.DataFrame({
    "season": [2023, 2023, 2024, 2024, 2025, 2025],
    "team1": ["CSK", "MI", "RCB", "KKR", "CSK", "MI"],
    "team2": ["MI", "CSK", "KKR", "RCB", "RCB", "KKR"],
    "winner": ["CSK", "MI", "RCB", "KKR", "CSK", "MI"],
    "win_by_runs": [20, 0, 15, 0, 30, 0],
    "win_by_wickets": [0, 5, 0, 7, 0, 6]
})

print("TASK 1 - IPL Dataset")
print(ipl_df.head())


# TASK 2: Remove Rows with Missing Winner
ipl_df = ipl_df.dropna(subset=["winner"]).reset_index(drop=True)

print("\nTASK 2 - Cleaned Data")
print(ipl_df)


# TASK 3: Match Margin Type
ipl_df["match_margin_type"] = np.select(
    [ipl_df["win_by_runs"] > 0,
     ipl_df["win_by_wickets"] > 0],
    ["Runs", "Wickets"],
    default="Tie/No Result"
)

print("\nTASK 3 - Match Margin Type")
print(ipl_df)


# TASK 4: Add Home City of Both Teams
teams = pd.DataFrame({
    "team": ["CSK", "MI", "RCB", "KKR"],
    "home_city": ["Chennai", "Mumbai", "Bangalore", "Kolkata"]
})

ipl_df = ipl_df.merge(
    teams.rename(columns={"team": "team1", "home_city": "team1_city"}),
    on="team1",
    how="left"
)

ipl_df = ipl_df.merge(
    teams.rename(columns={"team": "team2", "home_city": "team2_city"}),
    on="team2",
    how="left"
)

print("\nTASK 4 - Team Home Cities")
print(ipl_df)


# TASK 5: Pivot - Wins by Team and Season
wins = ipl_df.groupby(
    ["season", "winner"]
).size().reset_index(name="wins")

pivot = wins.pivot(
    index="winner",
    columns="season",
    values="wins"
).fillna(0)

print("\nTASK 5 - Wins by Team and Season")
print(pivot)

print("\nTop 3 Teams by Wins:")
print(wins.sort_values("wins", ascending=False).head(3))