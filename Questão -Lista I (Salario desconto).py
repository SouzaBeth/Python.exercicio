imp_renda = 0.11
inss = 0.08
sindicato = 0.05


sal_horas = float(input(f"Quanto voce ganha por hora? \n "))
#Essa funçao vai solicitar o valor do salário por hora. 
horas_trabalhadas_meses = int(input(f"quantas horas você trabalhou no mês? \n"))
#Essa função vai solicitar a quantidades de horas trabalhadas.
sal_bruto = sal_horas * horas_trabalhadas_meses
#Essa função vai multiplicar salário em horas e a quantidade trabalhada no mês.
desconto_inss = sal_bruto * inss
#Essa função vai multiplicar o salário bruto e a porcentagem de INSS que é de 0.08
desconto_sindicato = sal_bruto * sindicato
#Essa função vai multiplicar o salário bruto e a porcentagem do sindicato que é de 0.05
desconto_imp_renda = sal_bruto * imp_renda
#Essa função vai calcular o salário bruto e a porcentagem do IR que é de 0.11
sal_liquido = sal_bruto - desconto_imp_renda - desconto_inss - desconto_sindicato
#Essa função vai calcular todos os descontos.

print(f"Seu salário bruto é: \n" , sal_bruto)
#Essa funççao vai calcular o valor do seu salário baseado na quantidade de horas trabalhadas.
print(f"Voce pagou de um total de IR: \n" , desconto_imp_renda)
#Essa função vai calcular o valor do seu imposto de renda, baseado no seu salário bruto.
print(f"voce pagou de INSS um total de: \n", desconto_inss)
#Essa função vai calcular o valor do seu INSS baseado no seu salário bruto.
print(f"Voce pagou ao sindicato um total de \n: ",  desconto_sindicato)
#Essa função vai calcular o valor do sindicato baseado no seu salário bruto.
print(f"Seu salario liquido é: \n", sal_liquido)
#Essa função vai calcular todos os descontos em cima do seu salário bruto, resultando o valor final.