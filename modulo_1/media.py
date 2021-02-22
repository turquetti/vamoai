aluno1 = float(input("Digite a nota do 1o aluno: "))
aluno2 = float(input("Digite a nota do 2o aluno: "))
aluno3 = float(input("Digite a nota do 3o aluno: "))
aluno4 = float(input("Digite a nota do 4o aluno: "))
aluno5 = float(input("Digite a nota do 5o aluno: "))

def media(aluno1,aluno2,aluno3,aluno4,aluno5):
    media = (aluno1 + aluno2 + aluno3 + aluno4 + aluno5)/5
    return media

print(f"A média entre os alunos é de {media(aluno1,aluno2,aluno3,aluno4,aluno5)}")


