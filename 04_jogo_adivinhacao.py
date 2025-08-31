import random

secreto = random.randint(1, 100)
tentativas = 0
print("Tente adivinhar o número entre 1 e 100!")

while True:
    try:
        palpite = int(input("Seu palpite: "))
        tentativas += 1
        if palpite == secreto:
            print(f"Acertou! Número: {secreto}. Tentativas: {tentativas}.")
            break
        dica = "maior" if palpite < secreto else "menor"
        print(f"Errou! Tente um número {dica}.")
    except ValueError:
        print("Digite um número inteiro válido.")
