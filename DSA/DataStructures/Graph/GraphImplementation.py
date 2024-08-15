class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dictionary: ", self.graph_dict)

    def getPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path =  self.getPaths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return  paths

    def getShortestPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return []
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.getShortestPaths(node, end, path)
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    routes_graph = Graph(routes)
    print(routes_graph.getPaths("Mumbai", "New York"))
    print(routes_graph.getShortestPaths("Mumbai", "New York"))
