from distutils.command.config import config
import mysql.connector
from mysql.connector import errorcode
import os
import sys

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
    cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES('Tom','Bombadil',1)")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
    teams = cursor.fetchall()
    print("\n-- DISPLAYING PLAYERS AFTER INSERT --")
    for x in teams:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(x[0],x[1],x[2],x[3]))
    cursor.execute("UPDATE player SET team_id = 2 WHERE first_name = 'Tom'")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")    
    teams = cursor.fetchall()    
    print("\n-- DISPLAYING PLAYERS AFTER DELETE --")
    for x in teams:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(x[0],x[1],x[2],x[3]))
    cursor.execute("DELETE FROM player WHERE first_name = 'Tom'")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")    
    teams = cursor.fetchall()    
    print("\n-- DISPLAYING PLAYERS AFTER DELETE --")
    for x in teams:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(x[0],x[1],x[2],x[3]))
    print("\n\nPress any key to continue...")
    f = open('nul', 'w')
    sys.stdout = f  
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