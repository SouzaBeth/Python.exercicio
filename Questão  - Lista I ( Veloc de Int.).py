tamanho = float(input(f"Tamanho do arquivo(MB)): )\n "))
#Essa função irá soliciar o tamanho do arquivo em megabytes
velocidade = float(input(f"Velocidade de internet (Mbps):\n  "))
#Essa função irá solicitar a velocidade usada da internet
print(f"Tempo aproximado de download: %0.2f minutos \n "% ((tamanho / velocidade) * 60))
#Essa função irá calcular o tempo de download da internet por megabytes358