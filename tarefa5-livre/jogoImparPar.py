from random import randint


def boas_vindas():
    nome = input("Informe seu nome, Player! ")
    print(f"--- Bem vindo, {nome}. ---")
    return nome


def perguntar_jogar():
    return input("Deseja iniciar o jogo? (s/n): ").lower()


def escolher_par_ou_impar(nome):
    while True:
        escolha = input(
            f"{nome}, você quer ser Par ou Ímpar? (par/impar): "
        ).lower()

        if escolha in ("par", "impar"):
            return escolha
        else:
            print("Digite apenas 'par' ou 'impar'.")


def ler_numero(nome):
    return int(input(f"{nome}, informe um número: "))


def gerar_numero_maquina(limite):
    return randint(0, limite)


def calcular_resultado(num_jogador, num_maquina):
    return num_jogador + num_maquina


def verificar_vencedor(resultado, escolha):
    if resultado % 2 == 0 and escolha == "par":
        return "jogador"
    elif resultado % 2 != 0 and escolha == "impar":
        return "jogador"
    else:
        return "maquina"


def jogo():
    nome = boas_vindas()

    while True:
        jogar = perguntar_jogar()

        if jogar == "s":
            print("Vamos jogar!")

            escolha = escolher_par_ou_impar(nome)
            numero_jogador = ler_numero(nome)
            numero_maquina = gerar_numero_maquina(numero_jogador)

            print(f"Você escolheu: {numero_jogador}")
            print(f"A máquina escolheu: {numero_maquina}")

            resultado = calcular_resultado(numero_jogador, numero_maquina)
            print(f"Soma: {resultado}")

            vencedor = verificar_vencedor(resultado, escolha)

            if vencedor == "jogador":
                print(f"{nome}, você venceu!")
            else:
                print("A máquina venceu!")

            break

        elif jogar == "n":
            print(f"Até a próxima, {nome}!")
            break

        else:
            print("Digite apenas 's' ou 'n'.")

jogo()