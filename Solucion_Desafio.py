#Edutec solutions

nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0
promedio = 0
nota1 = int(input("Escriba su primera nota: "))
nota2 = int(input("Escriba su segunda nota: "))
nota3 = int(input("Escriba su tercera nota: "))
nota4 = int(input("Escriba su cuarta nota: "))
nota5 = int(input("Escriba su quinta nota: "))
promedio = (nota1+nota2+nota3+nota4+nota5)/5
if promedio >= 60:(
    print("Aprobado")
)
elif 40 < promedio > 60: (
    print("En recuperación")
)
else: (
    print("Reprobado")
)