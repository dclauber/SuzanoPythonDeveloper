#Dayvson Clauber
#variaveis_globais
saldo = 0
limite_saques = 3
qtd_saques = 0
valormax_saques = 500
extrato_geral = ""

#funções
def Depositar():
    global saldo, extrato_geral
    try:
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato_geral += f"Depósito: R$ {valor:.2f}\n"            
            print(f"Operação realizada com sucesso")
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Insira um valor válido! Por favor tente novamente!")
            Depositar()
    except ValueError:
        print("O valor informado é inválido! Por favor tente novamente!")

def Sacar():
    global qtd_saques, limite_saques, valormax_saques, saldo, extrato_geral
    try:
        if qtd_saques < limite_saques:
            valor = float(input("Informe o valor a ser sacado: "))
            if valor <= 0: #checar se valor negativo
                print("Valor inválido \nPor favor digite novamente")
                Sacar()
            elif  valor > saldo: #checar saldo suficiente
                print("Saldo insuficiente \n Por favor verifique o seu saldo")
                Sacar()            
            elif  valor > valormax_saques: #checar se valor está dentro do permitido
                print("Valor acima do permitido \n Por favor digite um novo valor")
                Sacar()            
            else: #operação de saque
                saldo -= valor
                qtd_saques += 1
                extrato_geral += f"Saque: R$ {valor:.2f}\n"            
                print(f"Operação realizada com sucesso")
                print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Número de operações permitidas já foram realizadas")

    except ValueError:
        print("O valor informado é inválido! Por favor tente novamente!")    

def Extrato():
    global saldo, extrato_geral

    if extrato_geral == "":
        print("Nenhuma movimentação realizada")
    else:
        print("\n================ EXTRATO ================")
        print(f"{extrato_geral}\n================ Saldo atual: R$ {saldo:.2f}" )

def Sair():
    exit()

menu = {"D":Depositar, "S":Sacar, "E":Extrato,"X":Sair}

while True:
    operacao = input(
                    "Selecione a operação desejada: \n"
                    "[D] Depósito\n"
                    "[S] Saque\n"
                    "[E] Extrato\n"
                    "[X] Sair\n"
                    ).upper()

    resultado = [v for k, v in menu.items() if k == operacao]

    if len(resultado)>0:
        func = resultado[0]
        func()  # chama a função correspondente
    else:
        print("Operação inválida. Tente novamente!")