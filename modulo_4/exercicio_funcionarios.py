import statistics as st
import matplotlib.pyplot as plt
import numpy as np

dias = [26,27,28,29,30]

funcionarios = {
    'Luana': [4,7,12,5,3],
    'Adoniran': [2,8,9,3,12],
    'Marcela': [7,2,10,3,11],
    'Joana': [12,4,1,8,14],
    'Cristina': [3,6,8,10,2]
}

# Estatistica Descritiva
print('-'*20, 'MÉDIA','-'*20)
for k,v in funcionarios.items():
    print(f"{k}: {st.mean(v)}")

print('-'*20, 'MODA','-'*20)
for k,v in funcionarios.items():
    if st.mode(v) == v[0]:
        print(f"{k}: Não é possível calcular a moda.")
    else: 
        print(f"{k}: {st.mode(v)}")

print('-'*20, 'MEDIANA','-'*20)
for k,v in funcionarios.items():
    print(f"{k}: {st.median(v)}")

#Visualizacao dos dados
width = 0.2
n_dias = np.arange(0,len(dias))

plt.barh(n_dias, funcionarios['Adoniran'], width, label='Adoniran')
plt.barh(n_dias + width, funcionarios['Luana'], width, label='Luana')
plt.barh(n_dias + width*2, funcionarios['Cristina'], width, label='Cristina')
plt.barh(n_dias + width*3, funcionarios['Joana'], width, label='Joana')
plt.barh(n_dias + width*4, funcionarios['Marcela'], width, label='Marcela')

plt.legend()

plt.yticks((n_dias + width), dias)
plt.xlabel("Vendas")
plt.ylabel("Dias")

plt.show()



