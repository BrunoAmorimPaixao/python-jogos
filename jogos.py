import forca
import adivinhacao

def escolha_jogo():
    print("********************");
    print("Escolha o jogo!");
    print("********************");

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo:"))

    if (jogo == 1):
        print("Jogar forca");
        forca.jogar_forca();
    elif(jogo == 2):
        print("jogar adivinhação");
        adivinhacao.jogar_adivinhacao();

if(__name__ == "__main__"):
    escolha_jogo();
