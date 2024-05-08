def desayuno (total):
    while True:
        print("""
 |=============================|
 |          Desayuno           |
 |=============================|
 | A |Café             |S/4.50 |
 | B |Chocolate        |S/5.00 |
 | C |Jugo de Fresa    |S/9.00 |
 | D |Jugo de Papaya   |S/8.00 |
 | E |Pan con Pollo    |S/7.00 |
 | F |Pan con Jamón    |S/7.50 |
 | G |Pan con Tortilla |S/5.00 |
 | J |========= SALIR =========|
 |=============================|
 """)
        op=input("Elige lo de tu preferencia: ").upper()
        if op=="A":
            print("Café")
            total+=4.50
        elif op=="B":
            print("Chocolate")
            total+=5.00
        elif op=="C":
            print("Jugo de Fresa")
            total+=9.00
        elif op=="D":
            print("Jugo de Papaya")
            total+=8.00
        elif op=="E":
            print("Pan con Pollo")
            total+=7.00
        elif op=="F":
            print("Pan con Jamón")
            total+=7.50
        elif op=="G":
            print("Pan con Tortilla")
            total+=5.00
        elif op=="J":
            break
        else:
            print("Opción no Válida")
    return total
print()
def almuerzo(total):
    while True:
        print("""
 |=============================|
 |          Almuerzo           |
 |=============================|
 | A |Tallarin        |S/11.00 |
 | B |Cubana          |S/9.00  |
 | C |Seco de Carne   |S/12.00 |
 | D |Ají de Gallina  |S/10.00 |
 | E |Pollo al Horno  |S/11.00 |
 | F |Menestrón       |S/10.00 |
 | G |Ensalada Rusa   |S/11.00 |
 | J |======== SALIR ==========|
 |=============================|
 """)
        op=input("Elige lo de tu preferencia: ").upper()
        if op=="A":
            print("Tallarin")
            total+=11.00
        elif op=="B":
            print("Cubana")
            total+=9.00
        elif op=="C":
            print("Seco de Carne")
            total+=12.00
        elif op=="D":
            print("Aji de Gallina")
            total+=10.00
        elif op=="E":
            print("Pollo al Horno")
            total+=11.00
        elif op=="F":
            print("Menestrón")
            total+=10.00
        elif op=="G":
                print("Ensalada Rusa")
                total+=11.00
        elif op=="J":
                break
        else:
            print("Opción no Válida")
    return total
print()
def cena(total):
    while True:
        print("""
 |=============================|
 |            Cena             |
 |=============================|
 | A |Pizza Americana |S/7.00  |
 | B |Té              |S/4.00  |
 | C |Pan con huevo   |S/5.00  |
 | D |Caldo de gallina|S/12.00 |
 | E |Café con leche  |S/6.00  |
 | F |Yogurt          |S/7.00  |
 | G |======== SALIR ==========|
 |=============================|
 """)
        op=input("Elige lo de tu preferencia: ").upper()
        if op=="A":
            print("Pizza Americana")
            total+=7.00
        elif op=="B":
            print("Té")
            total+=4.00
        elif op=="C":
            print("Pan con Huevo")
            total+=5.00
        elif op=="D":
            print("Caldo de Gallina")
            total+=12.00
        elif op=="E":
            print("Café con Leche")
            total+=6.00
        elif op=="F":
            print("Yogurt")
            total+=7.00
        elif op=="G":
            break
        else:
            print("Opción no Válida")
    return total
#--------------------------------------------
total=0
desayunoo=0
almuerzoo=0
cenaa=0
IGV=0.18
while True:
    print("""
 |=============================|
 |       RESTAURANTE S.A       |
 |=============================|
 | A |Desayuno                 |
 | B |Almuerzo                 |
 | C |Cena                     |
 | D |==========SALIR==========|
 |=============================|
      """)
    opw=input("Elige la opción de tu agrado: ").upper()
    if opw=="A":
        desayunoo=desayuno(total)
    elif opw=="B":
        almuerzoo=almuerzo(total)
    elif opw=="C":
        cenaa=cena(total)
    elif opw=="D":
        break
    else:
        print("Opción no Válida")
print("|================================|")
print("|        BOLETA DE VENTAS        |")
print("|================================|")
print(f"|PRECIO DEL DESAYUNO   S/. {desayunoo:.2f}".rjust(3),"|")
print(f"|PRECIO DEL ALMUERZO   S/. {almuerzoo:.2f}".rjust(3),"|")
print(f"|PRECIO DE LA CENA     S/. {cenaa:.2f}".rjust(3),"|")

neto= desayunoo + almuerzoo + cenaa
x=(neto)*IGV
y=neto+x
print("|================================|")
print("|SubTotal      : S/.","{0:.2f}".format(neto).rjust(11),"|")
print("|IGV           : S/.","{0:.2f}".format(x).rjust(11),"|")
print("|Total a Pagar : S/.","{0:.2f}".format(y).rjust(11),"|")
print("|                                |")
print("|      GRACIAS POR TU COMPRA     |")
print("|================================|")
