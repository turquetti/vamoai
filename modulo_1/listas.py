comidas_preferidas = ['risoto', 'falafel', 'hommus', 'guioza', 'misso']
print('-'*100)
print("Minhas comidas preferidas: ", comidas_preferidas)
print('-'*100)

comidas_preferidas.append('bolo da ivone')
print("Método Append: ", comidas_preferidas)
print('-'*100)

comidas_preferidas.pop()
print("Método Pop: ", comidas_preferidas)
print('-'*100)

comidas_preferidas.remove('falafel')
print("Método Remove: ", comidas_preferidas)
print('-'*100)

print("Quantas vezes a palavra 'risoto' aparece na lista? ", comidas_preferidas.count('risoto'))
print('-'*100)

comidas_preferidas.reverse()
print("Invertendo a lista: ", comidas_preferidas)
print('-'*100)

comidas_preferidas.insert(2, 'patê')
print('Inserindo uma nova comida preferida: ', comidas_preferidas)
print('-'*100)

print("O número total de comidas na lista é de: ", len(comidas_preferidas))
print('-'*100)

print("Lista de Repartição: ", comidas_preferidas[::2])
print('-'*50)

