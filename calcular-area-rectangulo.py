def calcular_area (ancho, alto):
    area = ancho * alto
    return area
ancho = float(input("Ingrese el ancho del rectangulo: "))
alto = float(input("Ingerese el alto del rectangulo: "))

resultado = calcular_area (ancho, alto)
print ("El areal del rectangulo es: ", resultado)
