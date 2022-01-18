import random

def jogar_adivinhacao():
    print("********************");
    print("Bem vindo ao jogo da ADINHACAO!");
    print("********************");

    numero_secreto = round(random.randrange(1, 101));
    total_tentativas = 3;
    tentativas = 1;
    ok = True;

    for tentativas in range(1, total_tentativas + 1):
        print("Tentativa: {} de {}".format(tentativas, total_tentativas))
        chute = int(input("Digite o seu numero de 1 a 100:"));

        if (chute < 1 or chute > 100):
            print("Seu chute deve ser entre 1 a 100!");
            continue;

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns, você acertou!");
            ok = False;
            break;
        else:
            if (maior):
                print("Você errou! Seu chute foi maior que o numero secreto.")
            elif (menor):
                print("Você errou! Seu chute foi menor que o numero secreto.")

    print("********************");
    if (ok):
        print("o numero secreto era: {} ".format(numero_secreto));
    print("Fim de jogo!")
    print("********************");

if(__name__ == "__main__"):
    jogar_adivinhacao();