def ajoutI (tableau, ele):

    nouveau = []

    for liste in tableau:

        liste.append (ele)
        nouveau.append (liste)

    return nouveau


def p (E):

    if E == []:
        return [[]]
    
    else:
        return p (E[1 :]) + ajoutI (p (E[1 :]), E[0])


assert ajoutI([[],[1]],2)==[[2],[1,2]]
assert ajoutI([[],[1],[2,3]],2)==[[2],[1,2],[2,3,2]]
assert ajoutI([[]],2)==[[2]]

E = []
assert p (E) == [[]]
E = [1, 3, 0]
assert sorted (p (E)) == sorted ([[], [1], [3], [0], [1, 0], [1, 3], [3, 0], [1, 3, 0]])
