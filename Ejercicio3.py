lista = [18, -3, 8, 7, 24, -5, 8, 11, -27, 22, 4, 7, 10, 6, 13]

def modificar(l):
    l = list(set(l))
    l.sort(reverse = True)

    l_temporal = []
    for i in l:
        if i%2 == 0:
            l_temporal.append(i)

    sumas = sum(l_temporal)
    l_temporal.insert(0, sumas)
    return l_temporal

nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )