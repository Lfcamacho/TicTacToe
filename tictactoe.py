import random


#tablero=["X","X"," "," "," "," "," "," ","O"]
tablero=[" "," "," "," "," "," "," "," "," "]
jugador=["O","X"]
esquinas=[0,2,6,8]
elegir=[6,0,8,2]
aristas=[1,3,5,7]



#metodo para imprimir el tablero

def imprimir(tablero):
    a=0
    print()
    for x in tablero:
        print(" "+x, end = " ")
        a=a+1
        if a%3!=0:
            print(end="|")
        elif a!=9:
            print("\n-----------")


#metodo para saber si ya se acabo

def yaseacabo(tablero):
    for x in tablero:
        if x==" ":
            return "seguir"


#metodo para saber si esta vacio

def vacio(tablero,posicion):
    if tablero[posicion]==" ":
        return "vacio"
    else:
        return "lleno"


#metodo para verificar victoria

def ganar(tablero):
    if (tablero[0]==tablero[1] and tablero[0]==tablero[2] and tablero[0]!=" ") or (tablero[3]==tablero[4] and tablero[3]==tablero[5] and tablero[3]!=" ") or (tablero[6]==tablero[7] and tablero[6]==tablero[8] and tablero[6]!=" "):
        return "gano"
    if (tablero[0]==tablero[3] and tablero[0]==tablero[6] and tablero[0]!=" ") or (tablero[1]==tablero[4] and tablero[1]==tablero[7] and tablero[1]!=" ") or (tablero[2]==tablero[5] and tablero[2]==tablero[8] and tablero[2]!=" "):
        return "gano"
    if (tablero[0]==tablero[4] and tablero[0]==tablero[8] and tablero[0]!=" ") or (tablero[6]==tablero[4] and tablero[6]==tablero[2] and tablero[6]!=" "):
        return "gano"


#Copia Tablero

def copiar(tablero):
    copia=[]
    for i in tablero:
        copia.append(i)
    return copia

# metodo movimiento computadora

def computadora(tablero,tipo,turno,anterior):
    i=0
    for x in tablero:
        copia=copiar(tablero)
        if copia[i]==" ":
            copia[i] = jugador[tipo]
            if ganar(copia)=="gano":
                return i
        i=i+1

    i=0
    if tipo==1:
        tipo=tipo-1
    else:
        tipo=tipo+1

    for x in tablero:
        copia=copiar(tablero)
        if copia[i]==" ":
            copia[i] = jugador[tipo]
            if ganar(copia)=="gano":
                return i
        i=i+1

    if turno==0 or turno==1 and tablero[4]!=" ":
        return random.choice(esquinas)

    if turno==1 and tablero[4]==" ":
        return 4

    dale=True

    if turno%2==0 and turno!=8:
        posicion=esquinas.index(anterior)
        if tablero[elegir[posicion]]==" ":
            return elegir[posicion]
        else:
            while dale:
                k=random.choice(esquinas)
                if tablero[k]==" ":
                    dale=False
                    return k
    else:
        dale=True
        while dale:
            if turno!=8:
                k = random.choice(aristas)
            else:
                k=random.randint(0,8)
            if tablero[k] == " ":
                dale = False
                return k


#aqui comienza codigo del juego

primero=random.randint(1,2)



modo=int(input("\n\nIngrese 1 si desea jugar contra la computadora\nIngrese 2 si desea jugar contra otra persona\n\n"))
w=0
turno=0
if modo==1:
    sim=input("Escribe si quieres ser X's o O's: ")
    if jugador[primero-1]==sim:
        print("Tu comienzas el juego")
        w=0
    else:
        print("Comienza la computadora")
        w=1

    print("\n\nEmpiezan las "+jugador[(primero-1)]+"'s")
    turno=0
    anterior=0

while yaseacabo(tablero)=="seguir" and ganar(tablero)!="gano":

    imprimir(tablero)

    #parte humana
    if modo==2 or (modo==1 and w%2==0):
        z=True
        posicion=int(input("\n\nIngrese la posicion: \n"))
        while z==True:
            if posicion<1 or posicion>9:
                posicion=int(input("Esta posicion es invalida, ingrese otra: \n"))
            elif vacio(tablero,posicion-1)=="lleno":
                posicion = int(input("\nEsa posicion ya esta ocupada, ingrese otra: \n"))
            else:
                z=False

        tablero[posicion-1] = jugador[(primero%2)-1]

    # parte computadora
    else:
        print("\ncomputadora")
        posicion=computadora(tablero,(primero%2)-1,turno,anterior)
        anterior=posicion
        tablero[posicion] = jugador[(primero%2)-1]

    primero=primero+1
    w=w+1
    turno=turno+1
imprimir(tablero)
if ganar(tablero)=="gano":
    print("\n\nSe acabo el juego, ganaron las "+jugador[primero%2]+"'s")
else:
    print("\n\nEs un empate")

