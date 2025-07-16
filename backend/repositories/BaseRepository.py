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
        config = json.load(open('repositories/database.config'))
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
            if values is None:
                cursor.execute(command)
            else:
                cursor.execute(command, values)
            connection.commit()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            if connection.is_connected():
                connection.rollback()
                connection.close()
            raise err

    def executeQuery(self, query:str):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result
    
    def getById(self, id:int) -> T:
        query = f"SELECT * FROM {self.tableName} WHERE id = {id}"
        result = self.executeQuery(query)
        if result:
            return self.from_dict(result[0])
        return None
    
    def getAll(self) -> list[T]:
        query = f"SELECT * FROM {self.tableName}"
        results = self.executeQuery(query)
        return [self.from_dict(row) for row in results] if results else []
    
    def getAllPaged(self, page:int, page_size:int) -> list[T]:
        offset = (page - 1) * page_size
        query = f"SELECT * FROM {self.tableName} LIMIT %s OFFSET %s"
        values = (page_size, offset)
        results = self.executeQuery(query, values)
        return [self.from_dict(row) for row in results] if results else []
    
    def create(self, entity:T):
        command = f"""
        INSERT INTO {self.tableName} ({', '.join(entity.__dict__.keys())})
        VALUES ({', '.join(['%s'] * len(entity.__dict__))})
        """
        values = tuple(entity.__dict__.values())
        self.execute(command, values)
    
    def update(self, entity:T):
        set_clause = ', '.join([f"{key} = %s" for key in entity.__dict__.keys()])
        command = f"""
        UPDATE {self.tableName}
        SET {set_clause}
        WHERE id = %s
        """
        values = tuple(entity.__dict__.values()) + (entity.id,)
        self.execute(command, values)
    
    def delete(self, id:int):
        command = f"DELETE FROM {self.tableName} WHERE id = {id}"
        self.execute(command)

    def getByFilters(self, **filters) -> list[T]:
        filter_clause = ' AND '.join([f"{key} = %s" for key in filters.keys()])
        query = f"SELECT * FROM {self.tableName} WHERE {filter_clause}"
        values = tuple(filters.values())
        results = self.executeQuery(query, values)
        return [self.from_dict(row) for row in results] if results else []
    
    def getPagedByFilters(self, page:int, page_size:int, **filters) -> list[T]:
        offset = (page - 1) * page_size
        filter_clause = ' AND '.join([f"{key} = %s" for key in filters.keys()])
        query = f"SELECT * FROM {self.tableName} WHERE {filter_clause} LIMIT %s OFFSET %s"
        values = tuple(filters.values()) + (page_size, offset)
        results = self.executeQuery(query, values)
        return [self.from_dict(row) for row in results] if results else []
