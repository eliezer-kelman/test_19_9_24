from toolz import pipe, partial
from repository.games_repository import find_all_2022, find_all_fantasy, delete_player


def get_player_by_id(player_id: str):
    all_players = find_all_2022()
    player = pipe(
        all_players,
        partial(filter, lambda pl: pl.player_Id == player_id),
        partial(next, None)
    )
    return player


def get_players_by_team(team_name: str):
    all_players = find_all_fantasy()
    players = pipe(
        all_players,
        partial(filter, lambda pl: pl.team == team_name),
        list
    )
    return players


def get_five_players():
    pass
