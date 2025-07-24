def Print_Clients(CLIENTS):
    cont=0
    for code, dat in CLIENTS.items() :
        cont=cont+1
        print(f"{cont}) Cliente: {code}")
        print(f"Lugares visitados:")
        for a in dat["Lugares visitados"].keys():
            print(a)
def Count_Visits(CLIENTS,clientcont):

    dat=CLIENTS[clientcont]
    for a in dat["Lugares visitados"].keys():
        cont=cont+1
    return cont,Count_Visits(CLIENTS,clientcont-1)

CLIENTS={}
CLIENT_CONT=int(input("Ingrese el numero de clientes a registrar:"))
if CLIENT_CONT >= 1:
    for i in range(CLIENT_CONT):
        print(f"{i+1})")
        CodClient = input("Ingrese el codigo del cliente: ")
        CLIENTS[CodClient] = {}

        CLIENTS[CodClient]["nombre"] = input("Ingrese el nombre: ")
        CLIENTS[CodClient]["Lugares visitados"] = {}
        imput="1"
        contVisit=0
        print("Ingrese los lugares visitados (ingrese 0 para detener)"
              "(Min 1 - Max 5 lugares)")
        while not imput=="0" and ( not imput=="0" or not contVisit==5) and contVisit < 5:
            imput=input()
            contVisit=contVisit+1
            if(contVisit==1 and imput=="0"):
                print("Debe de tener como minimo 1 lugar visitado, intente denuevo")
                contVisit=contVisit-1
                imput="1"
            elif(imput!="0"):
                CLIENTS[CodClient]["Lugares visitados"][imput]=imput


elif CLIENT_CONT < 1:
    print("Valor Invalido: Debe ser como minimo 1")

Print_Clients(CLIENTS)
VisitTot=Count_Visits(CLIENTS,CLIENT_CONT)