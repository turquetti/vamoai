print("="*60)
print("RESULTADO DE EXAMES DO HOSPITAL SANTA HELENA")
print("="*60)

paciente1 = int(input("Por favor, digite o resultado do exame do primeiro paciente: "))
paciente2 = int(input("Por favor, digite o resultado do exame do segundo paciente: "))
paciente3 = int(input("Por favor, digite o resultado do exame do terceiro paciente: "))

print("="*60)
print("RELATÓRIO FINAL")
print("="*60)

def analise_exame(resultado):
    if resultado >= 7 and resultado <= 10:
        print("Continue assim.")
    elif resultado >= 4 and resultado <= 6:
        print("Busque se cuidar mais e fazer acompanhamento médico")
    else: 
        print("Buscar a equipe médica IMEDIATAMENTE!")

analise_exame(paciente1)
analise_exame(paciente2)
analise_exame(paciente3)