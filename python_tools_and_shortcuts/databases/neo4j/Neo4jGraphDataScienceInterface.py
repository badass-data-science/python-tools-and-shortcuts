from graphdatascience import GraphDataScience

from python_tools_and_shortcuts.databases.neo4j.Neo4jInterface import Neo4jInterface

class Neo4jGraphDataScienceInterface(Neo4jInterface):
    
    def __init__(
        self,
        password,
        database = 'neo4j',
        uri = 'neo4j://localhost:7687',         
        username = 'neo4j',
    ):
        super().__init__(
            password,
            database = database,
            uri = uri,
            username = username,
        )
        
        self.gds = GraphDataScience(uri, auth = self.auth)

        
    def create_a_gds_graph_projection(
        self,
        graph_name : str,
        node_label : str,
        relationship_type : str,
    ):

        try:
            self.graph_projection = self.gds.graph.get(graph_name)
            self.graph_projection.drop()
        except:
            pass
            
        try:
            self.graph_projection, project_result = self.gds.graph.project(
                graph_name,
                node_label,
                relationship_type,
            )
        except Exception:
            # If it already_exists
            self.graph_projection = self.gds.graph.get(graph_name)

    def run_pagerank_on_gds_graph_projection(
        self,
        max_iterations : int = 20,
        damping_factor : float = 0.85,
    ):
        self.df_pagerank = self.gds.pageRank.stream(
            self.graph_projection, 
            maxIterations = max_iterations,
            dampingFactor = damping_factor,
        )

        self.df_pagerank['node_name'] = self.df_pagerank['nodeId'].apply(
            lambda node_id: self.gds.util.asNode(node_id)['name']
        )

        self.df_pagerank = self.df_pagerank.reset_index(drop = True)

    def run_label_propagation_on_gds_graph_projection(
        self,
    ):
        self.df_lpa_results = self.gds.labelPropagation.stream(self.graph_projection)

        self.df_lpa_results['node_name'] = self.df_lpa_results['nodeId'].apply(
            lambda node_id: self.gds.util.asNode(node_id)['name']
        )

        self.df_lpa_results = self.df_lpa_results[['node_name', 'communityId']].copy()
