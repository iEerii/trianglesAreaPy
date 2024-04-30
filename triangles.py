title = "Welcome to the triangle calculator"
print(title +  "\n" + "-" * len(title) + "\n")

def triangleArea(baseT, height):
    return (baseT * height) / 2

def typeOfTriangleA(side1, side2, side3):

    trianglePerimeter = side1 + side2 + side3

    if side1 == side2 and side1 == side3:
        print("Tu triángulo es equilatero")
    elif side1 == side2 != side3:
        print("Tu triangulo es es escaleno")
    else: side1 != side2 and side2 != side3
    print("Tu triangulo es isóseles")

    return trianglePerimeter
