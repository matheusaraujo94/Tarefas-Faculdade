saborA = int(input("Digite o valor do primeiro feijãozinho: "))
saborB = int(input("Digite o valor do segundo feijãozinho: "))

print("Sabor A: {}, Sabor B: {}".format(saborA, saborB))

saborA, saborB = saborB, saborA

print("E agora, por um pouco de mágica... Sabores após a troca: Sabpr A: {}, Sabpr B: {}".format(saborA, saborB))