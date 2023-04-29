""" 
    File to test the mechanics of the LP code
    Testing has revealed that something is not working the way it should
    TO BE FIXED
"""

from opt_algorithm.lp import *
from opt_algorithm.objects import *


def main():
    # Dummy values - absolutely no reasoning behind them
    alpha = 900
    beta = -40
    gamma = 25

    # Note that the materials have to be repeated for each layer since recyclability can vary
    layers = [Layer("l1", [Material("PET", 0.5, 0.7, 0.8), Material("PP", 0.6, 0.9, 0.3)]),
              Layer("l2", [Material("PET", 0.8, 0.6, 0.8), Material("PP", 0.9, 0.6, 0.4)]),
              Layer("l3", [Material("PET", 0.8, 0.6, 0.8), Material("PP", 0.9, 0.6, 0.4), 
                           Material("Nylon 6", 0.4, 0.7, 0.1), Material("Nylon 66", 0.4, 0.1, 0.05)]),
              Layer("l4", [Material("Generic Thermoplastic", 0.4, 0.1, 0.2)])]


    lp_solve(alpha, beta, gamma, layers)

if __name__ == '__main__':
    main()