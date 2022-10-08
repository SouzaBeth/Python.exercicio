sexo = int(input(f"Escolha: 1- sexo masculino / 2- sexo feminino: \n"))
h = float(input(f"Altura: \n"))
peso = float(input(f"peso: \n"))

peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7
    #essa funcao vai calcular o peso de acordo com o sexo escolhido. 
if peso < peso_ideal:
    print(f"Abaixo do peso ideal!\n")
    #Esta função vai mostrar se o peso estiver abaixo do solicitado, conforme o sexo escolhido.
elif peso == peso_ideal:
    print(f"Dentro do peso ideal!\n")
    #Essa função vai mostrar se o peso está ideal, conforme o sexo escolhido.
else:print(f"acima do peso ideal!\n")
    #Essa função vai mostrar se o peso está acima do ideal, conforme o sexo escolhido
print (f"Peso: %.2f / peso ideal: %2.f \n" %(peso, peso_ideal))
    #Essa função vai calcular o resultado final, conforme o sexo escolhido.