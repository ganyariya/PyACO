class Parameters:
    def __init__(self, num_of_ants, num_of_vertexes, Q, alpha, beta, rou, max_iterations, initial_vertex, tau_min,
                 tau_max, ant_prob_random, super_not_change, plot_time):
        self.mC_num_of_ants = num_of_ants
        self.mC_num_of_vertexes = num_of_vertexes
        self.mC_Q = Q
        self.mC_alpha = alpha
        self.mC_beta = beta
        self.mC_rou = rou
        self.mC_max_iterations = max_iterations
        self.mC_initial_vertex = initial_vertex
        self.mC_tau_min = tau_min
        self.mC_tau_max = tau_max
        self.mC_ant_prob_random = ant_prob_random
        self.mC_super_not_change = super_not_change
        self.mC_plot_time = plot_time
