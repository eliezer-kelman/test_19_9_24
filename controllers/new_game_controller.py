from typing import List
from repository.games_repository import create_player, delete_player
from toolz.curried import reduce
from services.new_game_service import get_player_by_id, get_players_by_team


def create_new_game(team_name: str, players_ids: List[str]):
    if len(players_ids) != 5:
        raise ValueError("A team must have exactly 5 players")
    # get all players
    five_players = reduce(lambda acc, player_id: acc + [get_player_by_id(player_id)], players_ids, [])
    # Checks if all players are not in the same position
    if len(set([player.position for player in five_players])) != 5:
        raise ValueError("All players must be in different positions")
    five_players = map(lambda player: player.team == team_name, five_players)
    # for each player to create it in the database
    for player in five_players:
        create_player(player, "fantasy")


def update_game(team_name: str, players_ids: List[str]):
    if len(players_ids) != 5:
        raise ValueError("A team must have exactly 5 players")
    # get five players from the same team
    five_players_in_team = get_players_by_team(team_name)
    for player in five_players_in_team:
        delete_player(player.playerId)
    # get all players
    five_new_players = reduce(lambda acc, player_id: acc + [get_player_by_id(player_id)], players_ids, [])
    # Checks if all players are not in the same position
    if len(set([player.position for player in five_new_players])) != 5:
        raise ValueError("All players must be in different positions")
    five_players = map(lambda pl: pl.team == team_name, five_new_players)
    # for each player to create it in the database
    for player in five_players:
        create_player(player, "fantasy")


def delete_game(team_name: str):
    five_players_in_team = get_players_by_team(team_name)
    if len(five_players_in_team) == 0:
        raise ValueError("The team does not exist")
    for player in five_players_in_team:
        delete_player(player.playerId)
