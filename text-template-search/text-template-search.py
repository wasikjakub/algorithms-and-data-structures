import time


def naiwne(S, W):
    how_many = 0
    for i in range(len(S)):
        m = 0
        while m < len(W) and S[i + m] == W[m]:
            m += 1
        if m > 0 and m == len(W):
            how_many += 1
    return how_many, i


with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()
S = ' '.join(text).lower()
wzorzec = 'time.'

t_start = time.perf_counter()
c, d = naiwne(S, wzorzec)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(f'({c}' + '; ' + f'{d})')


def hash_(word):
    hw = 0
    for i in range(len(word)):
        hw = (hw * 256 + ord(word[i])) % 101
    return hw


def rabin_karp(S, W):
    how_many = 0
    how_many_comp = 0
    how_many_coll = 0
    M = len(S)
    N = len(W)
    hW = hash_(W)
    for m in range(1, M - N + 2):
        hS = hash_(S[m: m + N])
        how_many_comp += 1
        if hS == hW:
            how_many_coll += 1
            if S[m:m + N] == W:
                how_many += 1
    return how_many, how_many_comp, how_many_coll


t_start = time.perf_counter()
c, d, e = rabin_karp(S, wzorzec)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(f'({c}; ' + f'{d}; ' + f'{e})')


def kmp_table(W):
    pos = 1
    cnd = 0
    T = [0]*(len(W)+1)
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T


def KMP(S, W):
    m = 0
    i = 0
    T = kmp_table(W)
    nP = 0
    how_many = 0
    how_many_comp = 0
    while m < len(S):
        how_many_comp += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                how_many += 1
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return how_many, how_many_comp


t_start = time.perf_counter()
c, d = KMP(S, wzorzec)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(f'({c}' + '; ' + f'{d})')
