minha_lista = [0, 5, 10, 15, 20, 25, 30]


def filtro(numero):
    if numero > 10:
        return True
    return False


minha_lista_filtrada = filter(filtro, minha_lista)
print(minha_lista_filtrada)
