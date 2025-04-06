import math

radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))

# Cálculo del volumen
area_base = math.pi * (radio ** 2)
volumen = area_base * altura

# Cálculo del área lateral y total
area_lateral = 2 * math.pi * radio * altura
area_superficial = area_lateral + 2 * area_base

print("Radio:", radio)
print("Altura:", altura)
print("Volumen del cilindro:", volumen)
print("Área superficial del cilindro:", area_superficial)
