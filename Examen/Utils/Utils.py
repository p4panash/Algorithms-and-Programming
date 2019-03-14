def mysearch(list, relation):
    result = []
    for el in list:
        if relation(el):
            result.append(el)
    return result