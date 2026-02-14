import pandas as pd
import pathlib as pl

print("=" * 70)
print("IPL Data Exploration")
print("=" * 70)

BASE_DIR = pl.Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input" 

csvs = {}

for file_path in INPUT_DIR.glob("*.csv"):
    csvs[file_path.name] = pd.read_csv(file_path)
    print(f"Loaded {file_path.name} into dictionary.")

# Load the datasets
matches = csvs["ipl_matches.csv"]
players = csvs["ipl_player_stats.csv"]

#Basic info about matches
print("\n📊 MATCHES DATASET:")
print(f"Total records: {len(matches)}")
print(f"Columns: {list(matches.columns)}")
print("\nFirst 5 rows:")
print(matches.head())

print("\nData types:")
print(matches.dtypes)

# Basic info about players
print("\n" + "=" * 70)
print("🏏 PLAYER STATS DATASET:")
print(f"Total records: {(len(players))}")
print(f"Columns: {list(players.columns)}")
print("\nFirst 5 rows:")
print(players.head())

print("\nData types:")
print(players.dtypes)

# Quick stats
print("\n" + "=" * 70)
print("📈 QUICK STATISTICS:")
print(f"\nUnique seasons: {sorted(matches["season"].unique().tolist())}")
print(f"Unique teams: {sorted(matches['team1'].unique())}")
print(f"Unique venues: {sorted(matches['venue'].unique())}")
print(f"\nTotal matches per season: {matches.groupby('season').size().to_dict()}")

print("\n" + "=" * 70)
print("Exploration done!")