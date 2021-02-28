def f21(x):
    if x[2] == 1964:
        if x[1] == 'raml':
            if x[4] == 1990:
                return 0
            elif x[4] == 1984:
                if x[3] == 'agda':
                    return 1
                elif x[3] == 'yang':
                    return 2
                elif x[3] == 'x10':
                    return 3
        elif x[1] == 'sqlpl':
            return 4
    elif x[2] == 1993:
        return 5
    elif x[2] == 1973:
        if x[3] == 'agda':
            if x[4] == 1990:
                if x[1] == 'raml':
                    return 6
                elif x[1] == 'sqlpl':
                    return 7
            elif x[4] == 1984:
                if x[0] == 'sql':
                    return 8
                elif x[0] == 'minid':
                    return 9
                elif x[0] == 'golo':
                    return 10
        elif x[3] == 'yang':
            return 11
        elif x[3] == 'x10':
            return 12


#print(f21(['minid', 'sqlpl', 1993, 'yang', 1990]))