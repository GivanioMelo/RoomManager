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
        issue.id = self.get_last_insert_id()
        return issue
    
    def get_all(self) -> list[Issue]:
        query = f"SELECT * FROM {self.tableName}"
        return self.executeQuery(query)
    
    def get_by_id(self, issue_id: int) -> Issue:
        query = f"SELECT * FROM {self.tableName} WHERE id = {issue_id}"
        result = self.executeQuery(query)
        return result[0] if result else None