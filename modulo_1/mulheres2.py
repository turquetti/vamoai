def comparar(idade_usuario, pais_usuario, idade_mulher_stem, pais_mulher_stem):
    if idade_usuario == idade_mulher_stem:
        print(f"Que legal, você e a Joan possuem {idade_usuario} anos!")
    else: 
        print(f"Que pena, você e a Joan não tem a mesma idade. Você tem {idade_usuario} e a Joan tem {idade_mulher_stem}.")
    
    if pais_usuario == pais_mulher_stem:
        print(f"Que legal, vocês moram na {pais_usuario}!")
    else: 
        print(f"Que pena, vocês não moram no mesmo país. Você mora no {pais_usuario} e a Joan mora na {pais_mulher_stem}.")

comparar(25,'Brasil', 34, 'Inglaterra')

