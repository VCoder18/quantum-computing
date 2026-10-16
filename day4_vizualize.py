from day4_max_cut_solver import *
import networkx as nx

edges, n = graphs["Complete graph K4"]

def draw_graph(edges, n, coloring=None):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    
    pos = nx.circular_layout(G)
    colors = ['red' if coloring and coloring[i] == 0 else 'blue' for i in range(n)] if coloring else 'lightblue'
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, font_color="white")
    plt.title("Graph")
    plt.show()

draw_graph(edges, n, coloring=[0, 1, 0, 1])

depths = [1, 2, 3, 4]
results = []

for p in depths:
    best_cut, _, _ = solve_maxcut(edges, n, p=p, num_samples=20)
    results.append(best_cut)

plt.plot(depths, results, 'o-')
plt.xlabel("QAOA depth (p)")
plt.ylabel("Best cut found")
plt.title("QAOA quality vs depth")
plt.grid(True)
plt.show()