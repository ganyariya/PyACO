from Parameters import Parameters
from Colony import Colony
from Graph import Graph


class ACOSolver:
    def __init__(self, num_of_ants, num_of_vertexes, Q, alpha, beta, rou, max_iterations, initial_vertex, tau_max):
        self.mC_parameters = Parameters(num_of_ants, num_of_vertexes, Q, alpha, beta, rou, max_iterations,
                                        initial_vertex,
                                        tau_max)
        self.m_graph = Graph(self.mC_parameters)
        self.m_colony = Colony(self.m_graph, self.mC_parameters)
        self.m_best_ant = None

    def run_aco(self):
        for T in range(self.mC_parameters.mC_max_iterations):
            self.__update_aco()
            self.__reset_aco()
            print(self.m_best_ant[0], self.m_best_ant[1])

    def __update_aco(self):
        self.m_colony.update_colony()
        self.__update_next_pheromones()
        self.m_best_ant = self.m_colony.get_best_ant_path()

    def __reset_aco(self):
        self.m_colony.reset_colony()
        self.m_graph.reset_graph()

    def __update_next_pheromones(self):
        num_of_vertexes = self.mC_parameters.mC_num_of_vertexes
        rou = self.mC_parameters.mC_rou
        for i in range(num_of_vertexes):
            for j in range(num_of_vertexes):
                self.m_graph.m_edge_pheromone[i][j] = self.m_graph.m_edge_pheromone[i][j] * rou + \
                                                      self.m_graph.m_edge_next_pheromone[i][j]
