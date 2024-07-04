from os import system
system("cls")

personas = []
cliente = []
comunas = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]

def Registro_pedido():
    while True:

        nombre = str(input("ingrese su nombre: "))
        if len(nombre) == 0 or (nombre.isnumeric()):
            print("ingrese su nombre")
        else:
            break

    while True:
        apellido = str(input("ingrese su apellido: "))
        if len(apellido) == 0 or (apellido.isnumeric()):
            print("ingrese su apellido")
        else:
            break

    while True:
        comuna = input("ingrese su comuna: ")
        
        while True:
            disp_6 = []
            disp_10 = []
            disp_20 = []
            cilindros_6 = input("cuantos cilindo de 6 litros desea comprar: ")
            cilindros_10 = input("cuantos cilindo de 10 litros desea comprar: ")
            cilindros_20 = input("cuantos cilindo de 20 litros desea comprar: ")
            cilindros_total= cilindros_6 + cilindros_10 + cilindros_20
            if cilindros_total == 0:
                print("tiene que ser almenos 1")
            else:
                break
            
            for cliente in personas:
                cliente = [nombre, apellido, comuna, disp_6, disp_10, disp_20, cilindros_total]
                personas.append(cliente)

def imprimir_rutas():
        archivo = open("pedidos.csv", "w")
        archivo.write(personas)
        archivo.readline("\n")

def listar_pedidos():
    for personas in comunas:
        personas ==[0]
        print(f''' Nombre         comuna         disp_6         disp_10          disp_20        cilindros
                   apellido
                {personas[0]}  {personas[2]}  {personas[3]}  {personas[4]}   {personas[5]}    {personas[6]}
                {personas[1]}
''')


while True:
    print('''
1. Registrar pedido
2. Listar los todos los pedidos
3. Imprimir hoja de ruta
4. Buscar un pedido por ID
5. Salir del programa
''')
    opcion = input("ingrese una opcion: ")
    match opcion:
        case "1":
            system("cls")
            Registro_pedido()
        case "2":
            system("cls")
            listar_pedidos()
        case "3":
            system("cls")
            imprimir_rutas()
        case "4":
            pass
        case "5":
            break