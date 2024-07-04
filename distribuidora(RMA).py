import csv
#Lista para almacenar los pedidos 
pedidos=[]
#Lista de sectores disponibles
sectores=["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]

def menu_principal():
    while True:
        print("Menu")
        print("1) Registrar pedido")
        print("2) Listar pedidos")
        print("3) Imprimir Hoja de ruta")
        print("4) Buscar pedido por ID")
        print("5) Salir")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            registrar_pedido()
        elif opcion==2:
            listar_pedidos()
        elif opcion==3:
            imprimir_hoja()
        elif opcion==4:
            buscar_pedido()
        elif opcion==5:
            print("Saliendo de la aplicacion")
            break
        else:
            print("Opcion invalida")

def registrar_pedido():
    print("Registrar pedido")
    #Ingresar y validar datos del cliente
    nombre=input("Nombre y apellido del cliente: ").strip()
    direccion=input("Direccion del cliente: ").strip()
    comuna=input("Comuna del cliente: ").strip()
    #Ingresar cantidad de dispensadores
    disp_6=int(input("Cantidad de dispensadores de 6L: "))
    disp_10=int(input("Cantidad de dispensadores de 10L: "))
    disp_20=int(input("Cantidad de dispensadores de 20L: "))
    
    if disp_6 + disp_10 + disp_20>0:
        #Creacion de diccionario con los detalles del pedido
        pedido={
            'ID':len(pedidos)+1,
            'Cliente': nombre,
            'Direccion': direccion,
            'Comuna': comuna,
            'Disp.6lts': disp_6,
            'Disp.10lts': disp_10,
            'Disp.20lts': disp_20
        }
        pedidos.append(pedido)
        print("Pedido correctamente registrado")
    else:
        print("Cantidad total de dispensadores debe ser mayor a 0. Ingrese el pedido nuevamente")

def listar_pedidos():
    print("Lista de pedidos")
    if not pedidos:
        print("No hay pedidos registrados")
    else:
        for pedido in pedidos:
            print(f"{pedido['ID']}|{pedido['Cliente']}|{pedido['Direccion']}|{pedido['Comuna']}|{pedido['Disp.6lts']}|{pedido['Disp.10lts']}|{pedido['Disp.20lts']}")

def imprimir_hoja():
    print("Sectores disponibles")
    for i, sector in enumerate(sectores):
        print(f"{i+1}.{sector}")
    opcion=int(input("Seleccione el sector: "))

    if 1<=opcion<=len(sectores):
        sector_elegido=sectores[opcion -1]
        nombre_archivo=f"Hoja_ruta_{sector_elegido}.csv" #Creacion del archivo con su respectivo nombre
        #Creacion csv
        with open(nombre_archivo, 'w',newline='') as archivo_csv:
            writer=csv.writer(archivo_csv)
            writer.writerow(["ID","Cliente","Direccion","Comuna","Disp.6lts","Disp.10lts","Disp.20lts"])
            for pedido in pedidos:
                if pedido['Comuna']==sector_elegido:
                    writer.writerow([pedido['ID']],[pedido['Cliente']],[pedido['Direccion']],[pedido['Comuna']],[pedido['Disp.6lts']],[pedido['Disp.10lts']],[pedido['Disp.20lts']])
        print(f"Hoja de ruta para {sector_elegido} generada exitosamente")

def buscar_pedido():
    print("Buscar pedido por ID")
    id_pedido=int(input("Ingrese ID del pedido: "))
    encontrado=False
    for pedido in pedidos:
        if pedido['ID']==id_pedido:
            #Detalles del pedido
            print(f"ID:{pedido['ID']}|Cliente:{pedido['Cliente']}|Direccion:{pedido['Direccion']}|Comuna:{pedido['Comuna']}|Disp.6lts:{pedido['Disp.6lts']}|Disp.10lts:{pedido['Disp.10lts']}|Disp.20lts:{pedido['Disp.20lts']}")
            encontrado=True
            break
        if not encontrado:
            print("Pedido no encontrado")

#Iniciar programa 
if __name__=="__main__":
    menu_principal()