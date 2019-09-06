import random
import bisect


class Ant:
    def __init__(self, graph, parameters):
        self.m_graph = graph
        self.m_visited_vertex = [False for i in range(parameters.mC_num_of_vertexes)]
        self.m_visited_path = []
        self.m_num_of_vertex = parameters.mC_num_of_vertexes
        self.m_parameters = parameters
        self.m_init_vertex = parameters.mC_initial_vertex

    def construct_path(self):
        self.m_visited_path.append(self.m_init_vertex)
        self.m_visited_vertex[self.m_init_vertex] = True
        for i in range(self.m_num_of_vertex - 1):
            v = self.m_visited_path[-1]
            to_vertexes, to_prob = self.calc_prob_from_v(v)
            random_p = random.uniform(0.0, 0.999999999)
            to = to_vertexes[bisect.bisect_left(to_prob, random_p)]
            self.m_visited_path.append(to)
            self.m_visited_vertex[to] = True

    def calc_next_pheromone(self):
        length = self.calc_all_path_length()
        Q = self.m_parameters.mC_Q
        for i in range(self.m_num_of_vertex - 1):
            self.m_graph.m_edge_next_pheromone[self.m_visited_path[i]][self.m_visited_path[i + 1]] += Q / length

    def calc_all_path_length(self):
        length = 0
        for i in range(self.m_num_of_vertex - 1):
            length += self.m_graph.m_edge_length[self.m_visited_path[i]][self.m_visited_path[i + 1]]
        return length

    def calc_prob_from_v(self, v):
        sumV = 0
        to_vertexes = []
        to_pheromones = []
        alpha = self.m_parameters.mC_alpha
        beta = self.m_parameters.mC_beta
        for to in range(self.m_num_of_vertex):
            if (to == v) or self.m_visited_vertex[to]:
                continue
            pheromone = self.m_graph.m_edge_pheromone[v][to] ** alpha + self.m_graph.m_edge_heuristics[v][to] ** beta
            sumV += pheromone
            to_vertexes.append(to)
            to_pheromones.append(pheromone)
        to_prob = [x / sumV for x in to_pheromones]
        for i in range(len(to_prob) - 1):
            to_prob[i + 1] += to_prob[i]
        return to_vertexes, to_prob

    def reset_ant(self):
        self.m_visited_vertex = [False for i in range(self.m_parameters.mC_num_of_vertexes)]
        self.m_visited_path = []
