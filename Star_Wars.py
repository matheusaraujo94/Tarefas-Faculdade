Nome = str(input("Qual é o seu nome? "))
Porcas = int(input("{}, quantas porcas você irá levar? ".format(Nome)))
Parafusos = int(input("Quantos parafusos? "))
Arruelas = int(input("Quantas arruelas? "))

Total = Porcas * 0.25 + Parafusos * 0.30 + Arruelas * 0.20
print("{}, sua compra é de: Porcas: {}, Parafusos: {}, Arruelas: {}. O valor total a ser pago é de: R$ {:.2f}".format(Nome, Porcas, Parafusos, Arruelas, Total))