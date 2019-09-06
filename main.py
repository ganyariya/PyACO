from ACOSolver import ACOSolver

aco_solver = ACOSolver(num_of_ants=30, num_of_vertexes=50, Q=500, alpha=1, beta=5, rou=0.9, max_iterations=300,
                       initial_vertex=0, tau_max=0.67)

aco_solver.run_aco()
