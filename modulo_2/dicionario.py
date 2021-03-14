series_preferidas = dict()

series_preferidas[1] = 'Sex Education'
series_preferidas[2] = 'The Last Kingdom'
series_preferidas[3] = 'Atypical'
series_preferidas[4] = 'Community'
series_preferidas[5] = 'Friends'

print(series_preferidas)

mais_series = dict()

mais_series[6] = 'The Good Place'
mais_series[7] = '3%'
mais_series[8] = 'Onisciente'

print(mais_series)

series_preferidas.update(mais_series)

print(series_preferidas)

print(f"Qual série eu vou assistir agora? {series_preferidas.popitem()}")

print(series_preferidas)