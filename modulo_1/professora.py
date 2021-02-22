#Uma professora deseja desenvolver um sistema para automatizar
#seu trabalho. Ela precisa criar uma solução onde seus alunos
#consigam inserir suas notas (seja a média geral de todas as
#matérias ou a média de uma única disciplina), receber a média, e
#saber sua situação (aprovação, reprovação ou recuperação).

#FUNÇÕES PARA FAZER O PROGRAMA RODAR
def media_geral(n1,n2,n3,n4):
    media = (n1 + n2 + n3 + n4)/4
    return media

def media_disciplina(p1,p2,p3):
    media = (p1 + p2 + p3)/3
    return media

def situacao(nota):
    if nota >= 7:
        print("="*60)
        print(f"Parabéns! Você foi aprovado com uma média de {media:.1f} pontos! Boas férias! :-)")
        print("="*60)
    elif nota >= 5 and nota < 7:
        print("="*60)
        print(f"Ah! Que pena! Você está de recuperação, sua média final é de {media:.1f}! :-/")
        print("="*60)
    else:
        print("="*60)
        print(f"Sinto muito! Você foi reprovado, sua média final é de {media:.1f} :-(")
        print("="*60)


print('='*60)
print(''' 
SISTEMA DE NOTAS - ESCOLA SÃO CAMILO

Selecione uma das opções abaixo para inserir suas notas:
[ 1 ] Média geral de todas as matérias
[ 2 ] Média de uma única disciplina
''')
print('='*60)

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    #Media Geral
    materia1 = float(input("Digite a nota final de Português: "))
    materia2 = float(input("Digite a nota final de Matemática: "))
    materia3 = float(input("Digite a nota final de Ciências: "))
    materia4 = float(input("Digite a nota final de Artes: "))
    media = media_geral(materia1, materia2, materia3, materia4)

    print(f"A média final do bimestre {media:.1f} pontos.")

else:
    #Media da Disciplina
    prova1 = float(input("Digite a nota da prova 1: "))
    prova2 = float(input("Digite a nota da prova 2: "))
    prova3 = float(input("Digite a nota da prova 3: "))
    media = media_disciplina(prova1, prova2, prova3)
    print(f"A média final da disciplina {media:.1f} pontos.")

print('='*60)
print(''' 
Obrigado por inserir suas notas, o que gostaria de fazer agora? 
[ 1 ] Situação (Aprovado/Recuperação/Reprovado)
[ 2 ] Finalizar programa
''')
print('='*60)

opcao_situacao = int(input("Digite a opção desejada: "))

if opcao_situacao == 1:
    resultado = situacao(media)
else:
    print("Finalizando o programa. Obrigado por utilizar nosso serviço.")

