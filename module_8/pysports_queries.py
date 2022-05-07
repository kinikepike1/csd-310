from distutils.command.config import config
import mysql.connector
from mysql.connector import errorcode
import os

config = {
    "user":"pysports_user",
    "password":"sports",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings":True
}

try:
    db=mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()
    print("-- DISPLAYING TEAM RECORDS --")
    for x in teams:
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(x[0],x[1],x[2]))

    print("\n-- DISPLAYING PLAYER RECORDS --")
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    teams = cursor.fetchall()
    for x in teams:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(x[0],x[1],x[2],x[3]))
    print("\n\nPress any key to continue...")
    os.system('pause > NULL')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
finally:
    db.close()