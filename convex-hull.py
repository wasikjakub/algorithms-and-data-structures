# PRACA SKONCZONA

def jarvis(tab):
    mini = 0
    for i in range(1, len(tab)):
        if tab[i][0] < tab[mini][0]:
            mini = i
        if tab[i][0] == tab[mini][0]:
            if tab[i][1] > tab[mini][1]:
                mini = i
    p = mini
    ans = []
    while True:
        ans.append(p)
        q = (p + 1) % len(tab)
        for i in range(len(tab)):
            value = (tab[i][1] - tab[p][1]) * (tab[q][0] - tab[i][0]) - \
                    (tab[i][0] - tab[p][0]) * (tab[q][1] - tab[i][1])
            if value < 0:
                q = i
        p = q
        if p == mini:
            break
    temp = []
    for i in ans:
        temp.append((tab[i][0], tab[i][1]))
    return temp


tab = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
tab2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
tab3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

print(jarvis(tab3))
