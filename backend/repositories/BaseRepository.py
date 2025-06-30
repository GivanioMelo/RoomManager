import mysql.connector

class BaseRepository():
    dataBaseHostName:str
    dataBasePort:str
    dataBaseName:str
    dataBaseUser:str
    dataBasePassWord:str

    def __init__(self):
        self.dataBaseHostName = "localhost"
        self.dataBasePort = "3307"
        self.dataBaseName = "stock"
        self.dataBaseUser = "root"
        self.dataBasePassWord = ""
    
    def connect(self): 
        connection = mysql.connector.connect(host=self.dataBaseHostName,
        port=self.dataBasePort,
        user=self.dataBaseUser,
        password=self.dataBasePassWord,
        database=self.dataBaseName)
        return connection

    def execute(self, command:str):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        connection.close()

    def executeQuery(self, query:str):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result