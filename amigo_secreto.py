import random

def sortear_amigo_secreto(participantes):
    sorteio = participantes[:]
    random.shuffle(sorteio)
    
    # Garantir que ninguém se sorteie a si mesmo
    for i in range(len(participantes)):
        if sorteio[i] == participantes[i]:
            return sortear_amigo_secreto(participantes)  # Tentar novamente se houver repetição
    
    return dict(zip(participantes, sorteio))

# Entrada de participantes
participantes = []
n = int(input("Quantas pessoas vão participar? "))

for _ in range(n):
    nome = input("Digite o nome do participante: ")
    participantes.append(nome)

# Realizar o sorteio
resultado = sortear_amigo_secreto(participantes)

# Exibir os pares
print("\nResultado do Amigo Secreto:")
for remetente, destinatario in resultado.items():
    print(f"{remetente} -> {destinatario}")
