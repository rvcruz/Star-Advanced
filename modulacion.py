from os import path
from math import ceil
from random import randint
from parametros import PROB_BESTIA, POND_PUNT


class Jugador:
    def __init__(self):
        self.nombre = ' '
        self.puntaje = 0


def comprobar_tablero(tablero_visible, col, fil): #Retorna valor para comprobar si gana el juego
    fil = int(fil)
    col = int(col)
    counter = 0
    if fil == col:
        for y in range(col):
            for x in range(fil):
                if tablero_visible[x][y] == ' ':
                    counter += 1
        return counter
    else:
        for y in range(fil):
            for x in range(col):
                if tablero_visible[x][y] == ' ':
                    counter += 1
        return counter


def calculo_puntaje(tablero_visible, col, fil, cantidad_bestias): #Retorna calculo de puntaje
    fil = int(fil)
    col = int(col)
    counter = 0
    if fil == col:
        for y in range(col):
            for x in range(fil):
                if type(tablero_visible[y][x]) == int:
                    counter += 1
        return cantidad_bestias * counter * POND_PUNT
    else:
        for y in range(fil):
            for x in range(col):
                if type(tablero_visible[x][y]) == int:
                    counter += 1
        return cantidad_bestias * counter * POND_PUNT


def crear_tablero(fil, col, casilla): #Retorna tablero de dimensiones col,fil rellenado casillas
    tablero = []
    for i in range(int(fil)):
        fila = []
        for j in range(int(col)):
            fila.append(casilla)
        tablero.append(fila)
    return tablero


def escribir_partida(tablero_visible, tablero_oculto, fil, col, usuario): #Guarda partida txt
    casillas_abiertas = []
    casillas_bestias = []
    casillas_ocultas = []
    for i in range(int(col)):
        for j in range(int(fil)):
            if type(tablero_visible[i][j]) == int:
                mov_visible = []
                mov_visible.append(tablero_visible[i][j])
                mov_visible.append(i)
                mov_visible.append(j)
                casillas_abiertas.append(mov_visible)
    for i in range(int(col)):
        for j in range(int(fil)):
            mov_oculto = []
            mov_oculto.append(tablero_oculto[i][j])
            mov_oculto.append(i)
            mov_oculto.append(j)
            casillas_ocultas.append(mov_oculto)
    for i in range(int(col)):
        for j in range(int(fil)):
            if tablero_oculto[i][j] == 'N':
                bestia_loc = []
                bestia_loc.append(i)
                bestia_loc.append(j)
                casillas_bestias.append(bestia_loc)
    fileruta = path.join('partidas', f"{usuario}.txt")
    archivo = open(fileruta, 'w')
    archivo.write('VISIBLES')
    for i in casillas_abiertas:
        archivo.write(f";{i}")
    archivo.write('\n')
    archivo.write('BESTIAS')
    for i in casillas_bestias:
        archivo.write(f";{i}")
    archivo.write('\n')
    archivo.write('OCULTO')
    for i in casillas_ocultas:
        archivo.write(f";{i}")
    archivo.write('\n')
    archivo.write(f"Dimensiones;[{col},{fil}]")
    archivo.close()


def cargar_partida(usuario): # Carga los datos de una partida y retorna en lista data
    fileruta = path.join('partidas', f"{usuario}.txt")
    if path.isfile(fileruta) == True:
        archivo = open(fileruta, 'r')
        data = archivo.readlines()
        archivo.close()
        return data
    else:
        return False


def data_filter(data): #Retorna las listas de string a listas de listas.
    data_filter = []
    for linea in data:
        info = linea.strip().split(';')
        info.pop(0)
        data_filter.append(info)
    cantidad_bestias = 0 #Filtro cantidad bestias
    for elemento in data_filter[1]:
        cantidad_bestias += 1
    dim_filter = [] #Filtro dimensional
    for i in data_filter[3]:
        linea = i.split(",")
        for elemento in linea:
            formato = ''
            for caracter in elemento:
                if caracter.isdigit() == True:
                    formato += caracter
            dim_filter.append(int(formato))
    fil = dim_filter[0]
    col = dim_filter[1]
    beast_filter = [] #Filtro casilla de bestias
    for i in data_filter[1]:
        linea = i.split(",")
        auxiliar = []
        for elemento in linea:
            formato = ''
            for caracter in elemento:
                if caracter.isdigit() == True:
                    formato += caracter
            auxiliar.append(int(formato))
        beast_filter.append(auxiliar)
    tablero_oculto_filter = [] #Filtro casillas oculto
    for i in data_filter[2]:
        linea = i.split(",")
        auxiliar = []
        for elemento in linea:
            formato = ''
            for caracter in elemento:
                if caracter.isdigit() == True:
                    formato += caracter
                elif caracter == 'N':
                    formato += 'N'
            if formato == 'N':
                auxiliar.append(formato)
            else:
                auxiliar.append(int(formato))
        tablero_oculto_filter.append(auxiliar)
    tablero_visible_filter = [] #Filtro casillas visibles
    for i in data_filter[0]:
        linea = i.split(",")
        auxiliar = []
        for elemento in linea:
            formato = ''
            for caracter in elemento:
                if caracter.isdigit() == True:
                    formato += caracter
            auxiliar.append(int(formato))
        tablero_visible_filter.append(auxiliar)
    tablero_visible = crear_tablero(fil, col, ' ') #Crea tablero visible
    for coordenadas in tablero_visible_filter:
        x = coordenadas[1]
        y = coordenadas[2]
        tablero_visible[x][y] = coordenadas[0]
    tablero_oculto = crear_tablero(fil, col, 0) #Crea tablero oculto
    for coordenadas in tablero_oculto_filter:
        x = coordenadas[1]
        y = coordenadas[2]
        tablero_oculto[x][y] = coordenadas[0]
    return col, fil, cantidad_bestias, tablero_oculto, tablero_visible


def escribir_ranking(nombre, puntaje): #Escribe puntaje en archivo ranking luego de una partida
    fileruta = path.join('partidas', 'puntajes.txt')
    archivo = open(fileruta, 'a')
    archivo.write(f"{nombre};{puntaje}\n")
    archivo.close()


def por_puntaje(sub): #Criterio para ordenar listas segun puntaje
    return sub[1]


def cargar_ranking(): #Muestra por pantalla TOP 10 jugadores
    fileruta = path.join('partidas', 'puntajes.txt')
    if path.isfile(fileruta) == True:
        archivo = open(fileruta, 'r')
        data = archivo.readlines()
        archivo.close()
    else:
        print("No existe archivo, intente en otro momento")
        return
    print("\n\nRedoble de tambores para les mas pro de la liga\n\n")
    ranking = []
    for linea in data:
        info = linea.strip().split(';')
        ranking.append(info)
    for i in ranking:
        i[1] = int(i[1])
    top = sorted(ranking, key=por_puntaje, reverse= True)
    print("\t\tHonorables TOP 10")
    print("______________________________________________")
    if len(top) >= 10:
        for i in range(0, 10):
            print(f"{i + 1})\t\t{top[i][0]}:{top[i][1]}")
    else:
        for i in range(0, len(top)):
            print(f"{i + 1})\t\t{top[i][0]}:{top[i][1]}")


def numeros_validos(): #Retorna lista de numeros validos para comprobar dimensiones de tablero
    numeros_validos = [] 
    for i in range (3, 16):
        numeros_validos.append(str(i))
    return numeros_validos


def bonus(tablero_o, tablero_v, col, fil, y, x, valor):
    fil = int(fil)
    col = int(col)
    if fil == col:
        ceros = [(y, x)]
        while len(ceros) > 0:
            y, x = ceros.pop()
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (0 <= y + i <= fil-1) and (0 <= x + j <= col - 1):
                        if (tablero_v[y + i][x + j] == valor) and (tablero_o[y + i][x + j] == 0):
                            tablero_v[y + i][x + j] = 0
                            if (y + i, x + j) not in ceros:
                                ceros.append((y + i,x + j))
                        else:
                            tablero_v[y + i][x + j] = tablero_o[y + i][x + j]
        return tablero_v
    else:
        ceros = [(y, x)]
        while len(ceros) > 0:
            y, x = ceros.pop()
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (0 <= y + i <= col-1) and (0 <= x + j <= fil - 1):
                        if (tablero_v[y + i][x + j] == valor) and (tablero_o[y + i][x + j] == 0):
                            tablero_v[y + i][x + j] = 0
                            if (y + i, x + j) not in ceros:
                                ceros.append((y + i,x + j))
                        else:
                            tablero_v[y + i][x + j] = tablero_o[y + i][x + j]
        return tablero_v


def calcular_bestias(fil, col): #Retorna la cantidad de bestias para el tablero
    return ceil(int(col) * int(fil) * PROB_BESTIA)


def invocar_bestias(tablero_oculto, cantidad_bestias, fil, col): #Retorna tablero con las bestias
    num = 0
    while num < cantidad_bestias:
        y = randint(0, int(fil) - 1)
        x = randint(0, int(col) - 1)
        if tablero_oculto[y][x] != 'N':
            tablero_oculto[y][x] = 'N'
            num += 1
    return tablero_oculto


def valor_casilla(tablero_oculto, col, fil): #Retorna los valores de casillas cercanas a bestias
    fil = int(fil)
    col = int(col)
    for y in range(fil):
        for x in range(col):
            if tablero_oculto[y][x] == 'N':
                for i in [-1 , 0, 1]:
                    for j in [-1, 0, 1]:
                        if (0 <= y + i <= fil - 1) and (0 <= x + j <= col - 1):
                            if tablero_oculto[y + i][x + j] != 'N':
                                tablero_oculto[y + i][x + j] += 1
    return tablero_oculto
                        
def dicti(fil, col): #Retorna diccionario de valores admitidos en el descubrimiento de casillas
    col = int(col)
    fil = int(fil)
    dic = {}
    if col == 3:
        string = "ABC"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 4:
        string = "ABCD"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 5:
        string = "ABCDE"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 6:
        string = "ABCDEF"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 7:
        string = "ABCDEFG"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 8:
        string = "ABCDEFGH"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 9:
        string = "ABCDEFGHI"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 10:
        string = "ABCDEFGHIJ"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 11:
        string = "ABCDEFGHIJK"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 12:
        string = "ABCDEFGHIJKL"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 13:
        string = "ABCDEFGHIJKLM"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 14:
        string = "ABCDEFGHIJKLMN"
        for i in range(len(string)):
            for j in range(fil):
                dic[string[i] + str(j)] = [i, j]
        return dic
    elif col == 15:
        string = "ABCDEFGHIJKLMNO"
        for i in range(len(string)):
            for j in range(0, fil):
                dic[string[i] + str(j)] = [i, j]
        return dic