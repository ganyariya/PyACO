from PyACO.Parameters import Parameters
from PyACO.Colony import Colony
from PyACO.Graph import Graph
from PyACO import plot


class ACOSolver:
    def __init__(self, num_of_ants, num_of_vertexes, Q, alpha, beta, rou, max_iterations, initial_vertex, tau_min,
                 tau_max, ant_prob_random, super_not_change, plot_time):
        self.mC_parameters = Parameters(num_of_ants, num_of_vertexes, Q, alpha, beta, rou, max_iterations,
                                        initial_vertex, tau_min,
                                        tau_max, ant_prob_random, super_not_change, plot_time)
        self.m_graph = Graph(self.mC_parameters)
        self.m_colony = Colony(self.m_graph, self.mC_parameters)
        self.m_best_ant = None
        self.m_super_ant = None
        self.m_cnt_super_not_change = 0
        plot.init_plot()

    def run_aco(self):
        for T in range(self.mC_parameters.mC_max_iterations):
            self.__update_aco()
            self.__reset_aco()
            if self.m_super_ant is None:
                self.m_super_ant = self.m_best_ant
            if self.m_super_ant[0] > self.m_best_ant[0]:
                self.m_super_ant = self.m_best_ant
            else:
                self.m_cnt_super_not_change += 1

            if self.m_cnt_super_not_change > self.mC_parameters.mC_super_not_change:
                self.reset_pheromones()
                self.m_cnt_super_not_change = 0

            print(T, self.m_super_ant)
            plot.play_plot(self.m_graph.m_coordinates, self.m_super_ant[1], self.m_best_ant[1],
                           self.mC_parameters.mC_plot_time)

    def reset_pheromones(self):
        self.m_graph.reset_graph_when_stagnation()

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
        tau_min = self.mC_parameters.mC_tau_min
        tau_max = self.mC_parameters.mC_tau_max
        for i in range(num_of_vertexes):
            for j in range(num_of_vertexes):
                self.m_graph.m_edge_pheromone[i][j] = self.m_graph.m_edge_pheromone[i][j] * rou + \
                                                      self.m_graph.m_edge_next_pheromone[i][j]
        for i in range(num_of_vertexes):
            for j in range(num_of_vertexes):
                self.m_graph.m_edge_pheromone[i][j] = min(tau_max, max(self.m_graph.m_edge_pheromone[i][j], tau_min))
