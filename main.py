from ACOSolver import ACOSolver

aco_solver = ACOSolver(num_of_ants=30, num_of_vertexes=50, Q=100, alpha=3, beta=5, rou=0.9, max_iterations=300,
                       initial_vertex=0, tau_min=0, tau_max=3000, ant_prob_random=0.1, super_not_change=30, plot_time=0.2)
#ok
aco_solver.run_aco()
