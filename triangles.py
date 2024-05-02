title = "Calcula el área y perímetro de un triángulo"
print(title +  "\n" + "-" * len(title) + "\n")

def triangleArea(baseT, height):
    return (baseT * height) / 2

def typeOfTriangle(side1, side2, side3):
    trianglePerimeter = side1 + side2 + side3

    if side1 == side2 and side1 == side3:
        print("Tu triángulo es equilatero")
    elif side1 == side2 != side3:
        print("Tu triángulo es escaleno")
    else:
        print("Tu triángulo es isóseles")

    return trianglePerimeter

while True:
    try:
        menu = int(input("""Selecciona la opcion
                        1) Area del triangulo
                        2) Perimetro del triangulo
                        Opcion: """))

        if menu == 1:
            baseT = int(input("Ingresa la base del triángulo: "))
            height = int(input("Ingresa la altura del triángulo: "))
            print(f"La base del triángulo es de {triangleArea(baseT, height)}")
        elif menu == 2:
            side1 = int(input("Ingrese la medida del primer lado: "))
            side2 = int(input("Ingrese la medida del segundo lado: "))
            side3 = int(input("Ingrese la medida del tercer lado: "))
            print(f" y su perímetro es de {typeOfTriangle(side1, side2, side3)} cm")
        else:
            print("Solo se permiten 1 y 2 como opciones")
    
    except ValueError:
        print("Por favor, ingresa el número válido para la opción")
    