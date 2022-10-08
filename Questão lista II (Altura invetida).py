Pessoas = 5 
idade = [ ]
Altura= [ ]

for i in range(Pessoas):
    idade.append(int(input(f"digite a idade {i+1}: \n")))
    Altura.append(int(input(f" digite a altura {i+1} em cm: \n")))

for i in range(Pessoas -1, -1,-1):
    print("A pessoa{i+1 mede {altura[i]1:.2f}cm e tem 1{idades[i]} anos")
    