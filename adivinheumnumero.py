#Projeto: Adivinhe um número

import random

print("Bem-Vindo ao jogo do 'Adivinhe um número'")

#Repetir um código até o usuário acertar

while True:

    #Gerar um número aleatório de (1-50)
    numero_aleatorio = random.randint(1, 50)

    print(numero_aleatorio)

    tentativas_restantes = 5

    print("Pensei em um número entre 1 e 50...")
    print("Você tem 5 tentativas para tentar adivinhar!")

    #Loop até as tentativas acabarem
    while tentativas_restantes > 0:

        #Palpite do usuário (input)

        palpite = input ("Digite um número: ")

        #Validação do palpite

        if not palpite.isdigit():
            print("Entrada inválida, digite um número entre um número entre 1 a 50")
            continue

        #converter para inteiro
        palpite = int(palpite)

        #ver se o palpite está no intervalo estipulado
        if palpite < 1 or palpite >50:
            print("Escolha um número no intervalo entre 1 a 50")
            continue

        #Descontar tentativas 
        tentativas_restantes -= 1

        #Verificar se o palpite está correto
        if palpite == numero_aleatorio:
            print(f"Você acertou!, você ainda tinha {5 - tentativas_restantes} tentativas")

            break

        elif palpite < numero_aleatorio:
            print("O numero é maior que o número secreto")
        else:
            print("O numero é menor que o número secreto")

        print (f"Tentativas restantes: {tentativas_restantes} ")

    #while, else para quando as tentativas acabam
    else:
        print(f"Você perdeu, o número secreto era {numero_aleatorio}")

    #perguntar se o jogador quer jogar novamente
    jogar_novamente = input ("Deseja jogar novamente? (s/n):").lower()

    if jogar_novamente != "s":
        print("Até a próxima!...")
        break