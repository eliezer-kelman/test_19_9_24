from typing import List, Dict
from model.Player import Player
from repository.database import get_db_connection
from utils.json_loader import load_json


def create_player(player: Player, season: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        f"""
        INSERT INTO {season} 
        (id, 
        playerName, 
        position, 
        age, 
        games, 
        gamesStarted, 
        minutesPg,
        fieldGoals,
        fieldAttempts,
        fieldPercent,
        threeFg,
        threeAttempts,
        threePercent,
        twoFg,
        twoAttempts,
        twoPercent,
        effectFgPercent,
        ft,
        ftAttempts,
        ftPercent,
        offensiveRb,
        defensiveRb,
        totalRb,
        assists,
        steals,
        blocks,
        turnovers,
        personalFouls,
        points,
        team,
        season,
        playerId) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (player.id,
         player.playerName,
         player.position,
         player.age,
         player.games,
         player.gamesStarted,
         player.minutesPg,
         player.fieldGoals,
         player.fieldAttempts,
         player.fieldPercent,
         player.threeFg,
         player.threeAttempts,
         player.threePercent,
         player.twoFg,
         player.twoAttempts,
         player.twoPercent,
         player.effectFgPercent,
         player.ft,
         player.ftAttempts,
         player.ftPercent,
         player.offensiveRb,
         player.defensiveRb,
         player.totalRb,
         player.assists,
         player.steals,
         player.blocks,
         player.turnovers,
         player.personalFouls,
         player.points,
         player.team,
         player.season,
         player.playerId)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return


def find_all_2023() -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM twenty_three")
    players = [Player(
        id=u['id'],
        playerName=u['playername'],
        position=u['position'],
        age=u['age'],
        games=u['games'],
        gamesStarted=u['gamesstarted'],
        minutesPg=u['minutespg'],
        fieldGoals=u['fieldgoals'],
        fieldAttempts=u['fieldattempts'],
        fieldPercent=u['fieldpercent'],
        threeFg=u['threefg'],
        threeAttempts=u['threeattempts'],
        threePercent=u['threepercent'],
        twoFg=u['twofg'],
        twoAttempts=u['twoattempts'],
        twoPercent=u['twopercent'],
        effectFgPercent=u['effectfgpercent'],
        ft=u['ft'],
        ftAttempts=u['ftattempts'],
        ftPercent=u['ftpercent'],
        offensiveRb=u['offensiverb'],
        defensiveRb=u['defensiverb'],
        totalRb=u['totalrb'],
        assists=u['assists'],
        steals=u['steals'],
        blocks=u['blocks'],
        turnovers=u['turnovers'],
        personalFouls=u['personalfouls'],
        points=u['points'],
        team=u['team'],
        season=u['season'],
        playerId=u['playerid']
    ) for u in cursor.fetchall()]
    cursor.close()
    connection.close()
    return players


def find_all_2024() -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM twenty_four")
    players = [Player(
        id=u['id'],
        playerName=u['playername'],
        position=u['position'],
        age=u['age'],
        games=u['games'],
        gamesStarted=u['gamesstarted'],
        minutesPg=u['minutespg'],
        fieldGoals=u['fieldgoals'],
        fieldAttempts=u['fieldattempts'],
        fieldPercent=u['fieldpercent'],
        threeFg=u['threefg'],
        threeAttempts=u['threeattempts'],
        threePercent=u['threepercent'],
        twoFg=u['twofg'],
        twoAttempts=u['twoattempts'],
        twoPercent=u['twopercent'],
        effectFgPercent=u['effectfgpercent'],
        ft=u['ft'],
        ftAttempts=u['ftattempts'],
        ftPercent=u['ftpercent'],
        offensiveRb=u['offensiverb'],
        defensiveRb=u['defensiverb'],
        totalRb=u['totalrb'],
        assists=u['assists'],
        steals=u['steals'],
        blocks=u['blocks'],
        turnovers=u['turnovers'],
        personalFouls=u['personalfouls'],
        points=u['points'],
        team=u['team'],
        season=u['season'],
        playerId=u['playerid']
    ) for u in cursor.fetchall()]
    cursor.close()
    connection.close()
    return players


def delete_player(player_id: int, season: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {season} WHERE id = %s", (player_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return


def find_all() -> List[Player]:
    all_players = find_all_2022() + find_all_2023() + find_all_2024()
    return all_players


def find_all_2022() -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM twenty_two")
    players = [Player(
        id=u['id'],
        playerName=u['playername'],
        position=u['position'],
        age=u['age'],
        games=u['games'],
        gamesStarted=u['gamesstarted'],
        minutesPg=u['minutespg'],
        fieldGoals=u['fieldgoals'],
        fieldAttempts=u['fieldattempts'],
        fieldPercent=u['fieldpercent'],
        threeFg=u['threefg'],
        threeAttempts=u['threeattempts'],
        threePercent=u['threepercent'],
        twoFg=u['twofg'],
        twoAttempts=u['twoattempts'],
        twoPercent=u['twopercent'],
        effectFgPercent=u['effectfgpercent'],
        ft=u['ft'],
        ftAttempts=u['ftattempts'],
        ftPercent=u['ftpercent'],
        offensiveRb=u['offensiverb'],
        defensiveRb=u['defensiverb'],
        totalRb=u['totalrb'],
        assists=u['assists'],
        steals=u['steals'],
        blocks=u['blocks'],
        turnovers=u['turnovers'],
        personalFouls=u['personalfouls'],
        points=u['points'],
        team=u['team'],
        season=u['season'],
        playerId=u['playerid']
    ) for u in cursor.fetchall()]
    cursor.close()
    connection.close()
    return players


def find_all_fantasy() -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fantasy")
    players = [Player(
        id=u['id'],
        playerName=u['playername'],
        position=u['position'],
        age=u['age'],
        games=u['games'],
        gamesStarted=u['gamesstarted'],
        minutesPg=u['minutespg'],
        fieldGoals=u['fieldgoals'],
        fieldAttempts=u['fieldattempts'],
        fieldPercent=u['fieldpercent'],
        threeFg=u['threefg'],
        threeAttempts=u['threeattempts'],
        threePercent=u['threepercent'],
        twoFg=u['twofg'],
        twoAttempts=u['twoattempts'],
        twoPercent=u['twopercent'],
        effectFgPercent=u['effectfgpercent'],
        ft=u['ft'],
        ftAttempts=u['ftattempts'],
        ftPercent=u['ftpercent'],
        offensiveRb=u['offensiverb'],
        defensiveRb=u['defensiverb'],
        totalRb=u['totalrb'],
        assists=u['assists'],
        steals=u['steals'],
        blocks=u['blocks'],
        turnovers=u['turnovers'],
        personalFouls=u['personalfouls'],
        points=u['points'],
        team=u['team'],
        season=u['season'],
        playerId=u['playerid']
    ) for u in cursor.fetchall()]
    cursor.close()
    connection.close()
    return players


def load_player_from_json(json_file: Dict, season: int):
    for p in [Player(**p) for p in json_file]:
        create_player(p, season)


def load_players_from_json():
    players_json = load_json('../local_database/2022.json')
    for p in [Player(**p) for p in players_json]:
        create_player(p, "twenty_two")
    players_json = load_json('../local_database/2023.json')
    for p in [Player(**p) for p in players_json]:
        create_player(p, "twenty_three")
    players_json = load_json('../local_database/2024.json')
    for p in [Player(**p) for p in players_json]:
        create_player(p, "twenty_four")
