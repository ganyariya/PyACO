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

            # 現在の頂点
            v = self.m_visited_path[-1]

            # 頂点vから移動できる頂点と確率を求める
            to_vertexes, to_prob = self.__calc_prob_from_v(v)
            to = -1

            # もし一様乱数よりも小さいなら、完全ランダムで選ぶ
            if random.random() < self.m_parameters.mC_ant_prob_random:
                to = to_vertexes[random.randint(0, len(to_vertexes) - 1)]
            else:

            # 確率選択を行う
                random_p = random.uniform(0.0, 0.999999999)
                to = to_vertexes[bisect.bisect_left(to_prob, random_p)]

            # toは次に向かう頂点で、pathに追加する
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

    def __calc_prob_from_v(self, v):

        # 確率の合計(分母)
        sumV = 0

        # 行き先候補情報
        to_vertexes = []
        to_pheromones = []
        alpha = self.m_parameters.mC_alpha
        beta = self.m_parameters.mC_beta

        for to in range(self.m_num_of_vertex):

            # すでに訪ねていたら
            if (to == v) or self.m_visited_vertex[to]:
                continue

            # フェロモン分子の計算
            pheromone = self.m_graph.m_edge_pheromone[v][to] ** alpha + self.m_graph.m_edge_heuristics[v][to] ** beta
            sumV += pheromone

            # 候補に足す
            to_vertexes.append(to)
            to_pheromones.append(pheromone)

        # 分母で割る
        to_prob = [x / sumV for x in to_pheromones]

        # 確率の累積和を取る
        for i in range(len(to_prob) - 1):
            to_prob[i + 1] += to_prob[i]

        # 行き先の頂点集合と確率を返す
        return to_vertexes, to_prob

    def reset_ant(self):
        self.m_visited_vertex = [False for i in range(self.m_parameters.mC_num_of_vertexes)]
        self.m_visited_path = []
