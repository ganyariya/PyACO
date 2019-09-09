from PyACO.Ant import Ant
from copy import deepcopy


class Colony:
    def __init__(self, graph, parameters):
        self.m_num_of_ants = parameters.mC_num_of_ants
        self.m_parameters = parameters
        self.m_graph = graph
        self.m_ants = [Ant(self.m_graph, self.m_parameters) for i in range(self.m_num_of_ants)]

    def update_colony(self):
        self.__construct_ants()
        self.__calc_next_pheromones()

    def get_best_ant_path(self):
        length = 1e20
        path = []
        for ant in self.m_ants:
            if ant.calc_all_path_length() < length:
                length = ant.calc_all_path_length()
                path = deepcopy(ant.m_visited_path)
        return [length, path]

    def reset_colony(self):
        for ant in self.m_ants:
            ant.reset_ant()

    def __construct_ants(self):

        for ant in self.m_ants:
            ant.construct_path()

    def __calc_next_pheromones(self):
        for ant in self.m_ants:
            ant.calc_next_pheromone()
