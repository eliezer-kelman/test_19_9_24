# Create a function that calculates for each player his average points per game
def calculate_ppg(player):
    return player.points / player.games


# Create a function that accepts all players and finds the average points per game of all players
def average_ppg(players):
    return sum(calculate_ppg(player) for player in players) / len(players)


# Create a function that receives all the players and produces a dictionary with all relevant
# details and calculates atr, ppg, and returns a list of all players
def get_player_details(players):
    return [
        {
            "playerName": player.playerName,
            "team": player.team,
            "position": player.position,
            "season": player.season,
            "points": player.points,
            "games": player.games,
            "towPercent": player.twoPercent,
            "threePercent": player.threePercent,
            "ppg": calculate_ppg(player) / average_ppg(players),
            "atr": player.assists / player.turnovers
        }
        for player in players
    ]
