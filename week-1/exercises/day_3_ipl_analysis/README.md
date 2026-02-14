# IPL Data Analysis Project

## 📋 Project Overview
Analysis of Indian Premier League (IPL) cricket data using Python and Pandas.
This project demonstrates data manipulation, aggregation, and analysis skills.

## 🎯 What I Learned
- Loading and exploring CSV files with pandas
- Filtering data using boolean conditions
- GROUP BY operations and aggregations
- Sorting and ranking data
- Creating calculated columns
- Saving analysis results to CSV files

## 📁 Project Structure
```
ipl-data-analysis/
│
├── create_ipl_data.py          # Data generation script
├── explore_data.py              # Initial data exploration
├── ipl_analysis.py              # Main analysis script
│
├── ipl_matches.csv              # Input: Match data (300 matches)
├── ipl_player_stats.csv         # Input: Player statistics (160 records)
│
├── output_top_scorers.csv       # Output: Top 10 all-time run scorers
├── output_season_top_scorers.csv # Output: Top 5 per season
├── output_team_win_stats.csv    # Output: Team win percentages
└── output_venue_stats.csv       # Output: Venue statistics
```

## 📊 Key Analyses Performed

### 1. Top Run Scorers (All Time)
- Aggregated total runs across all seasons
- Ranked top 10 players

### 2. Season-wise Top Performers
- Top 5 run scorers for each season (2020-2024)
- Identified consistent performers

### 3. Team Win Percentage
- Calculated win rates for all teams
- Identified most successful teams

### 4. Venue Analysis
- Matches played at each venue
- Average winning margins

### 5. Statistical Summary
- Descriptive statistics for runs, wickets, strike rates

## 🚀 How to Run
```cmd
# Step 1: Generate data
python create_ipl_data.py

# Step 2: Explore data (optional)
python explore_data.py

# Step 3: Run analysis
python ipl_analysis.py
```

## 📈 Key Findings
- Total matches analyzed: 300 (5 seasons × 60 matches)
- Total players tracked: 160 (8 teams × 4 players × 5 seasons)
- Seasons covered: 2020-2024

## 🛠️ Technologies Used
- Python 3.x
- Pandas
- CSV file handling

## 📚 Pandas Concepts Applied
- `pd.read_csv()` - Loading data
- `groupby()` - Aggregation (like SQL GROUP BY)
- `agg()` - Multiple aggregations
- `sort_values()` - Sorting (like SQL ORDER BY)
- `nlargest()` - Getting top N records
- Boolean filtering - Data filtering (like SQL WHERE)
- `to_csv()` - Saving results

## 🎓 Skills Demonstrated
✅ Data loading and exploration  
✅ Data cleaning and preparation  
✅ Grouping and aggregation  
✅ Statistical analysis  
✅ Result documentation  

## 🔜 Next Steps
- Add data visualizations
- Connect to PostgreSQL database
- Automate with scheduling
- Add more complex metrics

---

**Project created as part of 90-day Data Engineering roadmap - Day 3**