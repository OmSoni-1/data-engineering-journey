# Complete IPL Data Analysis 
import pandas as pd
import pathlib as pl

print("=" * 70)
print("IPL DATA ANALYSIS PROJECT - DAY 3")
print("=" * 70)

BASE_DIR = pl.Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE_TOP_SCORER = OUTPUT_DIR / "output_top_scorers.csv"
OUTPUT_FILE_SEASON_SCORER = OUTPUT_DIR / "output_season_top_scorers.csv"
OUTPUT_FILE_WIN_STATS = OUTPUT_DIR / "output_team_win_stats.csv"
OUTPUT_FILE_VENUE_STATS = OUTPUT_DIR / "output_venue_stats.csv"

dfs = {}

for file_path in INPUT_DIR.glob("*.csv"):
    dfs[file_path.name] = pd.read_csv(file_path)
    print(f"Loaded {file_path.name} into dictionary")

# Load Data
print("\n 📂 Loading data...")
matches = dfs['ipl_matches.csv']
players = dfs['ipl_player_stats.csv']

print(f"✓ Loaded {len(matches)} matches")
print(f"✓ Loaded {len(players)} player records")

# Analysis 1: TOP 10 run scorers of all time
print("\n" + "=" * 70)
print("🏏 Analysis 1: Top 10 Run Scorers (All Time)")
print("\n" + "=" * 70)

# To do that we need to group by player name and sum the runs across seasons
top_scorers = (players.groupby('player_name')['runs_scored']
               .sum()
               .sort_values(ascending=False)
               .head(10)
               )

print("\nTop 10 Run Scorers:")
print("\n" + "=" * 50)
for rank, (player, runs) in enumerate(top_scorers.items(), 1):
    print(f"{rank:2d}. {player:30s}: {runs:6d} runs")

# Saving to CSV
top_scorers_df = pd.DataFrame({
    "rank": range(1, 11),
    'player_name': top_scorers.index,
    "total_runs": top_scorers.values
})

top_scorers_df.to_csv(OUTPUT_FILE_TOP_SCORER, index=False)
print(f"\n✓ Saved to: output_top_scorers.csv")


# Analysis 2: TOP run scorers per season
print("\n" + "=" * 70)
print("📅 Analysis 2: Top Run Scoreres by Season")
print("\n" + "=" * 70)

season_top_scorers = []

for season in sorted(players['season'].unique()):
    # Filter data for this season
    season_data = players[players['season'] == season]

    # Get Top 5 for this particular season
    top_5 = season_data.nlargest(5, 'runs_scored')

    print(f"\n--- Season {season} ---")

    for rank, row in enumerate(top_5.itertuples(), 1):
        print(f"{rank}. {row.player_name:30s}: {row.runs_scored:4d} runs ({row.team})")

        # Collect for CSV
        season_top_scorers.append({
            'season': season,
            'rank': rank,
            'player_name': row.player_name,
            'runs_scored': row.runs_scored
        })

# Save season wise top scorers
season_scorers_df = pd.DataFrame(season_top_scorers)
season_scorers_df.to_csv(OUTPUT_FILE_SEASON_SCORER, index=False)
print("\n✓ Saved to: output_season_top_scorers.csv")

# Analysis 3: Team Win Percentage
print("\n" + "=" * 70)
print("🏆 ANALYSIS 3: Team Win Percentage")
print("\n" + "=" * 70)

# Count matches per team (team1 + team2)
team1_counts = matches['team1'].value_counts()
team2_counts = matches['team2'].value_counts()
total_matches = team1_counts.add(team2_counts, fill_value=0)

# Count wins per team
wins = matches['winner'].value_counts()

# Calculate Win Percentage
win_percentage = (wins / total_matches * 100).sort_values(ascending=False)

print("\nTeam Win Statistics:")
print("\n" + "=" * 70)
print(f"{'Team':<30s} {'Wins':>8s} {"Matches":>8s} {'Win %':>8s}")
print("\n" + "=" * 70)

win_stats_list = []

for team in win_percentage.index:
    team_wins = int(wins[team])
    team_matches = int(total_matches[team])
    win_pct = win_percentage[team]

    print(f"{team:<30s} {team_wins:6d} {team_matches: 8d} {win_pct:7.2f}%")

    win_stats_list.append({
        'team': team,
        'wins': wins,
        'total_matches': team_matches,
        'win_percentage': round(win_pct, 2)
    })

# Save Team stats
win_stats_df = pd.DataFrame(win_stats_list)
win_stats_df.to_csv(OUTPUT_FILE_WIN_STATS, index=False)
print("\n ✓ Saved to: output_team_win_stats.csv")

# Analysis 4: Venue Statistics
print("\n" + "=" * 70)
print("🏟️ ANALYSIS 4: Venue Statistics")
print("\n" + "=" * 70)

venue_stats = matches.groupby('venue').agg({
    'match_id': 'count',
    'margin': 'mean'
}).rename(columns={
    'match_id': 'matches_played',
    'margin': 'avg_margin'
})

venue_stats = venue_stats.sort_values('matches_played', ascending=False)

print("\nMatches by Venue")
print('-' * 50)
for venue, stats in venue_stats.iterrows():
    print(f"{venue:<20s} {int(stats['matches_played']):3d} matches (Avg margin: {stats['avg_margin']:.1f})")

# Storing Venue Stats to CSV
venue_stats_df = pd.DataFrame(venue_stats)
venue_stats_df.to_csv(OUTPUT_FILE_VENUE_STATS, index=False)
print("\n ✓ Saved to: output_venue_stats.csv")

# Analysis 5: Player Performance Summary
print("\n" + "="*70)
print("📊 ANALYSIS 5: Overall Player Statistics")
print("="*70)

print("\nRuns Statistics:")
print(round(players['runs_scored'].describe(), 0))

print("\Wickets Statistics:")
print(round(players['wickets_taken'].describe(),0))

print("\Strike Rate Statistics:")
print(round(players['strike_rate'].describe(),0))

# Final Summaryprint("\n" + "="*70)
print("ANALYSIS COMPLETE!")
print("="*70)
print("\n📁 Output files created:")
print("  1. output_top_scorers.csv")
print("  2. output_season_top_scorers.csv")
print("  3. output_team_win_stats.csv")
print("  4. output_venue_stats.csv")
print("="*70)