idade_maioridade = 33
idade_atual = int(input("Digite sua idade: "))

anos_para_maioridade = max(0, idade_maioridade - idade_atual)

mensagem = "Faltam {} anos para você atingir a maioridade e ter a sua grande festa.".format(anos_para_maioridade) * (anos_para_maioridade > 0) + "A celebração já pode começar!" * (anos_para_maioridade == 0)
print(mensagem)
