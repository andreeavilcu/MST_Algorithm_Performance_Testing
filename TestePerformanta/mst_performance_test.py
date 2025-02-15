from graph_utilities import GraphUtility
import time
import matplotlib.pyplot as plt
import networkx as nx

def generate_test_graph(n,p):
    return GraphUtility.generate_erdos_renyi_graph(n, p)

def measure_mst_time(G, algorithm, use_manual=True):
    """
        Măsoară timpul de execuție al unui algoritm MST pe un graf dat.
    """
    start_time = time.time()
    if use_manual:
        if algorithm == "boruvka":
            GraphUtility.boruvka_mst(G.to_undirected())
        elif algorithm == "prim":
            GraphUtility.prim_mst(G.to_undirected())
        elif algorithm == "kruskal":
            GraphUtility.kruskal_mst(G.to_undirected())
        else:
            raise ValueError(f"Unsupported manual algorithm: {algorithm}")
    else:
        if algorithm in ["prim", "kruskal"]:
            nx.minimum_spanning_tree(G.to_undirected(), algorithm=algorithm)
        else:
            raise ValueError(f"Unsupported NetworkX algorithm: {algorithm}")

    return time.time() - start_time

def run_performance_test():
    node_sizes = [50, 100, 200, 300, 500]
    edge_probs = [0.1, 0.25, 0.5]
    algorithms = ["prim", "kruskal", "boruvka"]

    results_manual = {algo: [] for algo in algorithms}
    results_networkx = {algo: [] for algo in ["prim", "kruskal"]}

    for algo in algorithms:
        print(f"Testing manual algorithm: {algo}")
        for n in node_sizes:
            for p in edge_probs:
                print(f"  Generating graph with {n} nodes and p={p}")
                G = generate_test_graph(n, p)
                print("  Measuring execution time (manual)...")
                execution_time = measure_mst_time(G, algo, use_manual=True)
                results_manual[algo].append((n, p, execution_time))
                print(f"    Manual execution time: {execution_time:.4f} seconds")

                if algo in results_networkx:  # Testăm doar Prim și Kruskal în NetworkX
                    print("  Measuring execution time (NetworkX)...")
                    execution_time = measure_mst_time(G, algo, use_manual=False)
                    results_networkx[algo].append((n, p, execution_time))
                    print(f"    NetworkX execution time: {execution_time:.4f} seconds")

    return results_manual, results_networkx, node_sizes

def plot_results(results_manual, results_networkx, node_sizes):
    """
    Generează grafice comparative între implementările manuale și NetworkX.
    """
    for algo, data in results_manual.items():
        manual_times = {size: [] for size in node_sizes}
        for n, p, time in data:
            manual_times[n].append(time)

        if algo in results_networkx:
            networkx_times = {size: [] for size in node_sizes}
            for n, p, time in results_networkx[algo]:
                networkx_times[n].append(time)

        for idx, p in enumerate([0.1, 0.25, 0.5]):
            plt.plot(
                node_sizes,
                [manual_times[size][idx] for size in node_sizes],
                label=f"Manual p={p}",
                linestyle='--'
            )
            if algo in results_networkx:
                plt.plot(
                    node_sizes,
                    [networkx_times[size][idx] for size in node_sizes],
                    label=f"NetworkX p={p}",
                    linestyle='-'
                )

        plt.title(f"Execution time comparison for {algo.capitalize()} MST")
        plt.xlabel("Number of Nodes")
        plt.ylabel("Execution Time (s)")
        plt.legend()
        plt.grid()
        plt.show()


if __name__ == "__main__":
    results_manual, results_networkx, node_sizes = run_performance_test()
    plot_results(results_manual, results_networkx, node_sizes)
