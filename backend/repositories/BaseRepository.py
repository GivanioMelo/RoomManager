from flask import json
import mysql.connector
from entities.Entity import Entity

class BaseRepository[T:Entity]():

    dataBaseHostName:str
    dataBasePort:str
    dataBaseName:str
    dataBaseUser:str
    dataBasePassWord:str

    def __init__(self):
        config = json.load(open('database.config'))
        self.dataBaseHostName = config.get("DB_HOST", "localhost")
        self.dataBasePort = config.get("DB_PORT", "3307")
        self.dataBaseName = config.get("DB_NAME", "default_db")
        self.dataBaseUser = config.get("DB_USER", "root")
        self.dataBasePassWord = config.get("DB_PASSWORD", "")

        self.tableName = T.__class__.__name__.lower() + 's'
    
    def connect(self): 
        connection = mysql.connector.connect(host=self.dataBaseHostName,
        port=self.dataBasePort,
        user=self.dataBaseUser,
        password=self.dataBasePassWord,
        database=self.dataBaseName)
        return connection

    def execute(self, command:str, values:dict = None):
        try:
            connection = self.connect()
            cursor = connection.cursor()
            if values is None: cursor.execute(command)
            else: cursor.execute(command, values)
            connection.commit()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            if connection.is_connected():
                connection.rollback()
                connection.close()
            raise err

    def executeQuery(self, query:str, values:dict = None):
        connection = self.connect()
        cursor = connection.cursor(dictionary=True)
        if values is None: cursor.execute(query)
        else: cursor.execute(query, values)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result