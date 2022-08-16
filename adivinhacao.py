import random

def jogar():

    print("***********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("***********************************")

    numero_secreto = random.randrange(1,101)
    numero_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual Nível de Dificuldade você deseja?")
    print("(1) Fácil, (2)Médio, (3) Difícil")

    nivel = int(input("Defina o Nível de Dificuldade:"))

    if(nivel == 1):
        numero_de_tentativas = 20
    elif(nivel == 2):
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5

    while(rodada <= numero_de_tentativas):
        print("Tentativa {} de {}" .format(rodada, numero_de_tentativas))
        chute_str = input("Digite o seu número !")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)


        if(chute < 1 or chute > 100):
            print("Só serão válidos números entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        chutemaior = chute > numero_secreto
        chutemenor = chute < numero_secreto


        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(chutemaior):
                print("Seu número foi MAIOR do que o Sorteado")
            elif(chutemenor):
                print("Seu número foi MENOR do que o Sorteado")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("FIM do JOGO.")


if(__name__=="__main__"):
    jogar()

