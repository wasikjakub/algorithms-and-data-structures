import polska


class Edge:
    pass


class Vertex:

    def __init__(self, key):
        self.key = key

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

    def insertEdge(self, vertex1, vertex2):
        if vertex1 not in self.neighbours:
            self.neighbours[vertex1] = [vertex2]
            self.edges.append((vertex1, vertex2))
        elif vertex2 not in self.neighbours[vertex1]:
            self.neighbours[vertex1].append(vertex2)
            self.edges.append((vertex1, vertex2))

        if vertex2 not in self.neighbours:
            self.neighbours[vertex2] = [vertex1]
            self.edges.append((vertex2, vertex1))
        elif vertex1 not in self.neighbours[vertex2]:
            self.neighbours[vertex2].append(vertex1)
            self.edges.append((vertex2, vertex1))

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
        if vertex in self.dict_of_vertex:
            return self.dict_of_vertex[vertex]
        else:
            return None

    def getVertex(self, vertex_idx):
        if vertex_idx in self.list_of_vertex:
            return self.list_of_vertex[vertex_idx]
        else:
            return None

    def neighbours(self, vertex_idx):
        temp = []
        for i in self.neighbours[self.getVertex(vertex_idx)]:
            temp.append(i.key)
        return temp

    def order(self):
        if self.neighbours is not None:
            return len(self.neighbours)
        else:
            return None

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


class Matrix:
    def __init__(self):
        self.matrix = []
        self.dict_of_vertex = {}
        self.neighbours = []
        self.edges = []

    def insertVertex(self, vertex):
        self.dict_of_vertex[vertex] = len(self.dict_of_vertex)
        self.neighbours.append(vertex)
        self.matrix.append([0] * len(self.matrix))
        for i in self.matrix:
            i.append(0)

    def insertEdge(self, vertex1, vertex2):
        edge = (vertex1,vertex2)
        self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = edge
        self.matrix[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = edge
        self.edges.append((vertex1, vertex2))

    def deleteEdge(self, vertex1, vertex2):
        self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = None #?
        self.matrix[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = None #?
        self.edges.remove((vertex1, vertex2))
        self.edges.remove((vertex2, vertex1))

    def deleteVertex(self, vertex):
        for i in self.edges:
            if i[0] == vertex:
                self.deleteEdge(Vertex(i[0]), Vertex(i[1]))
            if i[1] == vertex:
                self.deleteEdge(Vertex(i[0]), Vertex(i[1]))
        del self.neighbours[self.dict_of_vertex[vertex]]
        for i in self.matrix:
            del i[self.dict_of_vertex[vertex]]
        a = self.dict_of_vertex[vertex]
        del self.dict_of_vertex[vertex]
        for i in self.dict_of_vertex.keys():
            if self.dict_of_vertex[i] > a:
                self.dict_of_vertex[i] -= 1

    def getVertexIdx(self, vertex):
        if vertex in self.dict_of_vertex:
            return self.dict_of_vertex[vertex]
        else:
            return None

    def getVertex(self, vertex_idx):
        if vertex_idx in self.neighbours:
            return self.neighbours[vertex_idx]
        else:
            return None

    def neighbours(self, vertex_idx):
        temp = []
        for i in range(len(self.matrix[vertex_idx])):
            if self.matrix[vertex_idx][i] != 0:
                temp.append(i)
        return temp

    def order(self):
        if self.dict_of_vertex is not None:
            return len(self.dict_of_vertex)
        else:
            return None

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


def func(x):

    wojewodztwa = ['Z', 'G', 'N', 'B', 'F', 'P', 'C', 'E', 'W', 'L', 'D', 'O', 'S', 'T', 'K', 'R']

    graf = [('Z', 'G'), ('Z', 'P'), ('Z', 'F'),
            ('G', 'Z'), ('G', 'P'), ('G', 'C'), ('G', 'N'),
            ('N', 'G'), ('N', 'C'), ('N', 'W'), ('N', 'B'),
            ('B', 'N'), ('B', 'W'), ('B', 'L'),
            ('F', 'Z'), ('F', 'P'), ('F', 'D'),
            ('P', 'F'), ('P', 'Z'), ('P', 'G'), ('P', 'C'), ('P', 'E'), ('P', 'O'), ('P', 'D'),
            ('C', 'P'), ('C', 'G'), ('C', 'N'), ('C', 'W'), ('C', 'E'),
            ('E', 'P'), ('E', 'C'), ('E', 'W'), ('E', 'T'), ('E', 'S'), ('E', 'O'),
            ('W', 'C'), ('W', 'N'), ('W', 'B'), ('W', 'L'), ('W', 'T'), ('W', 'E'),
            ('L', 'W'), ('L', 'B'), ('L', 'R'), ('L', 'T'),
            ('D', 'F'), ('D', 'P'), ('D', 'O'),
            ('O', 'D'), ('O', 'P'), ('O', 'E'), ('O', 'S'),
            ('S', 'O'), ('S', 'E'), ('S', 'T'), ('S', 'K'),
            ('T', 'S'), ('T', 'E'), ('T', 'W'), ('T', 'L'), ('T', 'R'), ('T', 'K'),
            ('K', 'S'), ('K', 'T'), ('K', 'R'),
            ('R', 'K'), ('R', 'T'), ('R', 'L')]

    for i in wojewodztwa:
        x.insertVertex(i)
    for i in graf:
        x.insertEdge(i[0], i[1])
    x.deleteVertex("K")
    x.deleteEdge("W", "E")
    # polska.draw_map(x.edges)


lista = List()
func(lista)