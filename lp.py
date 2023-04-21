"""
    This file contains the description of the BIP in code
"""

from mip import Model, xsum, maximize, BINARY, OptimizationStatus




# Assume that `layers` is a list of given `Layer` objects with
# an attribute being a list of `Material` objects called `materials`
def lp_solve(alpha, beta, gamma, layers):
    # Set up appropriate binary LP solver - will tune if necessary
    model = Model("knapsack")

    # Iterables to make summation descriptions neat
    L = range(len(layers))
    M = [range(len(layers[i].materials)) for i in L]

    # Set up appropriately-sized decision variable x
    x = [[model.add_var(name=(layers[l].name + ', ' + layers[l].materials[m].name), var_type=BINARY) for m in M[l]] for l in L]

    # Objective function
    model.obj = maximize(
                    xsum(
                        (alpha * layers[l].materials[m].rec + beta * layers[l].materials[m].proc_cost + gamma * layers[l].materials[m].mkt_value) * x[l][m] \
                        for l in L for m in M[l]
                    )
                )
    
    # Constraints
    for l in L:
        model += xsum(x[l][m] for m in M[l]) == 1

    # Run optimization
    status = model.optimize()

    # Print optimization results
    if status == OptimizationStatus.OPTIMAL:
        print('optimal solution cost {} found'.format(model.objective_value))
    elif status == OptimizationStatus.FEASIBLE:
        print('sol.cost {} found, best possible: {}'.format(model.objective_value, model.objective_bound))
    elif status == OptimizationStatus.NO_SOLUTION_FOUND:
        print('no feasible solution found, lower bound is: {}'.format(model.objective_bound))
    if status == OptimizationStatus.OPTIMAL or status == OptimizationStatus.FEASIBLE:
        print('solution:')
        for v in model.vars:
            if abs(v.x) > 1e-6: # only printing non-zeros
                print('{} : {}'.format(v.name, v.x))