import time
import numpy as np


def string_compare(P, T, i=None, j=None):
    if i is None and j is None:
        i = len(P) - 1
        j = len(T) - 1
    if i == 0:
        return j
    if j == 0:
        return i
    zamiana = string_compare(P, T, i-1, j-1) + int(P[i] != T[j])
    wstawienie = string_compare(P, T, i, j-1) + 1
    usuniecie = string_compare(P, T, i-1, j) + 1
    lowest_cost = min(zamiana, wstawienie, usuniecie)
    return lowest_cost


P = ' kot'
T = ' pies'

# t_start = time.perf_counter()
print(string_compare(P, T))
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def PD_compare(P, T, i=None, j=None):
    D = np.zeros((len(P), len(T)))
    D[0:] = [i in range(len(T))]
    D[:0] = [i in range(len(P))]
    rodzice = np.full((len(P), len(T)), 'x')
    rodzice[0, 1:] = ['I']*(len(T) - 1)
    rodzice[1:, 0] = ['D']*(len(P) - 1)
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamiana = D[i-1][j-1] + int(P[i] != T[j])
            wstawienie = D[i][j-1]+1
            usuniecie = D[i-1][j]+1
            lowest_cost = min(zamiana, wstawienie, usuniecie)
            D[i][j] = lowest_cost
            if P[i] == T[j]:
                rodzice[i][j] = 'M'
            elif lowest_cost == zamiana:
                rodzice[i][j] = 'S'
            elif lowest_cost == wstawienie:
                rodzice[i][j] = 'I'
            elif lowest_cost == usuniecie:
                rodzice[i][j] = 'D'
    rodzice[0][0] = 'x'
    end = int(D[-1][-1])
    return end, rodzice


P = ' biały autobus'
T = ' czarny autokar'

# t_start = time.perf_counter()
print(PD_compare(P, T)[0])
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def sciezka(rodzice):
    i = rodzice.shape[0]-1
    j = rodzice.shape[1]-1
    sciezka = ""
    while rodzice[i][j] != 'x':
        sciezka += rodzice[i][j]
        if rodzice[i][j] == 'I':
            j -= 1
        if rodzice[i][j] == 'D':
            i -= 1
        else:
            i -= 1
            j -= 1
    return sciezka[::-1]


P = ' thou shalt not'
T = ' you should not'
end, rodzice = PD_compare(P, T)

# t_start = time.perf_counter()
print(sciezka(rodzice))
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def goal_cell(P, T, D):
    i = len(P) - 1
    j = 0
    for k in range(1, len(T)):
        if D[i][k] < D[i][j]:
            j = k
    return j


def dopasowanie(P, T, i=None, j=None):
    D = np.zeros((len(P), len(T)))
    D[:, 0] = [i for i in range(len(P))]
    rodzice = np.full((len(P), len(T)), 'x')
    rodzice[1:, 0] = ['D']*(len(P) - 1)
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamiana = D[i-1][j-1] + int(P[i] != T[j])
            wstawienie = D[i][j-1]+1
            usuniecie = D[i-1][j]+1
            lowest_cost = min(zamiana, wstawienie, usuniecie)
            D[i][j] = lowest_cost
            if P[i] == T[j]:
                rodzice[i][j] = 'M'
            elif lowest_cost == zamiana:
                rodzice[i][j] = 'S'
            elif lowest_cost == wstawienie:
                rodzice[i][j] = 'I'
            elif lowest_cost == usuniecie:
                rodzice[i][j] = 'D'
    rodzice[0][0] = 'x'
    j = goal_cell(P, T, D)
    end = j - len(P)+2  # indeks zaczecie sie podciagu
    return end, rodzice


P = ' bin'
T = ' mokeyssbanana'
P1 = ' ban'

print(dopasowanie(P, T)[0])
print(dopasowanie(P1, T)[0])


def sciezka_2(rodzice):
    i = rodzice.shape[0]-1
    j = rodzice.shape[1]-1
    sciezka = ""
    temp = []
    while rodzice[i][j] != 'x':
        sciezka += rodzice[i][j]
        if rodzice[i][j] == 'I':
            j -= 1
        if rodzice[i][j] == 'D':
            i -= 1
        if rodzice[i][j] == 'M' or rodzice[i][j] == 'S':
            i -= 1
            j -= 1
            temp.append(i)
    return sciezka, temp


def sekwencja(P, T, i=None, j=None):
    D = np.zeros((len(P), len(T)))
    D[0, :] = [i for i in range(len(T))]
    D[:, 0] = [i for i in range(len(P))]
    rodzice = np.full((len(P), len(T)), 'x')
    rodzice[0, 1:] = ['I']*(len(T) - 1)
    rodzice[1:, 0] = ['D']*(len(P) - 1)
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                zamiana = D[i - 1][j - 1] + 9999999
            else:
                zamiana = D[i - 1][j - 1]
            wstawienie = D[i][j-1]+1
            usuniecie = D[i-1][j]+1
            lowest_cost = min(zamiana, wstawienie, usuniecie)
            D[i][j] = lowest_cost
            if P[i] == T[j]:
                rodzice[i][j] = 'M'
            elif lowest_cost == zamiana:
                rodzice[i][j] = 'S'
            elif lowest_cost == wstawienie:
                rodzice[i][j] = 'I'
            elif lowest_cost == usuniecie:
                rodzice[i][j] = 'D'
    rodzice[0][0] = 'x'
    sciezka, temp = sciezka_2(rodzice)
    res = ''
    for i in range(len(P)):
        if i-1 in temp:
            res += P[i]
    return res


P = ' democrat'
T = ' republican'

print(sekwencja(P, T))


P = ' 123456789'
T = ' 243517698'
print(sekwencja(P, T))

