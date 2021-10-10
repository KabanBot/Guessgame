import random
def humanguess():
    number=random.randrange(0,10)
    print(number)
    respuesta=int(input("Dame un numero del 0 al 10:  "))
    while number != respuesta:
        respuesta=int(input("Dame un numero del 0 al 10:  "))
        if number==respuesta:
            print(f"Ganaste el numero era {number}")
        elif respuesta>number:
            print(f"Te pasaste  {respuesta}")
        else:
            print(f"Aun te falta  {respuesta}")

def computerGuess():
    bandera=False
    minimo=0
    maximo=1000
    number=random.randrange(minimo,maximo)
    while(bandera ==False):
        print(number)
        respuesta=input("Este es tu numero si , no: ").lower()

        if respuesta=="no":
            opc=input("Es mayor o menor: ").lower()
        
            if opc=="menor":
                maximo=number
                nuenum=random.randrange(minimo,maximo)
                number=nuenum
            else:
                minimo=number
                nuenum=random.randrange(minimo,maximo)
                number=nuenum
        else: 
            bandera=True
            print("Numero")
         
computerGuess()