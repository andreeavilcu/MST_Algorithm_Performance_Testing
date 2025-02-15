import networkx as nx
import random

class GraphUtility:
    @staticmethod
    def generate_erdos_renyi_graph(n, p):
        while True:
            G = nx.DiGraph()
            for i in range(n):
                G.add_node(i)

            for i in range(n):
                for j in range(i + 1, n):
                    if random.random() < p:
                        weight = random.randint(1, 10)
                        G.add_edge(i, j, weight=weight)
                        G.add_edge(j, i, weight=weight)

            if nx.is_strongly_connected(G):
                return G

    @staticmethod
    def boruvka_mst(G):
        mst_edges = set()
        components = [{node} for node in G.nodes()]

        while len(components) > 1:
            min_edges = []

            for comp in components:
                min_edge = None
                min_weight = float('inf')

                for u in comp:
                    for v, data in G[u].items():
                        if v not in comp and data['weight'] < min_weight:
                            min_weight = data['weight']
                            min_edge = (u, v)

                if min_edge:
                    min_edges.append(min_edge)

            if not min_edges:
                break

            for edge in min_edges:
                mst_edges.add(edge)
                comp1 = next(c for c in components if edge[0] in c)
                comp2 = next(c for c in components if edge[1] in c)
                if comp1 != comp2:
                    comp1.update(comp2)
                    components.remove(comp2)

        return list(mst_edges)

    @staticmethod
    def prim_mst(G):
        start_node = list(G.nodes())[0]
        visited = set()
        edges = []
        mst_edges = []

        for neighbor, data in G[start_node].items():
            edges.append((data['weight'], start_node, neighbor))
        visited.add(start_node)

        edges.sort()

        while edges:
            weight, u, v = edges.pop(0)
            if v not in visited:
                visited.add(v)
                mst_edges.append((u, v, weight))

                for neighbor, data in G[v].items():
                    if neighbor not in visited:
                        edges.append((data['weight'], v, neighbor))
                edges.sort()

        return mst_edges

    @staticmethod
    def kruskal_mst(G):
        edges = [(data['weight'], u, v) for u, v, data in G.edges(data=True)]
        edges.sort()
        parent = {node: node for node in G.nodes()}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parent[root2] = root1

        mst_edges = []

        for weight, u, v in edges:
            if find(u) != find(v):
                mst_edges.append((u, v, weight))
                union(u, v)

        return mst_edges
