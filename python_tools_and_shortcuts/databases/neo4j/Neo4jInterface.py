import time
from neo4j import GraphDatabase
from neo4j import Result

class Neo4jInterface():
    def __init__(
        self,
        password,
        database = 'neo4j',
        uri = 'neo4j://localhost:7687',         
        username = 'neo4j',
    ):
        auth = (username, password)
        self.database = database
        self.driver = GraphDatabase.driver(uri, auth = auth)

    def query_to_df(self, query):
        df = self.driver.execute_query(
            query,
            database_ = self.database,
            result_transformer_ = Result.to_df
        )
        return df
    
    def drop_everything(self):
        self.driver.execute_query('MATCH (n) DETACH DELETE n', database = self.database)

    def drop_everything_by_node_type(self, the_type):
        self.driver.execute_query('MATCH (n:' + the_type + ') DETACH DELETE n', database = self.database)
    
    def batch_it(self, function_to_use, list_batch):
        start_time = time.perf_counter()
        with self.driver.session() as session:
            session.execute_write(function_to_use, list_batch)
        
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return elapsed_time
