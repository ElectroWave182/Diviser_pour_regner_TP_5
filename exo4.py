def quadruplets (debut, fin):

    liste = []
    for x0 in range (debut, fin):
        for x1 in range (debut, fin):
            for x2 in range (debut, fin):
                for x3 in range (debut, fin):

                    if x0 != x1 and x2 != x3 and x0 + x2 < x1:
                        liste.append ((x0, x1, x2, x3))

    return liste

assert len (quadruplets (0, 4)) == 30