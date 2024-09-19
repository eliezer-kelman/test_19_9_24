import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI


def get_db_connection():
    return psycopg2.connect(
        SQL_URI,
        cursor_factory=RealDictCursor)


def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS twenty_two (
            id INT PRIMARY KEY,
            playerName VARCHAR(50) NOT NULL,  
            position VARCHAR(10) NOT NULL,
            age INT NOT NULL,
            games INT,
            gamesStarted INT,
            minutesPg INT,
            fieldGoals INT,
            fieldAttempts INT,
            fieldPercent FLOAT,
            threeFg INT,
            threeAttempts INT,
            threePercent FLOAT,
            twoFg INT,
            twoAttempts INT,
            twoPercent FLOAT,
            effectFgPercent FLOAT,
            ft INT NOT NULL,
            ftAttempts INT,
            ftPercent FLOAT,
            offensiveRb INT,
            defensiveRb INT,
            totalRb INT,
            assists INT,
            steals INT,
            blocks INT,
            turnovers INT,
            personalFouls INT,
            points INT,
            team VARCHAR(50),
            season INT,
            playerId VARCHAR(50) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS twenty_three (
            id INT PRIMARY KEY,
            playerName VARCHAR(50) NOT NULL,  
            position VARCHAR(10) NOT NULL,
            age INT NOT NULL,
            games INT,
            gamesStarted INT,
            minutesPg INT,
            fieldGoals INT,
            fieldAttempts INT,
            fieldPercent FLOAT,
            threeFg INT,
            threeAttempts INT,
            threePercent FLOAT,
            twoFg INT,
            twoAttempts INT,
            twoPercent FLOAT,
            effectFgPercent FLOAT,
            ft INT NOT NULL,
            ftAttempts INT,
            ftPercent FLOAT,
            offensiveRb INT,
            defensiveRb INT,
            totalRb INT,
            assists INT,
            steals INT,
            blocks INT,
            turnovers INT,
            personalFouls INT,
            points INT,
            team VARCHAR(50),
            season INT,
            playerId VARCHAR(50) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS twenty_four (
            id INT PRIMARY KEY,
            playerName VARCHAR(50) NOT NULL,  
            position VARCHAR(10) NOT NULL,
            age INT NOT NULL,
            games INT,
            gamesStarted INT,
            minutesPg INT,
            fieldGoals INT,
            fieldAttempts INT,
            fieldPercent FLOAT,
            threeFg INT,
            threeAttempts INT,
            threePercent FLOAT,
            twoFg INT,
            twoAttempts INT,
            twoPercent FLOAT,
            effectFgPercent FLOAT,
            ft INT NOT NULL,
            ftAttempts INT,
            ftPercent FLOAT,
            offensiveRb INT,
            defensiveRb INT,
            totalRb INT,
            assists INT,
            steals INT,
            blocks INT,
            turnovers INT,
            personalFouls INT,
            points INT,
            team VARCHAR(50),
            season INT,
            playerId VARCHAR(50) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS fantasy (
            id INT PRIMARY KEY,
            playerName VARCHAR(50) NOT NULL,  
            position VARCHAR(10) NOT NULL,
            age INT NOT NULL,
            games INT,
            gamesStarted INT,
            minutesPg INT,
            fieldGoals INT,
            fieldAttempts INT,
            fieldPercent FLOAT,
            threeFg INT,
            threeAttempts INT,
            threePercent FLOAT,
            twoFg INT,
            twoAttempts INT,
            twoPercent FLOAT,
            effectFgPercent FLOAT,
            ft INT NOT NULL,
            ftAttempts INT,
            ftPercent FLOAT,
            offensiveRb INT,
            defensiveRb INT,
            totalRb INT,
            assists INT,
            steals INT,
            blocks INT,
            turnovers INT,
            personalFouls INT,
            points INT,
            team VARCHAR(50),
            season INT,
            playerId VARCHAR(50) NOT NULL
        );
        '''
    )
    connection.commit()
    cursor.close()
    connection.close()


def drop_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE twenty_two")
    cursor.execute("DROP TABLE twenty_three")
    cursor.execute("DROP TABLE twenty_four")
    cursor.execute("DROP TABLE fantasy")
    connection.commit()
    cursor.close()
    connection.close()

#drop_table()
