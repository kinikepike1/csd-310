from distutils.command.config import config
import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"pysports_user",
    "password":"sports",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings":True
}

try:
    db=mysql.connector.connect(**config)
    print("\n Database User {} connected to MySQL on host {} with database {}".format(config["user"],config["host"],config["database"]))
    input("\n\n Press and key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
finally:
    db.close()