import math


print("El Movimiento Rectilíneo Uniformemente Acelerado (MRUA), es aquel donde un objeto se desplaza en línea recta con una aceleración "
      "constante y diferente de cero. La velocidad cambia uniformemente a un ritmo constante en cada intervalo de tiempo, como en la caída libre.")


print("MRUA, \nTrabajaremos en el Sistema Internacional (SI), "
      "\nVelocidad → m/s, \nAceleración → m/s², \nTiempo → s, \nDistancia → m")


print("\n¿Qué deseas calcular?")
print("1. Velocidad final (Vf² = Vo² + 2a·x)")
print("2. Velocidad final (Vf = Vo + a·t)")
print("3. Aceleración (a = (Vf - Vo) / t)")
print("4. Distancia (x = ((Vf + Vo) / 2) · t)")
print("5. Distancia (x = Vo·t + (a·t²)/2)")


opcion = input("Seleccione una opción: ")


match opcion:


    case "1":
        Vo = float(input("Ingrese velocidad inicial (Vo) en m/s: "))
        a = float(input("Ingrese aceleración (a) en m/s²: "))
        x = float(input("Ingrese distancia (x) en m: "))
       
        resultado = Vo**2 + 2*a*x
       
        if resultado >= 0:
            Vf = math.sqrt(resultado)
            print("Velocidad final:", Vf, "m/s")
        else:
            print("Error: no se puede calcular raíz de número negativo")


    case "2":
        Vo = float(input("Ingrese velocidad inicial (Vo) en m/s: "))
        a = float(input("Ingrese aceleración (a) en m/s²: "))
        t = float(input("Ingrese tiempo (t) en s: "))
       
        Vf = Vo + a*t
        print("Velocidad final:", Vf, "m/s")


    case "3":
        Vf = float(input("Ingrese velocidad final (Vf) en m/s: "))
        Vo = float(input("Ingrese velocidad inicial (Vo) en m/s: "))
        t = float(input("Ingrese tiempo (t) en s: "))
       
        if t != 0:
            a = (Vf - Vo) / t
            print("Aceleración:", a, "m/s²")
        else:
            print("Error: el tiempo no puede ser 0")


    case "4":
        Vf = float(input("Ingrese velocidad final (Vf) en m/s: "))
        Vo = float(input("Ingrese velocidad inicial (Vo) en m/s: "))
        t = float(input("Ingrese tiempo (t) en s: "))
       
        x = ((Vf + Vo) / 2) * t
        print("Distancia:", x, "m")


    case "5":
        Vo = float(input("Ingrese velocidad inicial (Vo) en m/s: "))
        a = float(input("Ingrese aceleración (a) en m/s²: "))
        t = float(input("Ingrese tiempo (t) en s: "))
       
        x = Vo*t + (a*(t**2))/2
        print("Distancia:", x, "m")


    case _:
        print("Opción inválida")
