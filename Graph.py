import random
import math


class Graph:
    def __init__(self, parameters):
        self.m_num_of_vertexes = parameters.mC_num_of_vertexes
        self.m_coordinates = [None] * self.m_num_of_vertexes
        self.m_edge_length = [[0 for j in range(self.m_num_of_vertexes)] for i in range(self.m_num_of_vertexes)]
        self.m_edge_pheromone = [[0 for j in range(self.m_num_of_vertexes)] for i in range(self.m_num_of_vertexes)]
        self.m_edge_heuristics = [[0 for j in range(self.m_num_of_vertexes)] for i in range(self.m_num_of_vertexes)]
        self.m_edge_next_pheromone = [[0 for j in range(self.m_num_of_vertexes)] for i in
                                      range(self.m_num_of_vertexes)]
        self.m_parameters = parameters
        self.__prepare_graph()

    def __prepare_graph(self):
        for i in range(self.m_num_of_vertexes):
            self.m_coordinates[i] = (random.uniform(0, 1000), random.uniform(0, 1000))
        for i in range(self.m_num_of_vertexes):
            for j in range(self.m_num_of_vertexes):
                self.m_edge_length[i][j] = Graph.__calc_edge_length(self.m_coordinates[i], self.m_coordinates[j])
        for i in range(self.m_num_of_vertexes):
            for j in range(self.m_num_of_vertexes):
                if i < j:
                    self.m_edge_pheromone[i][j] = self.m_parameters.mC_Q / self.m_edge_length[i][j]
                    self.m_edge_pheromone[j][i] = self.m_parameters.mC_Q / self.m_edge_length[i][j]
        for i in range(self.m_num_of_vertexes):
            for j in range(self.m_num_of_vertexes):
                if i < j:
                    h = self.m_parameters.mC_Q / self.m_edge_length[i][j]
                    self.m_edge_heuristics[i][j] = h
                    self.m_edge_heuristics[j][i] = h

    def reset_graph(self):
        self.m_edge_next_pheromone = [[0 for j in range(self.m_num_of_vertexes)] for i in
                                      range(self.m_num_of_vertexes)]

    def reset_graph_when_stagnation(self):
        for i in range(self.m_num_of_vertexes):
            for j in range(self.m_num_of_vertexes):
                if i < j:
                    self.m_edge_pheromone[i][j] = self.m_parameters.mC_Q / self.m_edge_length[i][j]
                    self.m_edge_pheromone[j][i] = self.m_parameters.mC_Q / self.m_edge_length[i][j]

    @staticmethod
    def __calc_edge_length(p1, p2):
        dx = (p1[0] - p2[0]) ** 2
        dy = (p1[1] - p2[1]) ** 2
        return math.sqrt(dx + dy)
