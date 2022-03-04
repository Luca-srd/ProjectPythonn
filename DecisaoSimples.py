nome=input("Digite o Nome: ")
idade=int(input("Digite a idade: "))
prioridade="NÃO"
if idade>=65:
    prioridade="SIM"
print("O paciente " + nome  +  "possui atendimento prioritário?" + prioridade)