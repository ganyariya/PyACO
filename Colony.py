from Ant import Ant


class Colony:
    def __init__(self, graph, parameters):
        self.m_num_of_ants = parameters.mC_num_of_ants
        self.m_parameters = parameters
        self.m_graph = graph
        self.m_ants = [Ant(self.m_graph, self.m_parameters) for i in range(self.m_num_of_ants)]

    def construct_ants(self):
        for i in range(self.m_num_of_ants):
            self.m_ants[i].constrct_path()
