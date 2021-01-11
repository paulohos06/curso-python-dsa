# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3.
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print('Selecione o número da operação desejada:\n 1- Soma\n 2- Subtração\n 3- Multiplicação\n 4- Divisão\n')
opcao = int(input('Digite sua opção (1/2/3/4): '))
num1 = int(input('Digite o 1o número: '))
num2 = int(input('Digite o 2o número: '))

def operacao(opcao):
  if(opcao == 1): res = num1 + num2
  elif(opcao == 2): res = num1 - num2
  elif(opcao == 3): res = num1 * num2
  elif(opcao == 4): res = num1 / num2
  return res

print(operacao(opcao))



