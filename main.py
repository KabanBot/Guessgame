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

humanguess()   