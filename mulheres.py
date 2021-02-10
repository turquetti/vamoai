print('-'*60)
print('VOCÊ JÁ OUVIU FALAR DA ZOÓLOGA JOAN BEAUCHAMP PROCTER?')
print('-'*60)
print('''Joan nasceu na Inglaterra em 1897, e cresceu em uma época em que as 
mulheres não podiam fazer ciência. Descubra um pouco mais sobre essa cientista
respondendo o teste abaixo:  ''')
print('-'*60)

print('''
[ 1 ] Joan era zoóloga e tinha vários animais de estimação, quais desses abaixo você acha que ela tinha? 

a) Cobras
b) Tubarões
c) Pássaros
d) Crocodilos

''')

resposta1 = input("Digite a resposta da Pergunta [ 1 ]: ")

print('''
[ 2 ] Joan era considerada uma herpetologista, e seu primeiro trabalho foi no Museu Britânico,
qual foi um grande feito dela enquanto trabalhava lá? 

a) Descobriu uma nova espécie de lagarto
b) Publicou um artigo na revista "Zoological Society of London"
c) Projetou a casa de répteis mais complexa da sua época
d) Escreveu um livro sobre répteis

''')

resposta2 = input("Digite a resposta da Pergunta [ 2 ]: ")

print('''
[ 3 ] Selecione uma alternativa ERRADA sobre Joan:

a) Ela faleceu com 67 anos
b) Ela passeava com um réptil na coleira
c) Ela frequentou a universidade
d) A mãe dela também era zoóloga

''')

resposta3 = input("Digite a resposta da Pergunta [ 3 ]: ")

total = 0
if resposta1 == 'a' or resposta1 == 'd':
    total+=1
if resposta2 == 'a' or resposta2 == 'c':
    total+=1
if resposta3 == 'c' or resposta3 == 'd':
    total+=1

print('-'*60)
print(f"O seu total de pontos foi de: {total} pontos!")
print('-'*60)
print('''
Joan é considerada uma especialista em herpetologia. Ela trabalhou no Museu Britânicos de Londres,
e lá descobriu uma espécie nova de lagarto oriundo da Austrália, chamada Peninsula Dragon Lizard.

Ela construiu a primeira casa adaptada para répteis no Zoológico de Londres em 1926, que foi considerada
a casa mais complexa e avançada de répteis da sua época, Joan mostrou a todos a importância de criar 
ambientes naturais para que os animais se sentissem mais confortáveis, onde ela criou um
sistema de temperatura adaptado para répteis.

Joan veio a falecer com seus 34 anos, em 1931, mas seu legado continua vivo até hoje no Zoológico de Londres.''')

print('-'*60)
