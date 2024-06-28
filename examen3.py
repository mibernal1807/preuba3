import csv

prestamo:[]

def menu():
    print("bienvenido aqui te prestaremos un notebook ara la clase")
    print("1.Prestar notebooks.")
    print("2.Devolver notebooks.")
    print("3.Modificar préstamo de notebooks (por falla o batería agotada).")
    print("4.Imprimir la lista de notebooks prestados.")
    print("5.Terminar clase.")
    return
    
def registro():
    print("ingrese los datos para el prestamo")
    rut=input("ingrese su rut\n")
    nombre=input("igrese su nombre\n")
    documento=input("tipo de documento entregado( carnet o pase escolar )\n")
    notebook=input(("ingrese numero de notebook\n"))
    print("desea registrar los datos del prestamo\n")
    print(f"rut:{rut} nombre:{nombre} documento:{documento} notebook:{notebook}")

    prestamo:{
            'rut':rut,
            'nombre':nombre,
            'documento':documento,
            'notebook':notebook}
    prestamo.append(prestamo)

    opcion=input("desea registrarlo 1 si o 2 no\n")

    if opcion=="1":
        print("prestamo registrado")
        with open("Pablo Saldaña BIY1101-008D.csv","w") as file:
            for prestamo in prestamo:
                file.write(f"{rut[rut],nombre[nombre],documento[documento],notebook[notebook]}")
            prestamo.append(prestamo)    
    else:
        print("no se registro el prestamo")    
           
    
def Devolver():
    with open("Pablo Saldaña BIY1101-008D.csv","w") as file:
        for prestamo in prestamo:
            file.write(f"{rut:[rut],nombre:[nombre],documento:[documento],notebook:[notebook]}")
        prestamo.delete(prestamo)


def imprimir():
    for idx,prestamo in enumerate(prestamo,start=20):
     print(f"{idx}.{rut:[rut],nombre:[nombre],documen:[documento],notebook:[notebook]}")   



def main():
    while True:
        menu()
        opcion=input("ingrese una opcion\n")

        if opcion=="1":
            registro()
        if opcion=="2":
            devolver()
        if opcion=="3":    
            print()
        if opcion=="4": 
            inprimir()
        if opcion=="5":
            print("se termino la clase entreguen todo y pueden retirarse")     
            break
        else:
            print()
        
main()
