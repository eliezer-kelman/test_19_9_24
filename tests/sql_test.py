import pytest
from repository.database import create_tables, get_db_connection
from repository.games_repository import find_all_2022, load_players_from_json


@pytest.fixture(scope='module')
def setup_database():
    create_tables()
    load_players_from_json()
    connection = get_db_connection()
    yield connection
    cursor = connection.cursor()
    cursor.execute("DROP TABLE twenty_two")
    connection.commit()
    cursor.close()
    connection.close()


def test_get_all(setup_database):
    players = find_all_2022()
    assert len(players) > 0
