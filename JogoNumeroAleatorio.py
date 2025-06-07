import random


def main():
  print("Bem vindo ao jogo de adivinhação!")
  numAleatorio = random.randint(1, 200)

  tentativas = 0
  numDigitado = 0

  while numDigitado != numAleatorio:
    numDigitado = int(input("Digite um número: "))

    if numDigitado == numAleatorio:
      print("Você acertou!\n")
      break
    elif numDigitado < numAleatorio:
      print("O número digitado é menor que o número aleatório\n")
    else:
      print("O número digitado é maior que o número aleatório\n")
    tentativas += 1

  print("Você acertou com ", tentativas, " tentativas")
  return 0


main()
