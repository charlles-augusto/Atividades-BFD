# Program to calculate the area of N quadrilaterals

n = int(input("Digite o número de quadriláteros: "))

for i in range(n):
    lado = float(input(f"Digite o comprimento do lado do quadrilátero {i+1}: "))
    area = lado * lado
    print(f"Área do quadrilátero {i+1}: {area}")
