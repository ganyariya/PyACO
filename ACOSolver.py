from Parameters import Parameters
from Colony import Colony
from Graph import Graph


class ACOSolver:
    def __init__(self, num_of_ants, num_of_vertexes, Q, alpha, beta, rou, max_iterations, initial_vertex, tau_max):
        self.mC_parameters = Parameters(num_of_ants, num_of_vertexes, Q, alpha, beta, rou, max_iterations, initial_vertex,
                                     tau_max)
        self.m_graph = Graph(self.mC_parameters)
        self.m_colony = Colony(self.m_graph, self.mC_parameters)
