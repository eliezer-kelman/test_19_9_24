from toolz import pipe
from toolz.curried import partial
from services.home_service import get_player_details
from repository.database import create_tables, drop_table
from repository.games_repository import load_players_from_json, find_all_2022


def run_app():
    drop_table()
    create_tables()
    load_players_from_json()


def get_players_by_position(position):
    all_players = find_all_2022()
    players = pipe(
        all_players,
        partial(filter, lambda player: player.position == position),
        partial(get_player_details, lambda player: player),
        list
    )
    return players
