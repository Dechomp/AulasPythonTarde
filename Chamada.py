def main():
  print("Lista de chamada")
  i = int(input("Digite a quantidade de alunos: "))
  vet = [""] * i
  j = 0

  for i in vet:
    vet[j] = input("Digite o nome do aluno: ")
    j = j + 1
    
  nome = "Júlio de Souza Gonçalves dos Santos"

  print("As 5 primeiras letras dos seu nome são: ", nome[0:5])
  print("Alunos que vieram hoje \n", vet)
  
  return 0


main()
