# PRACA SKONCZONA

class Edge:
    pass


class Vertex:

    def __init__(self, key):
        self.key = key
        self.color = None

    def __eq__(self, other):
        return self.key == other

    def __hash__(self):
        return hash(self.key)


class List:

    def __init__(self):
        self.list_of_vertex = []
        self.dict_of_vertex = {}
        self.neighbours = {}
        self.edges = []

    def insertVertex(self, vertex):
        self.list_of_vertex.append(vertex)
        self.dict_of_vertex[vertex] = len(self.dict_of_vertex)

    def insertEdge(self, vertex1, vertex2, weight):
        if vertex1 not in self.neighbours:
            self.neighbours[vertex1] = [(vertex2, weight)]
            self.edges.append((vertex1, vertex2, weight))
        elif vertex2 not in self.neighbours[vertex1]:
            self.neighbours[vertex1].append((vertex2, weight))
            self.edges.append((vertex1, vertex2, weight))

        if vertex2 not in self.neighbours:
            self.neighbours[vertex2] = [(vertex1, weight)]
            self.edges.append((vertex2, vertex1, weight))
        elif vertex1 not in self.neighbours[vertex2]:
            self.neighbours[vertex2].append((vertex1, weight))
            self.edges.append((vertex2, vertex1, weight))

    def deleteEdge(self, vertex1, vertex2):
        if vertex2 in self.neighbours[vertex1]:
            self.neighbours[vertex1].remove(vertex2)
        if vertex1 in self.neighbours[vertex2]:
            self.neighbours[vertex2].remove(vertex1)
        self.edges.remove((vertex1, vertex2))
        self.edges.remove((vertex2, vertex1))

    def deleteVertex(self, vertex):
        for i in self.edges:
            if i[0] == vertex:
                self.deleteEdge(Vertex(i[0]), Vertex(i[1]))
            if i[1] == vertex:
                self.deleteEdge(Vertex(i[0]), Vertex(i[1]))
        a = self.dict_of_vertex[vertex]
        del self.neighbours[vertex], self.dict_of_vertex[vertex]
        for i in self.dict_of_vertex.keys():
            if self.dict_of_vertex[i] > a:
                self.dict_of_vertex[i] -= 1
        for i in self.neighbours:
            if vertex in self.neighbours[i]:
                self.neighbours[i].remove(vertex)

    def getVertexIdx(self, vertex):
        return self.dict_of_vertex.get(vertex)

    def getVertex(self, vertex_idx):
        return self.list_of_vertex[vertex_idx]

    def neighbours_fun(self, vertex_idx):
        temp = []
        for i in self.neighbours[self.getVertex(vertex_idx)]:
            a = self.getVertexIdx(i[0])
            temp.append((a, i[1]))
        return temp

    def order(self):
        return len(self.list_of_vertex)

    def size(self):
        if self.edges is not None:
            return len(self.edges)
        else:
            return None

    def edges(self):
        if self.edges is not None:
            return self.edges
        else:
            return None


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours_fun(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


def prim(G):
    v = 0
    intree = [0 for i in range(G.order())]
    distance = [float('inf') for i in range(G.order())]
    parent = [-1 for i in range(G.order())]
    MST = List()
    suma = 0
    for i in G.list_of_vertex:
        MST.insertVertex(i)
    while intree[v] == 0:
        intree[v] = 1
        neigh = G.neighbours_fun(v)
        for j in neigh:
            if j[1] < distance[j[0]] and intree[j[0]] == 0:
                distance[j[0]] = j[1]
                parent[j[0]] = v
        mini = float('inf')
        min_vert = 0
        for k in range(G.order()):
            if intree[k] == 0 and distance[k] < mini:
                mini = distance[k]
                min_vert = k
        if intree[min_vert] == 0:
            MST.insertEdge(MST.getVertex(min_vert), MST.getVertex(parent[min_vert]), mini)
            suma += mini
        v = min_vert
    return MST, suma


wiercholki = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
        ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
        ('C', 'G', 9), ('C', 'D', 3),
        ('D', 'G', 10), ('D', 'J', 18),
        ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
        ('F', 'H', 2), ('F', 'G', 8),
        ('G', 'H', 9), ('G', 'J', 8),
        ('H', 'I', 3), ('H', 'J', 9),
        ('I', 'J', 9)]

lista = List()

for i in wiercholki:
    lista.insertVertex(i)
for i in graf:
    lista.insertEdge(i[0], i[1], i[2])
a, b = prim(lista)
printGraph(a)