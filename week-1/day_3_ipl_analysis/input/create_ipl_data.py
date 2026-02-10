import pandas as pd
import random
from datetime import datetime, timedelta

print("Generating IPL Dataset...")

# Teams data
teams = [
    'Royal Challengers Bengaluru',
    'Delhi Capitals',
    'Rajasthan Royals',
    'Mumbai Indians',
    'Chennai Super Kings',
    'Kolkata Knight Riders',
    'Sunrisers Hyderabad',
    'Punjab Kings',
    'Gujarat Titans',
    'Lucknow Super Giants'
]

# Players for each team
players_dict = {
    'Royal Challengers Bengaluru': ['Virat Kohli', 'AB de Villiers', 'Glenn Maxwell', 'Mohammed Siraj', 'Chris Gayle'],
    'Delhi Capitals': ['Rishabh Pant', 'Prithvi Shaw', 'Axar Patel', 'Kagiso Rabada', 'KL Rahul'],
    'Rajasthan Royals': ['Ravindra Jadeja', 'Sam Curran', 'Yuzvendra Chahal', 'Trent Boult', 'Vaibhav Sooryawanshi'],
    'Mumbai Indians': ['Rohit Sharma', 'Jasprit Bumrah', 'Hardik Pandya', 'Suryakumar Yadav', 'Tilak Verma'],
    'Chennai Super Kings': ['MS Dhoni', 'Aayush Mhatre', 'Ruturaj Gaikwad', 'Deepak Chahar', 'Sanju Samson'],
    'Kolkata Knight Riders': ['Andre Russell', 'Sunil Narine', 'Rinku Singh', 'Varun Chakravarthy', 'Gautam Gambhir'],
    'Sunrisers Hyderabad': ['David Warner', 'Heinrich Klassen', 'Bhuvneshwar Kumar', 'Kane Williamson', 'Abhishek Sharma'],
    'Punjab Kings': ['Shreyas Aiyer', 'Mayank Agarwal', 'Mohammed Shami', 'Ashutosh Sharma', 'Arshdeep Singh'],
    'Gujarat Titans': ['Shubman Gill', 'Sai Sudharsan', 'Jos Buttler', 'Rashid Khan', 'Rahul Tewatia'],
    'Lucknow Super Giants': ['Mitchell Marsh', 'Aiden Markram', 'Ayush Badoni', ' Mayank Yadav', 'Ravi Bishnoi']
}

seasons = [2020, 2021, 2022, 2023, 2024, 2025]

venues = ['Bengaluru', 'Delhi', 'Jaipur', 'Mumbai', 'Chennai', 'Kolkata', 'Hyderabad', 'Mohali', 'Ahemdabad', 'Lucknow']

# Generating matches data
matches_list = []
match_id = 1

for season in seasons:
    for match_num in range(1, 61):
        team1, team2 = random.sample(teams, 2)
        winner = random.choice([team1, team2])

        matches_list.append({
            'match_id': match_id,
            'season': season,
            'team1': team1,
            'team2': team2,
            'winner': winner,
            'margin': random.randint(1, 100),
            'venue': random.choice(venues),
            'date': f"{season} - {random.randint(3, 5):02d} - {random.randint(1, 28):02d}"
        })

        match_id += 1

# Generate Player stats
player_stats_list = []

for season in seasons:
    for team, team_players in players_dict.items():
        for player in team_players:
            player_stats_list.append({
                'season': season,
                'player_name': player,
                'team': team,
                'matches_played': random.randint(10, 16),
                'runs_scored': random.randint(150, 850),
                'wickets_taken': random.randint(0, 26),
                'catches': random.randint(2, 18),
                'strike_rate': round(random.uniform(100, 200), 2),
                'average': round(random.uniform(18, 62), 2)
            })

# Create Dataframes
matches_df = pd.DataFrame(matches_list)
players_df = pd.DataFrame(player_stats_list)

# Saving to CSV
matches_df.to_csv('ipl_matches.csv', index=False)
players_df.to_csv('ipl_player_stats.csv', index=False)

print(f"✓ Created ipl_matches.csv with {len(matches_df)} matches")
print(f"✓ Created ipl_player_stats.csv with {len(players_df)} player records")
print(f"✓ Seasons covered: {seasons}")
print(f"✓ Total Teams: {len(teams)}")