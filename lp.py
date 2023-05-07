"""
    This file contains the description of the Binary Integer Program in code
"""

from mip import Model, xsum, maximize, BINARY, OptimizationStatus




# Assume that `layers` is a list of given `Layer` objects with
# an attribute being a list of `Material` objects called `materials`
def lp_solve(alpha, beta, gamma, layers):
    # Set up appropriate binary LP solver
    model = Model("knapsack")

    # Iterables to make summation descriptions neat
    L = range(len(layers))
    M = [range(len(layers[i].materials)) for i in L]

    # Set up appropriately-sized decision variable x
    x = [[model.add_var(name=(layers[l].name + ', ' + layers[l].materials[m].name), var_type=BINARY) for m in M[l]] for l in L]

    # Objective function
    model.objective = maximize(
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

    result_str = ""

    # Return optimization results
    if status == OptimizationStatus.OPTIMAL:
        result_str += "Maximum benefit {} found\n".format(model.objective_value)
    elif status == OptimizationStatus.FEASIBLE:
        result_str += 'sol.cost {} found, best possible: {}\n'.format(model.objective_value, model.objective_bound)
    elif status == OptimizationStatus.NO_SOLUTION_FOUND:
        result_str += 'No feasible solution found, lower bound is: {}\n'.format(model.objective_bound)
    if status == OptimizationStatus.OPTIMAL or status == OptimizationStatus.FEASIBLE:
        result_str += 'Optimal Material Choices:\n\n'
        for v in model.vars:
            if abs(v.x) > 1e-6: # only printing non-zeros
                #result_str += '{} : {}\n'.format(v.name, v.x)
                result_str += '{}\n'.format(v.name)
    
    return result_str