print("1. CORONAVAC") 
print("2. OXFORD") 
print("3. PFIZER") 

vacina = int(input("Qual vacina você tomou? Digite 1, 2 ou 3: "))

if (vacina == 1) or (vacina == 2) or (vacina == 3):
    print("Parabéns, você está protegido!")
    if vacina == 1:
        print("E você virou um jacaré!")
    elif vacina == 2:
        print("E agora você está microchipado")
    else: 
        print("E agora você é mutante!")
else: 
    print("Você não está protegido! #Ficaemcasa")

