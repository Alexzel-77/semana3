salario_bruto = float(input("Ingresa el salario bruto del empleado: "))
impuesto = salario_bruto * 0.10
seguro_social = salario_bruto * 0.05
fondo_pensiones = salario_bruto * 0.03
descuentos = impuesto + seguro_social + fondo_pensiones
salario_neto = salario_bruto - descuentos
print("Salario bruto:", salario_bruto)
print("Descuentos totales:", descuentos)
print("Salario neto:", salario_neto)