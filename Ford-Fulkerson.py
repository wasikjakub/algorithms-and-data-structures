class Edge:

    def __init__(self, v1, v2, cap, isres: bool):
        self.v1 = v1
        self.v2 = v2
        self.capacity = cap
        self.isResidual = isres
        self.residual = cap
        self.flow = 0

    def __str__(self):
        # return str(self.capacity), str(self.flow), str(self.residual), str(self.isResidual())
        return 'pojemność: ' + str(self.capacity) + ', przepływ: ' + str(self.flow) + ', przepływ resztowy: ' + str(self.residual) + ', czy krawędź jest resztowa? ' + str(self.residual)

    def __repr__(self):
        # return str(self.capacity), str(self.flow), str(self.residual), str(self.isResidual())
        return 'pojemność: ' + str(self.capacity) + ', przepływ: ' + str(self.flow) + ', przepływ resztowy: ' + str(self.residual) + ', czy krawędź jest resztowa? ' + str(self.residual)


class Vertex:

    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class List:

    def __init__(self):
        self.list_of_vertex = []
        self.dict_of_vertex = {}
        self.edges = []

    def insertVertex(self, vertex):
        self.edges.append(vertex)
        self.dict_of_vertex[vertex] = len(self.edges) - 1
        self.list_of_vertex.append([])

    def insertEdge(self, vertex1, vertex2, weight):
        vertex1 = Vertex(vertex1)
        vertex2 = Vertex(vertex2)
        if vertex1 not in self.edges:
            self.insertVertex(vertex1)
        if vertex2 not in self.edges:
            self.insertVertex(vertex2)
        edge = Edge(vertex1, vertex2, weight, isres=False)
        self.list_of_vertex[self.getVertexIdx(vertex1)].append(edge)
        edge2 = Edge(vertex2, vertex1, 0, isres=True)
        self.list_of_vertex[self.getVertexIdx(vertex2)].append(edge2)

    def getVertexIdx(self, vertex):
        return self.dict_of_vertex.get(vertex)

    def getVertex(self, vertex_idx):
        return self.edges[vertex_idx]

    def neighbours_fun(self, vertex_idx):
        return self.list_of_vertex[vertex_idx]

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
        for j in nbrs:
            print(j.v2, j.capacity, j.flow, j.residual, j.isResidual, end=";")
        print()
    print("-------------------")


def BFS(graf, w):
    visited = [w]
    parent = [-1 for i in range(graf.order())]
    que = [w]
    while que:
        w1 = que.pop(0)
        neigh = graf.neighbours_fun(w1)
        for i in neigh:
            iD = graf.getVertexIdx(i.v2)
            if i.residual > 0 and iD not in visited:
                que.append(iD)
                visited.append(iD)
                parent[iD] = w1
    return parent


def path(graf, w, k, parent):
    mincap = float('inf')
    current = k
    if parent[current] == -1:
        return 0
    while current != w:
        parentid = parent[current]
        neigh = graf.neighbours_fun(parentid)
        for i in neigh:
            if i.isResidual is False:
                if graf.getVertexIdx(i.v2) == current:
                    if i.residual < mincap:
                        mincap = i.residual
                    break
        current = parentid
    return mincap


def augument(graf, w, k, parent, mincap):
    current = k
    if parent[current] == -1:
        return 0
    while current != w:
        parentid = parent[current]
        neigh = graf.neighbours_fun(parentid)
        for i in neigh:
            if i.isResidual is False:
                if graf.getVertexIdx(i.v2) == current:
                    i.flow += mincap
                    i.residual -= mincap
                    break
        neigh = graf.neighbours_fun(current)
        for i in neigh:
            if i.isResidual is True:
                if graf.getVertexIdx(i.v2) == parentid:
                    if i.residual < mincap:
                        i.residual += mincap
                    break
        current = parentid


def ford_fulkerson(graf, w, k):
    list = BFS(graf, w)
    current = k
    while current != w or current == -1:
        current = list[current]
    mincap = path(graf, w, k, list)
    maxcap = 0
    while mincap > 0:
        augument(graf, w, k, list, mincap)
        list = BFS(graf, w)
        mincap = path(graf, w, k, list)
    neigh = graf.neighbours_fun(k)
    for i in neigh:
        maxcap += i.residual
    maxcap += 1
    return maxcap


graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
graf = List()
for i, j, k in graf_0:
    graf.insertEdge(i, j, k)
print('Wynik: ', ford_fulkerson(graf, 0, 2))
printGraph(graf)

graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
graf = List()
for i, j, k in graf_1:
    graf.insertEdge(i, j, k)
print('Wynik: ', int(ford_fulkerson(graf, 0, 4)))
printGraph(graf)

graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graf = List()
for i, j, k in graf_2:
    graf.insertEdge(i, j, k)
print('Wynik: ', int(ford_fulkerson(graf, 0, 6)))
printGraph(graf)

graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
graf = List()
for i, j, k in graf_2:
    graf.insertEdge(i, j, k)
print('Wynik: ', int(ford_fulkerson(graf, 0, 4)))
printGraph(graf)
