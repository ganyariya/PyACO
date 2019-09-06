class Ant:
    def __init__(self, graph, parameters):
        self.graph = graph
        self.m_visited_vertex = [False for i in range(parameters.mC_num_of_vertexes)]
        self.m_visited_path = []

    def constrct_path(self):
        print(self.m_visited_vertex)
