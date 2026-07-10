peliculas = {

    'P101': ['Luz de otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche de neon', 'accion', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Codigo zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje lunar', 'ciencia ficcion', 132, 'B', 'Ingles', False],

    }
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 25],
}
def validartextovacio(texto):
    if texto and texto.strip() != "":
        return True
    return False
def buscar_codigo(codigo):
    if not validartextovacio(codigo):
        return False
    if codigo.upper() in [k.upper() for k in peliculas.keys()]:
        return True
def validarclasificacion(clasificacion):
    if clasificacion in ['A', 'B', 'C']:
        return True
    return False
def validares_3d(es_3d):
    if es_3d.lower() in ['s', 'n']:
        return True
    return False
def validarprecio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False
def validarduracion(duracion):
    try:
        return int(duracion) > 0
    except ValueError:
        return False
def validarcupo(cupo):
    try:
        return int(cupo) >= 0
    except ValueError:
        return False
def cupos_genero(genero, peliculas, cartelera):
    total_genero = 0 
    genero_buscar = genero.strip().lower()
    for cod_pelicula, datos in peliculas.items():
        if datos[1].lower() == genero_buscar:
            if cod_pelicula in cartelera:
                total_genero = total_genero + cartelera[cod_pelicula][1]
    print(f"total de cupo es {total_genero}")
def busqueda_precio(p_min, p_max, peliculas, cartelera):
    res = []
    for cod_pelicula, datos_p in cartelera.items():
        precio = datos_p[0]
        cupo = datos_p[1]
        if p_min <= precio <= p_max and cupo > 0:
            if cod_pelicula in peliculas:
                titulo = peliculas[cod_pelicula][0]
                res.append(f"{titulo}--{cod_pelicula}")
    if res:
        res.sort()
        print(f"Las peliculas encontradas son: {res}")
    else:
        print(f"no hay peliculas en ese rango de precio")
def actualizar_precio(codigo, nuevo_precio, cartelera):
    cod_buscar = codigo.upper()
    for k in cartelera.keys():
        if k.upper() == cod_buscar:
            cartelera[k][0] = nuevo_precio
            return True
        return False
def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupo,  peliculas, cartelera):
    cod_pel = codigo.upper()
    if cod_pel in peliculas or cod_pel in cartelera:
        return False
    mp_bool = True if es_3d.lower() == 's' else False
    peliculas[cod_pel] = [titulo, genero, duracion, clasificacion, idioma, mp_bool]
    cartelera[cod_pel] = [int(precio), int(cupo)]
    return True

def eliminar_pelicula(codigo, peliculas, cartelera):
    codigo_maiu = [clave.upper() for clave in peliculas.keys()]
    if codigo.upper() in codigo_maiu:
        for clave in peliculas.keys():
            if clave.upper() == codigo.upper():
                peliculas.pop(clave)
                cartelera.pop(clave)
                return True
            return False

def leer_opcion():
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc >= 1 and opc <= 7:
            return opc
        else:
            raise ValueError
    except ValueError:
        print("Ingresar una opcion valida")
def menu_principal():
    while True:
        print("Menu principal")
        print("1.- Cupos por genero")
        print("2.- Busqueda de peliculas por rango de precio")
        print("3.- actualizar precio de la pelicula")
        print("4.- agregar pelicula")
        print("5.- eliminar pelicula")
        print("6.- salir")
        opc = leer_opcion()
        if opc == 1:
            gen = input("Ingresar el genero a buscar: ")
            cupos_genero(gen, peliculas, cartelera)
        elif opc == 2:
            while True:
                try:
                    p_min = int(input("ingresar el minimo a buscar: "))
                    p_max = int(input("ingresar el maximo a buscar: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                except ValueError:
                    print("ingresar un numero entero")
            busqueda_precio(p_min, p_max,peliculas, cartelera)
        elif opc == 3:
            while True:
                code = input("ingresar codigo de la pelicula a actualizar: ")
                while True:
                    nuevoprecio = input("ingresar nuevo precio: ")
                    if validarprecio(nuevoprecio):
                        nuevo_precio = int(nuevoprecio)
                        break
                    print("precio debe ser mayor ")
                if actualizar_precio(code, nuevo_precio, cartelera):
                    print("precio actualizado")
                    break
                else:
                    print("codigo no existe")
        elif opc == 4:
            cod = input("Ingrese el codigo de la pelicula a agregar: ")
            tit = input("Ingrese el titulo de la pelicula a agregar: ")
            gen = input("Ingrese el genero de la pelicula a agregar: ")
            dur = input("Ingrese la duracion de la pelicula a agregar: ")
            clas = input("Ingrese la clasificacion de la pelicula a agregar: ")
            idio = input("Ingrese el idioma de la pelicula a agregar: ")
            es = input("Ingresar si es 3d la pelicula a agregar(s o n): ")
            pre = input("Ingrese el precio de la pelicula a agregar: ")
            cupos = input("Ingrese los cupos de la pelicula a agregar: ")
            validaciones = [
                buscar_codigo(cod), validartextovacio(tit), validartextovacio(gen), validarduracion(dur), validarclasificacion(clas),validartextovacio(idio), validares_3d(es), validarprecio(pre), validarcupo(cupos)

            ]
            if False in validaciones:
                print("error al ingresar datos")
            else:
                if agregar_pelicula(cod,tit,gen,dur,clas,idio,es,pre,cupos,  peliculas, cartelera):
                    print("peliculas agregada")
                else:
                    print("el codigo existe")
        elif opc == 5:
            codigo = input("Ingrese el codigo de la pelicula a eliminar: ")
            eliminar_pelicula(codigo, peliculas, cartelera)
                
        
        elif opc == 6:
            print("Programa finalizado")
            break

menu_principal()


        




