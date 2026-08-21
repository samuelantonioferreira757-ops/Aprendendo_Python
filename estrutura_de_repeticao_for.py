""" computador=["Processador","Teclado","Mouse",]


for item in computador:
    if item == "Mouse":
        print(computador[1])"""


""" for i in range(7,21,7):
    print(i)
 """
""" 
for letra in "Python":
    print(letra) """

aluno = {"nome":"João","idade":20}

print(aluno.items())
for chave, valor in aluno.items():
    print(chave,":",valor)
    print(f"{chave}:{valor}")

soma= 0
for x in range(1,4):
    print("X:",x)
    soma+=x
    print("Soma:",soma)