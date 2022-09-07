from modulacion import calculo_puntaje, data_filter, numeros_validos, crear_tablero, \
    calcular_bestias, invocar_bestias, dicti, valor_casilla, bonus, comprobar_tablero, \
        cargar_partida, escribir_partida, cargar_ranking, escribir_ranking, Jugador
from tablero import print_tablero


class StarAdvanced:
    def __init__(self, llave):
        self.jugador = Jugador()
        self.llave = llave 
        self.comenzar_juego(self.llave) #(2) Para comenzar el juego


    def menu_de_inicio(self): #(5) Muestra menu de inicio
        while self.llave == True:
            print('Seleccione una opcion:')
            print('[1] Crear partida\n[2] Cargar partida\n[3] Ver ranking\n[4] Salir')
            accion = input("\nIndique su opcion (1, 2, 3 o 4): ")
            if (accion.isdigit() == True) and (accion in '1234'):
                if accion == '1': #Crea Partida
                    self.jugador.nombre = input("\nIngrese su nombre de usuario: ")
                    validos = numeros_validos() #Determina cuales son las dimensiones validas
                    k = True 
                    while k == True:
                        fil = input("Ingrese cantidad de filas entre [3, 15]: ")
                        if (fil.isdigit() == True) and (fil in validos):
                            while k == True:
                                col = input("Ingrese cantidad de columnas entre [3, 15]: ")
                                if (col.isdigit() == True) and (col in validos):
                                    k = False
                                    option = dicti(fil, col) #Diccionario de acciones validas
                                    cantidad_bestias = calcular_bestias(fil, col)
                                    tablero_visible = crear_tablero(fil, col, ' ')
                                    tablero_oculto = crear_tablero(fil, col, 0)
                                    tablero_oculto = invocar_bestias(tablero_oculto, \
                                        cantidad_bestias, fil, col)
                                    tablero_oculto = valor_casilla(tablero_oculto, col, fil)
                                    self.menu_de_juego(tablero_visible, tablero_oculto, \
                                        option, fil, col, cantidad_bestias) 
                                    #(6) Inicia juego
                                else:
                                    print("\nOpcion invalida, por favor intente nuevamente\n")
                        else:
                            print("\nOpcion invalida, por favor intente nuevamente\n")
                if accion == '2': #Carga partida segun exista o no 
                    usuario = input("Ingrese nombre de jugador de partida guardada: ")
                    if cargar_partida(usuario) == False:
                        print("No existe partida, intente nuevamente")
                    else:
                        self.jugador.nombre = usuario
                        data = cargar_partida(self.jugador.nombre)
                        fil, col, cantidad_bestias,\
                            tablero_oculto, tablero_visible = data_filter(data)
                        option = dicti(col, fil)
                        self.menu_de_juego(tablero_visible, tablero_oculto, \
                            option, col, fil, cantidad_bestias)
                        #Se cargaron datos e inicia partida
                if accion == '3': #Muestra Ranking
                    cargar_ranking()
                    self.menu_de_inicio()
                if accion == '4': #Salir del juego
                    self.llave = False
            else:
                print("\nOpcion invalida, por favor intente nuevamente\n")   


    def menu_de_juego(self, tablero_visible, tablero_oculto, \
        option, col, fil, cantidad_bestias):
        d = comprobar_tablero(tablero_visible, col, fil)
        if d == cantidad_bestias: #Comprueba si gana el juego
            print('Ganaste')
            print_tablero(tablero_oculto)
            self.jugador.puntaje = calculo_puntaje(tablero_visible, col, fil, cantidad_bestias)
            print("USUARIO: ", self.jugador.nombre)
            print("PUNTAJE: ", self.jugador.puntaje)
            escribir_ranking(self.jugador.nombre, self.jugador.puntaje)
            self.menu_de_inicio()
        print('\n\tEstado del tablero\n') #Imprime estado de tablero e inicia partida normal
        print_tablero(tablero_visible)
        print('\nIngrese una opcion:\n[1] Descubrir sector\n[2] Guardar partida\n[3] Salir')
        accion = input("\nIndique su opcion (1, 2 o 3): ")
        if (accion.isdigit() == True) and (accion in '123'):
            if accion == '1':
                k = True
                while k == True: #Ciclo para comprobar si eleccion es valida en diccionario option
                    turn = input('Indique el sector a descubrir (Considere mayusculas): ')
                    if (turn in option):
                        k=False
                        x = option[turn][0]
                        y = option[turn][1]
                        if tablero_oculto[y][x] == 0: #Abre casilla y aplica bonus
                            tablero_visible[y][x] = 0
                            tablero_visible = bonus(tablero_oculto, tablero_visible, \
                                col, fil, y, x, ' ')
                            self.menu_de_juego(tablero_visible, tablero_oculto,\
                                option, col, fil, cantidad_bestias)
                        elif tablero_oculto[y][x] == 'N': #Si hay bestia, pierdes
                            tablero_visible[y][x] = 'N'
                            print_tablero(tablero_visible)
                            print("Perdiste")
                            print_tablero(tablero_oculto)
                            self.jugador.puntaje = calculo_puntaje(tablero_visible, col, fil, \
                                cantidad_bestias)
                            print("USUARIO: ", self.jugador.nombre)
                            print("PUNTAJE: ", self.jugador.puntaje)
                            escribir_ranking(self.jugador.nombre, self.jugador.puntaje)
                            self.menu_de_inicio()
                        elif tablero_oculto[y][x] != 0: #Abre casilla sin aplicar bonus
                            tablero_visible[y][x] = tablero_oculto[y][x]
                            self.menu_de_juego(tablero_visible, tablero_oculto, \
                                option, col, fil, cantidad_bestias)
                    else:
                        print("Opcion invalida, intente nuevamente")              
            elif accion == '2':
                print('\nGuardando Partida\n')
                usuario = self.jugador.nombre
                escribir_partida(tablero_visible, tablero_oculto, fil, col, usuario)
                print('\nPartida Guardada\n')
                self.menu_de_inicio()
            elif accion == '3':
                k = True #llave para analizar si es valido o no la opcion elegida
                while k == True:
                    print('Seleccione una opcion:\n[1] Salir con guardar\n[2] Salir sin guardar')
                    accion = input("\nIndique su opcion (1, 2 o 3): ")
                    if (accion.isdigit() == True) and (accion in '12'):
                        k = False #si es correcto, cierra ciclo while
                        if accion == '1':
                            print('\nGuardando Partida\n')
                            usuario = self.jugador.nombre
                            escribir_partida(tablero_visible, tablero_oculto, fil, col, usuario)
                            print('\nPartida Guardada\n')
                            self.menu_de_inicio()
                        elif accion == '2':
                            print('\n¡Nos vemos!\n')
                            self.menu_de_inicio()
                    else:
                        print("\nOpcion invalida, por favor intente nuevamente\n")
        else:
            print("\nOpcion invalida, por favor intente nuevamente\n")
            self.menu_de_juego(tablero_visible, tablero_oculto, \
                option, col, fil, cantidad_bestias)


    def comenzar_juego(self, llave): #(3) Comienza el juego al llamar la funcion.
        while self.llave == True:
            print('Bienvenido a Star Advanced\n')
            self.llave = self.menu_de_inicio()  #(4) Envia a menu de inicio

#(1) Se inicia la clase para comenzar el juego
star_advanced = StarAdvanced(True)
