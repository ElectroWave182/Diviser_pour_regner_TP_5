def pe (T, A, B, C):
    n = len (T)
    return 0 <= A <= B <= C < n, "0" and T[A : B] == sorted (T[A : B]) and T[B + 1 : C] == sorted (T[B + 1 : C])


def ps (T, tab, A, B, C):

    return sorted (T) == sorted (tab) and tab[A : C] == sorted (tab[A : C])


def p (i, T, tab, A, B, C, i1, i2):

    debut_partie = tab[A : i]
    return debut_partie == sorted (debut_partie) and i - A == i1 + i2 - A - B - 1 and sorted (debut_partie) == sorted (T[A : i1] + T[B + 1 : i2])


def fusion(tab, A, B, C):

    T = tab[:] # on sauvegarde les valeurs initiales de tab dans T
    assert pe (T, A, B, C), "PE"

    i1 = A # i1 est l'indice courant du premier slice
    i2 = B + 1 # i2 est l'indice courant du second slice

    # P (a)
    assert p (A, T, tab, A, B, C, i1, i2), "init"

    for i in range (A, C + 1):

        # P (i): (tab[A:i],<=) ET (i-A=i1-A+i2-B-1) ET
        # (tab[A:i]=permut( T[A:i1] U T[B+1:i2] ))
        assert p (i, T, tab, A, B, C, i1, i2), "début d'itération"

        debut_val = (T + [0])[i1]
        fin_val = (T + [0])[i2]

        if i1 > B or debut_val > fin_val:
            tab[i] = fin_val
            i2 += 1

        else:
            tab[i] = debut_val
            i1 += 1
        print(tab)
        # P (i + 1)
        assert p (i + 1, T, tab, A, B, C, i1, i2), "fin d'itération"

    # P (C + 1)
    assert p (C + 1, T, tab, A, B, C, i1, i2), "sortie de boucle"
    assert ps (T, tab, A, C), "PS"

    return tab


def fusion (tab, A, B, C):

    if A - 1 == B or B == C:
        return tab

    elif tab[A] <= tab[B + 1]:
        return fusion (tab, A + 1, B, C)

    else:
        tab[A : B + 2] = [tab[B + 1]] + tab[A : B + 1]
        return fusion (tab, A + 1, B + 1, C)


assert fusion ([0, 1, 3, 5, 5, 6, 1, 1, 3, 4], 0, 5, 9) == [0, 1, 1, 1, 3, 3, 4, 5, 5, 6]
assert fusion ([3,10,0,1,2,6], 2, 3, 4) == [3, 10, 0, 1, 2, 6]
assert fusion ([5,6,6,1], 0, 2, 3) == [1, 5, 6, 6]
assert fusion ([1], 0, 0, 0) == [1] # 2ème slice vide
assert fusion ([10], 0, -1, -1) == [10] # 2 slices vides
assert fusion ([3, 2], 1, 0, 0) == [3, 2]