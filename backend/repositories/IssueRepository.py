from repositories.BaseRepository import BaseRepository
from entities.Issue import Issue

class IssueRepository(BaseRepository[Issue]):
    def __init__(self):
        super().__init__()
        self.tableName = 'issues'
    
    def create(self, issue: Issue) -> Issue:
        query = f"""
            INSERT INTO {self.tableName} (title, description, status)
            VALUES ('{issue.title}', '{issue.description}', '{issue.status}');
        """
        print(f"Executing query: {query}")
        self.execute(query)
        return issue
    
    def getAll(self) -> list[Issue]:
        query = f"SELECT * FROM {self.tableName}"
        return self.executeQuery(query)
    
    def getById(self, id: int) -> Issue:
        query = f"SELECT * FROM {self.tableName} WHERE id = {id}"
        result = self.executeQuery(query)
        if len(result): return Issue.fromDict(result[0])
        else: return None
    
    def getByUser(self, userId) ->list[Issue]:
        query = f"SELECT * FROM {self.tableName} WHERE creationUser = {userId}"
        result = self.executeQuery(query)
        if len(result): return [Issue.fromDict(record) for record in result]
        else: return []