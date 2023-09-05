import numpy as np


class Vertex:

    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other

    def __hash__(self):
        return hash(self.key)


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

    def insertEdge(self, vertex1, vertex2, weigth):
        edge = (vertex1, vertex2)
        self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = weigth
        self.matrix[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = weigth
        self.edges.append((vertex1, vertex2))

    def getVertexIdx(self, vertex):
        return self.dict_of_vertex[vertex]

    def neighbours(self, vertex_idx):
        temp = []
        for i in range(len(self.matrix[vertex_idx])):
            if self.matrix[vertex_idx][i] != 0:
                temp.append(i)
        return temp


graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

wierzcholki = ['A', 'B', 'C', 'D', 'E', 'F']

wierzcholki2 = ['A', 'B', 'C']

grafG = Matrix()
grafP = Matrix()
for i in wierzcholki:
    grafG.insertVertex(i)
for i, j, k in graph_G:
    grafG.insertEdge(i, j, k)

for i in wierzcholki2:
    grafP.insertVertex(i)
for i, j, k in graph_P:
    grafP.insertEdge(i, j, k)

graf_G = np.array(grafG.matrix)
graf_P = np.array(grafP.matrix)

M = np.zeros((graf_P.shape[0], graf_G.shape[1]))
M0 = np.ones((graf_P.shape[0], graf_G.shape[1]))


def ullman_1(used_columns, current_row, G, P, M, result=None):
    if result is None:
        result = [0, 0]
    if current_row == M.shape[0]:
        temp = M @ G
        temp_transposed = np.transpose(temp)
        temp2 = M @ temp_transposed
        if np.allclose(P, temp2):  # funkcja porownujaca macierze
            result[0] += 1
            return result
    else:
        M_prim = np.matrix.copy(M)
        for unused_col in range(0, len(used_columns)):
            if used_columns[unused_col] is False:
                M_prim[current_row][unused_col] = 1
                for i in range(unused_col+1, M_prim.shape[1]):
                    M_prim[current_row][i] = 0
                used_columns[unused_col] = True
                result[1] += 1
                result = ullman_1(used_columns, current_row + 1, G, P, M_prim, result)
                used_columns[unused_col] = False
                M_prim[current_row][unused_col] = 0
    return result


def ullman_2(used_columns, current_row, G, P, M, M0=None, result=None):
    if result is None:
        result = [0, 0]
    if current_row == M.shape[0]:
        temp = M @ G
        temp_transposed = np.transpose(temp)
        temp2 = M @ temp_transposed
        if np.allclose(P, temp2):  # funkcja porownujaca macierze
            result[0] += 1
            return result
    else:
        M_prim = np.matrix.copy(M)
        for unused_col in range(0, len(used_columns)):
            if used_columns[unused_col] is False:
                M_prim[current_row][unused_col] = 1
                for i in range(unused_col+1, M_prim.shape[1]):
                    M_prim[current_row][i] = 0
                used_columns[unused_col] = True
                result[1] += 1
                result = ullman_2(used_columns, current_row + 1, G, P, M_prim, M0, result)
                used_columns[unused_col] = False
                M_prim[current_row][unused_col] = 0
    return result


def prune(M, G, P, lst, current_row):
    for row in range(0, M.shape[0]):
        for col in range(0, M.shape[1]):
            if M[row][col] == 1:
                temp = False
                for k in P.neighbours(row) and G.neighbours(col):
                    temp = True
                if temp is not True:
                    M[row][col] = 0
                    lst.append((row, col))
                    current_row = row
    return lst, current_row


def ullman_3(used_columns, current_row, G, P, M, M0=None, result=None, lst=[]):
    if result is None:
        result = [0, 0]
    if current_row == M.shape[0]:
        temp = M @ G
        temp_transposed = np.transpose(temp)
        temp2 = M @ temp_transposed
        if np.allclose(P, temp2):  # funkcja porownujaca macierze
            result[0] += 1
            return result
    else:
        M_prim = np.matrix.copy(M)
        lst = prune(M_prim, G, P, lst, current_row)
        current_row = lst[1]
        for unused_col in range(0, len(used_columns)):
            if used_columns[unused_col] is False:
                M_prim[current_row][unused_col] = 1
                for i in range(unused_col+1, M_prim.shape[1]):
                    M_prim[current_row][i] = 0
                used_columns[unused_col] = True
                result[1] += 1
                result = ullman_2(used_columns, current_row + 1, G, P, M_prim, M0, result)
                used_columns[unused_col] = False
                M_prim[current_row][unused_col] = 0
    return result


used_columns = [False for i in range(M.shape[1])]
print(ullman_1(used_columns, 0, graf_G, graf_P, M))
print(ullman_2(used_columns, 0, graf_G, graf_P, M, M0))
lst = []
print(ullman_3(used_columns, 0, graf_G, graf_P, M, M0))
