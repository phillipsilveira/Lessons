#Calculadora Bancaria
#Deposito, saque e extrato.

###VARIAVEIS DE OP BANCARIAS
dep = 0
saq = 1
ext = 2
sair = 3
###VARIAVEIS PARA CALCULO 
q_dep = []
q_saq = []
dep1 = float()
dep2 = float()
saq1 = float()
saldo = float()
cont_saque = 0

#######################

#def x():
while True:
    oper = int(input('Qual operação você quer realizar? 0- Deposito, 1 - Saque, 2- extrato, 3- sair '))

    if oper > 0 or oper < 2:
        if oper == 0:
            dep1 = float(input('Qual o valor do deposito? '))
            if dep1 < 0:
                print('Digite um valor valido')
            else:
                q_dep.append(f'Deposito R${dep1:,.2f}')
                saldo += dep1
                print(saldo)
        elif oper == 1:
            saq1 = float(input('Digite o valor do saque: '))
            if saq1 < 0:
                print('Digite um valor valido')
            elif saldo - saq1 < 0:
                print('Saldo insuficiente')
            elif cont_saque == 3:
                print('Valor máximo de 3 saques excedido')
            else:
                print(f'Saque realizado no valor de R$ {saq1:,.2f}')
                cont_saque += 1
                q_saq.append(f'Saque R$ {saq1:,.2f}')
                saldo = float(saldo - saq1)
                #print(s_ext)
                #print(saldo)
        if oper == 2:
            print('----------------------------------')
            print('             EXTRATO')
            print(f'Saldo= R${saldo:,.2f}')
            print(f'Saques realizados= {q_saq}')
            print(f'Depositos realizados= {q_dep}')
            print('')
            print('----------------------------------')
        if oper == 3:
            break    
