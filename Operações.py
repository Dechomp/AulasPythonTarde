def main():
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))

  soma = num1 + num2
  sub = num1 - num2
  mult = num1 * num2
  div = num1 / num2

  print("A soma de ", num1, " + ", num2, " = ", soma)
  print("A subtração de ", num1, " - ", num2, " = ", sub)
  print("A multiplicação de ", num1, " * ", num2, " = ", mult)
  print("A divisão de ", num1, " / ", num2, " = ", div)
  
  return 0
main()