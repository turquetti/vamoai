lista_tarefas = []

print("Algo me diz que você tem um dia cheio hoje, o que você quer fazer hoje?")


while True:
    tarefas = input("Digite sua tarefas de hoje: ")
    resposta = input("Deseja incluir mais tarefas? [S/N] ")
    if resposta == 'S':
        lista_tarefas.append(tarefas)
        continue
    else:
        lista_tarefas.append(tarefas)
        break

print(lista_tarefas)