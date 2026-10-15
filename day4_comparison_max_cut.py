from day4_max_cut_solver import *
from itertools import product

def brute_force_maxcut(edges, n):
    best_cut = 0
    best_coloring = None
    for bits in product([0, 1], repeat=n):
        cut = sum(1 for i, j in edges if bits[i] != bits[j])
        if cut > best_cut:
            best_cut = cut
            best_coloring = bits
    return best_cut, best_coloring

for name, (edges, n) in graphs.items():
    classical_best, classical_coloring = brute_force_maxcut(edges, n)
    qaoa_best, qaoa_bitstring, _ = solve_maxcut(edges, n, p=2)
    
    print(f"\n{name}:")
    print(f" Classical best: {classical_best} (coloring: {classical_coloring})")
    print(f" QAOA best: {qaoa_best} (coloring: {qaoa_bitstring})")