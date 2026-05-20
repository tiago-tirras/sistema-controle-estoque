import time
from app.funcoes.menu import menu 
from  app.funcoes.cadastrar_produto import cadastrar_produto
from app.funcoes.registrar_entrada import registrar_entrada
from app.funcoes.registrar_saida import registrar_saida
from app.funcoes.consultar_estoque import consultar_estoque
from app.funcoes.alertar_estoque_baixo import alertar_estoque_baixo
from app.funcoes.mostrar_estoque_completo import mostrar_estoque_completo

while True:
    menu()

    try:
        opcao = int(input('Digite o número da função desejada: '))
    except ValueError:
        print('Apenas números inteiros são válidos!')
        continue
    
    if opcao == 1:
        cadastrar_produto()
    
    elif opcao == 2:
        registrar_entrada()

    elif opcao == 3:
        registrar_saida()

    elif opcao == 4:
        consultar_estoque()

    elif opcao == 5:
        alertar_estoque_baixo()
    
    elif opcao == 6:
        mostrar_estoque_completo()
    
    elif opcao == 7:
        print('Saindo do programa em:')
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)
        print('Programa encerrado!')
        break