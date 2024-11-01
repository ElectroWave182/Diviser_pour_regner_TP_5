def bs_rec(LG,LT):
    if len(LT)==0:
        return True
    else:
        if len(LG)==0:
            return False
        else:
            return (abs(LG[0]-LT[0])<=2 or bs_rec(LG[1:],LT[:1])) and bs_rec(LG,LT[1:])


def selections_gardiens (LG, LT):

    