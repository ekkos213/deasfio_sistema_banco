menu = """

[1] Depositar
[2] Retiro
[3] Extrato
[0] Salir

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

while True:

    opcao = input(menu)
    
    # Deposito

    if opcao == "1":
        valor = float(input("Informe el valor a depósitar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("La operação fallo! El valor informado es inválido.")
            
            # saque

    elif opcao == "2":
        valor = float(input("Informe el valor a retirar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("La Operación fallo! Usted no tiene saldo suficiente.")

        elif excedeu_limite:
            print("La Operación fallo! el valor del saldo excede el limite")

        elif excedeu_saques:
            print("La Operación fallo! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
            
            # Estrato

    elif opcao == "3":
        print("\n**************** EXTRATO ****************")
        print("No se realizaron Movimientos." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operación inválida, por favor selecione novamente la operación deseada.")