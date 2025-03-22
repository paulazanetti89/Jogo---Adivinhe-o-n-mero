import random

def jogo_adivinhe_o_numero():
    print("Bem-vindo ao jogo 'Adivinhe o Número'!")
    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0

    while True:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))
            tentativas += 1
            if chute < 1 or chute > 100:
                print("Por favor, escolha um número entre 1 e 100.")
            elif chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    jogo_adivinhe_o_numero()