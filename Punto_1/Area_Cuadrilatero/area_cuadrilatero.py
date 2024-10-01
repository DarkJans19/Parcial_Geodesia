import math

def calcular_semi_perimetro(valor_1, valor_2, diagonal) -> float:
    perimetro = valor_1 + valor_2 + diagonal
    return perimetro/2

# formula de Heron 
def formula_heron(valor_1, valor_2, diagonal) -> float:
    s = calcular_semi_perimetro(valor_1, valor_2, diagonal)
    area = math.sqrt( s * (s - valor_1) * (s - valor_2) * (s - diagonal)) 
    return area

def area_cuadrilatero(a, b, c, d, diagonal):
    area_1 = formula_heron(a, b, diagonal)
    area_2 = formula_heron(c, d, diagonal)
    return area_1 + area_2

# Solicitamos los valores
a = float(input("Ingrese el valor de la recta a: "))
b = float(input("Ingrese el valor de la recta b: "))
c = float(input("Ingrese el valor de la recta c: "))
d = float(input("Ingrese el valor de la recta d: "))
diagonal = float(input("Ingrese el valor de alguna de las diagonales: "))

# triangulo_1
semi_perimetro_1 = calcular_semi_perimetro(a, b, diagonal)
print("Valor del semi-perimetro del primer triangulo", semi_perimetro_1)
area_triangulo_1 = formula_heron(a, b, diagonal)
print("Valor del area del primer triangulo: ", area_triangulo_1)

# triangulo_2
semi_perimetro_2 = calcular_semi_perimetro(c, d, diagonal)
print("Valor del semi-perimetro del segundo triangulo", semi_perimetro_2)
area_triangulo_2 = formula_heron(c, d, diagonal)
print("Valor del area del segundo triangulo", area_triangulo_2)

# Valor del cuadrilatero
area_total = area_cuadrilatero(a, b, c, d, diagonal)
print("El area total es: ", area_total)