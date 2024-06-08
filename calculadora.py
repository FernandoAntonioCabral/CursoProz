num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operador = int(input("Digite um número de acordo com a operação desejada: "))

def calculadora(num1, num2, operador) :
  result = 0
  if(operador == 1) :
    result = num1 + num2
  elif(operador == 2) :
    result = num1 - num2  
  elif(operador == 3) :
    result = num1 * num2 
  elif(operador == 4) :
    result = num1 / num2  
  else :
    print("ERRO: número inválido para operação") 
  return result

resultado = calculadora(num1, num2, operador) 
print("resultado: " + str(resultado))